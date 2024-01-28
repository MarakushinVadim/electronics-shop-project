from src.item import Item


item1 = Item('PC', 2000, 5)
Item.pay_rate = 0.5


def test_calculate_total_price():
    assert Item.calculate_total_price(item1) == 10000


def test_apply_discount():
    assert Item.apply_discount(item1) == 1000


def test_name():
    assert item1.name == 'PC'
    item1.name = 'Клавиатура'
    assert item1.name == 'Клавиатура'
    item1.name = '01234567890'
    assert item1.name == '0123456789'


def test_instantiate_from_csv():
    item1.instantiate_from_csv('../src/items.csv')
    assert len(item1.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5