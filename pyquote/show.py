"""blueprint for showing the results"""
from flask import Blueprint, redirect, render_template, url_for, flash
import sqlite3
import psycopg2.extras
import random
from . import db

bp = Blueprint('show', __name__, url_prefix='/')

@bp.route('/<subject>')
# specify each subject with a url
def index(subject):
    error = None
    d = db.get_db()
    cursor = d.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(
        "SELECT quote, author FROM quotes WHERE subject = '"
        + subject + "'"
    )
    # in sql we must use an extra "'"
    quotes = cursor.fetchall()
    if len(quotes) == 0:
        error = 'Page do not exist. Try again'
        # if entered a url not exist on database, flash an error.
        flash(error)
        cursor.close()
        d.close()
        return redirect('/')
    # get quotes from database
    cursor.execute(
        "SELECT image_url FROM photos WHERE subject = '"
        + subject + "'"
    )
    images = cursor.fetchall()
    # get images from database
    quote_id = random.randint(0, len(quotes) - 1)
    image_id = random.randint(0, len(images) - 1)
    return render_template('show.html', quotes=quotes, images=images,
                           quote_id=quote_id, image_id=image_id, subject=subject)

