import requests
import json


def test_get_locations_for_IN_560032_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/in/560032")
    assert response.status_code == 200

def test_get_locations_for_IN_560032_check_content_type_equals_json():
    response = requests.get("http://api.zippopotam.us/in/560032")
    assert response.headers['Content-Type'] == "application/json"


def test_get_locations_for_IN_560032_check_country_equals_united_states():
    response = requests.get("http://api.zippopotam.us/in/560032")
    response_body = response.json()
    assert response_body["country"] == "India"


def test_get_locations_for_IN_560032_check_city_equals_beverly_hills():
    response = requests.get("http://api.zippopotam.us/in/560032")
    response_body = response.json()
    assert response_body["places"][1]["place name"] == "P&T Colony"


def test_get_locations_for_IN_560032_check_one_place_is_returned():
    response = requests.get("http://api.zippopotam.us/in/560032")
    response_body = response.json()
    assert len(response_body["places"]) == 2