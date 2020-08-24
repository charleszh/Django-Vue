from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):

    def do_say(self):
        print("It says: Wang Wagn Wang")

class Cat(Animal):

    def do_say(self):
        print("It says: Miao Miao Miao")


class ForestFactory(object):

    def make_sound(self, object_type):
        return eval(object_type)().do_say()


if __name__ == '__main__':
    ff = ForestFactory()
    ff.make_sound('Cat')
