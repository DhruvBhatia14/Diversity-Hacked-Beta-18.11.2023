import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("University and Program Picker")

label = tk.Label(root, text="Welcome to University and Program Picker!", font=('Helvetica', 14))
label.pack(pady=30)

root.mainloop()