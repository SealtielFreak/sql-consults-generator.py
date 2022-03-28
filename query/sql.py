from typing import Any, Dict

literal_str = lambda s: f"\"{s}\""


class QuerySelect:
    def __call__(self, keys: Dict[str, str]) -> str:
        query = f"""SELECT {keys["select"]} FROM {keys["fromtable"]}"""

        if keys["join"]:
            query += f""" {keys["join"]} FROM {keys["foreigntable"]}"""

        return query + ";"


class QueryInsert:
    def __call__(self, keys: Dict[str, Any]) -> str:
        items = keys.pop("values")

        query = f"""INSERT INTO {keys["into"]}({", ".join(items.keys())}) VALUES({", ".join([literal_str(v) if type(v) == str else str(v) for v in items.values()])})"""

        return query + ";"


class QuerySQL:
    __statements = {
        "SELECT": QuerySelect(),
        "INSERT": QueryInsert()
    }

    def __init__(self) -> None:
        pass

    def __call__(self, statement: str, **keys) -> str:
        statement = statement.upper()
        return self.__statements[statement](keys)
