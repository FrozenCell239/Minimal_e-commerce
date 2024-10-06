from app.main import main_bp
from flask import render_template

@main_bp.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html.jinja')