import tkinter as tk

breite = int(input("Wie breit ist das Schachbrett?: "))
hoehe = int(input("Wie lang ist das Schachbrett?: "))
brettgroeße = 8
feldgroeße = breite // brettgroeße


fenster = tk.Tk()
fenster.title("Schachbrett")

canvas = tk.Canvas(fenster, width=breite, height=hoehe)
canvas.pack()

def draw_board():
    colors = ["white","black"]
    for reihe in range(brettgroeße):
        for spalte in range(brettgroeße):
            x = spalte * feldgroeße
            y = reihe * feldgroeße
            x2 = x + feldgroeße
            y2 = y + feldgroeße
            color = colors[(reihe + spalte) % 2]
            canvas.create_rectangle(x, y, x2, y2, fill=color)


def starte_spiel():
    draw_board()
    fenster.mainloop()

starte_spiel()


