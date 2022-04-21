import json
import pytest


def test_user_can_create_image_record(app):
    # Given (data to create image record)
    image_data = {"filename": "test.dcm", "size": 1234, "tags": ["bar", "baz"]}
    # When (create image record)
    response = app.http_api.post(url="/images",
                                 body=json.dumps(image_data),
                                 headers={"Content-Type": "application/json"},
                                 expected_code=200,  #TODO remove
                                 )
    # Then (check response)
    app.checkers.check_json_has_key(response, "id")
    assert response.json()["upload_url"].startswith("http")
    # Then (check that image record was created)
    id = response.json()["id"]
    response = app.http_api.get(f"/images/{id}")
    app.checkers.check_json_value_by_name(response, "filename", image_data["filename"],
                                          "Created image has wrong 'filename'")
    app.checkers.check_json_value_by_name(response, "size", image_data["size"], "Created image has wrong 'size'")
    app.checkers.check_json_has_key(response, "tags")
    tags_list = response.json()["tags"][0]
    for tag in tags_list:
        assert (item for item in tags_list if item["name"] == tag), "Created image has wrong tag name"


# @freeze_time("2021-11-03 21:00:00")
def test_get_image_not_exists(app):
    app.http_api.get("/images/0", expected_code=404)


def test_user_can_update_image_tags(app, image_record):
    # Given (existing image record)
    id, _, tags = image_record
    # When (user updates tags)
    new_tag = "foo"
    response = app.http_api.put(
        url=f"/images/{id}",
        body=json.dumps({"tags": [new_tag]}),
        headers={"Content-Type": "application/json"}
    ).json()
    tags_list = response["tags"]
    # Then (image record tags are updated)
    assert (item for item in tags if item["name"] == "foo"), "Tag was not updated"
