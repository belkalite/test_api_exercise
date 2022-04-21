import json
import os

from helpers.app import App
import pytest


@pytest.fixture(scope="session")
def app(env, request):
    with open(os.path.join("/home/anduser/Documents/test_exercise/test_api_exercise/configs", "app_config.json"), 'r') as config_file:
        app_config = json.load(config_file)[env]
        app = App(config=app_config)
        return app


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local",
                     help="Environment to run tests")


@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


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
