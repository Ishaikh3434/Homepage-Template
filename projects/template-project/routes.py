
from flask import render_template, request, jsonify, session, url_for, current_app
from . import bp


@bp.route('/', methods=['GET'])
def index():
    # build the full URL to the any endpoints 
    # generate_url = url_for('template-project.__endpointname__', _external=True)
    generate_url=''
    return render_template('template.html', path=generate_url)
