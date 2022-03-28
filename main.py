from lorem_text import lorem
from query.sql import QuerySQL, QuerySelect, QueryInsert
from string import ascii_lowercase
from random import shuffle, randint, choice

MAX_QUERYS = 25
query = QuerySQL()


def generate_token(size: int=8) -> str:
    tokens = list(range(size)) + list(ascii_lowercase)
    shuffle(tokens)

    return "".join([str(t) for t in tokens][:size])


def generate_datetime() -> str:
    def date():
        year = lambda: str(randint(2000, 2022))
        mounth = lambda: str(randint(1, 12))
        day = lambda: str(randint(1, 30))

        return f"{year()}-{mounth()}-{day()}"

    def time():
        hour = lambda: str(randint(1, 23))
        minutes = lambda: str(randint(0, 59))
        seconds = lambda: str(randint(0, 59))

        moment = lambda: choice(["AM", "PM"])

        return f"{hour()}:{minutes()}:{seconds()}"

    return " ".join([date(), time()]) # 18-06-12 10:34:09 PM


generate_name = lambda: lorem.words(1).capitalize()


[print(query("insert", into="Client", values={"FirtsName": generate_name(), "SecondName": generate_name(), "LicensePlate": generate_token(), "CirculationCard": generate_token(), "DateRegister": generate_datetime()})) for i in range(MAX_QUERYS)]