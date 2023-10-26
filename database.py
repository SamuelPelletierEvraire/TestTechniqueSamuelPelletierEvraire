import os

import psycopg2


class Database:
    def __init__(self):
        self.host = os.getenv('HOST')
        self.db = os.getenv('DATABASE')
        self.user = os.getenv('USER')
        self.password = os.getenv('PASSWORD')
        self.port = os.getenv('PORT')
        self.connection = None
        self.connect()

    def connect(self):
        try:
            print('connection to the database')
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.db,
                user=self.user,
                password=self.password,
                port=self.port)

        except(Exception, psycopg2.DatabaseError)as error:
            print(error)