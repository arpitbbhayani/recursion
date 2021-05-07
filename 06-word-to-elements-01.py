import json

with open('./data/elements.json') as fp:
    data = json.load(fp)
    elements = {element['symbol'].lower() for element in data}


def _is_chemifyable(word: str) -> bool:
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
        if _is_chemifyable(word[1:]):
            return True

    if prefix2 in elements:
        if _is_chemifyable(word[2:]):
            return True

    if prefix3 in elements:
        if _is_chemifyable(word[3:]):
            return True

    return False


def is_chemifyable(word: str) -> bool:
    return _is_chemifyable(word.lower())


if __name__ == '__main__':
    words = [
        'bose',
        'newton',
        'cooper',
        'ramanujan',
    ]

    for in_word in words:
        result = is_chemifyable(in_word)
        print(f"{in_word} {'is' if result else 'is not'} chemifyable")
