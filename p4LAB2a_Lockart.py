import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(4)            # increase pensize (takes integer)
t.pencolor("blue")     # set pencolor (takes string)
t.shape("turtle")

# draw square and triangle using for loops
for i in range(4):
    t.forward(50)          
    t.left(90)
for i in range(3):
    t.forward(100)          
    t.left(120) 
# end commands

# Wait for user to close window
win.mainloop()
