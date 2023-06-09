CREATE TABLE IF NOT EXISTS {STORY_TABLE} (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255),
  class VARCHAR(255),
  level INTEGER,
  experience INTEGER,
  background TEXT,
  race VARCHAR(50),
  strength INTEGER,
  dexterity INTEGER,
  constitution INTEGER,
  intelligence INTEGER,
  wisdom INTEGER,
  charisma INTEGER,
  hit_points INTEGER,
  speed INTEGER,
  initiative INTEGER,
  skill_acrobatics INTEGER,
  skill_animal_handling INTEGER,
  skill_arcana INTEGER,
  skill_athletics INTEGER,
  skill_deception INTEGER,
  skill_history INTEGER,
  skill_insight INTEGER,
  skill_intimidation INTEGER,
  skill_investigation INTEGER,
  skill_medicine INTEGER,
  skill_nature INTEGER,
  skill_perception INTEGER,
  skill_performance INTEGER,
  skill_persuasion INTEGER,
  skill_religion INTEGER,
  skill_sleight_of_hand INTEGER,
  skill_stealth INTEGER,
  skill_survival INTEGER,
  inventory TEXT,
  created_at TIMESTAMP,
  updated_at TIMESTAMP
);
