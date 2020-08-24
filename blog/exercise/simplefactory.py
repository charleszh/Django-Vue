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


class SimpleFactory(object):
    """
    simple factory
    """
    @staticmethod
    def produce_car(name):
        if name == 'mercedes':
            return Mercedes()
        else:
            return BMW()


car1 = SimpleFactory.produce_car('mercedes')
car2 = SimpleFactory.produce_car('bmw')
print(car1.__repr__(), car2.__repr__())
