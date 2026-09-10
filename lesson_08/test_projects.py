import uuid

from yougile_api import YougileApi


api = YougileApi()


def test_create_project_positive():
    body = {
        "title": f"Test project {uuid.uuid4()}"
    }

    response = api.create_project(body)

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_without_auth():
    body = {
        "title": f"Test project {uuid.uuid4()}"
    }

    response = api.create_project(body, use_auth=False)

    assert response.status_code == 401
    assert response.json()["error"] == "Unauthorized"


def create_test_project():
    body = {
        "title": f"Test project {uuid.uuid4()}"
    }

    response = api.create_project(body)

    assert response.status_code == 201

    return response.json()["id"]


def test_update_project_positive():
    project_id = create_test_project()

    new_title = f"Updated project {uuid.uuid4()}"

    body = {
        "title": new_title
    }

    response = api.update_project(project_id, body)

    assert response.status_code == 200

    get_response = api.get_project(project_id)

    assert get_response.status_code == 200
    assert get_response.json()["title"] == new_title


def test_update_project_negative():
    project_id = "00000000-0000-0000-0000-000000000000"

    body = {
        "title": "Updated project"
    }

    response = api.update_project(project_id, body)

    assert response.status_code == 404


def test_get_project_positive():
    project_id = create_test_project()

    response = api.get_project(project_id)

    assert response.status_code == 200
    assert response.json()["id"] == project_id


def test_get_project_negative():
    project_id = "00000000-0000-0000-0000-000000000000"

    response = api.get_project(project_id)

    assert response.status_code == 404
