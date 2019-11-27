# Python 3.6+


def extract_length(words: list) -> list:
    """
    :param words: list of strings
    :return: list of integers
    """
    return [len(word) for word in words]


# Containers
from typing import List


def extract_length(words: List[str]) -> List[int]:
    return [len(word) for word in words]


# Union
from typing import Union


def get_age_or_false(person: dict) -> Union[int, bool]:
    return person.get('age', False)


def get_age_or_none(person: dict) -> Union[int, None]:
    return person.get('age', None)


# Optional
from typing import Optional


def get_age_or_none(person: dict) -> Optional[int]:
    return person.get('age', None)


def append_one(items: Optional[list] = None) -> list:
    if items is None:
        items = []
    items.append(1)

    return items


# Simple refactoring
from typing import Dict


PersonData = Union[int, str]


def person_constructor(name: str, age: int,
                       city: str) -> Dict[str, PersonData]:
    return {
        'name': name,
        'age': age,
        'city': city
    }


# Custom types
from typing import NewType


UserName = NewType('UserName', str)
UserAge = NewType('UserAge', int)
UserObject = NewType('UserObject', Dict[str, Union[UserName, UserAge]])


def create_user(name: UserName, age: UserAge) -> UserObject:
    return UserObject({
        'name': name,
        'age': age
    })


create_user('Steve', 13)
create_user(UserName('Steve'), UserAge(13))


# Callable
import time
from functools import wraps

from typing import Callable


def timeit(function: Callable) -> Callable:
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        print(time.time() - start)
        return result
    return wrapper


def add_as_string(x: int, y: int) -> str:
    return f"{x + y}"


def calculations(items: List[List[int]],
                 callback: Callable[[int, int], str]) -> List[str]:
    return [callback(*item) for item in items]


# Generics
from typing import Mapping, Sequence


Student = NewType('Student', Dict[str, str])


def append_student(student: Mapping[str, str],
                   students: Sequence[Student]) -> None: ...


# Any
from typing import Any


def get_first(items: Any) -> Any:
    return items[0]


nothing: List[Any] = [False, 'test', 94.1, []]


# overload
from typing import overload


@overload
def add(x: int, y: int) -> int: ...
@overload
def add(x: str, y: str) -> str: ...


def add(x: Union[int, str], y: Union[int, str]) -> Union[int, str]:
    return x + y


add(15, 20)
add(15, 'World')
