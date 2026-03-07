class PIMPage:
    def __init__(self, page):
        self.page = page

        self._add_employee_nav = page.get_by_role("link", name="Add Employee")
        self._first_name = page.get_by_placeholder("First Name")
        self._last_name = page.get_by_placeholder("Last Name")


        self._login_details_switch = page.locator(".oxd-switch-input")


        self._emp_username = page.locator("xpath=//label[text()='Username']/../../div[2]/input")
        self._emp_password = page.locator("xpath=//label[text()='Password']/../../div[2]/input")
        self._confirm_password = page.locator("xpath=//label[text()='Confirm Password']/../../div[2]/input")

        self._save_button = page.get_by_role("button", name="Save")

    def go_to_add_employee(self):
        self._add_employee_nav.click()

    def add_employee(self, fname, lname, create_login=False, user_name=None, password=None):
        self._first_name.fill(fname)
        self._last_name.fill(lname)

        if create_login:
            self._login_details_switch.click()
            self._emp_username.fill(user_name)
            self._emp_password.fill(password)
            self._confirm_password.fill(password)

        self._save_button.click()