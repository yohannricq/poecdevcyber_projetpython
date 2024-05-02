from .db_config import load
import mysql.connector


class MyConnection:

    __connection = None
    __cursor = None

    def __init__(self) -> None:
        data_source = load()
        self.__connection = mysql.connector.connect(**data_source)
        self.__cursor = self.__connection.cursor()

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        self.__connection = value

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, value):
        self.__cursor = value

    def query(self, sql_request, params):
        self.__cursor.execute(sql_request, params)
        return self.__cursor

    def close(self):
        self.__cursor.close()
        self.__connection.close()
