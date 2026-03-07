class LoginPage:
   
    def __init__(self, page):
        self.page = page
        self._user_field = page.get_by_placeholder("Username")
        self._pass_field = page.get_by_placeholder("Password")
        self._btn = page.get_by_role("button", name="Login")

    def navigate(self):
      
        self.page.goto("https://opensource-demo.orangehrmlive.com/")

    def login(self, user, pwd):
        
        self._user_field.fill(user)
        self._pass_field.fill(pwd)
        self._btn.click()
        
