class LoginPage:
    def __init__(self, page):
        self.page = page

        self._username_field = page.get_by_placeholder("Username")
        self._password_field = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/")

    def login(self, user, pwd):
        self._username_field.fill(user)
        self._password_field.fill(pwd)
        self._login_button.click()