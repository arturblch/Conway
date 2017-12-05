import pytest
from RemoteRunner import Runner


def test_run_example():
    runner = Runner("Test_Conway")
    assert runner.run() == False #  player.is_alive == False
