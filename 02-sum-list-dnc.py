from typing import List


def _sum(numbers: List[int]) -> int:
    if len(numbers) == 1:
        return numbers[0]
    return numbers[0] + _sum(numbers[1:])


def sum_list(numbers: List[int]) -> int:
    return _sum(numbers)


if __name__ == '__main__':
    ll = [1, 4, 2, 3, 1, 6, 7, 1]
    print(sum_list(ll), sum(ll))
