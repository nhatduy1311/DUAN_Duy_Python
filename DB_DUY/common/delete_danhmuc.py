import mysql.connector
from mysql.connector import Error
from ketnoidb.ketnoi_mysql import connect_mysql

def delete_danhmuc(ma_danhmuc):
    """Xóa 1 danh mục theo mã"""
    connection = connect_mysql()
    if connection:
        try:
            cursor = connection.cursor()
            sql = "DELETE FROM danhmuc WHERE MaDanhMuc = %s"
            cursor.execute(sql, (ma_danhmuc,))
            connection.commit()
            if cursor.rowcount > 0:
                print(f"✅ Đã xóa danh mục có mã: {ma_danhmuc}")
            else:
                print(f"⚠️ Không tìm thấy danh mục có mã: {ma_danhmuc}")
        except Error as e:
            print(f"❌ Lỗi khi xóa danh mục: {e}")
        finally:
            cursor.close()
            connection.close()