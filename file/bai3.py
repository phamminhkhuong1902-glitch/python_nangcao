import os
src_img_name=input("Nhập tên file ảnh copy: ").strip()
if(not os.path.exists(src_img_name)):
    print("File ảnh không tồn tại")
else:
    new_img_name=input("Nhập tên file mới nhấp ok (bỏ qua):")
    if new_img_name =="":
        name,ext=os.path.splitext(src_img_name)
        new_img_name=name + "_1" + ext
    print(new_img_name)    