from mandrill import Mandrill
from . import app


def _get_mandrill():
    return Mandrill(apikey=app.config['MANDRILL_API_KEY'])


def get_templates():
    pass


def render_mandrill_template(slug, template_content=None, merge_vars=None):
    md = _get_mandrill()
    resp = md.templates.render(slug, template_content, merge_vars=merge_vars)
    return resp['html']
