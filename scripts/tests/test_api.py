import os
import requests
import random
import string
from dotenv import load_dotenv

token = os.getenv("TOKEN_GITHUB")
username = os.getenv("USER_NAME")

if not token or not username:
    print("Token or username not found - some tests will be skipped")
    import pytest
    pytest.skip("Skipping API tests - Token not configured")


# Test 1 : GET /user/repos avec auth

def test_get_user_repos():
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}

    response = requests.get(url, headers=headers)

    # Vérifie que la requête a réussi
    assert response.status_code == 200

    # Vérifie que la réponse est bien une liste de repos
    assert isinstance(response.json(), list)


# Test 2 : GET /user/repos sans auth

def test_get_user_repos_without_auth():
    url = "https://api.github.com/user/repos"
    
    response = requests.get(url)
    
    # GitHub peut renvoyer 401 ou 403 selon le contexte
    assert response.status_code in [401, 403], f"Status code reçu : {response.status_code}"


# Test 3 : POST /user/repos + DELETE 

def test_create_and_delete_repo():
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    
    # Générer un nom de repo unique
    repo_name = "test-repo-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    
    payload = {
        "name": repo_name,
        "description": "Repo créé pour test automatique",
        "private": False
    }
    
    # Créer le repo
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 201, f"Status code reçu : {response.status_code}"
    assert response.json()["name"] == repo_name
    print(f"Repo créé avec succès : {repo_name}")
    
    # -----------------------------
    # DELETE : supprimer le repo comme test
    # -----------------------------
    delete_url = f"https://api.github.com/repos/{username}/{repo_name}"
    del_response = requests.delete(delete_url, headers=headers)
    
    # Vérifie que la suppression a réussi (204)
    assert del_response.status_code == 204, f"Le repo n'a pas été supprimé : {del_response.status_code}"
    print(f"Repo supprimé avec succès : {repo_name}")

# -----------------------------
# Exécution directe pour python Test_api.py
# -----------------------------
if __name__ == "__main__":
    test_get_user_repos()
    print("Test 1 passé ")
    test_get_user_repos_without_auth()
    print("Test 2 passé ")
    test_create_and_delete_repo()
    print("Test 3 passé ")
