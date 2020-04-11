"""###
        One of the most common applications for this is to create
        better decorators, but it's not limited to that.
"""

from collections import defaultdict

class myClass:
    def __init__(self):
        self._counts = defaultdict(int)

    def __call__(self, arguments):
        """
        The magic method __call__ will be called when we try to execute our
        :param arguments:
        :return:
        """
        self._counts[arguments] += 1
        return self._counts[arguments]

if __name__=="__main__":
    cls = myClass()
    print(cls(1))
    print(cls(1))
    print(cls(1))
    print(cls("dada"))
    print(cls(1))