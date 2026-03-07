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

  
    page.get_by_role("link", name="PIM").click()


    unique_username = f"user{int(time.time())}"
    
    pim_pg.go_to_add_employee()
    pim_pg.add_employee(
        fname="Hassan",
        lname="WithLogin",
        create_login=True,
        user_name=unique_username,
        password="Password123!"
    )
    
    page.wait_for_url("**/viewPersonalDetails/**", timeout=45000)
    print(f"Success: Added employee with username: {unique_username}")
