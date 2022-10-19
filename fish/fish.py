from abc import ABC
from abc import abstractmethod


class Fish(ABC):
    @abstractmethod
    def get_info(self) -> str:
        ...


class FishFactory(ABC):
    @classmethod
    @abstractmethod
    def create_fish(cls) -> Fish:
        ...

    @classmethod
    def get_capture_description(cls) -> str:
        fish = cls.create_fish()
        return (
            f'First, the float completely dived into the water, and then began to move away from the shore\n'
            f'I began to wind the fishing line with all my might, after which I ended up '
            f'the {fish.get_info()} in my hands'
        )
