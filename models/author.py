from database import connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def articles(self):
        query = """
            SELECT * 
            FROM articles 
            WHERE author_id = ?
        """
        with connection.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (self.id,))
            return cursor.fetchall()

    def magazines(self):
        query = """
            SELECT magazines.* 
            FROM magazines 
            JOIN articles ON magazines.id = articles.magazine_id 
            WHERE articles.author_id = ?
        """
        with connection.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (self.id,))
            return cursor.fetchall()
