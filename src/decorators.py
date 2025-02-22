from functools import capsys, wraps

import pytest


def log(filename=None):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                msg = f'{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}'
                raise e
            else:
                msg = f' {func.__name__} ok '
                return result
            finally:
                if filename is None:
                    print(msg)
                elif filename is not None:
                    with open(filename, 'w') as file:
                        file.write(msg + '\n')

        return wrapper

    return inner


@capsys
@log()
def devider(x, y):
    return x / y


def test_devider_ok():
    assert devider(4, 2) == 2


def test_devider_zero_devision():
    with pytest.raises(ZeroDivisionError):
        devider(4, 0)
