from datetime  import datetime
class Product:
    def __init__(self,product_id,name,price,stock):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.stock=stock
    def purchase(self,quantity):
            if quantity<=0:
                print("Số lượng mua phải lớn hơn 0")
                return
            if (quantity>self.stock):
                print(f"Không đủ hàng trong kho,chỉ còn {self.stock} sản phẩm")
            else:
                 self.stock=quantity
                 print(f"Đã mua {quantity} sản phẩm ,số lượng còn lại {self.stock} sản phẩm")    
    def restock(self,quantity):
            if quantity<=0:
                print("Số lượng nhập phải lớn hơn 0")
                return
            self.stock+=quantity
            print(f"Đã nhận thêm {quantity} sản phẩm .Tổng số lượng hiện tại là {self.stock}" )
    def get_product_info(self):
         print ("----Thông tin sản phẩm----")
         print (f"Mã sản phẩm:{self.product_id}")
         print (f"Tên sản phẩm: {self.name}")
         print (f"Giá:{self.price} VND")
         print (f"Số lượng tồn kho: {self.stock}")
class PerishableProduct(Product):
    def __init__(self, product_id, name, price, stock,expiry_date):
          super().__init__(product_id, name, price, stock)
          self.expiry_date=datetime.strptime(expiry_date,"%d/%m/%Y")
    def check_expiry(self):
            today=datetime.now()
            if(today>self.expiry_date):
                 print ("Sản phẩm đã hết hạn")
            else:
                 day_left=(self.expiry_date -today).days
                 print(f"Sản phẩm còn hạn.Còn {day_left} ngày nữa hết hạn")
    def get_product_info(self):
         super().get_product_info()
         print(f"Ngày hết hạn :{self.expiry_date.strftime("%d/%m/%Y")}")
product1=Product("KH001","Bàn phím Mitsumi",22000,15)
product1.get_product_info()
product1.purchase(20)
product1.purchase(5)
product1.restock(10)
product1.get_product_info()
product2=PerishableProduct("ST","Sữa tươi vinamilk",25000,10,"15/03/2026")
product2.get_product_info()
product2.purchase(5)
product2.check_expiry()
product2.restock(10)
product2.get_product_info()