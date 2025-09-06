from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items(self):
        elements = self.driver.find_elements(*self.cart_items)
        return [el.text for el in elements]
