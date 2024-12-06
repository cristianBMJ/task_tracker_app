PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL
            );
INSERT INTO users VALUES(1,'Cristian_0');
INSERT INTO users VALUES(2,'cristian_0');
INSERT INTO users VALUES(3,'cristian_1');
CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                task_name TEXT NOT NULL,
                completed INTEGER NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
INSERT INTO tasks VALUES(1,1,'Sleep',0,'2024-06-27');
INSERT INTO tasks VALUES(2,1,'Sleep',0,'2024-06-27');
INSERT INTO tasks VALUES(3,1,'Wake Early',0,'2024-06-27');
INSERT INTO tasks VALUES(4,2,'',0,'2024-06-27');
INSERT INTO tasks VALUES(5,2,'sleep',0,'2024-06-27');
INSERT INTO tasks VALUES(6,2,'English',0,'2024-06-27');
INSERT INTO tasks VALUES(7,1,'',0,'2024-07-02');
INSERT INTO tasks VALUES(8,1,'English Listening',0,'2024-07-02');
INSERT INTO tasks VALUES(9,3,'test task_tracker',0,'2024-07-02');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('users',3);
INSERT INTO sqlite_sequence VALUES('tasks',9);
COMMIT;
