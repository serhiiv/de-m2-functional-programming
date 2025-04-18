from functools import partial, reduce
from typing import Callable


def plus(v1: "Vector", v2: "Vector"):
    return Vector(*[v1[i] + v2[i] for i in range(0, len(v1))])


def minus(v1: "Vector", v2: "Vector"):
    return Vector(*[v1[i] - v2[i] for i in range(0, len(v1))])


class Vector:
    def __init__(self, *params: int):
        self._params = params

    def __len__(self):
        return len(self._params)

    def __getitem__(self, item):
        return self._params[item]

    def transform(self, *fns: Callable[["Vector"], "Vector"]) -> "Vector":
        return reduce(lambda v, f: f(v), fns, self)

    def __str__(self):
        return f"Vector([{', '.join([str(param) for param in self._params])}])"

    def __eq__(self, other: "Vector") -> bool:
        return other._params == self._params


def do_math(v1: Vector, v2: Vector, v3: Vector) -> Vector:
    return v1.transform(partial(plus, v2=v2), partial(minus, v2=v3))
    # return minus(plus(v1, v2), v3)


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    v3 = Vector(7, 8, 9)
    print(do_math(v1, v2, v3) == Vector(-2, -1, 0))  # True
