# Immutable dictionary
from types import MappingProxyType


person = MappingProxyType({
    'name': 'Steve',
    'age': 30
})

print(isinstance(person, MappingProxyType))  # True
person['country'] = 'UK'  # TypeError
