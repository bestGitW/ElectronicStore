import sqlite3


class Database:
    def __init__(self, db_path='shop_database.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users(
        id int NOT NULL,
        phone text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id: int, phone: str = None):
        sql = 'INSERT INTO Users(id, phone) VALUES(?, ?)'
        parameters = (id, phone)
        self.execute(sql, parameters, commit=True)

    def select_user_info(self, **kwargs) -> list:
        sql = 'SELECT * FROM Users WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def select_all_users(self) -> list:
        sql = "SELECT * FROM Users"
        return self.execute(sql, fetchall=True)

    def update_user_phone(self, id: int, phone: str):
        sql = "UPDATE Users SET phone=? WHERE id=?"
        return self.execute(sql, parameters=(phone, id), commit=True)

    def delete_user(self, **kwargs):
        sql = "DELETE FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def create_table_items(self):
        sql = """
        CREATE TABLE Items(
        id int NOT NULL,
        name text,
        count int,
        photo_path text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_item(self, id: int, name: str = None, count: int = 0, photo_path: str = ''):
        sql = 'INSERT INTO Items(id, name, count, photo_path) VALUES(?, ?, ?, ?)'
        parameters = (id, name, count, photo_path)
        self.execute(sql, parameters, commit=True)

    def select_items_info(self, **kwargs) -> list:
        sql = 'SELECT * FROM Items WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def select_all_items(self) -> list:
        sql = "SELECT * FROM Items"
        return self.execute(sql, fetchall=True)

    def update_item_count(self, id: int, count: str):
        sql = "UPDATE Items SET count=? WHERE id=?"
        return self.execute(sql, parameters=(count, id), commit=True)

    def get_items_count(self) -> int:
        sql = "SELECT * FROM Items"
        return len(self.execute(sql, fetchall=True))

    def create_table_basket(self):
        sql = """
        CREATE TABLE Basket(
        id int NOT NULL,
        user_basket text,
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_item_basket(self, id: int, user_basket: str = ''):
        sql = 'INSERT INTO Basket(id, user_basket) VALUES(?, ?)'
        parameters = (id, user_basket)
        self.execute(sql, parameters, commit=True)

    def select_user_basket(self, **kwargs) -> tuple[int, str]:
        sql = 'SELECT * FROM Basket WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        data = self.execute(sql, parameters, fetchone=True)
        if data is None:
            self.add_item_basket(id=kwargs['id'])
            data = (kwargs['id'], '')
        return data

    def update_basket(self, id: int, user_basket: str):
        sql = "UPDATE Basket SET user_basket=? WHERE id=?"
        return self.execute(sql, parameters=(user_basket, id), commit=True)

    def select_all_basket(self) -> list:
        sql = "SELECT * FROM Basket"
        return self.execute(sql, fetchall=True)

    def delete_all(self):
        self.execute("DELETE FROM Users WHERE True", commit=True)
        self.execute("DELETE FROM Items WHERE True", commit=True)
        self.execute("DELETE FROM Basket WHERE True", commit=True)

    def drop_all(self):
        self.execute("DROP TABLE Users", commit=True)
        self.execute("DROP TABLE Items", commit=True)
        self.execute("DROP TABLE Basket", commit=True)

    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
