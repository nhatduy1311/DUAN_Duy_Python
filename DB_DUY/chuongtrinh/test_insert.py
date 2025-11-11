from common.insertdanhmuc import insert_danhmuc
while True:
    ten=input("Nhập vào tên danh mục")
    mota=input("Nhập vaò mô tả")
    insert_danhmuc(ten,mota)
    con=input("Tiếp tục y, Thoát thì nhấn kí tự bất kỳ")
    if con!="y":
        break