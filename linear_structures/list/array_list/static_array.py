from ..array_list_interface import ArrayList


class StaticArray(ArrayList):

    def __init__(self, size):
        super().__init__()
        self._size = size
        self._list = [None for _ in range(self._size)]

    def add(self, val: int, ind: int):
        """
            Add the element in the selected position
        """
        if self._size > ind >= 0:
            self._list[ind] = val
        else:
            raise Exception("Index out of bounds")

    def remove(self, ind: int):
        """
            Puts the element as None
        """
        if self._size > ind:
            self._list[ind] = None
        else:
            raise Exception("Index out of bounds")
