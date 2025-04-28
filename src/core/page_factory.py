from typing import Any, Type

def get_page(context: Any, cls: Type):
    cache = context.__dict__.setdefault("_page_cache", {})
    if cls not in cache:
        cache[cls] = cls(context.driver)
    return cache[cls]
