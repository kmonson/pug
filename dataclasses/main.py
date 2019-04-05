from dataclasses import dataclass, replace, is_dataclass
from typing import List


@dataclass(order=True, frozen=True)
class A:
    a: str
    b: str
    c: str
    d: int = 4


@dataclass(frozen=True)
class B(A):
    d: str = "abc"
    e: str = "def"

a = A('foo', 'bar', 'baz')
b = B('foo', 'bar', 'bonk')

c = replace(b, d="123")

print(repr(a))
print(repr(b))
print(repr(c))

print(c < b)
