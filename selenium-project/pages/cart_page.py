from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CartPage(BasePage):
    
    _PROCEED_TO_CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".check_out")
    _CART_ROWS = (By.CSS_SELECTOR, "#cart_info_table tbody tr")
    
    def is_cart_page_displayed(self) -> bool:
        return self.is_visible(self._PROCEED_TO_CHECKOUT_BUTTON)
    
    def product_row(self, product_id: int):
        selector = (By.ID, f"product-{product_id}")
        return self.find(selector)
    
    def product_name(self, product_id: int) -> str:
        row = self.product_row(product_id)
        return row.find_element(By.CSS_SELECTOR, ".cart_description h4 a").text.strip()

    def product_price(self, product_id: int) -> float:
        row = self.product_row(product_id)
        price_text = row.find_element(By.CSS_SELECTOR, ".cart_price p").text
        return float(price_text.replace("Rs.", "").strip())

    def product_quantity(self, product_id: int) -> int:
        row = self.product_row(product_id)
        qty_text = row.find_element(By.CSS_SELECTOR, ".cart_quantity button").text
        return int(qty_text.strip())

    def product_total(self, product_id: int) -> float:
        row = self.product_row(product_id)
        total_text = row.find_element(By.CSS_SELECTOR, ".cart_total_price").text
        return float(total_text.replace("Rs.", "").strip())

    def remove_product(self, product_id: int):
        row = self.product_row(product_id)
        delete_btn = row.find_element(By.CSS_SELECTOR, f"a.cart_quantity_delete[data-product-id='{product_id}']")
        self.scroll_to(delete_btn)
        delete_btn.click()
        
    def products_count(self) -> int:
        rows = self.find_all(self._CART_ROWS)
        return len(rows)
    
    def click_proceed_to_checkout_button(self):
        self.click(self._PROCEED_TO_CHECKOUT_BUTTON)

    def wait_for_cart_items_count_to_be(self, expected_count: int):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: len(self.find_all(self._CART_ROWS)) == expected_count
    )