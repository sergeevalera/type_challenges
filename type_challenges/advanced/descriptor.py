"""
TODO:

Create a descriptor and annotate the __get__ method.
"""
from typing import Any, Self, overload


class Descriptor:
    @overload
    def __get__(self, instance: None, owner: type) -> Self:
        ...

    @overload
    def __get__(self, instance: Any, owner: type) -> str:
        ...

    def __get__(self, instance: Any, owner: type) -> Self | str:
        ...
