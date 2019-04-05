from typing import Callable, Iterable, Union, Optional, List

import numbers


def stringify(num: Union[int, float]) -> str:
    return str(num)

stringify(7)

stringify(7.0)

stringify('abc')

def plus(num1: int, num2: int) -> int:
    return num1 + num2

def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float

x: Callable[[int, float], float] = f

def f(n: int) -> Iterable[int]:
    i = 0
    while i < n:
        yield i
        i += 1

def quux(__x: int) -> None:
    pass

quux(3)
quux(__x=3)

