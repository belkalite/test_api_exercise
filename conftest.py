import json
import pytest

from helpers.app import App
from test_data.test_data import tag_name


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


@pytest.fixture()
def tag(app) -> object:
    response = app.http_api.post(
        url=f"/tags/",
        body=json.dumps({"name": tag_name}),
        expected_code=200  # TODO remove when status codes are fixed
    ).json()
    tag_id = response["id"]
    yield tag_id
