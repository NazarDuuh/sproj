import tkinter as tk
from tkinter import ttk

#relx rely relwidth relheight
root = tk.Tk()
root.geometry("500x500")
root.title("hey")

testtw = ttk.Treeview(root, columns=("t1", "t2"))
testtw.heading("#0", text="test 0",)
testtw.heading("t1", text="test 1")
testtw.heading("t2", text="test 2")

testtw.insert(
    "",
    tk.END,
    text="keyvalue",
    values=("test1value", "test2value")
)

testtw.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.6)

root.mainloop()
