# app is instanced in __init__.py; this gets it from there
from . import app
from .utils import render_mandrill_template
from flask import render_template, request
import json


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/render/', methods=['POST'])
def render():
    template_slug = request.form.get('template-slug')
    template_content = json.loads(request.form.get('template-content'))
    merge_vars = json.loads(request.form.get('merge-vars'))
    html = render_mandrill_template(template_slug,
                                    template_content=template_content,
                                    merge_vars=merge_vars)
    return html
