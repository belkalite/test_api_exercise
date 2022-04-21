import json

from helpers.app import App
import pytest


@pytest.fixture(scope="session")
def app():
    app = App()
    return app


@pytest.fixture()
def image_record(app) -> object:
    filename = "test.dcm"
    size = 1234
    tags = ["bar", "baz"]
    image_data = {"filename": filename, "size": size, "tags": tags}
    response = app.http_api.post(url="/images",
                                 body=json.dumps(image_data),
                                 headers={"Content-Type": "application/json"},
                                 expected_code=200).json()  # TODO remove
    id = response["id"]
    yield id, filename, tags
