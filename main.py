import turtle

bunny = turtle.Turtle()
bunny.speed(0)

def square():
 length = 100
 for i in range(4):
   bunny.forward(length)
   bunny.right(90)
   
# make circle with square
for i in range(100):
  square()
  bunny.right(11) #11 not divisible by 360


