from src.item import Item


item1 = Item('PC', 2000, 5)
Item.pay_rate = 0.5


def test_calculate_total_price():
    assert Item.calculate_total_price(item1) == 10000


def test_apply_discount():
    assert Item.apply_discount(item1) == 1000
