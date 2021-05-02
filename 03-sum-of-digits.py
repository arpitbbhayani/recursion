#
#  Perform sum of digits using recursion
#    sum_digits(123) = 1 + 2 + 3 = 6
#

def _sod(number: int) -> int:
    if number == 0:
        return 0
    units_digit = number % 10
    remaining_number = number // 10
    return units_digit + _sod(remaining_number)


def sum_digits(number: int) -> int:
    return _sod(number)


if __name__ == '__main__':
    print(sum_digits(12321))
