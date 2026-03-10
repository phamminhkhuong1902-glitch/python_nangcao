import tkinter as tk
def tinh_BMI():
    try:
        h=float(entrychieucao.get())
        w=float(entrycannang.get())
        bmi=w/(h**2)
        if bmi<18:
            loai="Thiếu cân"
        elif bmi <23:
            loai="Bình thường"
        elif bmi<30:
            loai="Thừa cân"
        else:
            loai="Béo phì"
        lbl_kq.config(text=f"BMI của bạn:{bmi:.1f} - Bạn thuộc loại :{loai}")
    except ValueError:
        lbl_kq.config("Vui lòng nhập đúng giá trị")
   

root=tk.Tk()
root.title("Tính chỉ số BMI")
root.geometry("300x200")
lbl_title=tk.Label(root,text="Tính chỉ số BMI",font=("Arial",18,"bold"))
lbl_title.grid(row=0,column=0,columnspan=2)
lblchieucao=tk.Label(root,text="Chiều cao:")
lblchieucao.grid(row=1,column=0)
entrychieucao=tk.Entry(root)
entrychieucao.grid(row=1,column=1)
lblcannang=tk.Label(root,text="Cân nặng:")
lblcannang.grid(row=2,column=0)
entrycannang=tk.Entry(root)
entrycannang.grid(row=2,column=1)
tinhbmi=tk.Button(root,text="Tính BMI",command=tinh_BMI)
tinhbmi.grid(row=3,column=0,columnspan=2)
lbl_kq=tk.Label(root,text="")
lbl_kq.grid(row=4,column=0,columnspan=2)
root.mainloop()
