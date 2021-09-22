from core.BaseClass import BaseCase
from config import config_data

class BaseOA(BaseCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.token = cls.get_token(secret=config_data['secret']['OAsecret'])