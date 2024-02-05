from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """

        @type quantity_sim: int
        атрибут, содержащий количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = int(number_of_sim)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"



    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity




