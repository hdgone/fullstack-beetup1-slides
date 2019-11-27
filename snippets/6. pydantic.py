# Python 3.6+
from typing import List
from pydantic import BaseModel, ValidationError


class School(BaseModel):
    id: int
    name: str
    location: str


class Student(BaseModel):
    id: int
    name: str
    school: School


class Section(BaseModel):
    id: int
    name: str
    students: List[Student]


input_data = {
    'id': 0,
    'name': 'Computer Science',
    'students': [
        {
            'id': 0,
            'name': 'Steve',
            'school': {
                'id': 0,
                'name': 'Gyno School',
                'location': 'NYC'
            }
        },
        {
            'id': 1,
            'name': 'Kevin',
            'school': {
                'id': 0,
                'name': 'Gyno School',
                'location': 'NYC'
            }
        }
    ]
}


try:
    sec = Section(**input_data)
except ValidationError as e:
    print(e.json())
else:
    print(sec.id)
    print(sec.name)
    print(sec.students)
