import requests
from test_data.test_data import request_headers


def api_method(default_expected_code: int = 200):
    def my_decorator(func):
        def wrapped(self, *args, **kwargs):
            expected_code = kwargs.pop("expected_code", default_expected_code)
            response = func(self, *args, **kwargs)
            if response.status_code != expected_code:
                raise AssertionError("Expected status code: {} but was {}.".format(expected_code, response.status_code))
            return response
        return wrapped
    return my_decorator


class HttpApi:

    @property
    def base_url(self):
        return "http://localhost:8000/v1"

    @api_method()
    def get(self, url: str):
        full_url = self.base_url + url
        response = requests.get(url=full_url)
        return response

    @api_method(default_expected_code=201)
    def post(self, url: str, body: dict = None, json: dict = None, headers: dict = request_headers):
        full_url = self.base_url + url
        response = requests.post(url=full_url, data=body, json=json, headers=headers)
        return response

    @api_method()
    def put(self, url: str, body: dict = None, json: dict = None, headers: dict = request_headers):
        full_url = self.base_url + url
        response = requests.put(url=full_url, data=body, json=json, headers=headers)
        return response

    @api_method(default_expected_code=204)
    def delete(self, url: str):
        full_url = self.base_url + url
        response = requests.delete(url=full_url)
        return response
