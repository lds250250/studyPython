import functools


def log(text='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(f'{text} {func.__name__}():')
            return func(*args, **kw)

        return wrapper

    return decorator


@log()
def now():
    print('2015-3-25')


now()
