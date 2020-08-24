import sqlite3
import threading

#元类方式
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj
db1 = Database().connect()
db2 = Database().connect()
print("database objects db1: ", db1)
print("Database objects db2:", db2)

#####new方法
class Singleton(object):
    """To do singleton exercese
    return one instance for different
    :param object the instance
    :param exa1 the example
    """
    _instance_lock = threading.Lock()
    connection = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

    def connect(self):
        """

        :return: dabase connection obj
        """
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()

        return self.cursorobj

db3 = Singleton().connect()
db4 = Singleton().connect()
print("database objects db3: ", db3)
print("Database objects db4:", db4)
print(db4.__doc__)


class HealthCheck(object):
    """Health Check for singleton exercise"""
    _instances = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instances:
            HealthCheck._instances = super(HealthCheck,
                cls).__new__(cls, *args, **kwargs)

        return HealthCheck._instances

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append("1")
        self._servers.append("2")
        self._servers.append("3")
        self._servers.append("4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("5")


hc1 = HealthCheck()
hc2 = HealthCheck()
hc1.addServer()
print(hc1._servers)
hc2.changeServer()
print(hc2._servers)
