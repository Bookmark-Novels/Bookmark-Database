import os
import sys
import uuid

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bookmark_database import config

config.set_host(os.environ['DATABASE_HOST'])
config.set_user(os.environ['DATABASE_USER'])
config.set_password(os.environ['DATABASE_PASS'])
config.set_database(os.environ['DATABASE_NAME'])

from bookmark_database.models.account import Account
from bookmark_database.models.session import Session

def test_session():
    email = str(uuid.uuid4())
    ip_address = 'blah'
    ip_address2 = 'blahblah'
    test_account_id = Account.create('test', email, 'test')
    session_key = Session.create(test_account_id, ip_address)

    test_s = Session.from_key(session_key)

    assert test_s is not None

    assert test_s.account_id == test_account_id
    assert test_s.ip_address == ip_address
    assert test_s.is_active is True

    test_s.update_ip(ip_address2)

    test_s = Session.from_key(session_key)

    assert test_s.ip_address == ip_address2
    assert test_s.use() is True

    test_s.invalidate()

    assert test_s.use() is False
    assert Session.is_valid(session_key) is False
