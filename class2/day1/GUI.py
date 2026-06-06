# Importing the GUI
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("setconst's text editor")

# Create a text editor within the window
editor = tk.Text(root, width=80, height=20)
editor.pack()

# Keep the window open
root.mainloop()
