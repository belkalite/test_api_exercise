import json
import pytest

from helpers.assert_helper import check_tags
from test_data.test_data import image_body


class TestAddImage:

    @pytest.mark.smoke
    def test_user_can_create_image_record(self, app):
        response = app.http_api.post(url="/images",
                                     body=json.dumps(image_body),
                                     expected_code=201,  # TODO remove when status codes are fixed
                                     )
        assert response.json()["upload_url"].startswith("http"), "Upload url has wrong format"

        id = response.json()["id"]
        response = app.http_api.get(f"/images/{id}")
        app.checkers.check_json_value_by_name(response, "filename", image_body["filename"],
                                              "Created image has wrong 'filename'")
        app.checkers.check_json_value_by_name(response, "size", image_body["size"], "Created image has wrong 'size'")
        app.checkers.check_json_has_key(response, "tags")
        check_tags(response, image_body)
