from typing import Iterator


class InventoryIterator(Iterator):
    def __init__(self, interable):
        self.__interable = interable
        self.__index = 0

    def __next__(self):
        try:
            result = self.__interable[self.__index]
        except IndexError:
            raise StopIteration()
        self.__index += 1
        return result
