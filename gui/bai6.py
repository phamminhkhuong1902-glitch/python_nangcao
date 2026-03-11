import tkinter as tk
import math
def tinh_PT():
    try:
        a=float(entryA.get())
        b=float(entryB.get())
        c=float(entryC.get())
        delta=b**2-4*a*c
        x=-b/2*a
        x1=-(b+math.sqrt(a))/2*a
        x2=-(b-math.sqrt(a))/2*a
        if delta>0:
            ketqua=f"Phương trình có 2 nghiệm x1={x1},x2={x2}"
        elif delta ==0:
            ketqua=f"Phương trình có nghiệm kép x={x}"
        else:
            ketqua="Phương trình vô nghiệm"
        lbl_kq.config(text=f"delta=:{delta:.1f} - {ketqua}")
    except ValueError:
        lbl_kq.config("Vui lòng nhập đúng giá trị")

root=tk.Tk()
root.title("Phương trình bậc 2")
root.geometry("500x400")
lbl_title=tk.Label(root,text="Phương trình bậc 2",font=("Arial",14,"bold"))
lbl_title.grid(row=0,column=0,columnspan=2)
lbl_pt=tk.Label(root,text="AX^2 + BX+ C =0",font=("Arial",14,"bold"))
lbl_pt.grid(row=1,column=0,columnspan=2)
lblA=tk.Label(root,text="A=")
lblA.grid(row=2,column=0)
entryA=tk.Entry(root)
entryA.grid(row=2,column=1)
lblB=tk.Label(root,text="B=")
lblB.grid(row=2,column=2)
entryB=tk.Entry(root)
entryB.grid(row=2,column=3)
lblC=tk.Label(root,text="C=")
lblC.grid(row=2,column=4)
entryC=tk.Entry(root)
entryC.grid(row=2,column=5)
tinhPT=tk.Button(root,text="Tính PT",command=tinh_PT)
tinhPT.grid(row=3,column=0)
lbl_kq=tk.Label(root,text="")
lbl_kq.grid(row=4,column=0,columnspan=5)
root.mainloop()