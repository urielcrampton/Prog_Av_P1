from typing import Generic, TypeVar, Callable

T = TypeVar('T')

class Maybe(Generic[T]):
    def __init__(self, value: T = None):
        self._value = value

    def is_nothing(self) -> bool:
        return self._value is None

    def bind(self, func: Callable[[T], 'Maybe']) -> 'Maybe':
        if self.is_nothing():
            return self
        return func(self._value)

    def get_or_else(self, default: T) -> T:
        return self._value if not self.is_nothing() else default
