class fourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

class moreFourCal(fourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class safeFourCal(fourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = moreFourCal(4, 2)
print(a.pow())

b = safeFourCal(4, 0)
print(b.div())
