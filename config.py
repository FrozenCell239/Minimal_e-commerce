from datetime import timedelta
from os import urandom, getenv

class Config :
    """
    Contains the app's configuration.\n
    You must not create an instance of this class because of its purpose.
    """

    def __init__(self) -> None :
        """
        You must NOT create an instance of this class since it contains app's configuration.
        """

        raise Exception(
            "You must NOT create an instance of Config class since it contains app's configuration."
        )

    # Security configuration
    SECRET_KEY : str = getenv('SECRET_KEY')\
        or urandom(32).hex()
    PERMANENT_SESSION_LIFETIME : timedelta = timedelta(minutes = 10)
    PASSWORD_LIMITS : str = getenv('PASSWORD_LIMITS')

    # Database configuration
    SQLALCHEMY_DATABASE_URI : str = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS : bool = False

    # Running environnement configuration
    WEB_APP_NAME : str = getenv('WEB_APP_NAME')
    DOMAIN_NAME : str = getenv('DOMAIN_NAME') + '/'