import pytest
from RemoteProcessClient import RemoteProcessClient
from model.Move import Move


def test_write_message():
    remote_process_client = RemoteProcessClient('wgforge-srv.wargaming.net',
                                                443)
    assert remote_process_client.write_message('LOGIN', {
        "name": "Test_Conway"
    })[0] == 0
    remote_process_client.write_message('LOGOUT')
    remote_process_client.close()


def test_defult_example():
    remote_process_client = RemoteProcessClient('wgforge-srv.wargaming.net',
                                                443)
    assert remote_process_client.login("Test12345")[0] == 0
    assert remote_process_client.move(Move(1, 1, 0))[0] == 0
    assert remote_process_client.map(1)[0] == 0
    assert remote_process_client.turn()[0] == 0
    remote_process_client.logout()
    remote_process_client.close()
