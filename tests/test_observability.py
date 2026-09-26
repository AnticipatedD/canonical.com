from werkzeug.exceptions import NotFound
from webapp.observability import init_sentry

def test_sentry_filters_http_4xx():
    dsn, env = "fake-dsn", "test"
    init_sentry(dsn, env)
    event = {"message": "error"}
    hint = {"exc_info": (None, NotFound(), None)}
    # The before_send function should drop 404 events
    assert sentry_sdk.Hub.current.client.options["before_send"](event, hint) is None
