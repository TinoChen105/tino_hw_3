import pytest
import re
from apis import breeds_list_all, breeds_image_random

@pytest.mark.parametrize("api_module, expected_keys", [
    (breeds_list_all, ["message", "status"]),
    (breeds_image_random, ["message", "status"]),
])
def test_api_response_structure(api_module, expected_keys, base_session):
    """Test to verify the structure of API responses."""
    response = api_module.get(base_session)
    
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    data = response.json()
    for key in expected_keys:
        assert key in data, f"Key '{key}' not found in response"

def test_api_response_contains_image(base_session):
    response = breeds_image_random.get(base_session)
    
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    
    data = response.json()
    assert re.match(r"https?://.*\.(jpg|jpeg|png)", data["message"]) is not None, \
        f"Validation failed for endpoint breeds_image_random: {data}"