import tkinter
import turtle
from tkinter import *


def print_hi():
    print('Hi, test')


def change_to_triangle():
    triangleMenu.pack()
    main.pack_forget()


def setup_triangle():
    sideC = float(triangleSideCEntry.get())
    sideB = float(triangleSideBEntry.get())
    sideA = float(triangleSideAEntry.get())

    cornerC = float(triangleCornerCEntry.get())
    cornerB = float(triangleCornerBEntry.get())
    cornerA = float(triangleCornerAEntry.get())

    triangle = {"side": {"c": sideC, "b": sideB, "a": sideA}, "corners": {"C": cornerC, "B": cornerB, "A": cornerA}}

    turtle.setheading(0)
    turtle.speed(0)
    turtle.setpos(-105, -105)
    turtle.clear()
    draw_triangle(triangle)


def draw_triangle(triangle):
    scale = 200 / max(triangle["side"]["a"], max(triangle["side"]["b"], triangle["side"]["c"]))

    turtle.right(180 + triangle["corners"]["C"])
    turtle.forward(-1 * triangle["side"]["b"] * scale)

    turtle.right(180 + triangle["corners"]["A"])
    turtle.forward(-1 * triangle["side"]["c"] * scale)

    turtle.right(180 + triangle["corners"]["B"])
    turtle.forward(-1 * triangle["side"]["a"] * scale)

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
triangleSideALabel.grid(row=0, column=0)
triangleSideAEntry.grid(row=0, column=1)

triangleSideBLabel = Label(triangleMenu, text="Side B:", font=font)
triangleSideBEntry = Entry(triangleMenu)
triangleSideBLabel.grid(row=1, column=0)
triangleSideBEntry.grid(row=1, column=1)

triangleSideCLabel = Label(triangleMenu, text="Side C:", font=font)
triangleSideCEntry = Entry(triangleMenu)
triangleSideCLabel.grid(row=2, column=0)
triangleSideCEntry.grid(row=2, column=1)

triangleCornerALabel = Label(triangleMenu, text="Corner A:", font=font)
triangleCornerAEntry = Entry(triangleMenu)
triangleCornerALabel.grid(row=3, column=0)
triangleCornerAEntry.grid(row=3, column=1)

triangleCornerBLabel = Label(triangleMenu, text="Corner B:", font=font)
triangleCornerBEntry = Entry(triangleMenu)
triangleCornerBLabel.grid(row=4, column=0)
triangleCornerBEntry.grid(row=4, column=1)

triangleCornerCLabel = Label(triangleMenu, text="Corner C:", font=font)
triangleCornerCEntry = Entry(triangleMenu)
triangleCornerCLabel.grid(row=5, column=0)
triangleCornerCEntry.grid(row=5, column=1)

triangleSubmitButton = Button(triangleMenu, text="Submit", font=font, command=setup_triangle)
triangleSubmitButton.grid(row=6, column=0, columnspan=2)
# END TRIANGLE MENU #

turtle.setup(500, 500)
turtle.mode("logo")
turtle.hideturtle()
'''
triangle = {"side": {"c": 5, "b": 5, "a": 5}, "corners": {"C": 60, "B": 60, "A": 60}}
draw_triangle(triangle)

triangle = {"side": {"c": 5, "b": 4, "a": 3}, "corners": {"C": 90, "B": 53.13, "A": 36.87}}
draw_triangle(triangle)

triangle = {"side": {"c": 5.5, "b": 5.3, "a": 6.1}, "corners": {"C": 57.4, "B": 54, "A": 68.6}}
draw_triangle(triangle)

triangle = {"side": {"c": 5.5, "b": 3.2, "a": 7.9}, "corners": {"C": 33.1, "B": 18.2, "A": 128.6}}
draw_triangle(triangle)
'''
gui.mainloop()
