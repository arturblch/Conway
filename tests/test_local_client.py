import pytest
from LocalProcessClient import ProcessClient
from model.Move import Move


# Cуществует  5 команд + события модели
class TestProcessClient:
    def setup(self):
        self.process_client = ProcessClient()
        self.process_client.login(1)
        self.train = self.process_client.objects.trains[
            self.process_client.player.trains[0]]

    def test_right_move_from_node(self):
        self.train.position = 10
        self.process_client.update_trains_node()
        move = Move(7, 1, self.train.idx)
        self.process_client.move(move)
        assert self.train.speed == 1
        assert self.train.line_idx == 7

    def test_right_move_from_line(self):
        self.train.position = 5
        self.process_client.update_trains_node()
        move = Move(1, 1, self.train.idx)
        self.process_client.move(move)
        assert self.train.speed == 1
        assert self.train.line_idx == 1


    def test_wrong_move_from_line(self):
        self.train.position = 9
        self.process_client.update_trains_node()
        move = Move(7, 1, self.train.idx)
        self.process_client.move(move)
        assert self.train.speed == 0
        assert self.train.line_idx == 1

    def test_wrong_move_from_node(self):
        self.train.position = 10
        self.process_client.update_trains_node()
        move = Move(3, 1, self.train.idx)
        self.process_client.move(move)
        assert self.train.speed == 0
        assert self.train.line_idx == 1

    def test_turn_wrong_speed(self):
        self.train.position = 10
        self.train.speed = 1
        self.process_client.turn()
        assert self.train.speed == 0
        assert self.train.position == 10

    def test_turn_right_speed(self):
        self.train.position = 5
        self.train.speed = 1
        self.process_client.turn()
        assert self.train.speed == 1
        assert self.train.position == 6