DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS quote;

CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    subject TEXT UNIQUE NOT NULL,
    collector TEXT NOT NULL DEFAULT anonymous,
    collected TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE quotes (
    id INTEGER PRIMARY KEY,
    quote TEXT UNIQUE NOT NULL,
    author TEXT NOT NULL DEFAULT someone,
    subject TEXT NOT NULL,
    collected TIMESTAMP NOT NULL,
    FOREIGN KEY (subject) REFERENCES subjects (subject)
    FOREIGN KEY (collected) REFERENCES subjects(collected)
);
