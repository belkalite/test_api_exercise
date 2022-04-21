from requests import Response
import json


class Checkers:

    @staticmethod
    def check_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response isn't json format. Response text is {response.text}"

        assert name in response_as_dict, f"Response json doesn't have key '{name}'"
        assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    def check_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response isn't json format. Response text is {response.text}"

        assert name in response_as_dict, f"Response json doesn't have key '{name}'"

    @staticmethod
    def check_json_has_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response isn't json format. Response text is {response.text}"

        for name in names:
            assert name in response_as_dict, f"Response json doesn't have key '{name}'"

    @staticmethod
    def check_json_has_not_keys(response: Response, names: list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response isn't json format. Response text is {response.text}"

        for name in names:
            assert name not in response_as_dict, f"Response json shouldn't have key '{name}' but this key was found"
