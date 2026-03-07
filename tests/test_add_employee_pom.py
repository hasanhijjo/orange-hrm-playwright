import time
from pages.login_page import LoginPage
from pages.pim_page import PIMPage


def test_add_employee_scenarios(page):
    login_pg = LoginPage(page)
    pim_pg = PIMPage(page)


    login_pg.navigate()
    login_pg.login("Admin", "admin123")

    page.get_by_role("link", name="PIM").click()

    pim_pg.go_to_add_employee()
    pim_pg.add_employee("Hassan", "NoLogin")


    page.wait_for_url("**/viewPersonalDetails/**")
    print("تم إضافة الموظف الأول بنجاح")


    unique_user = f"user_{int(time.time())}"


    page.get_by_role("link", name="PIM").click()


    pim_pg.go_to_add_employee()
    pim_pg.add_employee(
        fname="Hassan",
        lname="WithLogin",
        create_login=True,
        user_name=unique_user,
        password="Password123!"
    )

    page.wait_for_url("**/viewPersonalDetails/**")
    print(f"تم إضافة الموظف الثاني بنجاح باليوزر: {unique_user}")
