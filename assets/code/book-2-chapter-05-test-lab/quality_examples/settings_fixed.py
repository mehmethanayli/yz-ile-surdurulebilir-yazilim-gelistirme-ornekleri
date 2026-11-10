"""Correct settings contract, retained from the preceding teaching example."""
def read_settings(environ):
    app_env = environ.get("APP_ENV", "development").strip().lower()
    if app_env not in {"development", "test", "production"}:
        raise ValueError("APP_ENV must be development, test or production.")
    raw_debug = environ.get("APP_DEBUG", "false").strip().lower()
    if raw_debug not in {"true", "false"}:
        raise ValueError("APP_DEBUG must be true or false.")
    debug = raw_debug == "true"
    if app_env == "production" and debug:
        raise ValueError("APP_DEBUG must be false in production.")
    return {"app_env": app_env, "debug": debug}
