import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bookmark_database import config

config.set_host(os.environ['DATABASE_HOST'])
config.set_user(os.environ['DATABASE_USER'])
config.set_password(os.environ['DATABASE_PASS'])
config.set_database(os.environ['DATABASE_NAME'])

from bookmark_database.db import session_factory
from bookmark_database.models.accounttype import AccountType, Types

def test_account_type():
    with session_factory() as session:
        account_type = session.query(AccountType).filter(
            AccountType.id==Types.Admin
        ).one()

        assert account_type.display_name == 'Admin'