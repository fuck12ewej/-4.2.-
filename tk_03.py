import tkinter as tk

width = 400
height = 200

window = tk.Tk()
window.title("Button events")
window.geometry(f"{width}x{height}")


def change_bg(color):
    window.configure(bg=color)


button1 = tk.Button(
    window,
    text="Red",
    bg="red",
    fg="white",
    command=lambda: change_bg("red")
)
button1.pack(side="left", padx=10, expand=True)

button2 = tk.Button(
    window,
    text="Green",
    bg="green",
    fg="white",
    command=lambda: change_bg("green")
)
button2.pack(side="left", padx=10, expand=True)

button3 = tk.Button(
    window,
    text="Blue",
    bg="blue",
    fg="white",
    command=lambda: change_bg("blue")
)
button3.pack(side="left", padx=10, expand=True)

window.mainloop()
