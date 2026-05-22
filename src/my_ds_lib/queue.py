from typing import TypeVar, Generic

T = TypeVar("T")

class Node(Generic[T]):
    def __init__(self, next: Node[T] | None, data: T) -> None:
        self.next = next
        self.data = data            

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None
        self._size: int = 0
    
    def enqueue(self, data: T) -> None:
        if not self.head:
            node = Node(next=None, data=data)
            self.head = node
            self.tail = node
        elif self.tail is not None:
            node = Node(next=None, data=data)
            self.tail.next = node
            self.tail = node
        else:
            raise ValueError("Last element equel None")
        self._size += 1

    def dequeue(self) -> T | None:
        if self.head is None:
            return None
        else: 
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return data
        
    def peek(self) -> T | None:
        if self.head:
            return self.head.data
        else:
            return None
    
    def is_empty(self) -> bool:
        return not self.head
    
    def size(self) -> int:
        return self._size
    
    def __len__(self) -> int:
        return self._size
        



