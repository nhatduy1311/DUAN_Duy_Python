from common.update_danhmuc import update_danhmuc

while True:
    madm = input("Nhập tên vàop danh muc")
    ten=input("Nhập vào tên danh mục")
    mota=input("Nhập vaò mô tả")
    update_danhmuc(madm,ten,mota)
    con=input("Tiếp tục y, Thoát thì nhấn kí tự bất kỳ")
    if con!="y":
        break