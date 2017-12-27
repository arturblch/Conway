from time import time
from pprint import pprint

from algo.PathSolver import solved, PathSolver
from algo.WHCA import WHCA
from algo.World import get_world

from GUI import GUI



def get_predictor():
    return None

def get_solver():
    predictor = None
    obstacle_penalty = 0
    obstacle_treshold = 1.0

    window = 5

    avlid_obscle = False

    rejoin_limit = 30

    return WHCA(
        window,
        rejoin_limit,
        predictor,
        obstacle_penalty,
        obstacle_treshold
        )


if __name__ == '__main__':
    world = get_world()

    trains = world.my_trains()
    trains[1].target = 5
    trains[2].target = 15

    trains[1].point = 1
    trains[2].point = 1



    solver = get_solver()
    gui = GUI(*(world.get_parts()))

    limit = 99
    start_time = time()

    while not solved(world):
        gui.turn()
        if((not gui.paused) or gui.onestep):
            world.next_tick()
            solver.step(world)      # apply consist move

            if (limit > 0 and world.tick() > limit):
                break

    stop_time = time()

    result = dict()

    result.update({'time_ms' : (stop_time - start_time) / 1000})
    result.update({'tick' : world.tick()})

    algo_result = dict()

    names = solver.stat_names()
    values = solver.stat_values()

    if len(names) == len(values):
        for i in range(len(names)):
            algo_result.update({names[i] : values[i]})

    pprint(result)
    pprint(algo_result)
