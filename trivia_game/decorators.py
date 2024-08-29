import time
from functools import wraps
from typing import Callable

def timeit(func: Callable) -> Callable:
    """Decorator to measure the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.2f} seconds")
        return result
    return wrapper
