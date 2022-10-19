import random

from .fish import Fish
from .fish import FishFactory


class Perch(Fish):
    def get_info(self) -> str:
        return random.choice(('small', 'huge')) + ' perch'


class PerchFactory(FishFactory):
    @classmethod
    def create_fish(cls) -> Fish:
        return Perch()
