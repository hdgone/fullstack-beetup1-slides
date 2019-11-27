# Python 3.6+
# Why "annotations"?


def add(x, y):
    """
    Takes 2 integers and returns their sum
    :param x: int
    :param y: int
    :return: int
    """
    return x + y


def add(x: int, y: int) -> int:
    return x + y


def append_ly(word):
    """
    Takes a single word and adds 'ly' at the end if needed
    :param word: str
    :return: str
    """
    if word.endswith('ly'):
        return f"{word}ing"
    return f"{word}ly"


def append_ly(word: str) -> str:
    if word.endswith('ly'):
        return f"{word}ing"
    return f"{word}ly"


def isfirstupper(word: str) -> bool:
    return word[0].isupper()


def person_constructor(name: str, age: int, city: str) -> dict:
    return {
        'name': name,
        'age': age,
        'city': city
    }


def extract_length(words: list) -> list:
    return [len(word) for word in words]


add(3, 4)  # 15
add("Hello ", "World")  # "Hello World", no errors
