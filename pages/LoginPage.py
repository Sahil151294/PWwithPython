import ProductListPage


class LoginPage:
    def __init__(self, page) -> None:
        self.page = page
        self._username = page.locator("[data-test=\"username\"]")
        self._password = page.locator("[data-test=\"password\"]")
        self._login_btn = page.get_by_role("button", name="LOGIN")

    def enter_username(self, u_name):
        self._username.clear()
        self._username.fill(u_name)

    def enter_password(self, p_word):
        self._username.clear()
        self._username.fill(p_word)
        
    def click_login(self):
        self._login_btn.click()

    def do_login(self, creds):
        self.enter_username(creds['username'])
        self.enter_password(creds['password'])
        self.click_login()
        return ProductListPage(self.page)