import tkinter as tk
from src.ai_models.ghost_detection_model import detectGhost

class GhostDetectionInterface:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg='black', bd=0, highlightthickness=0)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.detect_ghost)

    def detect_ghost(self, event):
        x, y = event.x, event.y
        result = detectGhost(x, y)
        if result:
            self.canvas.create_oval(x-10, y-10, x+10, y+10, fill='red')
        else:
            self.canvas.create_oval(x-10, y-10, x+10, y+10, fill='green')

if __name__ == "__main__":
    root = tk.Tk()
    GhostDetectionInterface(root)
    root.mainloop()