"""
005_decorators.py

A decorator is a gift wrapper: the function inside doesn't change, but
the wrapper adds something extra every time the function gets called.

Run with: uv run 005_decorators.py
"""

import functools
import time


def announce(func):
    """Announces when a function starts and finishes."""

    @functools.wraps(func) # this line keeps the metadata of the function unchanged. 
    def wrapper(*args, **kwargs): # passing arguments and keyword arguments
        print(f"Starting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}.")
        return result

    return wrapper 


@announce
def greet(name):
    return f"Hello, {name}!"


print(greet("Rohit"))


def timed(func):
    """Prints how long a function took to run."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - start) * 1000
        print(f"{func.__name__} took {elapsed_ms:.2f} ms")
        return result

    return wrapper


@timed
def slow_addition(a, b):
    time.sleep(0.05)
    return a + b


print(slow_addition(3, 4))


# --- Stacking two decorators on the same function --- || Here, order of application from will be from bottom to top. 
# --- Something like this slow_greeting = announce(timed(slow_greeting))
@announce
@timed
def slow_greeting(name):
    time.sleep(0.02)
    return f"Hello there, {name}!"


print(slow_greeting("Rohit"))


if __name__ == "__main__":
    print("\nDecorators done.")
