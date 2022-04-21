import base64
import json
from pathlib import Path


def test_user_can_create_image_record(app):
    image_data = {"filename": "test.dcm", "size": 1234, "tags": ["bar", "baz"]}
    response = app.http_api.post(url="/images",
                                 body=json.dumps(image_data),
                                 headers={"Content-Type": "application/json"},
                                 expected_code=200,  # TODO remove when status codes are fixed
                                 )
    assert response.json()["upload_url"].startswith("http"), "Upload url has wrong format"

    id = response.json()["id"]
    response = app.http_api.get(f"/images/{id}")
    app.checkers.check_json_value_by_name(response, "filename", image_data["filename"],
                                          "Created image has wrong 'filename'")
    app.checkers.check_json_value_by_name(response, "size", image_data["size"], "Created image has wrong 'size'")
    app.checkers.check_json_has_key(response, "tags")
    tags_list = response.json()["tags"][0]
    for tag in tags_list:
        assert (item for item in tags_list if item["name"] == tag), "Created image has wrong tag name"
    app.checkers.check_json_value_by_name(response, "size", image_data["size"], "Created image has wrong 'size'")



def test_upload(app):
    image_data = Path("tests/samples/image-00000.dcm").read_bytes()
    image_b64_bytes = base64.b64encode(image_data)
    image_b64_str = image_b64_bytes.decode("utf-8")
    image_body = {"filename": "test.dcm", "image_data": image_b64_str, "size": 1234, "tags": ["bar", "baz"]}
    response = app.http_api.post(
        "/upload",
        headers={"Content-Type": "application/json"},
        body=json.dumps(image_body),
        expected_code=200  # TODO remove when status codes are fixed
    )
    assert response.json()["url"].startswith("http"), "Url has wrong format"

    app.checkers.check_json_has_key(response, "id")
    assert response.json()["url"].startswith("http")
    app.checkers.check_json_value_by_name(response, "filename", image_body["filename"],
                                          "Created image has wrong 'filename'")
    app.checkers.check_json_has_key(response, "size")
    app.checkers.check_json_has_key(response, "tags")
    id = response.json()["id"]
    response = app.http_api.get(f"/images/{id}")
    app.checkers.check_json_value_by_name(response, "filename", image_body["filename"],
                                          "Created image has wrong 'filename'")
    app.checkers.check_json_has_key(response, "tags")
    tags_list = response.json()["tags"][0]
    for tag in tags_list:
        assert (item for item in tags_list if item["name"] == tag), "Created image has wrong tag name"
