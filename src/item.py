import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = int(price)
        self.quantity = int(quantity)


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name


    @classmethod
    def instantiate_from_csv(cls, file_path):
        new_path = os.path.abspath(file_path)
        with open((new_path), 'r', encoding="cp1251") as file:
            csv_dict = csv.DictReader(file)
            for item in csv_dict:
                item1 = Item(item['name'], item['price'], item['quantity'])
                item1.all.append(item1)


    @staticmethod
    def string_to_number(string):
        return int(float(string))


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f'{self.name}'
