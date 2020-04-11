
class myClass:
    def __init__(self,new_val):
        """
        Objects should only expose those attributes and methods that are relevant to an
        external caller object, namely, entailing its interface. Everything that is not strictly
        part of an object's interface should be kept prefixed with a single underscore.
        :param new_val:
        """
        self.i = new_val
        self._k = 0
        # with the double underscores,
        # Python creates a different name for the attribute (this is called
        # name mangling). What it does is create the attribute with the
        # following name instead: "_<class-name>__<attribute-name>".
        self.__j = 10

if __name__=='__main__':
    cls = myClass(10)
    print(cls.i)
    print(cls._k)
    # print(cls.__j) #         AttributeError: 'myClass' object has no attribute '__j'
    print(cls._myClass__j)
