"""blueprint for input and submit subjects"""
from flask import Blueprint, redirect, render_template, request, flash
import psycopg2.extras
from . import db, scrap

bp = Blueprint('search', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def home():
    """"homepage for displaying using GET method"""
    return render_template('search.html')

@bp.route('/', methods=('GET', 'POST'))
def add():
    """searching using POST method"""
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
            cursor = d.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(
                'SELECT subject FROM subjects'
            )
            subject_list = cursor.fetchall()
            # if subject have not been searched, do the scrap and writing into
            # datebase
            if subject not in [item['subject'] for item in subject_list]:
                # use my scraping package
                lines = scrap.scrap_quotes(subject)
                if lines is None:
                    error = 'No quote found, try another keyword.'
                    cursor.close()
                    d.close()
                    flash(error)
                    # if return None, flash the error message
                    return render_template('search.html', error=error)
                # then submit the requested subject to the database
                cursor.execute(
                    'INSERT INTO subjects (subject)'
                    'VALUES (%s)',
                    (subject,)
                )
                # lastrowid attribute as the subject_id
                lines.pop()
                # the last element is not a quote so delete it
                for item in lines:
                    # separate the quote and the author then write in variables
                    quote, _, author = item.get_text().partition('\n')
                    if not author:
                        # if no quote is subtracted then pass
                        author = 'Anonymous'
                    else:
                        cursor.execute(
                            'INSERT INTO quotes (quote, author, subject)'
                            'VALUES (%s, %s, %s)',
                            (quote, author, subject)
                        )
                image_url_list = scrap.scrap_unsplash(subject)
                for image_url in image_url_list:
                    cursor.execute(
                        'INSERT INTO photos (image_url, subject)'
                        'VALUES (%s, %s)',
                        (image_url, subject)
                    )
                d.commit()
                # after the commit is done close database connection
                cursor.close()
                d.close()
        # redirect to the specific show page
        return redirect('/'+subject)
