import re
EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+\.[^@]+")
def is_valid_email(potentially_valid_email: str):
    return re.match(EMAIL_FORMAT, potentially_valid_email) is not None

class myClass:
    def __init__(self,name: str = None):
        self.name = name
        self._email = None

    @property
    def email(self):
        """
        Properties are to be used when we need to define access control to
        some attributes in an object
        :return:
        """
        return self._email
    @email.setter
    def email(self,new_email):
        if not is_valid_email(new_email):
            raise Exception
        self._email = new_email

if __name__=='__main__':
    cls = myClass('vivek')
    print(cls.name)
    cls.email = 'vivek@gmail.com'
    print(cls.email)
    cls.email = 'ab'