class ListInterface:
    _list = {}
    _size = 0

    def __init__(self):
        pass

    def add(self, val: int, ind=-1):
        pass

    def remove(self, ind: int):
        pass

    def get(self, ind: int):
        pass

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def __str__(self) -> str:
        return str(self._list)
