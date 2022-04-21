"""blueprint for input and submit subjects"""
from flask import Blueprint, g, redirect, render_template, request, session, url_for, flash
import sqlite3
from . import db, scrap

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/', methods=['GET'])
def home():
    return render_template('search.html')

@bp.route('/', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        subject = request.form['subject']
        error = None

        if not subject:
            error = 'Subject need to be specified.'

        if error is not None:
            flash(error)
        else:
            # d as the database
            d = db.get_db()
            cursor = d.cursor()
            # first submit the requested subject to the database
            cursor.execute(
                'INSERT INTO subjects (subject)'
                'VALUES (?)',
                (subject,)
            )
            # lastrowid attribute as the subject_id
            counts = cursor.lastrowid
            # use my scraping package
            lines = scrap.scrap_quotes(subject)
            for item in lines:
                # separate the quote and the author then write in variables
                quote, _, author = item.get_text().partition('\n')
                if not quote:
                    # if no quote is subtracted then pass
                    pass
                else:
                    cursor.execute(
                        'INSERT INTO quotes (quote, author, subject, subject_id)'
                        'VALUES (?, ?, ?, ?)',
                        (quote, author, subject, counts)
                    )
            image_url_list = scrap.scrap_unsplash(subject)
            for image_url in image_url_list:
                cursor.execute(
                    'INSERT INTO photos (image_url, subject, subject_id)'
                    'VALUES (?, ?, ?)',
                    (image_url, subject, counts)
                )
            d.commit()
            # after the commit is done close database connection
            d.close()
        return redirect('/'+subject)


