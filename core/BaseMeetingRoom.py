from core.BaseClass import BaseCase
from config import config_data
class BaseMettingRoom(BaseCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.token = cls.get_token(secret=config_data['secret']['meetingroomsecret'])