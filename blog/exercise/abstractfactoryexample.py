import abc


class MercedesCar(object):
    """
    梅赛德斯
    """
    def __repr__(self):
        return "Mercedes Car class"


class BMWCar(object):
    """
    baoma
    """
    def __repr__(self):
        return "BMW Car class"


class MercedesSUV(object):
    """
    梅赛德斯
    """
    def __repr__(self):
        return "Mercedes SUV class"


class BMWSUV(object):
    """
    baoma
    """
    def __repr__(self):
        return "BMW SUV class"


class AbstractFactory(object):
    """
    abstract factory
    """
    @abc.abstractmethod
    def produce_car(self):
        pass

    @abc.abstractmethod
    def produce_suv(self):
        pass


class MercedesFactory(AbstractFactory):
    """
    Mercedes factory
    """
    def produce_car(self):
        return MercedesCar()

    def produce_suv(self):
        return MercedesSUV()


class BMWFactory(AbstractFactory):
    """
    BMW factory
    """
    def produce_car(self):
        return BMWCar()

    def produce_suv(self):
        return BMWSUV()


c1 = MercedesFactory().produce_car()
s1 = MercedesFactory().produce_suv()
print(c1, s1)
c2 = MercedesFactory().produce_car()
s2 = MercedesFactory().produce_suv()
print(c2, s2)
