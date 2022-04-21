from .checkers import Checkers
from .http_api import HttpApi


class App:

    def __init__(self):
        self.checkers = Checkers()
        self.http_api = HttpApi()
