import pymysql


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "root"
        db = "Restaurant_CourseVar91"
        self.connection = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                          DictCursor)
        self.cursor = self.connection.cursor()

    def first(self):
        self.cursor.execute("select * from Manager")
        return self.cursor.fetchall()
