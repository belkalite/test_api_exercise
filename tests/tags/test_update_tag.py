import json

from test_data import new_tag


class TestUpdateTag:
    def test_user_can_update_tag(self, app, tag):
        response = app.http_api.put(
            url=f"/tags/{tag}",
            body=json.dumps({"name": new_tag})
        ).json()
        assert response["name"] == new_tag, "Tag was not updated"

    def test_cannot_update_image_not_exists(self, app):
        response = app.http_api.put(
            url=f"/tags/0",
            body=json.dumps({"name": new_tag}),
            expected_code=404
        )
        assert response.json() != {}, "Wrong response body"
