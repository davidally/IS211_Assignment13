CREATE TABLE students(
id INTEGER PRIMARY KEY ASC,
first_name TEXT,
last_name TEXT)

CREATE TABLE quizzes(
id INTEGER PRIMARY KEY ASC,
subject TEXT,
questions INTEGER,
date TEXT)


CREATE TABLE results(
student_id INTEGER,
quiz_id INTEGER,
grade INTEGER)
