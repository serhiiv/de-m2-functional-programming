from typing import Callable
from Essentials.TailFibonacci.tail_recursion import tail_call_optimized

# Implement Fibonacci search using the optimized functional recursion
# Use @tail_call_optimized decorator for tail recursion implementation


def fibonacci_impl() -> Callable[[int], int]:
    @tail_call_optimized
    def fib(n: int, junior: int = 0, middle: int = 1) -> int:
        if n < 0:
            raise Exception("not defined for negative numbers")
        elif n == 0:
            return junior
        elif n == 1:
            return middle
        return fib(n - 1, middle, junior + middle)

    return fib


if __name__ == "__main__":
    print(fibonacci_impl()(0))
    print(fibonacci_impl()(10))
    print(fibonacci_impl()(5000))
    # print(fibonacci_impl()(-1))
