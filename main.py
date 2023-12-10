import tkinter as tk

width = int(input("What is the width?: "))
height = int(input("What is the height?: "))
boardsize = 8
squaresize = width // boardsize


window = tk.Tk()
window.title("Schachbrett")

canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()

def draw_board():
    colors = ["white","black"]
    for row in range(boardsize):
        for columnn in range(boardsize):
            x = columnn * squaresize
            y = row * squaresize
            x2 = x + squaresize
            y2 = y + squaresize
            color = colors[(row + columnn) % 2]
            canvas.create_rectangle(x, y, x2, y2, fill=color)


def start():
    draw_board()
    window.mainloop()

start()


