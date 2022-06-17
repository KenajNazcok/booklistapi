import datetime

from book.utils import read_date


def test_read_date():
    dt1 = "2022-04-05"
    dt2 = "2022-04"
    dt3 = "2022"
    dt4 = ""

    assert read_date(dt1) == datetime.date(2022, 4, 5)
    assert read_date(dt2) == datetime.date(2022, 4 , 1)
    assert read_date(dt3) == datetime.date(2022, 1, 1)
    assert read_date(dt4) == None
