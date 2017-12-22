from .A_star import A_star

class WCAStar(A_star):
    """
    Implementation of WCA
    """

    def __init__(self, map_graph, towns, reserv_pos, invalid_field,
                 from_, to, cur_tick, window=10):
        super().__init__(map_graph, from_, to, cur_tick, window)
        self.map = map_graph  # need lines property for func get_neighbors
        self.towns = towns
        self._reserv_table = reserv_pos
        self._invalid_field = invalid_field
        self.window = window

    def passable(self, from_pos, to_pos, time):

        if any(to_pos == pos for pos in self._invalid_field):
            return False
        for reserv_path in self._reserv_table.values():
            if time+1 not in reserv_path.keys():
                continue
            if any(to_pos == town for town in self.towns):
                continue

            if (to_pos == reserv_path[time+1] or to_pos == reserv_path[time]
                    and from_pos == reserv_path[time+1]):
                return False

        return True
