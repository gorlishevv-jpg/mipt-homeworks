-- инцидент data quality: уроним NOT NULL и вставим NULL'ы → DQOps это поймает

CREATE TABLE users (
  id INT PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  age INT
);

INSERT INTO users VALUES
  (1, 'a@x.com', 25),
  (2, 'b@x.com', 31),
  (3, 'c@x.com', 28);

-- ломаем структуру: убираем NOT NULL и пихаем NULL'ы в email
ALTER TABLE users MODIFY COLUMN email VARCHAR(255) NULL;

INSERT INTO users VALUES
  (4, NULL, 19),
  (5, NULL, 22),
  (6, NULL, NULL);

-- DQOps на профилировании увидит:
-- - email completeness упал с 100% до 50%
-- - schema change (NULL стал допустим)
-- → инцидент в Incidents
