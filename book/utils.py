from datetime import date, datetime


def read_date(date: str) -> date | None:

    try:
        date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        try:
            date = datetime.strptime(date, "%Y-%m")
        except ValueError:
            try:
                date = datetime.strptime(date, "%Y")
            except ValueError:
                return None

    return date.date()
