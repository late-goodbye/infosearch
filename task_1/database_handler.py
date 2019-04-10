import sqlite3


class DatabaseHandler(object):

    _create_students_table_sql = """
        CREATE TABLE IF NOT EXISTS students
        (
            id text PRIMARY KEY,
            name text,
            surname text,
            mygroup text
        );
    """

    _create_articles_table_sql = """
        CREATE TABLE IF NOT EXISTS articles
        (
            id text PRIMARY KEY,
            title text,
            keywords text,
            content text,
            url text,
            student_id text,
            FOREIGN KEY (student_id) REFERENCES students(id)
        );
    """

    def __init__(self, config):
        self.config = config
        self.conn = self.create_connection()
        self.create_table(self._create_students_table_sql)
        self.create_table(self._create_articles_table_sql)

    def create_connection(self):
        try:
            conn = sqlite3.connect(self.config.db_file + '.sqlite3')
            return conn
        except sqlite3.Error as e:
            print(e)

        return None

    def create_table(self, sql: str):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except sqlite3.Error as e:
            print(e)

    def add_student(self, student: tuple):
        sql = "INSERT INTO students(id, name, surname, mygroup) VALUES(?, ?, ?, ?);"
        cursor = self.conn.cursor()
        cursor.execute(sql, student)
        self.conn.commit()
        return student[0]

    def add_article(self, article: tuple):
        sql = "INSERT INTO articles(id, title, keywords, content, url, student_id) VALUES(?, ?, ?, ?, ?, ?);"
        cursor = self.conn.cursor()
        cursor.execute(sql, article)
        self.conn.commit()
        return cursor.lastrowid

    def get_articles(self):
        sql = "SELECT content FROM articles;"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

    def get_students(self):
        sql = "SELECT * FROM students;"
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows