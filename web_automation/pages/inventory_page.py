from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        # Localisateurs des éléments
        self.add_to_cart_buttons = (By.CSS_SELECTOR, ".inventory_item button")
        self.cart_icon = (By.ID, "shopping_cart_container")

    def add_item_to_cart(self, item_name):
        # Parcours tous les articles et ajoute celui qui correspond
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == item_name:
                item.find_element(By.TAG_NAME, "button").click()
                return True
        return False

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
