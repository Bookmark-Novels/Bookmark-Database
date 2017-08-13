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
from bookmark_database.models.nonce import Nonce

origin_id = str(uuid.uuid4())
instance_name = str(uuid.uuid4())

def test_nonce():
    Instance(instance_id=origin_id, instance_name=instance_name).save()

    challenge = Nonce.create(origin_id)

    assert Nonce.use(challenge, origin_id) is True
    assert Nonce.use(challenge, origin_id) is False

def test_fake_nonce():
    assert Nonce.use('aijfoisdjfoiajoi4jofijijfiojf', origin_id) is False
    assert Nonce.use('aorjiwdfodifjo', 'ai4jfar90fajfvdifjd') is False
