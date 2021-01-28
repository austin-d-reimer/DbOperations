"""
Contains the DBOperations class and DB context manager
Author: Austin Reimer
"""
import sqlite3


class DBOperations:
    """
    A class used to create the DB, and do CRUD operations on it.
    Author: Austin Reimer
    """

    db_name = "contacts.db"
    table_name = "contact"

    def create_DB(self):
        """
        The method is used to create the SQLite DB if it doesn't exist.
        Author: Austin Reimer
        """
        try:
            with Open_DB(self.db_name) as db:
                db.execute(
                    f""" CREATE TABLE IF NOT EXISTS {self.table_name}
                        (id integer primary key autoincrement not null,
                        name string not null,
                        phoneNumber string not null
                        );
                    """
                )
        except Exception as error:
            print("DBOperations CreateDB", error)

    def add_contact(self, name, phoneNumber):
        sql = f"""
            INSERT INTO {self.table_name}
            (name, phoneNumber)
            values(?,?)
        """
        with Open_DB(self.db_name) as db:
            db.execute(sql, (name, phoneNumber))

    def read_from_db(self):
        """
        The method that is used to read from the Database.
        id, data, year, month, max_temp, min_temp, mean_temp
        Author: Austin Reimer
        """
        try:
            sql = f"SELECT name, phoneNumber FROM {self.table_name} "

            with Open_DB(self.db_name) as db:
                db.execute(sql)
                return_value = db.fetchall()
            return return_value
        except Exception as error:
            print("DBOperations read_from_db", error)

    def delete_all_rows(self):
        """
        Used to delete all rows from the database.
        Author: Austin Reimer
        """
        try:
            with Open_DB(self.db_name) as db:
                db.execute(f"DELETE FROM {self.table_name}")
        except Exception as error:
            print("DBOperations delete_db", error)


class Open_DB:
    """
    The context manager to manage the connection to the Database.
    Author: Austin Reimer
    """

    def __init__(self, name):
        """
        Sets the initial setting need for a db Connection.
        Author: Austin Reimer
        """
        try:
            self.name = name
            self.conn = None
            self.cursor = None
        except Exception as error:
            print("Open_DB init", error)

    def __enter__(self):
        """
        Used to set up the connection to the Database.
        Author: Austin Reimer
        """
        try:
            self.conn = sqlite3.connect(self.name)
            self.cursor = self.conn.cursor()
            return self.cursor
        except Exception as error:
            print("Open_DB enter", error)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        Used to taredown the connection to the database.
        Author: Austin Reimer
        """
        try:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        except Exception as error:
            print("Open_DB exit", error)
