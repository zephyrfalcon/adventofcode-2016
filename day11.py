# day11.py
# UNFINISHED -- more trouble than it's worth. Soz.

import itertools

initial_state = {
    "floor": 1, 
    "floors": {
        1: ["PoG", "ThG", "ThM", "PrG", "RuG", "RuM", "CoG", "CoM"],
        2: ["PoM", "PrM"],
        3: [],
        4: [],
    },
    "carrying": [],
}

states_seen = set()

def frozen_state(state):
    return (
        ('floor', state['floor']),
        ('carrying', tuple(sorted(state['carrying']))),
        ('floors', tuple([(k, tuple(sorted(v))) 
                          for (k, v) in state['floors'].items()])),
    )

def possible_moves(state):
    # in order to move, you need to carry 1 or 2 items with you to the next
    # floor (up or down). so we basically take all items present (i.e. the
    # ones you are carrying, and the ones already on the floor), select 1 or 2
    # of them, and a direction.
    objects = state['carrying'] + state['floors'][state['floor']]
    new_carrying = [x for x in objects]
    new_carrying += itertools.combinations(objects, 2)
    # XXX but the direction also matters! so we need to include the floor as
    # well.

def is_valid_floor(floor):
    for x in floor:
        if x.endswith("M"):
            matching_generator = x[:2] + "G"
            if not matching_generator in floor:
                return False
    return True

print(frozen_state(initial_state))
states_seen.add(frozen_state(initial_state))

