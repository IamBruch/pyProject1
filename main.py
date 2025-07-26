from tkinter import *
import math

ROWS = 8
COLS = 8
TILE = 50

root = Tk()

C = Canvas(root, height = ROWS * 50 + 100, width = COLS * 50 + 100, bg = "#fbf5de")
chessBoard = [[0 for _ in range(COLS)] for _ in range(ROWS)]
print(chessBoard)
C.pack()

class Piece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.id = None

    def moveTo(self, x, y):
        dx = x - self.x
        dy = y - self.y
        C.move(self.id, dx, dy)
        self.x = x
        self.y = y

class Pawn(Piece):
    def draw(self):
        self.id = C.create_oval(self.x + 5, self.y + 5, self.x + TILE - 5, self.y + TILE - 5, fill=self.color, outline="black", width=2)



def drawChessBoard():
    for row in range(ROWS):
        for col in range(COLS):
            x1 = col * TILE
            y1 = row * TILE
            x2 = x1 + TILE
            y2 = y1 + TILE
            color = "#fbf5de" if (row + col) % 2 == 0 else "#660000"
            C.create_rectangle(x1, y1, x2, y2, fill=color)

def convertCord(x, y):
    return x // TILE, y // TILE

def getCord(event):
    x,y = convertCord(event.x, event.y)
    print(f"Clicked at: x = {x}, y = {y}")

dragged_piece = None
offset_x = 0
offset_y = 0

def on_mouse_down(event):
    global dragged_piece, offset_x, offset_y
    items = C.find_overlapping(event.x, event.y, event.x, event.y)
    for item in items:
        if item == pawn.id:
            dragged_piece = pawn
            offset_x = event.x - pawn.x
            offset_y = event.y - pawn.y
            break

def on_mouse_move(event):
    if dragged_piece:
        new_x = event.x - offset_x
        new_y = event.y - offset_y
        dragged_piece.moveTo(new_x, new_y)

def on_mouse_up(event):
    global dragged_piece
    if dragged_piece:
        # zarovnaj na mriežku
        grid_x = (event.x // TILE) * TILE
        grid_y = (event.y // TILE) * TILE
        dragged_piece.moveTo(grid_x, grid_y)
        dragged_piece = None

drawChessBoard()

# Vytvorenie pešiaka vpravo od šachovnice
pawn = Pawn("white", COLS * TILE + 10, 10)
pawn.draw()

# Bindovanie udalostí
C.bind("<Button-1>", on_mouse_down)
C.bind("<B1-Motion>", on_mouse_move)
C.bind("<ButtonRelease-1>", on_mouse_up)

mainloop()
