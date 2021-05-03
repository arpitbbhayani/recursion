import os
import time
import random

layout = \
    """
            _____
           /     \\
          /       \\
    ,----(         )----.
   /      \\       /      \\
  /        \\_____/        \\
  \\        /     \\        /
   \\      /       \\      /
    )----(         )----(
   /      \\       /      \\
  /        \\_____/        \\
  \\        /     \\        /
   \\      /       \\      /
    `----(         )----'
          \\       /
           \\_____/


    """.split('\n')

layout = [
    list(row) for row in layout
]

# bounding chars of the hexagon
bound_chars = ['\\', '/', '\'', '_', '-', '.', ',', '`', '(', ')']

# points within each of the hexagon
points = [
    (4, 14),
    (6, 6),
    (6, 22),
    (9, 14),
    (11, 6),
    (11, 22),
    (14, 14),
]


def print_layout():
    os.system('clear')
    print("\n".join(["".join(row) for row in layout]))


def _flood(x, y):
    # check for the bounds
    if x >= len(layout) or x < 0 or y < 0 or y >= len(layout[x]):
        return

    # check for the bounds within each hexagon
    if layout[x][y] in bound_chars:
        return

    # check if already filled
    if layout[x][y] == '#':
        return

    # fix the position
    layout[x][y] = '#'

    # add sleep
    time.sleep(0.01)

    # render the layout
    print_layout()

    # recursively invoke the function
    # the core of the algorithm
    _flood(x + 1, y)
    _flood(x - 1, y)
    _flood(x, y + 1)
    _flood(x, y - 1)


def flood(x, y):
    _flood(x, y)


# randomly shuffle the points
random.shuffle(points)

# do flood fill for each hexagon
for X, Y in points:
    flood(X, Y)
