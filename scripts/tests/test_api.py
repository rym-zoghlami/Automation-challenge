import os
import requests
import random
import string
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN_GITHUB")
username = os.getenv("USER_NAME")

if not token or not username:
    print("⚠️  Token or username not found - using mock values for testing")
    token = "mock_token_for_testing"
    username = "test_user"

def test_get_user_repos():
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_repos_without_auth():
    url = "https://api.github.com/user/repos"
    response = requests.get(url)
    assert response.status_code in [401, 403]

def test_create_and_delete_repo():
    url = "https://api.github.com/user/repos"
    headers = {"Authorization": f"token {token}"}
    repo_name = "test-repo-" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    payload = {
        "name": repo_name,
        "description": "Repo créé pour test automatique",
        "private": False
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == repo_name
    print(f"Repo créé avec succès : {repo_name}")
    delete_url = f"https://api.github.com/repos/{username}/{repo_name}"
    del_response = requests.delete(delete_url, headers=headers)
    assert del_response.status_code == 204
    print(f"Repo supprimé avec succès : {repo_name}")

if __name__ == "__main__":
    test_get_user_repos()
    print("Test 1 passé ✅")
    test_get_user_repos_without_auth()
    print("Test 2 passé ✅")
    test_create_and_delete_repo()
    print("Test 3 passé ✅")