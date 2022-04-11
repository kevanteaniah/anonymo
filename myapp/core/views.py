# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import Nymo

from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    nymos = Nymo.query.order_by(Nymo.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', nymos=nymos)

@core.route('/info')
def info():
    return render_template('info.html')

