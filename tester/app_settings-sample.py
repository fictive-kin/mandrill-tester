class Config(object):
    """Configuration settings for the application."""

    DEBUG = True
    TESTING = True
    PERMANENT_SESSION_LIFETIME = 31556926  # 1 year
    SECRET_KEY = 'FILL ME'  # for secure session generation. some random string

    MANDRILL_API_KEY = "FILL ME"  # your Mandrill API key
