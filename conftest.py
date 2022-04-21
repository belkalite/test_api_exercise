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
                                 expected_code=200).json()  # TODO remove when status codes are fixed
    id = response["id"]
    yield id, filename, tags
