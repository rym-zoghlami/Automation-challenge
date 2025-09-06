import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_add_item_to_cart(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    # Ajouter un item
    inventory_page = InventoryPage(driver)
    added = inventory_page.add_item_to_cart("Sauce Labs Backpack")
    assert added, "L'item n'a pas été ajouté au panier"
    
    # Vérifier le panier
    inventory_page.go_to_cart()
    cart_page = CartPage(driver)
    items = cart_page.get_cart_items()
    assert "Sauce Labs Backpack" in items
