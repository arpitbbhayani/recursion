import json
from typing import List


with open('./data/elements.json') as fp:
    data = json.load(fp)
    elements = {element['symbol'].lower(): element for element in data}


def _get_composition(word: str, composition: List[str]) -> bool:
    # empty word is chemifyable
    if not word:
        return True

    # we compute 3 prefixes from the word
    # max length of element symbol is 3 hence we are
    # computing 3 prefixes - of length 1, 2 and 3.
    prefix1, prefix2, prefix3 = word[:1], word[:2], word[:3]

    # if prefix can be represented as a symbol (elemantable)
    # remaining word should also be elemntable
    if prefix1 in elements:
        composition.append(prefix1)
        if _get_composition(word[1:], composition):
            return True
        composition.pop()

    if prefix2 in elements:
        composition.append(prefix2)
        if _get_composition(word[2:], composition):
            return True
        composition.pop()

    if prefix3 in elements:
        composition.append(prefix3)
        if _get_composition(word[3:], composition):
            return True
        composition.pop()

    return False


def get_composition(word: str) -> List[str]:
    composition = []
    _get_composition(word.lower(), composition)
    return composition


if __name__ == '__main__':
    words = [
        'bose',
        'newton',
        'cooper',
        'ramanujan',
    ]

    for in_word in words:
        decomposed_elements = get_composition(in_word)
        if not decomposed_elements:
            print(f"{in_word} is not chemifyable")
        else:
            print(f"{in_word} is chemifyable")
            for symbol in decomposed_elements:
                element = elements[symbol]
                print(f"  - {element['symbol']}: {element['name']}")
        print('-' * 40)
