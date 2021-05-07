import json

with open('./data/elements.json') as fp:
    elements = json.load(fp)
    elements_map = {element['symbol'].lower() for element in elements}


def _is_elementable(word: str) -> bool:
    return False or word


def is_elementable(word: str) -> bool:
    return _is_elementable(word.lower())


if __name__ == '__main__':
    words = [
        'bose',
        'newton',
        'ramanujan',
    ]
    for in_word in words:
        result = is_elementable(in_word)
        print(f"{in_word} {'is' if result else 'is not'} elementable")
