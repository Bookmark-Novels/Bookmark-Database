from sqlalchemy import Column, Integer, String
from sqlalchemy.orm.exc import NoResultFound

from ..db import BaseModel, Model, session_factory

class Instance(BaseModel, Model):
    """
    Represents a single Bookmark service instance.
    """
    __tablename__ = 'bookmark_instances'

    id = Column(Integer, primary_key=True)
    instance_id = Column(String(50))
    instance_name = Column(String(100))

    @staticmethod
    def exists(instance_id):
        """
        Returns true or false depending on whether or not a
        service instance with the given ID exists.
        :param instance_id: The instance ID to lookup.
        :return: True or False depending on whether or not the service exists.
        """
        with session_factory() as sess:
            try:
                sess.query(Instance).filter(
                    Instance.instance_id==instance_id
                ).one()
                return True
            except NoResultFound:
                return False

    @staticmethod
    def from_id(instance_id):
        """
        Fetches a service instance given an instance ID.
        :param instance_id: The instance ID to fetch.
        :return: An Instance object or None if there is no instance found.
        """
        with session_factory() as sess:
            try:
                instance = sess.query(Instance).filter(
                    Instance.instance_id==instance_id
                ).one()

                sess.expunge(instance)

                return instance
            except NoResultFound:
                return None
