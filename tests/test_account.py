from datetime import datetime
import os
import sys
import uuid

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bookmark_database import config

config.set_host(os.environ['DATABASE_HOST'])
config.set_user(os.environ['DATABASE_USER'])
config.set_password(os.environ['DATABASE_PASS'])
config.set_database(os.environ['DATABASE_NAME'])

from bookmark_database.db import session_factory
from bookmark_database.models.account import Account
from bookmark_database.models.accounttype import Types

def test_create_account():
    email = str(uuid.uuid4())
    account_id = Account.create('test', email, 'test')
    test_account = Account.from_id(account_id)

    assert test_account.email == email
    assert test_account.display_name == 'test'

    test_account = Account.from_email(email)

    assert test_account.id == account_id

def test_no_account():
    assert Account.from_id('aeifj409fjdijdifojasd') is None
    assert Account.from_email('q49rje0f9jsfvfv=agf9wjgidfdif') is None

def test_update_account():
    email = str(uuid.uuid4())
    account_id = Account.create('test', email, 'test')
    test_account = Account.from_id(account_id)
    new_name = 'testing'

    now = datetime.utcnow()

    test_account.set_display_name(new_name)

    assert test_account.last_updated > now
    assert test_account.display_name == new_name