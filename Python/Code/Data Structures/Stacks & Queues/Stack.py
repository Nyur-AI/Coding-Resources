class stack:
    def __init__(self):
        self.values = []
    def push(self, x):
        self.values = [x] + self.values #Add elements From Start
        # self.values.append(x)  #Add elements From End
    def pop(self):
        return self.values.pop(0) #Remove elements From Start
        # return self.values.pop(-1) #Remove elements From End

s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.values)

print(s.pop())
print(s.values)
