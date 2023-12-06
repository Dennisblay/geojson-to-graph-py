import psycopg2
import os


class DataBase(object):
    PASSWORD = os.environ.get("PASSWORD")

    def __init__(self, dbname, user, host):
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = os.environ.get("PASSWORD")

    def connect_to_db(self):
        return psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password, host=self.host)

    def query_db(self, query):
        if query is None:
            return
