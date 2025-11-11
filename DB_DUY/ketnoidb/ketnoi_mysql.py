import mysql.connector
from mysql.connector import Error

def connect_mysql():
    try:
        # Thông tin kết nối CSDL
        connection = mysql.connector.connect(
            host='localhost',        # địa chỉ máy chủ MySQL
            user='root',             # tên tài khoản
            password='',             # mật khẩu MySQL (điền nếu có)
            database='qlthuocankhang'  # tên database bạn muốn dùng
        )
        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection
    except Error as e:
        print(f"❌ Lỗi kết nối: {e}")
        return None
