"""# project/tests/test_summaries.py"""


import json


def test_create_summary(test_app_with_db):
    """
    GIVEN test_app_with_db
    WHEN the POST method is called with valid data
    THEN a response status of 201 created should be returned
    """

    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"}))

    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"


def test_create_summaries_invalid_json(test_app):
    """
    GIVEN test_app
    WHEN the POST method is called with missing fields
    THEN a response message stating a value error should be returned
    """

    response = test_app.post("/summaries/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }


def test_read_summary(test_app_with_db):
    """
    GIVEN test_app_with_db
    WHEN the POST method is called with valid data
    THEN a response with id, url, summary and
        created_at values should be returned
    """

    response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"}))
    summary_id = response.json()["id"]

    response = test_app_with_db.get(f"/summaries/{summary_id}/")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == "https://foo.bar"
    assert response_dict["summary"]
    assert response_dict["created_at"]


def test_read_summary_incorrect_id(test_app_with_db):
    """
    GIVEN test_app_with_db
    WHEN the POST method is called with an invalid id
    THEN a 404 response message should be returned
    """

    response = test_app_with_db.get("/summaries/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"
