# import tkinter as tk
# import random
#
#
# # Function to draw random red box
# def draw_red_box(canvas, width, height):
#     # Random coordinates within the window bounds
#     x1 = random.randint(0, width - 50)
#     y1 = random.randint(0, height - 50)
#     x2 = x1 + random.randint(20, 100)
#     y2 = y1 + random.randint(20, 100)
#
#     # Draw the red box
#     canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=2)
#
#
# # Create the main window
# root = tk.Tk()
# root.title("Custom Window")
#
# # Define window size
# width = 400
# height = 300
#
# # Set window size
# root.geometry(f"{width}x{height}")
#
# # Create a canvas to draw on
# canvas = tk.Canvas(root, width=width, height=height)
# canvas.pack()
#
# # Draw text at specific coordinates
# canvas.create_text(50, 50, text="Hello, world!", font=("Arial", 16))
# canvas.create_text(200, 150, text="This is a random box", font=("Arial", 16))
#
# # Draw a random red box
# draw_red_box(canvas, width, height)
#
# # Run the application
# root.mainloop()

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()