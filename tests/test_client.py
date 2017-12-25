import pytest
from RemoteProcessClient import RemoteProcessClient
from model.Move import Move
from tabulate import tabulate


def test_login():
    remote_process_client = RemoteProcessClient('wgforge-srv.wargaming.net',
                                                443)
    try:
        remote_process_client.write_message('LOGIN', {"name": "Test_Conway"})
    finally:
        remote_process_client.write_message('LOGOUT')
        remote_process_client.close()


def test_defult_actions():
    try:
        remote_process_client = RemoteProcessClient(
            'wgforge-srv.wargaming.net', 443)
        assert remote_process_client.login("Test12345")
        assert remote_process_client.map(1)[0] == 0
        assert remote_process_client.map(0)[0] == 0
        assert remote_process_client.turn()[0] == 0

    finally:
        remote_process_client.logout()
        remote_process_client.close()


def test_speed():
    try:
        process_client = RemoteProcessClient('wgforge-srv.wargaming.net', 443)
        player = process_client.login("Test12345")
        map_graph = process_client.read_map()
        map_graph.pos = dict(
            [(cord['idx'], (cord['x'] / 200, cord['y'] / 200))
             for cord in process_client.read_position()["coordinate"]])
        objects = process_client.read_objects()
        process_client.update_objects(objects, map_graph, player)

        process_client.move(Move(1, 1, 1))
        process_client.turn()
        process_client.turn()
        process_client.update_objects(objects, map_graph, player)
        train = objects.trains[1]
        print(" pos - ", train.position, " speed - ", train.speed)

        process_client.move(Move(1, 0, 1))
        process_client.move(Move(1, -1, 1))
        process_client.turn()
        process_client.update_objects(objects, map_graph, player)
        print(" pos - ", train.position, " speed - ", train.speed)
    finally:
        process_client.logout()
        process_client.close()

process_client.move(1, 1, 1)
process_client.turn()
process_client.turn()
process_client.update_objects()
print(" pos - ", train.position, " speed - ", train.speed)
>>> pos -  2  speed -  1

process_client.move(1, -1, 1)
process_client.turn()
process_client.update_objects()
print(" pos - ", train.position, " speed - ", train.speed)
>>> pos -  3  speed -  1

process_client.move(1, 0, 1)
process_client.move(1, -1, 1)
process_client.turn()
process_client.update_objects()
print(" pos - ", train.position, " speed - ", train.speed)
>>> pos -  2  speed -  -1