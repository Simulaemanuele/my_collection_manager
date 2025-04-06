import tkinter as tk
from .gui.main_window import MainWindow

def start_app():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
    
if __name__ == "__main__":
    start_app()
    