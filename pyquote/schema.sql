DROP TABLE IF EXISTS subjects;
<<<<<<< HEAD
<<<<<<< HEAD
DROP TABLE IF EXISTS quote;

CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    subject TEXT UNIQUE NOT NULL,
=======
=======
>>>>>>> feature-search
DROP TABLE IF EXISTS quotes;

CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject TEXT NOT NULL,
<<<<<<< HEAD
>>>>>>> feature-search
=======
>>>>>>> feature-search
    collected TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE quotes (
<<<<<<< HEAD
<<<<<<< HEAD
    id INTEGER PRIMARY KEY,
    quote TEXT UNIQUE NOT NULL,
    author TEXT NOT NULL DEFAULT someone,
    subject TEXT NOT NULL,
    collected TIMESTAMP NOT NULL,
    FOREIGN KEY (subject) REFERENCES subjects (subject)
    FOREIGN KEY (collected) REFERENCES subjects(collected)
=======
=======
>>>>>>> feature-search
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subject_id INTEGER NOT NULL,
    quote TEXT NOT NULL,
    author TEXT NOT NULL DEFAULT someone,
    subject TEXT NOT NULL,
    collected TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
<<<<<<< HEAD
>>>>>>> feature-search
=======
>>>>>>> feature-search
);
