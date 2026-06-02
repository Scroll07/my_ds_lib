class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("Capacity must be positive number")
        self.capacity = capacity
        self.size = 0
        self.array: list[int | None] = [None] * capacity

    def get(self, i: int) -> int:
        if not (0 <= i < self.size):
            raise IndexError("Out of range")
        if self.size < 1:
            raise ValueError("Nothing to get")
        value = self.array[i]
        assert value is not None
        return value
        

    def set(self, i: int, n: int) -> None:
        if not (0 <= i < self.size):
            raise IndexError("Out of range")
        if self.size < 1:
            raise ValueError("Nothing to get")
        self.array[i] = n
        return None

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1
        return None

    def popback(self) -> int:
        if self.size < 1:
            raise ValueError("Nothing to get")
        n = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        assert n is not None
        return n

    def resize(self) -> None:
        self.capacity *= 2
        new_array: list[int | None] = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        return None

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity