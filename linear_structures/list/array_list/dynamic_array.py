from ..array_list_interface import ArrayList


class DynamicArray(ArrayList):

    def __init__(self):
        super().__init__()
        self._list = []

    def add(self, val: int, ind: int = -1):
        """
            Add the element in the selected position (last by default)
        """
        if self._size > ind >= 0:
            self._list[ind] = val

    def remove(self, ind: int):
        """
            Removes the element in the given index
        """
        if self._size > ind:
            self._list[ind] = None
        else:
            raise Exception("Index out of bounds")
