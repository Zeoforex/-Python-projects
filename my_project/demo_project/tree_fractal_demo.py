import turtle

print("Введите значение ширины стебля вашего дерева, длину деерева и угол поворота: ")
width_tree = int(input("Введите значение ширины стебля вашего дерева "))
branch_length_tree = int(input("Введите значение длины вашего дерева "))
rotation_tree = int(input("Введите значение поворота "))


class Tree_Fractal(turtle.Turtle):
    def __init__(self, level):
        super(Tree_Fractal, self).__init__()
        self.level = level
        self.hideturtle()
        self.speed('fastest')
        self.left(90)
        self.width(width_tree)
        self.penup()
        self.back(branch_length_tree * 1.5)
        self.pendown()
        self.forward(branch_length_tree)
        self.draw_tree(branch_length_tree, level)

    def draw_tree(self, branch_length, level):
        width = self.width()
        self.width(width * 3. / 4.)
        branch_length *= 3. / 4.
        self.left(rotation_tree)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.right(2 * rotation_tree)
        self.forward(branch_length)

        if level > 0:
            self.draw_tree(branch_length, level - 1)
        self.back(branch_length)
        self.left(rotation_tree)

        self.width(width)


if __name__ == '__main__':
    tree_level = 10
    tree = Tree_Fractal(tree_level)
    turtle.done()
