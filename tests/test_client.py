import pytest
from RemoteProcessClient import RemoteProcessClient
from model.Move import Move


def test_login():
    remote_process_client = RemoteProcessClient('wgforge-srv.wargaming.net',
                                                443)
    try:
        remote_process_client.write_message('LOGIN', {
            "name": "Test_Conway"
        })
    finally:
        remote_process_client.write_message('LOGOUT')
        remote_process_client.close()


def test_defult_actions():
    try:
        remote_process_client = RemoteProcessClient('wgforge-srv.wargaming.net',
                                                    443)
        assert remote_process_client.login("Test12345")
        assert remote_process_client.map(1)[0] == 0
        assert remote_process_client.map(0)[0] == 0
        assert remote_process_client.turn()[0] == 0

    finally:
        remote_process_client.logout()
        remote_process_client.close()
