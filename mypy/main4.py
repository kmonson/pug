import sys
import re
from typing import Match, AnyStr, IO

x: Match[str] = re.match(r'[0-9]+', "15")

f: IO[str] = open("foo")

def f(foo: 'A') -> int:
    pass
