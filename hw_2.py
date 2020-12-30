class ExtendedList(list):
    def __add__(self, other):
        other.extend(self)
        return other

    @staticmethod
    def average(lst):
        return sum(lst) / len(lst)

    def __lt__(self, other):
        if type(other) == list or isinstance(other, type(self)):
            if self.average(self) < self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __gt__(self, other):
        if type(other) == list or isinstance(other, type(self)):
            if self.average(self) > self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __eq__(self, other):
        if type(other) == list or isinstance(other, type(self)):
            if self.average(self) == self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __le__(self, other):
        if type(other) == list or isinstance(other, type(self)):
            if self.average(self) <= self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __ge__(self, other):
        if type(other) == list or isinstance(other, type(self)):
            if self.average(self) >= self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __ne__(self, other):
        if type(other) == list or isinstance(other, type(self)):
            if self.average(self) != self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")

    @staticmethod
    def next_val(lst):
        # return filter(lambda x: float(x), lst)
        for i in lst:
            yield float(i)


class TypeList(ExtendedList):
    def __eq__(self, other):
        if type(other) == list or isinstance(other, type(self)):
            if self[-1] == other[-1]:
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __ne__(self, other):
        if type(other) == list or isinstance(other, type(self)):
            if self[-1] != other[-1]:
                return True
            else:
                return False
        else:
            print("Not a list!!")

