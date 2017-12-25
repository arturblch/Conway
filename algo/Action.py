# from World import (translate, in_bounds, valid, tile)

class Action(object):
    """docstring for Action"""
    def __init__(self, pos, direct):
        self.from_ = pos
        self.where_ = direct

def valid(action, world):
    if not world.get_agent(action.from_):
        return False

    dest = translate(action.from_, action.where_)
    if not in_bounds(dest, world.map()):
        return False

    return world.get(dest) == tile.free

def apply(action, world):
    assert valid(action, world)

    agent = world.get_agent(action.from_)
    world.remove_agent(action.from_)
    world.put_agent(translate(agent.from_, agent.where_, agent))

    return world
