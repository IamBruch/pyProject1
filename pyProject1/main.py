from tkinter import *
import math



root = Tk()

C = Canvas(root, height = 400, width = 400, bg = "#fbf5de")

def drawChessBoard():
    bSquareX = 50
    bSquareY = 0

    for i in range(8):
        for i in range(4):
            blackSquare = C.create_rectangle(bSquareX, bSquareY, bSquareX + 50, bSquareY + 50, fill="#660000")
            bSquareX += 100
        bSquareY += 50
        bSquareX = 50 if bSquareY % 100 == 0 else 0

def convertCord(x, y):
    x = x / 50
    x = math.ceil(x)

    y = y / 50
    y = math.ceil(y)
    return x, y

def getCord(event):
    x,y = convertCord(event.x, event.y)
    print(f"Clicked at: x = {x}, y = {y}")

drawChessBoard()
# Example pieces

root.bind("<Button-1>", getCord)






C.pack()
mainloop()