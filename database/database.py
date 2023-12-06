import psycopg2
import os


class Database:
    def __init__(self, dbname, user, host):
        self.dbname = dbname
        self.user = user
        self.host = host
        self.password = os.environ.get("PASSWORD")
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(dbname=self.dbname, user=self.user, password=self.password,
                                               host=self.host)
            return True
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")
            return False

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, fetch=False):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            if fetch:
                return cursor.fetchall()
            else:
                self.connection.commit()
            cursor.close()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()


db = Database(dbname='analysis', user='postgres', host='localhost')
connected = db.connect()

if connected:
    # Execute a query and fetch the result
    result = db.execute_query("SELECT * FROM persondetails", fetch=True)
    print(result)

    # Execute a query without fetching result (e.g., INSERT, UPDATE, DELETE)
    # db.execute_query("INSERT INTO your_table (column1, column2) VALUES (value1, value2)")

    # Close the connection when done
    db.close()
