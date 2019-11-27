# Python 3.6+


def add(x: int, y: int) -> int:
    return x + y


print(add(15, 49))  # 64
print(add("Hello ", "World"))  # Error
print(add(24.11, 93.391))  # type: ignore


class Person:
    def __init__(self, age):
        self.age = age

    def __add__(self, other):
        return self.age + other.age

    def __repr__(self):
        return self.age


p1 = Person(19)
p2 = Person(20)

print(add(p1, p2))  # Error


# Dynamically typed functions


def dynamic_foo(a, b, c):
    if c > 5:
        return a + b
    return a + c


def static_foo(a: int, b: int, c: int) -> int:
    if c > 5:
        return a + b
    return a + c


# Ignoring annotations
from typing import List, no_type_check


@no_type_check
def append_student(student: dict, students: List[dict]) -> None:
    students.append(student)
    return students
