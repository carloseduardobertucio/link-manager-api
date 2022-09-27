import sqlite3


class Connection:
    def __init__(self):
        self.database_path = "./database.db"
        self.connection = None

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_connection(self):
        try:
            self.connection = sqlite3.connect(self.database_path)
            self.connection.row_factory = self.dict_factory
            return self.connection

        except Exception as err:
            print(f"Error when try to connect to database: {err}")

    def close_connection(self):
        self.connection.close()
