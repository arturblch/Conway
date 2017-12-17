from time import time
from pprint import pprint
from PathSolver import solved, PathSolver


def get_predictor():
    pass

def get_solver():
    pass

def get_world():
    pass





if __name__ == '__main__':
    world = get_world()
    solver = get_solver()

    limit = 99
    start_time = time()

    while not solved(world):
        world.next_tick()
        solver.step(world)

        if (limit > 0 and world.tick() > limit):
            break

    stop_time = time()

    result = dict()

    result.update({'time_ms' : (stop_time - start_time) / 1000})
    result.update({'tick' : world.tick()})
    result.update({'success' : solved()})

    algo_result = dict()

    names = solver.stat_names()
    values = solver.stat_values()

    if len(names) == len(values):
        for i in range(len(names)):
            algo_result.update({names[i] : values[i]})

    pprint(result)
    pprint(algo_result)
