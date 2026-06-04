

from abc import abstractmethod, ABCMeta

class Demo (metaclass=ABCMeta):

    @abstractmethod
    def fun(self):
        pass

class Memo:

    def gun(self):
        print("In gun")

print(type (Demo))          #<class 'abc.ABCMeta'>
