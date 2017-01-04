from ftatr import settings


def settings_value(name):
    return getattr(settings, name, "")
