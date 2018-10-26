import tkinter as tk

window = tk.Tk()
window.title("PyDatabase")
window.geometry("1400x1200")
title = tk.Label(text=("Hello World"))
title.grid(row = 0)
btn = tk.Button(text="Click here")
btn.grid(row =1)
window.mainloop()