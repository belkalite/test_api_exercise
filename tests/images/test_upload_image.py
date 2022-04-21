import base64
import json
from pathlib import Path

from helpers.assert_helper import check_tags
from test_data import image_path


class TestUploadImage:
    def test_user_can_upload_image(self, app):
        image_body = image_body_with_decoded_image()
        response = app.http_api.post(
            "/upload",
            body=json.dumps(image_body),
            expected_code=201  # TODO remove when status codes are fixed
        )
        assert response.json()["url"].startswith("http"), "Url has wrong format"
        app.checkers.check_json_has_key(response, "id")
        assert response.json()["url"].startswith("http")
        app.checkers.check_json_value_by_name(response, "filename", image_body["filename"],
                                              "Created image has wrong 'filename'")
        app.checkers.check_json_has_key(response, "size")
        app.checkers.check_json_has_key(response, "tags")


def image_body_with_decoded_image():
    image_data = Path(image_path).read_bytes()
    image_b64_bytes = base64.b64encode(image_data)
    image_b64_str = image_b64_bytes.decode("utf-8")
    body = {"filename": "test.dcm", "image_data": image_b64_str, "size": 1234, "tags": ["bar", "baz"]}
    return body
