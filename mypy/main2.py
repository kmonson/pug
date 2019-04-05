from typing import Mapping, MutableMapping, Sequence, Iterable, List, Set


def f(ints: Iterable[int]) -> List[str]:
    return [str(x) for x in ints]


def f(my_dict: Mapping[int, str]) -> List[int]:
    return list(my_dict.keys())
