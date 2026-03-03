class Book:
    def __init__(self,id,title,author):
        self.id=id
        self.title=title
        self.author=author
        self.status="Có sẵn"
    def get_book_infor(self):
        print ("--Thông tin sách--")
        print (f"Mã sách:{self.id}")
        print (f"Tiêu đề:{self.title}")
        print(f"Tác giả:{self.author}")
        print(f"Tình trạng:{self.status}")
    def borrow(self):
        if(self.status=="Có sẵn"):
            self.status="Đã mượn"
            print(f"Đã mượn sách {self.title}")
        else:
            print(f"Sách {self.title} chưa được mượn")
class Ebook(Book):
    def __init__(self,id,title,author,file_size,format):
        super().__init__(id, title, author)  
        self.file_size=file_size
        self.format=format
    def get_book_infor(self):
        super().get_book_infor()
        print(f"Kích thước file:{self.file_size}")
        print(f"Định dạng:{self.format}")
# book=Book(1,"Chí Phèo","Văn Cao")
# book.get_book_infor()
# book.borrow()
# book.get_book_infor()
ebook=Ebook(1,"Chí Phèo","Văn Cao",1000,"PDF")
ebook.get_book_infor()