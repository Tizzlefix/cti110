import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("purple")     # set pencolor (takes string)
t.shape("turtle")

#Pen commands to draw my initials
t.forward(50)
t.penup()
t.forward(-25)
t.pendown()
t.right(90)
t.forward(80)
t.right(90)
t.forward(35)
t.penup()
t.setposition(80, 0)
t.pendown()
t.left(90)
t.forward(80)
t.left(90)
t.forward(50)
# end commands

# Wait for user to close window
win.mainloop()            
