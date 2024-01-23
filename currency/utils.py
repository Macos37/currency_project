from functools import wraps
from time import sleep


def pause_between_requests(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(10)
        return func(*args, **kwargs)
    return wrapper
