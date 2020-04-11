import os

class myClass:
    def good_read_fiel(self,path: str = None) -> str:
        """
        this is good example of :Asking Forgiveness then Permission"
        :param path: path of the file
        :return: file contents
        """
        try:
            with open(path,'r') as f:
                s = f.read()
        except Exception as e:
            s=None
        return s
    def bad_read_file(self,path: str = None) -> str:
        if os.path.exists(path):
            f= open(path,'r')
            s=f.read()
        else:
            s=None
        return s

if __name__=='__main__':
    cls=myClass()
    # print(cls.good_read_fiel('C:\Program Files\Git\LICENSE.txt1'))
    print(cls.bad_read_file('C:\Program Files\Git\LICENSE.txt1'))