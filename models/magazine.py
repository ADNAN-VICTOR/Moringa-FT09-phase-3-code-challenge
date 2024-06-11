from database import connection 

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def articles(self):
        query = """
            SELECT * 
            FROM articles 
            WHERE magazine_id = ?
        """
        with connection.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (self.id,))
            return cursor.fetchall()

    def contributors(self):
        query = """
            SELECT authors.* 
            FROM authors 
            JOIN articles ON authors.id = articles.author_id 
            WHERE articles.magazine_id = ?
        """
        with connection.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, (self.id,))
            return cursor.fetchall()
