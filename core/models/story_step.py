from core.db import Database
from core.config import STORY_STEP_TABLE

class StoryStep:
    def __init__(self):
        self.story_id = None
        self.id = None
        self.text = None
        self.img = None
        self.audio = None
        self.action = 'text'

    def save(self):
        db = Database()
        if self.id is None:
            db.execute(f"INSERT INTO {STORY_STEP_TABLE} (story_id, text, img, audio, action) VALUES (?, ?, ?, ?, ?)",
                       (self.story_id, self.text, self.img, self.audio, self.action))
            self.id = db.lastrowid
        else:
            db.execute(f"UPDATE {STORY_STEP_TABLE} SET story_id = ?, text = ?, img = ?, audio = ?, action = ? WHERE id = ?",
                       (self.story_id, self.text, self.img, self.audio, self.action, self.id))
        db.commit()

    def delete(self):
        if self.id is not None:
            db = Database()
            db.execute(f"DELETE FROM {STORY_STEP_TABLE} WHERE id = ?", (self.id,))
            db.commit()
            self.id = None

    @staticmethod
    def retrieve_by_id(step_id):
        db = Database()
        db.execute(f"SELECT * FROM {STORY_STEP_TABLE} WHERE id = ?", (step_id,))
        row = db.fetchone()

        if row is not None:
            step = StoryStep()
            step.story_id = row[1]
            step.id = row[0]
            step.text = row[2]
            step.img = row[3]
            step.audio = row[4]
            step.action = row[5]
            return step
        return None