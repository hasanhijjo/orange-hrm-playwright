
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


    page.wait_for_selector("text=Personal Details")
    print("تم إضافة الموظف الأول بنجاح (بدون بيانات دخول)")


    page.get_by_role("link", name="PIM").click()


    pim_pg.go_to_add_employee()
    pim_pg.add_employee(
        fname="Hassan",
        lname="WithLogin",
        create_login=True,
        user_name="hassan.tester.2026",
        password="Password123!"
    )

    page.wait_for_selector("text=Personal Details")
    print("تم إضافة الموظف الثاني بنجاح (مع بيانات دخول)")
