```python
import tkinter as tk
from src.ai_models.standard_research_tools import StandardResearchTools

class StandardResearchToolsInterface:
    def __init__(self, root):
        self.root = root
        self.standard_tools = StandardResearchTools()

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.start_button = tk.Button(self.frame, text="Start Standard Tools", command=self.start_tools)
        self.start_button.pack()

        self.stop_button = tk.Button(self.frame, text="Stop Standard Tools", command=self.stop_tools)
        self.stop_button.pack()

    def start_tools(self):
        self.standard_tools.start()

    def stop_tools(self):
        self.standard_tools.stop()

if __name__ == "__main__":
    root = tk.Tk()
    interface = StandardResearchToolsInterface(root)
    root.mainloop()
```