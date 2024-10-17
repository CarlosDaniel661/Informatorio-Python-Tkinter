import os
import tkinter as tk
from interfaces.login import LoginApp

print("Directorio de trabajo actual:", os.getcwd())

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")
    app = LoginApp(root)
    root.mainloop()
