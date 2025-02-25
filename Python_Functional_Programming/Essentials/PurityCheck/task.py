from typing import Callable


class Integer:
    def __init__(self, value: int):
        self.value = value


def is_pure(increment_fn: Callable[[Integer], Integer]) -> bool:
    i1 = Integer(-1)
    i2 = increment_fn(i1)
    i3 = increment_fn(i1)
    return id(i1) != id(i2) != id(i3) and i1.value + 1 == i2.value == i3.value


def pure_increment(i: Integer) -> Integer:
    return Integer(i.value + 1)


def dirt_increment(i: Integer) -> Integer:
    i.value += 1
    return i


if __name__ == "__main__":
    print(is_pure(pure_increment))
    print(is_pure(dirt_increment))
