import json
from typing import List, Tuple, Set


with open('./data/elements.json') as fp:
    data = json.load(fp)
    elements = {element['symbol'].lower(): element for element in data}


def _get_all_compositions(
        word: str, composition: List[str], all_compositions: Set[Tuple[str]]) -> bool:
    # empty word is chemifyable
    if not word:
        all_compositions.add(tuple(composition))

    # we compute 3 prefixes from the word
    # max length of element symbol is 3 hence we are
    # computing 3 prefixes - of length 1, 2 and 3.
    prefix1, prefix2, prefix3 = word[:1], word[:2], word[:3]

    # if prefix can be represented as a symbol (elemantable)
    # remaining word should also be elemntable
    if prefix1 in elements:
        composition.append(prefix1)
        if _get_all_compositions(word[1:], composition, all_compositions):
            pass
        else:
            composition.pop()

    if prefix2 in elements:
        composition.append(prefix2)
        if _get_all_compositions(word[2:], composition, all_compositions):
            pass
        else:
            composition.pop()

    if prefix3 in elements:
        composition.append(prefix3)
        if _get_all_compositions(word[3:], composition, all_compositions):
            pass
        else:
            composition.pop()

    return False


def get_composition(word: str) -> Tuple[Tuple[str], float]:
    composition, compositions = [], set([])
    _get_all_compositions(word.lower(), composition, compositions)
    if not compositions:
        return None, 0

    entries: List[Tuple[str], float] = []
    for composition in compositions:
        atomic_mass = sum([elements[symbol]['atomic_mass']
                          for symbol in composition])
        entries.append((composition, atomic_mass,))

    return max(entries, key=lambda entry: entry[1])


if __name__ == '__main__':
    words = [
        'bose',
        'newton',
        'cooper',
        'ramanujan',
    ]

    for in_word in words:
        max_composition, max_atomic_mass = get_composition(in_word)
        if not max_composition:
            print(f"{in_word} is not chemifyable")
        else:
            print(f"{in_word} is chemifyable")
            for symbol in max_composition:
                element = elements[symbol]
                print(f"  - {element['symbol']}: {element['name']}")
            print(f"this composition has atomic mass of: {max_atomic_mass}")
        print('-' * 40)
