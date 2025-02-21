from typing import Callable


# Implement Fibonacci search using the simples functional recursion
def fibonacci_impl() -> Callable[[int], int]:
    def fib(n: int) -> int:
        if n < 0:
            raise Exception("not defined for negative numbers")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    return fib


if __name__ == "__main__":
    print(fibonacci_impl()(0))
    print(fibonacci_impl()(1))
    print(fibonacci_impl()(2))
    print(fibonacci_impl()(25))
    # print(fibonacci_impl()(-1))
