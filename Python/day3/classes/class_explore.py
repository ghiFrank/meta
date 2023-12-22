class A:
   def __init__(self, c):
       self.c = c
   def alpha(self):
       x = self.c + 1
       return x

a = A(1)
print(a.c)
a.alpha()
print(a.c)

class B:
   def __init__(self, a):
       self.a = a
   d = 5
   a.alpha()
   print(a.c)
   
   
b = B(a)