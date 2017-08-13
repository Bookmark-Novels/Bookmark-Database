from datetime import datetime, timedelta
import uuid

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm.exc import NoResultFound

from ..db import BaseModel, Model, session_factory

class Nonce(BaseModel, Model):
    """
    Represents a request nonce.
    """
    __tablename__ = 'bookmark_nonces'

    id = Column(Integer, primary_key=True)
    nonce = Column(String(100))
    origin = Column(String(100))
    is_active = Column(Boolean)
    expires = Column(DateTime)

    @staticmethod
    def use(challenge, origin_id):
        """
        Attempts to use the nonce with the given challenge
        and origin instance ID combination.
        :param challenge: The nonce challenge to test against.
        :param origin_id: The instance ID of the origin service.
        :return: True or False depending on whether or not usage
                 of the nonce was successful.
        """
        with session_factory() as sess:
            try:
                n = sess.query(Nonce).filter(
                    Nonce.nonce==challenge,
                    Nonce.origin==origin_id,
                    Nonce.is_active==True,
                    Nonce.expires > datetime.utcnow()
                ).one()

                n.is_active = False
                n.save()

                return True
            except NoResultFound:
                return False

    @staticmethod
    def create(origin_id):
        """
        Creates a Nonce object for a given origin instance ID.
        :param origin_id: The instance ID of the origin service to bind
                       the nonce to.
        :return: The challenge for the newly created nonce.
        """
        nonce = uuid.uuid4()

        Nonce(
            nonce=nonce,
            origin=origin_id,
            is_active=True,
            expires=datetime.utcnow() + timedelta(minutes=5)
        ).save()

        return str(nonce)
