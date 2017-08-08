from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

from locksmith import unlock, get_credentials

unlock(locksmith_token)
credentials = get_credentials('bookmark_database')

eng = 'mysql://{username}:{password}@{host}:{port}/{name}?charset=utf8'.format(**credentials)
engine = create_engine(
    eng, pool_recycle=600
)

factory = sessionmaker(bind=engine)
Session = scoped_session(factory)

BaseModel = declarative_base()

@contextmanager
def session_factory():
    s = Session()

    try:
        yield s
        s.commit()
    except:
        s.rollback()
        raise
    finally:
        s.close()

class Model():
__tablename__ = None

def save(self):
    with session_factory() as sess:
        sess.merge(self)

def delete(self):
    with session_factory() as sess:
        sess.delete(self)