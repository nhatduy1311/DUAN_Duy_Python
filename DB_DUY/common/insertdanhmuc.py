
"""Thêm 1 danh mục mới vào bảng danhmuc"""
from ketnoidb.ketnoi_mysql import connect_mysql
from mysql.connector import Error
def insert_danhmuc(ten_danhmuc, mota=None, trangthai=1):
    """Thêm 1 danh mục mới vào bảng danhmuc"""
    connection = connect_mysql()
    if connection:
        try:
            cursor = connection.cursor()
            sql = "INSERT INTO danhmuc (TenDanhMuc, MoTa, TrangThai) VALUES (%s, %s, %s)"
            data = (ten_danhmuc, mota, trangthai)
            cursor.execute(sql, data)
            connection.commit()
            print(f"✅ Đã thêm danh mục: {ten_danhmuc}")
        except Error as e:
            print(f"❌ Lỗi khi thêm danh mục: {e}")
        finally:
            cursor.close()
            connection.close()
