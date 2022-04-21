"""blueprint for showing the results"""
from flask import Blueprint, g, redirect, render_template, request, session, url_for, flash
import sqlite3
from . import db

bp = Blueprint('show', __name__, url_prefix='/')

@bp.route('/<subject>')
def index(subject):
    d = db.get_db()
    cursor = d.cursor()
    quotes = cursor.execute(
        "SELECT quote, subject, author FROM quotes WHERE subject == '"
        + subject + "'"
    ).fetchall()
    # in sqlite we must use an extra "'"
    return render_template('show.html', quotes=quotes)

