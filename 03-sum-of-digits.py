def _sum(number: int) -> int:
    if number == 0:
        return 0
    last_digit = number % 10
    remaining_number = number // 10
    return last_digit + _sum(remaining_number)


def sum_digits(number: int) -> int:
    return _sum(number)


if __name__ == '__main__':
    print(sum_digits(14321))
