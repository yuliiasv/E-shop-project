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

def test_get_figure_by_id():
    # Send the GET request
    response = requests.get(BASE_URL)

    # Convert response to JSON
    figures = response.json()

    figure_ids = [figure['id'] for figure in figures]

    # Construct the URL with the specific ID
    url = f"{BASE_URL}/{FIGURES_URL}/{figure_ids[0]}"

    response = requests.get(url)

    # Check status code
    assert_that(response.status_code).is_equal_to(200)

# # Test case to retrieve the Bearer token
# @pytest.mark.api
# def test_get_bearer_token():
#     token = get_bearer_token(LOGIN_URL)
#
#     # Ensure that a token is returned
#     assert token is not None
#     assert isinstance(token, str)
#
#     # Print the token for debugging (optional)
#     print(f"Bearer Token: {token}")
#
#     return token
#
#
# # Test case to use the Bearer token and check the user details
# @pytest.mark.api
# def test_get_user_details():
#     # Get the Bearer token from the previous test
#     token = get_bearer_token(LOGIN_URL)
#
#     # Set the headers with the Bearer token
#     headers = {
#         'Authorization': f'Bearer {token}',
#         'accept': 'application/json'
#     }
#
#     # Send GET request to retrieve user details
#     response = requests.get(USER_URL, headers=headers)
#
#     # Assertions to ensure the request was successful
#     assert response.status_code == 200
#     assert response.headers['Content-Type'] == 'application/json'
#
#     # Optionally, you can validate specific data from the response
#     user_data = response.json()
#     assert 'email' in user_data
#     assert user_data['email'] == "online.store.authority@gmail.com"