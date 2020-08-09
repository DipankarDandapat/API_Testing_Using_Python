import requests
import pytest

test_data_zip_codes = [
    ("in", "560032", "Gangenahalli Extn"),
    ("in", "560024", "Extn Iistage"),
    ("in", "560010", "Rajajinagar Bhashyam")
    ]


@pytest.mark.parametrize("country_code, zip_code, expected_place_name", test_data_zip_codes)
def test_using_test_data_object_get_location_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name
    assert response.status_code==200
    assert response.status_code == requests.codes.ok
    assert response.headers.get('Content-Type')=="application/json"
    assert response.encoding==None
    assert len(response_body["places"]) >= 1