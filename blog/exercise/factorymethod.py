import abc

class Mercedes(object):
    """
    梅赛德斯
    """
    def __repr__(self):
        return "Mercedes class"

class BMW(object):
    """
    baoma
    """
    def __repr__(self):
        return "BMW class"

class AbstractFactory(object):
    """
    abstract factory
    """
    @abc.abstractmethod
    def produce_car(self):
        pass


class MercedesFactory(AbstractFactory):
    """
    Mercedes factory
    """
    def produce_car(self):
        return Mercedes()


class BMWFactory(AbstractFactory):
    """
    BMW factory
    """
    def produce_car(self):
        return BMW()


c1 = MercedesFactory().produce_car()
print(c1.__repr__())
