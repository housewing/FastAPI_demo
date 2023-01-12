from model.encrypt_decrypt import EncryptDecrypt
from dotenv import load_dotenv
import pyodbc
import os

class DBconnect:
    __connect_type = {
        'SQL server': 'DRIVER={0}; SERVER={1}; DATABASE={2}; UID={3}; PWD={4}',
        'ODBC Driver 18 for SQL Server': 'DRIVER={0}; SERVER={1}; DATABASE={2}; UID={3}; PWD={4}; TrustServerCertificate=yes;'
    }

    def __init__(self, platform, db):
        load_dotenv()
        encrypt_driver = os.getenv('WIN_DRIVER') if platform != 'linux' else os.getenv('LINUX_DRIVER')
        encrypt_server = os.getenv('DB_SERVER')
        encrypt_username = os.getenv('DB_USERNAME')
        encrypt_password = os.getenv('DB_PASSWORD')

        ed = EncryptDecrypt(os.getenv('SYMMETRIC'))
        connect_info = ed.decrypt_info([encrypt_driver, encrypt_server, encrypt_username, encrypt_password])
        [self.__driver, self.__server, self.__username, self.__password] = list(connect_info)
        self.__database = db

    def __connect(self):
        connection_str = self.__connect_type.get(self.__driver).format(self.__driver,
                                                              self.__server,
                                                              self.__database,
                                                              self.__username,
                                                              self.__password)
        return pyodbc.connect(connection_str).cursor()

    def query(self, sql):
        crsr = self.__connect()
        crsr.execute(sql)
        return crsr.description, crsr.fetchall()

    def insert(self, sql, data):
        crsr = self.__connect()
        crsr.executemany(sql, data)
        crsr.commit()

    def delete(self, sql):
        crsr = self.__connect()
        crsr.execute(sql)
        crsr.commit()

if __name__ == '__main__':
    import sys
    db_connect = DBconnect(sys.platform, 'app')

    sql = 'SELECT * FROM [Order]'
    desc, data = db_connect.query(sql)
    print(data)
