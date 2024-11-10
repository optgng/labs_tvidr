import sys
from contextlib import redirect_stdout


def save_output_to_file(file_path: str, func, *args, **kwargs):
    with open(file_path, 'w') as f:
        with redirect_stdout(f):
            func(*args, **kwargs)
