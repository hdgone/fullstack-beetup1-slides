a = 13  # int
b = 13.0  # float
c = 7j  # complex
d = "13"  # str
e = True  # bool
f = None  # NoneType

list_ = [a, b, c]  # list
tuple_ = (a, b, c)  # tuple
dict_ = {'a': a, 'b': b, 'c': c}  # dict
set_ = {a, b, c}  # set
frozenset_ = frozenset([a, b, c])  # frozenset

print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, complex))
print(isinstance(d, str))
print(isinstance(e, bool))
print(f is None)

print(isinstance(type(a), type))
print(isinstance(type(b), type))
print(isinstance(type(c), type))
print(isinstance(type(d), type))
print(isinstance(type(e), type))
print(isinstance(type(f), type))
