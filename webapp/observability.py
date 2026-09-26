import random
import requests
from requests.exceptions import ConnectionError, HTTPError, RetryError
from urllib3.exceptions import MaxRetryError
from werkzeug.exceptions import HTTPException
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

def init_sentry(dsn, environment):
    def before_send(event, hint):
        if "exc_info" in hint:
            _, exc_value, _ = hint["exc_info"]
            if isinstance(exc_value, HTTPException) and 400 <= exc_value.code < 500:
                return None
            if isinstance(exc_value, HTTPError):
                response = getattr(exc_value, "response", None)
                if response is not None and 400 <= response.status_code < 500:
                    return None
            if isinstance(exc_value, (MaxRetryError, RetryError, ConnectionError)):
                error_msg = str(exc_value)
                if "/wp-json/wp/v2" in error_msg and random.random() > 0.05:
                    return None
        return event

    sentry_sdk.init(
        dsn=dsn,
        environment=environment,
        integrations=[FlaskIntegration()],
        before_send=before_send,
    )
from webapp.observability import init_sentry

sentry_dsn = get_flask_env("SENTRY_DSN")
environment = get_flask_env("FLASK_ENV", "production")
init_sentry(sentry_dsn, environment)
