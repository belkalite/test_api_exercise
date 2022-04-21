import json.decoder
from datetime import datetime
from requests import Response


class Core:

    auth_sid = None
    token = None
    user_id = None

    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Can't find cookie with name {cookie_name} in last response {response.text}"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Can't find cookie with name {header_name} in last response"
        return response.headers[header_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response isn't json format! response as text: {response.text}"

        assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"
        return response_as_dict[name]

    def prepare_registration_data(self, email=None, password=123, username='learnqa', firstname='learnqa', lastname='learnqa'):
        if email is None:
            base_part = 'learnqa'
            domain = "example.com"
            random_part = datetime.now().strftime("%m%d%Y%H%M%S%MS")
            email = f"{base_part}{random_part}@{domain}"
        return {
            'password': password,
            'username': username,
            'firstName': firstname,
            'lastName': lastname,
            'email': email
        }

    def auth(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        r = Methods.post("/api/user/login", data=data)

        self.auth_sid = self.get_cookie(r, "auth_sid")
        self.token = self.get_header(r, "x-csrf-token")
        self.user_id = self.get_json_value(r, "user_id")
