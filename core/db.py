import sqlite3
from core.config import GM_TABLE, PLAYER_TABLE, STORY_STEP_TABLE, STORY_TABLE

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect('data/database.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {STORY_TABLE} (
                                id INTEGER PRIMARY KEY,
                                title TEXT,
                                description TEXT,
                                img TEXT,
                                gm_id INTEGER,
                                FOREIGN KEY (gm_id) REFERENCES {GM_TABLE}(id)
                                )''')

        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {GM_TABLE} (
                                id INTEGER PRIMARY KEY,
                                img TEXT,
                                name TEXT
                                )''')

        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {PLAYER_TABLE} (
                                id INTEGER PRIMARY KEY,
                                name TEXT,
                                img TEXT
                                )''')

        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {STORY_STEP_TABLE} (
                                story_id INTEGER,
                                id INTEGER PRIMARY KEY,
                                text TEXT,
                                img TEXT,
                                audio TEXT,
                                action TEXT,
                                FOREIGN KEY (story_id) REFERENCES {STORY_TABLE}(id)
                                )''')
