import tkinter as tk
from tkinter import messagebox

def calculate_bill():
    try:
        previous = float(entry_previous.get())
        current = float(entry_current.get())
        
        if current < previous:
            messagebox.showwarning("Помилка", "Поточні покази не можуть бути меншими за попередні!")
            return
            
        used_kwh = current - previous
        price_per_kwh = 4.32
        total_price = used_kwh * price_per_kwh
        
        messagebox.showinfo("Результат", f"Використано: {used_kwh:.2f} кВт·год\nДо сплати: {total_price:.2f} грн")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові значення!")

# Створення головного вікна
root = tk.Tk()
root.title("Electricity bill")
root.geometry("350x200")
root.configure(bg="#d9d9d9") # Light gray background from the image

# Налаштування шрифтів
font_main = ("Arial", 10)
font_bold = ("Arial", 10, "bold")

# Центрування елементів
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Заголовок
label_title = tk.Label(root, text="Покази лічильника", bg="#d9d9d9", font=font_main)
label_title.grid(row=0, column=0, columnspan=2, pady=(10, 10))

# Попередні покази
label_previous = tk.Label(root, text="Попередні, кВт", bg="#d9d9d9", font=font_main)
label_previous.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_previous = tk.Entry(root, font=font_main)
entry_previous.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Поточні покази
label_current = tk.Label(root, text="Поточні, кВт", bg="#d9d9d9", font=font_main)
label_current.grid(row=2, column=0, padx=10, pady=5, sticky="e")

entry_current = tk.Entry(root, font=font_main)
entry_current.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Кнопка розрахунку
btn_calculate = tk.Button(
    root, 
    text="Розрахувати", 
    command=calculate_bill, 
    bg="black", 
    fg="white", 
    font=font_bold, 
    padx=10, 
    pady=5
)
btn_calculate.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
