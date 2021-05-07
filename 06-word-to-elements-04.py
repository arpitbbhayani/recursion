import json
from typing import List, Tuple, Set


with open('./data/elements.json') as fp:
    data = json.load(fp)
    elements = {element['symbol'].lower(): element for element in data}


def _get_all_compositions(
        word: str, symbols: List[str], results: Set[Tuple[str]]) -> bool:
    # empty word is elementable
    if not word:
        results.add(tuple(symbols))

    # we compute 3 prefixes from the word
    # max length of element symbol is 3 hence we are
    # computing 3 prefixes - of length 1, 2 and 3.
    prefix1, prefix2, prefix3 = word[:1], word[:2], word[:3]

    # if prefix can be represented as a symbol (elemantable)
    # remaining word should also be elemntable
    if prefix1 in elements:
        symbols.append(prefix1)
        if _get_all_compositions(word[1:], symbols, results):
            pass
        else:
            symbols.pop()

    if prefix2 in elements:
        symbols.append(prefix2)
        if _get_all_compositions(word[2:], symbols, results):
            pass
        else:
            symbols.pop()

    if prefix3 in elements:
        symbols.append(prefix3)
        if _get_all_compositions(word[3:], symbols, results):
            pass
        else:
            symbols.pop()

    return False


def get_composition(word: str) -> Tuple[Tuple[str], float]:
    symbols, compositions = [], set([])
    _get_all_compositions(word.lower(), symbols, compositions)
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
            print(f"{in_word} is not elementable")
        else:
            print(f"{in_word} is elementable")
            for symbol in max_composition:
                element = elements[symbol]
                print(f"  - {element['symbol']}: {element['name']}")
            print(f"this composition has atomic mass of: {max_atomic_mass}")
        print('-' * 40)
