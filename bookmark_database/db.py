from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

from .config import get_credentials

__all__ = ['BaseModel', 'Model', 'session_factory']

_connection_string = 'mysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(**get_credentials())
_engine = create_engine(
    _connection_string, pool_recycle=600
)

_factory = sessionmaker(bind=_engine)
_Session = scoped_session(_factory)

BaseModel = declarative_base()

@contextmanager
def session_factory():
    """
    Context function that yields a session object. This
    should be used to perform transactional database operations.
    :return: A database session object.
    """
    s = _Session()

    try:
        yield s
        s.commit()
    except:
        s.rollback()
        raise
    finally:
        s.close()

class Model():
    """
    Base model for all models. This class comes with
    several utility functions.
    """
    __tablename__ = None

    def save(self):
        """
        Upserts the current model back into the database.
        This is an atomic operation and is performed as
        a single transaction.
        """
        with session_factory() as sess:
            sess.merge(self)

    def delete(self):
        """
        Deletes the current model from the database.
        This is an atomic operation and is performed as
        a single transaction.
        """
        with session_factory() as sess:
            sess.delete(self)
