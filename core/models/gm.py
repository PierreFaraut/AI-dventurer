from core.db import Database
from core.config import GM_TABLE

class GM:
    def __init__(self):
        self.id = None
        self.img = None
        self.name = None

    def save(self):
        db = Database()
        if self.id is None:
            db.execute(f"INSERT INTO {GM_TABLE} (img, name) VALUES (?, ?)", (self.img, self.name))
            self.id = db.lastrowid
        else:
            db.execute(f"UPDATE {GM_TABLE} SET img = ?, name = ? WHERE id = ?", (self.img, self.name, self.id))
        db.commit()

    def delete(self):
        if self.id is not None:
            db = Database()
            db.execute(f"DELETE FROM {GM_TABLE} WHERE id = ?", (self.id,))
            db.commit()
            self.id = None

    @staticmethod
    def retrieve_by_id(gm_id):
        db = Database()
        db.execute(f"SELECT * FROM {GM_TABLE} WHERE id = ?", (gm_id,))
        row = db.fetchone()
        
        if row is not None:
            gm = GM()
            gm.id = row[0]
            gm.img = row[1]
            gm.name = row[2]
            return gm
        return None
