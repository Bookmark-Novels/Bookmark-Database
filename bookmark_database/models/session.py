from datetime import datetime
import uuid

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm.exc import NoResultFound

from ..db import BaseModel, Model, session_factory

class Session(BaseModel, Model):
    """
    Represents a Bookmark user session.
    """
    __tablename__ = 'bookmark_sessions'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    session_key = Column(String(255))
    ip_address = Column(String(100))
    last_use = Column(DateTime)
    is_active = Column(Boolean)

    def update_ip(self, ip):
        """
        Updates the last-seen IP address for the session.
        """
        self.ip_address = ip
        self.save()

    def use(self):
        """
        Sets the last use timestamp for the session
        to be the current time. If the session is not active
        then nothing will happen.
        :return: Returns True or False depending on whether
                 or not the session is active.
        """
        if self.is_active:
            self.last_use = datetime.utcnow()
            self.save()
            return True
        return False

    def invalidate(self):
        """
        Invalidates the session. Sets is_active to False.
        """
        self.is_active = False
        self.save()

    @staticmethod
    def is_valid(key):
        """
        Checks whether or not a given session key is valid.
        A key is valid if there exists a session with the given key
        that is currently active.
        :param key: The session key to check.
        :return: True or False depending on whether or not the session is valid.
        """
        with session_factory() as sess:
            try:
                sess.query(Session).filter(
                    Session.session_key == key,
                    Session.is_active == True
                ).one()
                return True
            except NoResultFound:
                return False

    @staticmethod
    def from_key(key):
        """
        Fetches a session object using a given session key.
        :param key: The session key to use when fetching.
        :return: A Session object or None if a session does not exist.
        """
        with session_factory() as sess:
            try:
                session = sess.query(Session).filter(
                    Session.session_key == key
                ).one()
                sess.expunge(session)
                return session
            except NoResultFound:
                return None

    @staticmethod
    def create(account_id, ip):
        """
        Creates a new Session object and binds it to the given
        account ID and IP address.
        :param account_id: The account ID to bind the session to.
        :param ip: The IP address to bind the session to.
        :return: The key for the newly created session.
        """
        session_key = uuid.uuid4()

        Session(
            account_id=account_id,
            session_key=session_key,
            ip_address=ip,
            last_use=datetime.utcnow(),
            is_active=True
        ).save()

        return str(session_key)
