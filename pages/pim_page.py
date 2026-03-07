class PIMPage:
    """Page Object Model for the PIM page."""

    def __init__(self, page):
        self.page = page

        self._add_employee_nav = page.get_by_role("link", name="Add Employee")
        self._first_name = page.get_by_placeholder("First Name")
        self._last_name = page.get_by_placeholder("Last Name")

        self._login_details_switch = page.locator(".oxd-switch-input")

        self._login_fields = {
            "username": page.get_by_label("Username"),
            "password": page.get_by_label("Password"),
            "confirm_password": page.get_by_label("Confirm Password"),
        }

        self._save_button = page.get_by_role("button", name="Save")
    def go_to_pim_page(self):
        """Navigate to the PIM main page."""
        self.page.get_by_role("link", name="PIM").click()

    def go_to_add_employee(self):
        self._add_employee_nav.click()

    def add_employee(self, fname, lname, create_login=False, login_details=None):
        self._first_name.fill(fname)
        self._last_name.fill(lname)

        if create_login and login_details:
            self._login_details_switch.click()
            self._login_fields["username"].fill(login_details["username"])
            self._login_fields["password"].fill(login_details["password"])
            self._login_fields["confirm_password"].fill(login_details["password"])

        self._save_button.click()
