import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bookmark_database import config

def test_requires_int():
    def try_port(test_value):
        try:
            config.set_port(test_value)
            assert False
        except ValueError:
            pass

    def try_pool_recycle(test_value):
        try:
            config.set_pool_recycle(test_value)
            assert False
        except ValueError:
            pass

    invalid_values = [None, False, True, '234019']

    for value in invalid_values:
        try_port(value)
        try_pool_recycle(value)
