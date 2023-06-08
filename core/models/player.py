from core.db import Database
from core.config import PLAYER_TABLE

class Player:
    def __init__(self):
        self.id = None
        self.name = None
        self.img = None

    def save(self):
        db = Database()
        if self.id is None:
            db.execute(f"INSERT INTO {PLAYER_TABLE} (name, img) VALUES (?, ?)", (self.name, self.img))
            self.id = db.lastrowid
        else:
            db.execute(f"UPDATE {PLAYER_TABLE} SET name = ?, img = ? WHERE id = ?", (self.name, self.img, self.id))
        db.commit()

    def delete(self):
        if self.id is not None:
            db = Database()
            db.execute(f"DELETE FROM {PLAYER_TABLE} WHERE id = ?", (self.id,))
            db.commit()
            self.id = None

    @staticmethod
    def retrieve_by_id(player_id):
        db = Database()
        db.execute(f"SELECT * FROM {PLAYER_TABLE} WHERE id = ?", (player_id,))
        row = db.fetchone()

        if row is not None:
            player = Player()
            player.id = row[0]
            player.name = row[1]
            player.img = row[2]
            return player
        return None
