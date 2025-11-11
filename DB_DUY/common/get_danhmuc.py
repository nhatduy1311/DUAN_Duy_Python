import mysql.connector
from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

"""Lấy danh sách tất cả danh mục"""
def get_all_danhmuc():
    connection = connect_mysql()
    danh_sach = []

    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            sql = "SELECT MaDanhMuc, TenDanhMuc, MoTa, TrangThai FROM danhmuc"
            cursor.execute(sql)
            danh_sach = cursor.fetchall()

            print(f"✅ Đã lấy {len(danh_sach)} danh mục từ CSDL.")
            return danh_sach
        except Error as e:
            print(f"❌ Lỗi khi lấy danh sách danh mục: {e}")
            return []
        finally:
            cursor.close()
            connection.close()
    else:
        print("⚠️ Không thể kết nối MySQL.")
        return []
