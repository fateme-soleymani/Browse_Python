class ExtendedList:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return str(self.lst)

    def __add__(self, other):
        other.extend(self.lst)
        print(other)

    @staticmethod
    def average(lst):
        return sum(lst) / len(lst)

    def __lt__(self, other):
        if type(other) == list:
            if self.average(self.lst) < self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __gt__(self, other):
        if type(other) == list:
            if self.average(self.lst) > self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __eq__(self, other):
        if type(other) == list:
            if self.average(self.lst) == self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __le__(self, other):
        if type(other) == list:
            if self.average(self.lst) <= self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __ge__(self, other):
        if type(other) == list:
            if self.average(self.lst) >= self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __ne__(self, other):
        if type(other) == list:
            if self.average(self.lst) != self.average(other):
                return True
            else:
                return False
        else:
            print("Not a list!!")


class TypeList(ExtendedList):
    def __eq__(self, other):
        if type(other) == list:
            if self.lst[-1] == other[-1]:
                return True
            else:
                return False
        else:
            print("Not a list!!")

    def __ne__(self, other):
        if type(other) == list:
            if self.lst[-1] != other[-1]:
                return True
            else:
                return False
        else:
            print("Not a list!!")
