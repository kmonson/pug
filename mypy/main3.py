from typing import ClassVar, List, Type, TypeVar

class MyClass:
    attr: int
    def __init__(self) -> None:
        self.attr = 100

    def method(self, num:int, str1: str) -> str:
        return num * str1

x: MyClass = MyClass()


class Car:
    seats: ClassVar[int] = 4
    passengers: ClassVar[List[str]]


MC = TypeVar("MC", bound=MyClass)

x: Type[MC] = MyClass
