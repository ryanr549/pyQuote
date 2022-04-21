DROP TABLE IF EXISTS subjects;
DROP TABLE IF EXISTS quotes;
DROP TABLE IF EXISTS photos;

CREATE TABLE subjects (
    id serial PRIMARY KEY,
    subject TEXT NOT NULL,
    collected TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE quotes (
    id serial PRIMARY KEY,
    subject_id INTEGER NOT NULL,
    quote TEXT NOT NULL,
    author TEXT NOT NULL DEFAULT 'someone',
    subject TEXT NOT NULL,
    collected TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
);

CREATE TABLE photos (
    id serial PRIMARY KEY,
    subject_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    subject TEXT NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
);
