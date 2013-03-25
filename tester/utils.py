from mandrill import Mandrill
from . import app


def _get_mandrill():
    return Mandrill(apikey=app.config['MANDRILL_API_KEY'])


def get_templates(slug=None):
    md = _get_mandrill()
    if not slug:
        tpls = md.templates.list()
        return tpls
    tpl = md.templates.info(slug)
    app.logger.debug(tpl)
    return tpl


def render_mandrill_template(slug, template_content=None, merge_vars=None):
    md = _get_mandrill()
    resp = md.templates.render(slug, template_content=None,
                               merge_vars=merge_vars)
    return resp['html']


def send_mail_mandrill(slug, to, subject, from_address='support@donenotdone.com',
                       from_name="Done Not Done", template_content=None,
                       merge_vars=None):
    """
    send an email using Mandrill
    """
    if not from_address:
        from_address = app.config['FEEDBACK_EMAIL'][0]

    message = {
        "track_opens": True,
        "track_clicks": True,
        'subject': subject,
        "from_email": from_address,
        "from_name": from_name,
        "to": [
            {
                "email": to,
            }
        ],
        "global_merge_vars": merge_vars,
    }

    md = _get_mandrill()
    resp = md.messages.send_template(slug, template_content, message, async=True)

    return resp


def send_mail_raw_mandrill(to, subject, html, from_address='support@donenotdone.com',
                           from_name="Done Not Done"):
    """
    send an email using Mandrill with no template -- raw html
    """
    if not from_address:
        from_address = app.config['FEEDBACK_EMAIL'][0]

    message = {
        "track_opens": True,
        "track_clicks": True,
        'subject': subject,
        "from_email": from_address,
        "from_name": from_name,
        "to": [
            {
                "email": to,
            }
        ],
        "html": html
    }

    md = _get_mandrill()
    resp = md.messages.send(message, async=True)

    return resp
