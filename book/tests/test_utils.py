import datetime

from book.utils import read_date


def test_read_date():
    dt1 = "2022-04-05"
    dt2 = "2022-04"
    dt3 = "2022"
    dt4 = ""

    assert read_date(dt1) == datetime.datetime(2022, 4, 5)
    assert read_date(dt2) == datetime.datetime(2022, 4)
    assert read_date(dt3) == datetime.datetime(2022)
    assert read_date(dt4) == datetime.datetime()
