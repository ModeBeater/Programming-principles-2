class naruto():
    def __init__(self,x,y,a):
        self.x = x
        self.y = y
        self.a = a
    def show(self):
        print(self.x)
        print(self.y)
    def move(self):
        self.x += a
        self.y += a
        print(self.x) 
        print(self.y)
    def dist(self):
        self.x = x
        self.y = y
        d = abs(self.y - self.x)
        return d
s = str(input())
x = int(input())
y = int(input())
if s == 'show':
    ans = naruto(x,y,0)
    ans.show()
if s == 'move':
    a = int(input())
    ans = naruto(x,y,a)
    ans.move()
if s == 'dist':
    ans = naruto(x,y,0)
    print(ans.dist())