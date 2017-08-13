from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm.exc import NoResultFound

from .accounttype import Types
from ..db import BaseModel, Model, session_factory


class Account(BaseModel, Model):
    """
    Represents a Bookmark account.
    """
    __tablename__ = 'bookmark_accounts'

    id = Column(Integer, primary_key=True)
    display_name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    is_active = Column(Boolean, default=True)
    account_type = Column(Integer, default=Types.Native)
    timezone = Column(String(100), default='N/A')
    created_at = Column(DateTime)
    last_updated = Column(DateTime)

    def set_display_name(self, new_name):
        """
        Sets an account's display name to something else.
        :param new_name: The new display name to use for the account.
        """
        with session_factory():
            self.display_name = new_name
            self.save()
            self._update_last_updated()

    def set_email(self, new_email):
        """
        Sets an account's email address to something else.
        :param new_email: The new email address to use for the account.
        """
        with session_factory():
            self.email = new_email
            self.save()
            self._update_last_updated()

    def set_password(self, new_password):
        """
        Sets an account's password to something else.
        Important: This method expects the provided password to already be
        well hashed.
        :param new_password: The new password to use for the account.
        """
        with session_factory():
            self.email = new_password
            self.save()
            self._update_last_updated()

    def set_active_state(self, active_state):
        """
        Sets an account's active state to something else
        :param active_state: The new active state for the account.
        """
        with session_factory():
            self.is_active = active_state
            self.save()
            self._update_last_updated()

    def set_timezone(self, timezone):
        """
        Sets an account's timezone to something else
        :param timezone: The new timezone for the account.
        """
        with session_factory():
            self.timezone = timezone
            self.save()
            self._update_last_updated()

    @staticmethod
    def from_id(account_id):
        """
        Fetches and returns an Account object given an
        account ID.
        :param account_id: The ID to fetch the account for.
        :return: An Account object or None if there is no account found.
        """
        with session_factory() as sess:
            try:
                account = sess.query(Account).filter(
                    Account.id == account_id
                ).one()

                sess.expunge(account)

                return account
            except NoResultFound:
                return None

    @staticmethod
    def from_email(email):
        """
        Fetches and returns an Account object given an
        email address.
        :param email: The email address to fetch the account for.
        :return: An Account object or None if there is no account found.
        """
        with session_factory() as sess:
            try:
                account = sess.query(Account).filter(
                    Account.email == email
                ).one()

                sess.expunge(account)

                return account
            except NoResultFound:
                return None

    @staticmethod
    def create(name, email, password):
        """
        Creates a new Bookmark account using the provided information.
        :param name: The display name for the account.
        :param email: The email address for the account.
        :param password: The password for the account.
        :return: The ID of the new user account.
        """
        now = datetime.utcnow()
        acc = Account(
            display_name=name,
            email=email,
            password=password,
            created_at=now,
            last_updated=now
        ).save()

        return Account.from_email(email).id

    def _update_last_updated(self):
        """
        Updates the last updated timestamp for an account.
        """
        with session_factory() as sess:
            self.last_updated = datetime.utcnow()
            self.save()
