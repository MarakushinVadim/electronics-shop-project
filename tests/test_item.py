"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone

item1 = Item('PC', 2000, 5)
Item.pay_rate = 0.5


def test_calculate_total_price():
    assert item1.calculate_total_price() == 10000


def test_apply_discount():
    assert Item.apply_discount(item1) == 1000


def test_name():
    assert item1.name == 'PC'
    item1.name = 'Клавиатура'
    assert item1.name == 'Клавиатура'
    item1.name = '01234567890'
    assert item1.name == '0123456789'
    item1.name = 'PC'


def test_instantiate_from_csv():
    item1.instantiate_from_csv('../src/items.csv')
    assert len(item1.all) == 5
    with pytest.raises(FileNotFoundError):
        item1.instantiate_from_csv()
    with pytest.raises(InstantiateCSVError):
        item1.instantiate_from_csv('../src/items1.csv')


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5




def test_repr():
    item1 = Item('PC', 2000, 5)
    assert repr(item1) == "Item('PC', 2000, 5)"


def test_str():
    assert str(item1) == 'PC'


def test_add():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_add_raise_TypeError():
    with pytest.raises(TypeError):
        item1 + 5

