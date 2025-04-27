from utils.config import config

def get_page(context, cls):
    attr = cls.__name__.lower()
    if not hasattr(context, attr):
        setattr(context, attr, cls(context.driver))
    return getattr(context, attr)
