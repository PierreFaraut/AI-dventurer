from core.db import Database
from core.config import STORY_TABLE
from core.models.gm import GM
from core.models.player import Player
from core.models.story_step import StoryStep


class Story:
    def __init__(self):
        self.id = None
        self.title = None
        self.desc = None
        self.img = None
        self.gm = None      # should be of class GM
        self.players = []   # should be a list of class Player
        self.content = []   # should be a list of class StoryStep

    def save(self):
        db = Database()
        if self.id is None:
            db.execute(f"INSERT INTO {STORY_TABLE} (title, desc, img) VALUES (?, ?, ?)", (self.title, self.desc, self.img))
            self.id = db.lastrowid
        else:
            db.execute(f"UPDATE {STORY_TABLE} SET title = ?, desc = ?, img = ? WHERE id = ?", (self.title, self.desc, self.img, self.id))
        db.commit()

        # Save GM
        if self.gm is not None:
            self.gm.save()

        # Save Players
        for player in self.players:
            player.save()

        # Save Content (StorySteps)
        for step in self.content:
            step.save()

    def delete(self):
        if self.id is not None:
            db = Database()
            db.execute(f"DELETE FROM {STORY_TABLE} WHERE id = ?", (self.id,))
            db.commit()
            self.id = None

            # Delete GM
            if self.gm is not None:
                self.gm.delete()

            # Delete Players
            for player in self.players:
                player.delete()

            # Delete Content (StorySteps)
            for step in self.content:
                step.delete()

    @staticmethod
    def retrieve_by_id(story_id):
        db = Database()
        db.execute(f"SELECT * FROM {STORY_TABLE} WHERE id = ?", (story_id,))
        row = db.fetchone()

        if row is not None:
            story = Story()
            story.id = row[0]
            story.title = row[1]
            story.desc = row[2]
            story.img = row[3]

            # Retrieve GM
            gm_id = row[4]
            if gm_id is not None:
                story.gm = GM.retrieve_by_id(gm_id)

            # Retrieve Players
            player_ids = row[5].split(',') if row[5] else []
            for player_id in player_ids:
                player = Player.retrieve_by_id(player_id)
                if player is not None:
                    story.players.append(player)

            # Retrieve Content (StorySteps)
            step_ids = row[6].split(',') if row[6] else []
            for step_id in step_ids:
                step = StoryStep.retrieve_by_id(step_id)
                if step is not None:
                    story.content.append(step)

            return story
        return None
