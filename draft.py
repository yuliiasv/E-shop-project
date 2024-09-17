import pytest
import requests
from assertpy.assertpy import assert_that

BASE_URL = "https://onlinestorepredprod.onrender.com/api"
USER_URL = "users"
LOGIN_URL = "login"
FIGURES_URL = "figures"

url = f"{BASE_URL}/{FIGURES_URL}"
# print (url)


response = requests.get(url)

# Convert response to JSON
figures = response.json()
# print(figures)
figure_ids = [figure['id'] for figure in figures]
print(figure_ids)
url = f"{BASE_URL}/{FIGURES_URL}/{figure_ids[0]}"
# print (url)
response = requests.get(url)
print(response)
# Check status code
# assert response.status_code == 200





# def test_get_figure_by_id():
#     # Construct the URL with the specific ID
#     url = f"{BASE_URL}/{FIGURE_ID}"
#
#     # Send the GET request
#     response = requests.get(BASE_URL)
#
#     # Convert response to JSON
#     response_data = response.json()

    # Assert that the status code is 200
    # assert_that(response.status_code).is_equal_to(200)
