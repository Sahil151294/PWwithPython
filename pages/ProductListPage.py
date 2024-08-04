class ProductListPage:
    def __init__(self, page) -> None:
        self.page = page
        self._product_header = page.locator("span.title")

    def product_header_verification(self):
        return self._product_header