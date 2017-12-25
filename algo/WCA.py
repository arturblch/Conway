from .A_star import A_star


class WCAStar(A_star):
    """
    Implementation of WCA
    """

    def __init__(self,
                 map_graph,
                 towns,
                 trains_pos,
                 reserv_pos,
                 invalid_field,
                 from_,
                 to,
                 cur_tick,
                 window=10):
        super().__init__(map_graph, from_, to, cur_tick, window)
        self.map = map_graph  # need lines property for func get_neighbors
        self.towns = towns
        self.trains_pos = trains_pos
        self._reserv_table = reserv_pos
        self._invalid_field = invalid_field
        self.window = window

    def passable(self, from_pos, to_pos, time):

        if to_pos in self._invalid_field:
            print("inval")
            return False

        for train_id, reserv_path in self._reserv_table.items():
            if time + 1 not in reserv_path.keys():
                continue
            elif (to_pos == reserv_path[time + 1] and to_pos not in self.towns
                  or to_pos == reserv_path[time]
                  and from_pos == reserv_path[time + 1]):
                return False

        return True

