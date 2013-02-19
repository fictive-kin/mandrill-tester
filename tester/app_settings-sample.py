class Config(object):
    """Configuration settings for the application."""

    DEBUG = True
    TESTING = True
    PERMANENT_SESSION_LIFETIME = 31556926  # 1 year
    SECRET_KEY = 'FILL ME'

    MANDRILL_API_KEY = "FILL ME"
