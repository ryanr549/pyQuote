"""blueprint for showing the results"""
from flask import Blueprint, g, redirect, render_template, request, session, url_for, flash
import sqlite3
from . import db

bp = Blueprint('show', __name__, url_prefix='/')

