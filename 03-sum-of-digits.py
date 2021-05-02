#
#  Perform sum of digits using recursion
#    sum_digits(123) = 1 + 2 + 3 = 6
#    sod(123) = 3 + sod(12)
#             = 3 + 2 + sod(1)
#             = 3 + 2 + 1 + sod(0)
#             = 6
#

def _sum(number: int) -> int:
    if number == 0:
        return 0
    units_digit = number % 10
    remaining_number = number // 10
    return units_digit + _sum(remaining_number)


def sum_digits(number: int) -> int:
    return _sum(number)


if __name__ == '__main__':
    print(sum_digits(12321))
