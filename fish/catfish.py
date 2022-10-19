import random

from .fish import Fish
from .fish import FishFactory


class Catfish(Fish):
    def get_info(self) -> str:
        return random.choice(('small', 'huge')) + ' catfish'


class CatfishFactory(FishFactory):
    @classmethod
    def create_fish(cls) -> Fish:
        return Catfish()
