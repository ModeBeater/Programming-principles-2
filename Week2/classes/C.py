class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
n = int(input()) 
m = int(input())
ans = Rectangle(n,m)
print(ans.area())