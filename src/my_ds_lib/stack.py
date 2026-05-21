from typing import TypeVar, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []
    
    def push(self, obj: T) -> None:
        self.items.append(obj)
    
    def pop(self) -> T | None:
        if len(self.items) > 0:
            return self.items.pop()
    
    def peek(self) -> T | None:
        if len(self.items) > 0:
            return self.items[-1]
    
    def is_empty(self) -> bool:
        return not self.items
    
    def size(self) -> int:
        return len(self.items)