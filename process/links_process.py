from connection.sqlite import Connection


class LinksProcess:
    def __init__(self):
        self.connection = Connection()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        connection = self.connection.get_connection()
        cursor = connection.cursor()

        query = """
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url VARCHAR(255) NOT NULL,
                label VARCHAR(50) NOT NULL
            );
        """

        try:
            cursor.execute(query)
            connection.commit()
        except Exception as err:
            print(f"Error when trying to create table: {err}")

        self.connection.close_connection()
        return

    def get_all_links(self):
        connection = self.connection.get_connection()
        cursor = connection.cursor()

        query = """
                SELECT * FROM links;
                """

        try:
            result = cursor.execute(query).fetchall()

        except Exception as err:
            print(f"Error when trying to get links: {err}")
            result = False

        self.connection.close_connection()
        return result

    def create_link(self, url, label):
        connection = self.connection.get_connection()
        cursor = connection.cursor()

        data = (url, label)

        query = """
                INSERT INTO links (url, label)
                VALUES (?,?);
                """
        try:
            cursor.execute(query, data)
            connection.commit()
            result = True

        except Exception as err:
            print(f"Error when trying to create links: {err}")
            result = False

        self.connection.close_connection()
        return result

    def edit_link(self, url, label, link_id):
        connection = self.connection.get_connection()
        cursor = connection.cursor()

        data = (url, label, link_id)

        query = """
                UPDATE links
                SET url = ?,
                    label = ?
                WHERE id = ?
                """
        try:
            cursor.execute(query, data)
            connection.commit()
            result = True

        except Exception as err:
            print(f"Error when trying to edit links: {err}")
            result = False

        self.connection.close_connection()
        return result

    def delete_link(self, link_id):
        connection = self.connection.get_connection()
        cursor = connection.cursor()

        query = "DELETE FROM links WHERE id=?"
        try:
            cursor.execute(query, (link_id,))
            connection.commit()
            result = True

        except Exception as err:
            print(f"Error when trying to delete links: {err}")
            result = False

        self.connection.close_connection()
        return result
