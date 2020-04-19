import pymysql


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "root"
        db = "Restaurant_CourseVar91"
        self.__connection = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.
                                          DictCursor)
        self.__cursor = self.__connection.cursor()

    def execute(self, commands):
        result = []
        for query in commands:
            if query.strip() != '':
                self.__cursor.execute(query)
                result.append(self.__cursor.fetchall())
        return result
