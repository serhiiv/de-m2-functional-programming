from typing import Callable

from Essentials.Factorial.tail_recursion import tail_call_optimized

# Implement Factorial calculation function
# Use @tail_call_optimized decorator for tail recursion implementation


def factorial_impl() -> Callable[[int], int]:
    @tail_call_optimized
    def factorial(n: int, acc: int = 1) -> int:
        if n < 0:
            raise Exception("not defined for negative numbers")
        elif n == 0:
            return acc
        return factorial(n - 1, acc * n)

    return factorial


if __name__ == "__main__":
    print(factorial_impl()(0))
    print(factorial_impl()(1))
    print(factorial_impl()(2))
    print(factorial_impl()(50))
    # print(factorial_impl()(-1))
