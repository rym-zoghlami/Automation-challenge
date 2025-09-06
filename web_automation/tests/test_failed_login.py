import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

# ------------------------------
# Fixture pour initialiser le driver
# ------------------------------
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Supprime si tu veux voir le navigateur
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.maximize_window()
    yield driver
    driver.quit()

# ------------------------------
# Test : login échoué
# ------------------------------
def test_failed_login(driver):
    login_page = LoginPage(driver)
    login_page.open()

    # Essayer un login avec un mauvais mot de passe
    login_page.login("standard_user", "wrong_password")

    # Vérifier que le message d'erreur est affiché
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error_message.is_displayed()
    assert "username and password do not match" in error_message.text.lower()
