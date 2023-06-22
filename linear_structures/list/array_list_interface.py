from linear_structures.list.list_interface import ListInterface


class ArrayList(ListInterface):
    _list = []

    def add(self, val: int, ind=-1):
        pass

    def remove(self, ind: int):
        pass

    def get(self, ind: int):
        return self._list[ind]

    def iterator(self):
        return self._list
