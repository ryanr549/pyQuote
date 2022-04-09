from flask import Blueprint, g, redirect, render_template, request, session, url_for
from . import db
bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/post', methods=['GET'])
def home():
    return render_template('search/search.html')

@bp.route('/post', methods=['POST'])
def add():
    subject = request.form['subject']
    try:
        db =
    return render_template('search/search.html')
