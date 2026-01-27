with open("btn.2cd.txt","w",encoding="utf-8") as f:
    f.write("Thân em vừa trắng lại vừa tròn\nBảy nổi ba chìm với nước non\n")

with open("btn.2cc.txt","w",encoding="utf-8") as f:
    f.write("Rắn nát mặc dầu tay kẻ nặn\nMà em vẫn giữ tâm lòng son")

with open("btn.txt","w",encoding="utf-8") as f,\
    open("btn.2cd.txt","r",encoding="utf-8") as f1,\
    open("btn.2cc.txt","r",encoding="utf-8") as f2:
    f.write("Bánh trôi nước\n")
    f.write(f1.read())
    f.write(f2.read())
    f.write("\nHồ Xuân Hương")
