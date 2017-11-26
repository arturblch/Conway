import pytest
from Runner import Runner
from model.Move import Move


def test_run_example():
    runner = Runner()
    runner.remote_process_client.login("Test_Conway")
    runner.remote_process_client.map(0)
    runner.remote_process_client.turn()                 # reset timer on server
    runner.remote_process_client.move(Move(1, 1, 0))
    for i in range(11):
        response = runner.remote_process_client.map(1)
        print("Position - ", response[1]["train"][0]["position"])
        runner.remote_process_client.turn()
    assert response[1]["train"][0]["position"] == 10
    runner.remote_process_client.move(Move(1, 1, 0))
    for i in range(11):
        response = runner.remote_process_client.map(1)
        print("Position - ", response[1]["train"][0]["position"])
        runner.remote_process_client.turn()
    assert response[1]["train"][0]["position"] == 10
    runner.remote_process_client.logout()
    runner.remote_process_client.close()
