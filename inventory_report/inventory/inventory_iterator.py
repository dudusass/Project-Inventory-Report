from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, report):
        self.report = report
        self._index = 0

    def __next__(self):
        try:
            curr_value = self.report[self._index]
        except IndexError:
            raise StopIteration()
        else:
            self._index += 1
            return curr_value
