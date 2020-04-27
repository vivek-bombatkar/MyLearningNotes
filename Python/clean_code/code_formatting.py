
class myClass:
    def my_func(self, i: int = 0, s:str = None) -> str:
        """
        this is my function
        :param i: interger
        :param s: stering
        :return: string
        """
        if i == 0:
            s = "test"
        return s

if __name__ == '__main__':
    c = myClass()
    print(c.my_func(10))
    print(c.my_func.__annotations__)
    print(c.my_func.__doc__)