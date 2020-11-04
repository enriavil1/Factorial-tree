import turtle

rotation= 35
main_length= 140
width= 15
colors= ["red","blue", "green", "yellow", "orange"]


class Tree_factor(turtle.Turtle):
    def __init__(self, level):
        super(Tree_factor, self).__init__()

        self.color("black")
        self.level= level
        self.hideturtle()
        self.speed(0)
        self.left(90)
        self.width(width)
        self.penup()
        self.back(main_length*1.5)
        self.pendown()
        self.forward(main_length)
        
        self.draw_tree(main_length,level)
    
    def draw_tree(self,branch_length,level):
        width= self.width()
        self.width(width * (1/2))
        branch_length *= 3./4.
        self.left(rotation)
        self.forward(branch_length)

        if level > 1:
            self.draw_tree(branch_length, level-1)
        
        try:
            self.color(colors[level-1])
        except Exception:
            self.color("black")
        

        self.back(branch_length)
        self.right(2*rotation)
        self.forward(branch_length)


        if level > 1:
            self.draw_tree(branch_length, level-1)

        try:
            self.color(colors[level-1])
        except Exception:
            self.color("black")

        self.back(branch_length)
        self.left(rotation)
        self.width(width)









if __name__ == "__main__":
    tree= Tree_factor(20)
    turtle.done()



