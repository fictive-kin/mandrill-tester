# app is instanced in __init__.py; this gets it from there
from . import app
from .utils import render_mandrill_template, get_templates, send_mail_mandrill
from flask import render_template, request, abort
import json


@app.route("/")
def index():
    data = {
        "templates": get_templates()
    }
    return render_template("index.html", data=data)


@app.route('/render/', methods=['POST'])
def render():
    """
    renders and/or sends!
    """
    app.logger.debug(request.form)
    action = request.form.get('action')
    template_slug = request.form.get('template-slug')
    template_content = json.loads(request.form.get('template-content'))
    merge_vars = json.loads(request.form.get('merge-vars'))

    app.logger.debug(action)

    if (action == 'render'):
        html = render_mandrill_template(template_slug,
                                        template_content=template_content,
                                        merge_vars=merge_vars)
        return html

    if (action == 'send'):
        to_email = request.form.get('to-email')
        from_email = request.form.get('from-email')
        subject = request.form.get('subject')
        resp = send_mail_mandrill(template_slug, to_email, subject,
                                  from_address=from_email,
                                  template_content=template_content,
                                  merge_vars=merge_vars)
        app.logger.debug(resp)
        return "Mandrill response: %s" % (resp)

    abort(400, "Bad action")


@app.route('/template/<slug>', methods=['GET'])
def template_get(slug):
    template_obj = get_templates(slug=slug)
    return render_template("template_view.html", template_obj=template_obj)
