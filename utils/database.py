import pymysql


class Database:
    def __init__(self, config):
        self.__connection = pymysql.connect(host=config['host'],
                                            user=config['user'],
                                            password=config['password'],
                                            db=config['db'],
                                            cursorclass=pymysql.cursors.DictCursor)
        self.__cursor = self.__connection.cursor()

    def __del__(self):
        self.__connection.close()

    def execute(self, commands, *args):
        result = []
        for query in commands:
            if args:
                self.__cursor.execute(query, args)
                self.__connection.commit()
            else:
                self.__cursor.execute(query)
                self.__connection.commit()
            result.append(self.__cursor.fetchall())
        return result
