class Circle:
    def __init__(self,bankinh=0):
        self.bankinh=bankinh
    

    def tinhchuvi(self):
        return self.bankinh*2*3.14
    def tinhdientich(self):
        return self.bankinh*self.bankinh*3.14
    def scale(self,k):
        self.bankinh*=k
    def show_infor(self):
        print (f"Bán kính:{self.bankinh}")
        print (f"Chu vi:{self.tinhchuvi()}")
        print (f"Diện tích:{self.tinhdientich()}")
    def input(self):
        while True:
            try:
                self.bankinh=float(input("Nhập bán kính: "))
                self.k=float(input("Nhập k: "))
                if self.bankinh>0 and self.k >0:
                    break
                print("Nhập bán kính và k lớn hơn 0")
            except ValueError:
                print ("Sai kiểu dữ liệu")

tron=Circle()
tron.input()
tron.show_infor()
while True:
    try:    
        k=float(input("Nhập k: "))
        if k >0:
            tron.scale(k)
            tron.show_infor()
            break
        print("Nhập k lớn hơn 0")
    except ValueError:
                print ("Sai kiểu dữ liệu")