"""Provides methods to insert on database"""

import sqlite3
from tools import Tools

DATABASE_FILE = "database.db"

class Database:
    """Exposes methods that interacts with database
    """
    def __init__(self):
        """Constructor. Defines instance variables
        """
        self.conn = sqlite3.connect(DATABASE_FILE)
        self.conn.text_factory = str
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.create_table()
        self.tools = Tools()

    def create_table(self):
        """Creates the table in database"""
        self.cursor.execute("CREATE TABLE IF NOT EXISTS light_sensor (id INTEGER PRIMARY KEY, device VARCHAR(100), information VARCHAR(100), moment INTEGER)")
        self.conn.commit()

    def insert_light_sensor(self, device, information):
        """Inserts on change of the light sensor

        Args:
            device (str): device name
            information (str): the information that is reported

        Returns:
            int: mktime of change
        """
        moment = self.tools.get_time()
        sql_insert = "INSERT INTO light_sensor (device, information, moment) VALUES ('{}', '{}', '{}')"
        self.cursor.execute(sql_insert.format(device, information, moment))
        self.conn.commit()
        return moment

    def get_light_sensor(self, device):
        """Get the device registries given the device name

        Args:
            device (str): name of device

        Returns:
            list: all the registries from device name
        """
        sql_query = "SELECT * FROM light_sensor WHERE device = '{}' ORDER BY id"
        print("XXX", device)
        query = self.cursor.execute(sql_query.format(device))
        data = []
        if query:
            for registry in query:
                data.append({"device": registry["device"], "information": registry["information"], "mktime": registry["moment"]})
        return data
