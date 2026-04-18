import random
import pytest
import requests


BASE_URL = "https://petstore3.swagger.io/api/v3"


def create_pet_payload(pet_id=None, name="alper-pet", status="available"):
    if pet_id is None:
        pet_id = random.randint(100000, 999999)

    return {
        "id": pet_id,
        "name": name,
        "category": {
            "id": 1,
            "name": "dogs"
        },
        "photoUrls": [
            "https://example.com/dog.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "qa"
            }
        ],
        "status": status
    }


@pytest.fixture
def pet_data():
    return create_pet_payload()


def test_pet_crud_positive_flow(pet_data):
    pet_id = pet_data["id"]

    # CREATE
    create_response = requests.post(f"{BASE_URL}/pet", json=pet_data)
    assert create_response.status_code == 200, f"Create failed: {create_response.text}"

    create_body = create_response.json()
    assert create_body["id"] == pet_id
    assert create_body["name"] == pet_data["name"]
    assert create_body["status"] == pet_data["status"]

    # READ
    get_response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert get_response.status_code == 200, f"Get failed: {get_response.text}"

    get_body = get_response.json()
    assert get_body["id"] == pet_id
    assert get_body["name"] == pet_data["name"]

    # UPDATE
    updated_payload = pet_data.copy()
    updated_payload["name"] = "alper-pet-updated"
    updated_payload["status"] = "sold"

    update_response = requests.put(f"{BASE_URL}/pet", json=updated_payload)
    assert update_response.status_code == 200, f"Update failed: {update_response.text}"

    update_body = update_response.json()
    assert update_body["name"] == "alper-pet-updated"
    assert update_body["status"] == "sold"

    # READ UPDATED
    get_updated_response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert get_updated_response.status_code == 200, f"Get updated failed: {get_updated_response.text}"

    get_updated_body = get_updated_response.json()
    assert get_updated_body["name"] == "alper-pet-updated"
    assert get_updated_body["status"] == "sold"

    # DELETE
    delete_response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert delete_response.status_code == 200, f"Delete failed: {delete_response.text}"

    # VERIFY DELETE
    get_deleted_response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert get_deleted_response.status_code == 404, (
        f"Expected 404 after delete, got {get_deleted_response.status_code}: "
        f"{get_deleted_response.text}"
    )


def test_get_pet_with_invalid_id_negative():
    response = requests.get(f"{BASE_URL}/pet/invalid-id")
    assert response.status_code == 400, (
        f"Expected 400 for invalid id, got {response.status_code}: {response.text}"
    )


def test_get_pet_with_non_existing_id_negative():
    non_existing_id = 999999999999
    response = requests.get(f"{BASE_URL}/pet/{non_existing_id}")
    assert response.status_code == 404, (
        f"Expected 404 for non-existing pet, got {response.status_code}: {response.text}"
    )


def test_create_pet_with_invalid_payload_negative():
    invalid_payload = {
        "id": "abc",
        "name": 123,
        "photoUrls": "not-a-list",
        "status": "available"
    }

    response = requests.post(f"{BASE_URL}/pet", json=invalid_payload)
    assert response.status_code in (400, 422), (
        f"Expected 400 or 422 for invalid payload, got {response.status_code}: {response.text}"
    )


def test_delete_pet_with_invalid_id_negative():
    response = requests.delete(f"{BASE_URL}/pet/invalid-id")
    assert response.status_code == 400, (
        f"Expected 400 for invalid delete id, got {response.status_code}: {response.text}"
    )