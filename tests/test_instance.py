import os
import sys
import uuid

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bookmark_database import config

config.set_host(os.environ['DATABASE_HOST'])
config.set_user(os.environ['DATABASE_USER'])
config.set_password(os.environ['DATABASE_PASS'])
config.set_database(os.environ['DATABASE_NAME'])

from bookmark_database.models.instance import Instance

def test_instance():
    instance_id = str(uuid.uuid4())
    instance_name = str(uuid.uuid4())

    Instance(instance_id=instance_id, instance_name=instance_name).save()

    assert Instance.exists(instance_id)
    assert Instance.from_id(instance_id).instance_name == instance_name

def test_no_instnance():
    assert Instance.exists('faofijoeifjodifjodifj') is False
    assert Instance.from_id('afiejofija9f49tjbjdifjdf') is None
