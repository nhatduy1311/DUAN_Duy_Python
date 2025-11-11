"""Cập nhật thông tin danh mục theo mã"""
from ketnoidb.ketnoi_mysql import connect_mysql


def update_danhmuc(ma_danhmuc, ten_moi=None, mota_moi=None, trangthai_moi=None):
    connection = connect_mysql()
    if connection:
        try:
            cursor = connection.cursor()

            # Xây dựng câu lệnh UPDATE động (chỉ cập nhật các cột được truyền vào)
            fields = []
            values = []

            if ten_moi is not None:
                fields.append("TenDanhMuc = %s")
                values.append(ten_moi)
            if mota_moi is not None:
                fields.append("MoTa = %s")
                values.append(mota_moi)
            if trangthai_moi is not None:
                fields.append("TrangThai = %s")
                values.append(trangthai_moi)

            if not fields:
                print("⚠️ Không có dữ liệu để cập nhật.")
                return

            values.append(ma_danhmuc)
            sql = f"UPDATE danhmuc SET {', '.join(fields)} WHERE MaDanhMuc = %s"

            cursor.execute(sql, tuple(values))
            connection.commit()

            if cursor.rowcount > 0:
                print(f"✅ Đã cập nhật danh mục có mã: {ma_danhmuc}")
            else:
                print(f"⚠️ Không tìm thấy danh mục có mã: {ma_danhmuc}")
        except Error as e:
            print(f"❌ Lỗi khi cập nhật danh mục: {e}")
        finally:
            cursor.close()
            connection.close()