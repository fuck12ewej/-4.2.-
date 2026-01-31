import tkinter as tk

def set_day():

    root.config(bg="white")
 
    btn_day.pack_forget()

    btn_night.pack(pady=50)

def set_night():

    root.config(bg="black")

    btn_night.pack_forget()

    btn_day.pack(pady=50)

root = tk.Tk()
root.title("Day/Night Switcher")
root.geometry("300x200")

btn_day = tk.Button(root, text="Day", command=set_day, width=10)
btn_night = tk.Button(root, text="Night", command=set_night, width=10)


root.config(bg="white")
btn_night.pack(pady=50)

root.mainloop()
