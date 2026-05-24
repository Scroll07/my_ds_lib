from typing import Generic, TypeVar, Iterable

from my_ds_lib.queue import Node, Queue

T = TypeVar("T")

class Deque(Queue, Generic[T]):        
    def appendleft(self, data: T) -> None:
        node = Node(next=self.head, data=data)
        self.head = node
        if self.tail is None:
            self.tail = node
        self._size += 1
        
    def popleft(self) -> T | None:
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        self._size -= 1
        return data
    
    def peekleft(self) -> T | None:
        if self.head is None:
            return None
        return self.head.data
    
    def extend(self, iterable: Iterable[T]) -> None:
        for i in iterable:
            self.append(data=i)
            
    def extendleft(self, iterable: Iterable[T]) -> None: #Исправить то что элементы добавляются в другом порядке
        for i in iterable:
            self.appendleft(data=i)
    
    
    
        
    
        