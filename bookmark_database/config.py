__all__ = ['set_port', 'set_database', 'set_password', 'set_user', 'get_credentials', 'set_host', 'set_pool_recycle', 'get_pool_recycle']

_user = None
_password = None
_database = None
_host = None
_port = 3306
_pool_recycle = 600

def set_user(u):
    """
    Sets the user to use when connecting to the database.
    :param u: The name of the user.
    """
    global _user
    _user = u

def set_password(p):
    """
    Sets the password to use when connecting to the database.
    :param p: The password to use.
    """
    global _password
    _password = p

def set_database(d):
    """
    Sets the database to use when connecting.
    :param d: The name of the database.
    """
    global _database
    _database = d

def set_host(h):
    """
    Sets the host to use when connecting to the database.
    :param h: The host address of the database server.
    """
    global _host
    _host = h

def set_port(p):
    """
    Sets the port to use when connecting to the database. This defaults
    to port 3306.
    :param p: The port to use defaulting to 3306.
    """
    _require_int(p)

    global _port
    _port = p

def set_pool_recycle(p):
    """
    Sets the pool recycle interval to use when pooling MySQL connections.
    This defaults to 600 seconds or 10 minutes.
    :param p: The pool recycle interval in seconds.
    :return:
    """
    _require_int(p)

    global _pool_recycle
    _pool_recycle = p

def get_credentials():
    """
    Fetches the credential configuration to use when building
    the database connection string.
    :return: A dictionary containing database connection information.
    """
    return {
        'user': _user,
        'password': _password,
        'database': _database,
        'host': _host,
        'port': _port
    }

def get_pool_recycle():
    """
    Fetches the connection pool recycle interval.
    :return: The recycle interval.
    """
    return _pool_recycle

def _require_int(value):
    """
    Errors if the given value is not some form of integer.
    :param value: The value to test.
    """
    # Booleans are integers in Python.
    if not isinstance(value, int) or value is True or value is False:
        raise ValueError('Expected integer value.')
