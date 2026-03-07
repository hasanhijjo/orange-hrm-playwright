class PIMPage:
    """Page Object Model for the PIM (Personal Information Management) page."""

    def __init__(self, page):
        self.page = page

        # Navigation
        self._pim_nav = page.get_by_role("link", name="PIM")
        self._add_employee_nav = page.get_by_role("link", name="Add Employee")

        # Employee fields
        self._first_name = page.get_by_placeholder("First Name")
        self._last_name = page.get_by_placeholder("Last Name")

        # Login details toggle
        self._login_details_switch = page.locator(".oxd-switch-input")

        # Login fields (باستخدام locators دقيقة)
        self._login_fields = {
            "username": page.locator("//label[text()='Username']/following::input[1]"),
            "password": page.locator("//label[text()='Password']/following::input[1]"),
            "confirm_password": page.locator("//label[text()='Confirm Password']/following::input[1]"),
        }

        # Buttons
        self._save_button = page.get_by_role("button", name="Save")

    # Navigation methods
    def go_to_pim_page(self):
        """Navigate to the main PIM page."""
        self._pim_nav.click()

    def go_to_add_employee(self):
        """Navigate to the Add Employee page."""
        self._add_employee_nav.click()

    # Action method
    def add_employee(self, first_name, last_name, create_login=False, login_details=None):
        """
        Add a new employee.

        Args:
            first_name (str): Employee first name.
            last_name (str): Employee last name.
            create_login (bool): Whether to create login credentials.
            login_details (dict): Dictionary with keys 'username' and 'password'.
        """
        # Fill basic employee info
        self._first_name.fill(first_name)
        self._last_name.fill(last_name)

        # Fill login credentials if needed
        if create_login and login_details:
            # اضغط على زر إنشاء بيانات تسجيل الدخول
            self._login_details_switch.click()

            # انتظر ظهور الحقول قبل الملء
            self._login_fields["username"].wait_for(state="visible", timeout=10000)
            self._login_fields["password"].wait_for(state="visible", timeout=10000)
            self._login_fields["confirm_password"].wait_for(state="visible", timeout=10000)

            # املأ الحقول
            self._login_fields["username"].fill(login_details["username"])
            self._login_fields["password"].fill(login_details["password"])
            self._login_fields["confirm_password"].fill(login_details["password"])

        # اضغط حفظ بعد ملء البيانات
        self._save_button.click()
