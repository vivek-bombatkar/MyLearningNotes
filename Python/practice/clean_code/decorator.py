
# Decorators were introduced in Python a long time ago, in (PEP-
# 318), as a mechanism to simplify the way functions and methods are
# defined when they have to be modified after their original definition.

import functools

def my_decorator(func):
    @functools.wraps(func)
    def something(*args):
        print(f"before {args}")
        func(*args)
        print('after')
    return something


@my_decorator
def hello():
    print('hello')

@my_decorator
def hello_there(name: str = None):
    print(f'hello {name}')

if __name__=="__main__":
    hello_there("vivek")
    hello()
    print(hello_there.__name__) # without functools = something