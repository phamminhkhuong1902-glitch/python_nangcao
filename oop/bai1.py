class Hinhchunhat:
    def __init__(self,chieuDai=0,chieuRong=0):
        self.chieuDai=chieuDai
        self.chieuRong=chieuRong
    def tinhchuvi(self):
        return (self.chieuDai+self.chieuRong)*2
    def tinhdientich(self):
        return self.chieuDai*self.chieuRong
    def show_infor(self):
        print (f"Chiều dài:{self.chieuDai}")
        print (f"Chiều rộng:{self.chieuRong}")
        print (f"Chu vi:{self.tinhchuvi()}")
        print (f"Diện tích:{self.tinhdientich()}")
    def nhap(self):
        while True:
            try:
                self.chieuDai=int(input("Nhập chiều dài: "))
                self.chieuRong=int(input("Nhập chiều rộng: "))
                if(self.chieuDai>0 and self.chieuRong>0):
                    break
                print("Vui lòng nhập các cạnh lớn hơn 0!")
            except ValueError:
                print ("Sai kiểu dữ liệu")
hcn=Hinhchunhat()
hcn.nhap()
hcn.show_infor()


