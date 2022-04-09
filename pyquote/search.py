from flask import Blueprint, g, redirect, render_template, request, session, url_for
import sqlite3
from . import db

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/post', methods=['GET'])
def home():
    return render_template('search/search.html')

@bp.route('/post', methods=['POST'])
def add():
    subject = request.form['subject']
    try:
        conn = sqlite3.connect('../instance/pyquote.sqlite')
        cur = conn.cursor()
        sql = "INSERT INTO subjects ('subject') \
            VALUES (%s)" % (subject)
        try:
            cur.execute(sql)
            # commit to db and execute
            conn.commit()
        except:
            # when errors occur, roll back
            conn.rollback()

        sql = "SELECT * FROM subjects;"
        cur.execute(sql)
        u = cur.fetchall()
        return render_template('search/output.html', u=u)
        conn.close()
    except:
        return render_template('search/search.html',message='input false!', var1=subject)
