import pytest


from src.phone import Phone


phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim():
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
    with pytest.raises(ValueError):
        phone1.number_of_sim = 1.5
