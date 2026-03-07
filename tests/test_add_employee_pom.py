import time
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

def test_add_employee_scenarios(page):
    login_pg = LoginPage(page)
    pim_pg = PIMPage(page)

    # تسجيل الدخول
    login_pg.navigate()
    login_pg.login("Admin", "admin123")

    # الانتقال إلى صفحة PIM
    pim_pg.go_to_pim_page()

    # إضافة موظف بدون حساب تسجيل دخول
    pim_pg.go_to_add_employee()
    pim_pg.add_employee("Hassan", "NoLogin")
    page.wait_for_url("**/viewPersonalDetails/**")
    print("تم إضافة الموظف الأول بنجاح")

    # إنشاء اسم مستخدم فريد
    unique_user = f"user_{int(time.time())}"

    # الانتقال إلى صفحة PIM مجددًا
    pim_pg.go_to_pim_page()

    # إضافة موظف مع تسجيل دخول
    pim_pg.go_to_add_employee()
    login_details = {"username": unique_user, "password": "Password123!"}
    pim_pg.add_employee("Hassan", "WithLogin", create_login=True, login_details=login_details)

    page.wait_for_url("**/viewPersonalDetails/**")
    print(f"تم إضافة الموظف الثاني بنجاح باليوزر: {unique_user}")
