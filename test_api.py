import pytest
import requests
from config import BASE_URL, FIGURES_URL, LOGIN_URL, USER_URL
from assertpy.assertpy import assert_that

# Function to get the Bearer token
def get_bearer_token(login_url=LOGIN_URL, email="online.store.authority@gmail.com", password="b9uT2rXE80Ls"):
    response = requests.post(login_url, json={
        "email": email,
        "password": password
    })

    # Check if the request was successful
    response.raise_for_status()

    # Extract and return the token from the response
    token = response.json().get('token')
    if not token:
        raise ValueError("Token not found in the response.")

    return token

def test_get_all_figures():
    url = f"{BASE_URL}/{FIGURES_URL}"
    response = requests.get(url)
    response_dict = response.json()

    assert_that(response.status_code).is_equal_to(200) #check that API returns a successful status
    assert_that(response_dict).is_instance_of(list).is_not_empty()
    assert_that(response_dict).is_not_empty() #check that API returns content

