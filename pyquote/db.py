"""use sqlite3 to keep saved quotes"""
import psycopg2
import os
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    """connect to the database"""
    DATABASE_URL = os.environ['DATABASE_URL']
    if 'db' not in g:
        g.db = psycopg2.connect(DATABASE_URL, sslmode='require')
    return g.db

def init_db():
    """initialize database"""
    d = get_db()
    cursor = d.cursor()

    # execute sql command to initialize the dadabase
    cursor.execute('DROP TABLE IF EXISTS subjects;')
    cursor.execute('DROP TABLE IF EXISTS quotes;')
    cursor.execute('DROP TABLE IF EXISTS photos;')
    cursor.execute(
        'CREATE TABLE subjects (id serial PRIMARY KEY, '
        'subject text, '
        'collected TIMESTAMP DEFAULT CURRENT_TIMESTAMP);'
    )
    cursor.execute(
        'CREATE TABLE quotes (id serial PRIMARY KEY,'
        'quote text NOT NULL,'
        'author text NOT NULL,'
        'subject text NOT NULL);'
    )
    cursor.execute(
        'CREATE TABLE photos (id serial PRIMARY KEY,'
        'image_url TEXT NOT NULL,'
        'subject TEXT NOT NULL);'
    )
    d.commit()
    cursor.close()
    d.close()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    create a command line which do the job:
    clear the existing data and create new tables.
    """
    init_db()
    click.echo('Initialized the database.')
