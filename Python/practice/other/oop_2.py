from datetime import date

class A:
    def __init__(self, a: int = None):
        self.a = a

    @staticmethod
    def _static(a):
        return a > 0

    @classmethod
    def _class(cls,a):
        return cls(a)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # a class method to create a Person object by birth year.

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

        # a static method to check if a Person is adult or not.

    @staticmethod
    def isAdult(age):
        return age > 18

if __name__=='__main__':
    obj_A = A(1)
    print(obj_A.a)
    print(obj_A._static(10))
    obj_A_1 = obj_A._class(-1)
    print(obj_A_1.a)
    print(obj_A_1._static(20))

    person1 = Person('mayank', 21)
    person2 = Person.fromBirthYear('mayank', 1996)

    print(person1.age)
    print(person2.age)

    # print the result
    print(Person.isAdult(22))

