import sys
import requests

response = requests.get(
    'https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json')
elements = response.json()["elements"]
periodic_table = {element['symbol'].lower(): element for element in elements}

# symbols = set(['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al',
#                'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe',
#                'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y',
#                'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te',
#                'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb',
#                'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt',
#                'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa',
#                'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf',
#                'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts',
#                'Og', 'Uue'])


def _chemi_name(word) -> str:
    if not word:
        return True

    ch1, ch2, ch3 = word[:1], word[:2], word[:3]

    if ch1 in periodic_table:
        if _chemi_name(word[1:]):
            return True

    if ch2 in periodic_table:
        if _chemi_name(word[2:]):
            return True

    if ch3 in periodic_table:
        if _chemi_name(word[3:]):
            return True

    return False


def chemi_name(word: str) -> str:
    return _chemi_name(word.lower())


print(chemi_name(sys.argv[1]))
