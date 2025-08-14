from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


new_person: Person = {'name': 'Abhay', 'age': 23}