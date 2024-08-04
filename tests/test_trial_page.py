import re
from playwright.sync_api import Page, expect
from pages.LoginPage import LoginPage

def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/v1/")
    credentials = {"username": "standard_user",
                   "password": "secret_sauce"}
    l_page = LoginPage(page)
    products_page = l_page.do_login(credentials)
    expect(products_page.product_header_verification()).to_have_text("Products")