import random

from fish.catfish import CatfishFactory
from fish.fish import FishFactory
from fish.perch import PerchFactory


def hook(fish_factory: FishFactory) -> None:
    print('Hello. I\'ll tell you about my recent fishing catch...')
    print(fish_factory.get_capture_description())


def main() -> None:
    hook(random.choice((CatfishFactory, PerchFactory)))


if __name__ == '__main__':
    main()
