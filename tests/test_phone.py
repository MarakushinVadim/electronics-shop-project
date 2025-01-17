import pytest


from src.phone import Phone


phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim():
    assert phone1.number_of_sim == 2


def test_nuber_of_sim_new_count():
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1


def test_number_of_sim_raise_ValueError():
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
    with pytest.raises(ValueError):
        phone1.number_of_sim = 1.5
