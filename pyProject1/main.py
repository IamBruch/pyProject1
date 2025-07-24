from tkinter import *
import math

ROWS = 8
COLS = 20

root = Tk()

C = Canvas(root, height = ROWS * 50 + 100, width = COLS * 50, bg = "#fbf5de")
chessBoard = [[0 for _ in range(COLS)] for _ in range(ROWS)]
print(chessBoard)

def drawChessBoard():

    #Vykresli chessboard na canvas podla definovanych rozmerov - ROWS, COLS
    #teda je flexibilny a da sa menit pocet riadkov a stlpcov

    for row in range(ROWS):
        for col in range(COLS):
            x1 = col * 50
            y1 = row * 50
            x2 = x1 + 50
            y2 = y1 + 50

            color = "#fbf5de" if (row + col) % 2 == 0 else "#660000"
            C.create_rectangle(x1, y1, x2, y2, fill=color)

def convertCord(x, y):
    x = x / 50
    x = math.ceil(x)

    y = y / 50
    y = math.ceil(y)
    return x, y

def getCord(event):
    x,y = convertCord(event.x, event.y)
    print(f"Clicked at: x = {x}, y = {y}")




class Piece:
    def __init__(self, color, row, col):
        self.row = int(row)
        self.col = int(col)
        self.color = color

    def draw(self):
        x1 = self.col * 50 + 5
        y1 = self.row * 50 + 5
        x2 = x1 + 25
        y2 = y1 + 25
        C.create_oval(x1, y1, x2, y2, fill=self.color)
        C.create_polygon(x1 + 12.5, y1 + 25, x1 + 25, y1 + 12.5, x1 + 25, y1 + 25, fill=self.color)


drawChessBoard()
Piece("red", 0, 0).draw()
# Example pieces

root.bind("<Button-1>", getCord)






C.pack()
mainloop()