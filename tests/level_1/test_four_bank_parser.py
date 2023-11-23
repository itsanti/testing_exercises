import datetime
import pytest

from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense():
    dt = datetime.datetime.now()
    cards = [BankCard('5100', 'Амелия Эрхарт'),
             BankCard('1601', 'Альберт Эйнштейн'),
             BankCard('2707', 'Юлий Цезарь')]

    sms = SmsMessage('23 33, 1231235101 13.11.23 23:22 test authcode 2345', 'iam', dt)
    with pytest.raises(IndexError):
        parse_ineco_expense(sms, cards)

    sms = SmsMessage('23 33, 1231231601 13.11.23 23:22 test authcode 2345', 'iam', dt)
    assert type(parse_ineco_expense(sms, cards)) == Expense
