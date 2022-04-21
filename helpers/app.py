from .core import Core
from .checkers import Checkers
from .http_api import HttpApi


class App:

    def __init__(self, config: dict):
        self.config = config
        self.core = Core()
        self.checkers = Checkers()
        self.http_api = HttpApi()
