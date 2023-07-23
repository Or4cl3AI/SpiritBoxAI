```python
import tkinter as tk
from tkinter import messagebox
from src.ai_models.ghost_detection_model import detectGhost
from src.ai_models.evp_enhancement_model import enhanceEVP
from src.ai_models.paranormal_activity_detection_model import detectParanormalActivity

class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("AI Ghost Hunting App")

        self.ghost_detection_canvas = tk.Canvas(self.window, width=500, height=500)
        self.ghost_detection_canvas.pack()

        self.evp_enhancement_player = tk.Label(self.window, text="EVP Player")
        self.evp_enhancement_player.pack()

        self.paranormal_activity_chart = tk.Label(self.window, text="Paranormal Activity Chart")
        self.paranormal_activity_chart.pack()

        self.detect_ghost_button = tk.Button(self.window, text="Detect Ghost", command=self.detect_ghost)
        self.detect_ghost_button.pack()

        self.enhance_evp_button = tk.Button(self.window, text="Enhance EVP", command=self.enhance_evp)
        self.enhance_evp_button.pack()

        self.detect_paranormal_activity_button = tk.Button(self.window, text="Detect Paranormal Activity", command=self.detect_paranormal_activity)
        self.detect_paranormal_activity_button.pack()

    def detect_ghost(self):
        result = detectGhost()
        messagebox.showinfo("Ghost Detection Result", result)

    def enhance_evp(self):
        result = enhanceEVP()
        messagebox.showinfo("EVP Enhancement Result", result)

    def detect_paranormal_activity(self):
        result = detectParanormalActivity()
        messagebox.showinfo("Paranormal Activity Detection Result", result)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
```