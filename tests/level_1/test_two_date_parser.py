import datetime
import pytest

from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from():
    date = datetime.date.today()
    dt = datetime.datetime(date.year, date.month, date.day, 22, 20)

    assert compose_datetime_from('lalala', '22:20') ==  dt
    assert compose_datetime_from('tomorrow', '22:20') == dt + datetime.timedelta(days=1)

    with pytest.raises(ValueError):
        compose_datetime_from('tomorrow', '22:AB')
        compose_datetime_from('tomorrow', '1212')
