from functools import wraps


def log(filename=None):
    """декоратор логирования"""

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
