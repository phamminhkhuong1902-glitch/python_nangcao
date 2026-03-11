import tkinter as tk
from tkinter import ttk
def get_city(event):
    print("Thành phố:",combo_city.get())
root=tk.Tk()
root.geometry("300x200")
tk.Label(root,text="Chọn thành phố:").pack()
combo_city=ttk.Combobox(root,width=20)
combo_city['values']=("Hà Nội","Đà Nẵng","TP.Hồ Chí Minh","Cần Thơ")
combo_city['state']="readonly"
combo_city.pack()
combo_city.bind("<<ComboboxSelected>>",get_city)
root.mainloop()