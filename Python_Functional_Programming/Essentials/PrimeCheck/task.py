# Implement function that checks if number is Prime


def is_prime(n: int) -> bool:
    if n < 1:
        raise ValueError("Number must be greater than 0")
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    return not any(
        n % (i - 1) == 0 or n % (i + 1) == 0 for i in range(6, int(n**0.5) + 1, 6)
    )


if __name__ == "__main__":
    print([i for i in range(1, 100) if is_prime(i)])
