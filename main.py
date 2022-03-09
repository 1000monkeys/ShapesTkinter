import tkinter
import turtle
from tkinter import *


def print_hi():
    print('Hi, test')


def change_to_triangle():
    triangleMenu.pack()
    main.pack_forget()


def draw_triangle(triangle):
    scale = 200 / max(triangle["edges"]["a"], max(triangle["edges"]["b"], triangle["edges"]["c"]))

    turtle.left(180 + triangle["corners"]["C"])
    turtle.forward(triangle["edges"]["b"] * scale)

    turtle.left(180 + triangle["corners"]["A"])
    turtle.forward(triangle["edges"]["c"] * scale)

    turtle.left(180 + triangle["corners"]["B"])
    turtle.forward(triangle["edges"]["a"] * scale)

'''
    turtle.right(180 + triangle["corners"]["B"])
    turtle.forward(triangle["edges"]["a"] * scale)

    turtle.right(180 + triangle["corners"]["C"])
    turtle.forward(triangle["edges"]["b"] * scale)

    turtle.right(180 + triangle["corners"]["A"])
    turtle.forward(triangle["edges"]["c"] * scale)
'''


gui = Tk()
gui.title("Shapes By Kjell Vos")

main = Frame(gui)

font = ('Verdana', 15)

main.columnconfigure(0, pad=15)
main.columnconfigure(1, pad=15)

main.rowconfigure(0, pad=15)
main.rowconfigure(1, pad=15)

squareLabel = Label(main, text="Square", font=font)
squareImage = PhotoImage(file="assets/square.png")
squareButton = Button(main, image=squareImage, text="Square", command=print_hi)

squareLabel.grid(row=0, column=0)
squareButton.grid(row=1, column=0)

circleLabel = Label(main, text="Circle", font=font)
circleImage = PhotoImage(file="assets/circle.png")
circleButton = Button(main, image=circleImage, text="Circle", command=print_hi)

circleLabel.grid(row=0, column=1)
circleButton.grid(row=1, column=1)

triangleLabel = Label(main, text="Triangle", font=font)
triangleImage = PhotoImage(file="assets/triangle.png")
triangleButton = Button(main, image=triangleImage, text="Triangle", command=change_to_triangle)

triangleLabel.grid(row=0, column=2)
triangleButton.grid(row=1, column=2)

main.pack()

# TRIANGLE MENU #
triangleMenu = Frame(gui)

triangleSideALabel = Label(triangleMenu, text="Side A:", font=font)
triangleSideAEntry = Entry(triangleMenu)
triangleSideALabel.grid(row=0, column=1)
triangleSideAEntry.grid(row=0, column=2)

triangleSideBLabel = Label(triangleMenu, text="Side B:", font=font)
triangleSideBEntry = Entry(triangleMenu)
triangleSideBLabel.grid(row=1, column=1)
triangleSideBEntry.grid(row=1, column=2)

triangleSideCLabel = Label(triangleMenu, text="Side C:", font=font)
triangleSideCEntry = Entry(triangleMenu)
triangleSideCLabel.grid(row=2, column=1)
triangleSideCEntry.grid(row=2, column=2)

triangleCornerALabel = Label(triangleMenu, text="Corner A:", font=font)
triangleCornerAEntry = Entry(triangleMenu)
triangleCornerALabel.grid(row=3, column=1)
triangleCornerAEntry.grid(row=3, column=2)

triangleCornerBLabel = Label(triangleMenu, text="Corner B:", font=font)
triangleCornerBEntry = Entry(triangleMenu)
triangleCornerBLabel.grid(row=4, column=1)
triangleCornerBEntry.grid(row=4, column=2)

triangleCornerCLabel = Label(triangleMenu, text="Corner C:", font=font)
triangleCornerCEntry = Entry(triangleMenu)
triangleCornerCLabel.grid(row=5, column=1)
triangleCornerCEntry.grid(row=5, column=2)
# END TRIANGLE MENU #

turtle.mode("logo")
turtle.hideturtle()

triangle = {"edges": {"c": 5, "b": 5, "a": 5}, "corners": {"C": 60, "B": 60, "A": 60}}
draw_triangle(triangle)

triangle = {"edges": {"c": 5, "b": 4, "a": 3}, "corners": {"C": 90, "B": 53.13, "A": 36.87}}
draw_triangle(triangle)

triangle = {"edges": {"c": 5.5, "b": 5.3, "a": 6.1}, "corners": {"C": 57.4, "B": 54, "A": 68.6}}
draw_triangle(triangle)

triangle = {"edges": {"c": 5.5, "b": 3.2, "a": 7.9}, "corners": {"C": 33.1, "B": 18.2, "A": 128.6}}
draw_triangle(triangle)

gui.mainloop()
