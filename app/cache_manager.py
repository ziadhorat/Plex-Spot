from functools import lru_cache

def cache_manager(ttl):
    def decorator(func):
        @lru_cache(maxsize=128)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

