import json


class TestUpdateImage:
    def test_user_can_update_image_tags(self, app, image_record):
        id, _, tags = image_record
        new_tag = "foo"
        response = app.http_api.put(
            url=f"/images/{id}",
            body=json.dumps({"tags": [new_tag]}),
            headers={"Content-Type": "application/json"}
        ).json()
        tags_list = response["tags"]
        assert (item for item in tags_list if item["name"] == "foo"), "Tag was not updated"

    def test_cannot_update_image_not_exists(self, app):
        new_tag = "foo"
        app.http_api.put(
            url=f"/images/0",
            body=json.dumps({"tags": [new_tag]}),
            headers={"Content-Type": "application/json"},
            expected_code=404)
