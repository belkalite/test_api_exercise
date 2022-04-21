import datetime
import os
from requests import Response


class Logger:

    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    log_req = None
    log_resp = None

    @staticmethod
    def _write_log_to_file(data: str):
        with open(Logger.file_name, 'a', encoding='utf-8') as log_file:
            log_file.write(data)

    @classmethod
    def add_request(cls, url: str, params: dict, data: dict, headers: dict, cookies: dict, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        data_to_add = "\n-----\n"
        data_to_add += f"Test {test_name}\n"
        data_to_add += f"Test {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method {method}\n"
        data_to_add += f"Request URL {url}\n"
        data_to_add += f"Request params {params}\n"
        data_to_add += f"Request data {data}\n"
        data_to_add += f"Request headers {headers}\n"
        data_to_add += f"Request cookies {cookies}\n"
        data_to_add += "\n"
        cls._write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, response: Response):
        cookies_as_dict = dict(response.cookies)
        headers_as_dict = dict(response.headers)
        data_to_add = f"Response code {response.status_code}\n"
        data_to_add += f"Response text {response.text}\n"
        data_to_add += f"Response headers {headers_as_dict}\n"
        data_to_add += f"Response cookies {cookies_as_dict}\n"
        data_to_add += "\n-----\n"
        cls._write_log_to_file(data_to_add)
