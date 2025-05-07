"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
The decorator takes an argument `message` of type string
"""


from typing import Callable


def decorator(message: str):
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
