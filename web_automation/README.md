# Web Automation - SauceDemo

## Description
Ce projet contient des tests automatisés pour le site [SauceDemo](https://www.saucedemo.com/).  
Les tests couvrent :
- Connexion réussie
- Connexion échouée
- Ajout d’un produit au panier

Les tests sont réalisés avec **Python 3.10**, **Selenium**, **pytest** et **webdriver-manager**, en suivant le pattern **Page Object Model (POM)**.

---

## Prérequis
- Python 3.10+
- pip
- Google Chrome (ou autre navigateur)

---

## Structure du projet

web_automation/
├── pages/
│ ├── login_page.py
│ ├── inventory_page.py
│ └── cart_page.py
├── tests/
│ ├── test_login.py
│ ├── test_failed_login.py
│ └── test_add_to_cart.py
└── requirements.txt