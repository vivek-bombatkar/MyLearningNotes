
# Decorators were introduced in Python a long time ago, in (PEP-
# 318), as a mechanism to simplify the way functions and methods are
# defined when they have to be modified after their original definition.

def my_decorator(func):
    def something():
        print("before")
        func()
        print('after')
    return something


@my_decorator
def hello():
    print('hello')

if __name__=="__main__":
    hello()