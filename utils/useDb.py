from utils import Database


class UseDb:
    def __init__(self, config):
        self.config = config

    def __enter__(self):
        self.conn = Database(self.config)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.conn
