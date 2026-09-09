import tkinter as tk

root = tk.Tk()
root.title("Larios Browser")
root.geometry("400x200")

label = tk.Label(root, text="Welcome to Larios Browser", font=("Arial", 16))
label.pack(pady=20)

root.mainloop()
