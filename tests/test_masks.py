import pytest


@pytest.mark.parametrize("card_number, expected", [(1234567891234567, '1234 56** **** 4567')])
def test_get_mask_card_number(card_number, expected):
    assert test_get_mask_account('card_number') == expected


@pytest.mark.parametrize("account, expected", [(123456, '**3456')])
def test_get_mask_account(account, expected):
    assert test_get_mask_account(account) == expected


@pytest.fixture
def card_number():
    return 1234567891234567


@pytest.fixture
def account():
    return 123456
