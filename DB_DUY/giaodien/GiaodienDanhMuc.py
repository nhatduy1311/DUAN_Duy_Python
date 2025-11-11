import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error


# ===== HÀM KẾT NỐI MYSQL =====
def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='qlthuocankhang'
        )
        return connection
    except Error as e:
        messagebox.showerror("Lỗi", f"Lỗi kết nối MySQL: {e}")
        return None


# ===== CÁC HÀM CSDL =====
def load_danhmuc():
    for row in tree.get_children():
        tree.delete(row)
    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM danhmuc")
        for row in cursor.fetchall():
            tree.insert("", "end", values=row)
        conn.close()


def insert_danhmuc():
    ten = entry_ten.get()
    mota = entry_mota.get()
    if ten == "":
        messagebox.showwarning("Thiếu dữ liệu", "Vui lòng nhập tên danh mục.")
        return
    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO danhmuc (TenDanhMuc, MoTa) VALUES (%s, %s)", (ten, mota))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Đã thêm danh mục mới.")
        load_danhmuc()
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)


def delete_danhmuc():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục cần xóa.")
        return
    values = tree.item(selected, "values")
    ma = values[0]

    if messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa danh mục '{values[1]}' không?"):
        conn = connect_mysql()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM danhmuc WHERE MaDanhMuc = %s", (ma,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Thành công", "Đã xóa danh mục.")
            load_danhmuc()


def update_danhmuc():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục cần sửa.")
        return
    values = tree.item(selected, "values")
    ma = values[0]

    ten = entry_ten.get()
    mota = entry_mota.get()

    if ten == "":
        messagebox.showwarning("Thiếu dữ liệu", "Tên danh mục không được để trống.")
        return

    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE danhmuc SET TenDanhMuc=%s, MoTa=%s WHERE MaDanhMuc=%s", (ten, mota, ma))
        conn.commit()
        conn.close()
        messagebox.showinfo("Thành công", "Đã cập nhật danh mục.")
        load_danhmuc()


def select_item(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, "values")
        entry_ten.delete(0, tk.END)
        entry_ten.insert(0, values[1])
        entry_mota.delete(0, tk.END)
        entry_mota.insert(0, values[2])


# ===== GIAO DIỆN CHÍNH =====
root = tk.Tk()
root.title("Quản lý Danh mục - Hệ thống Quản lý Nhà thuốc An Khang")
root.geometry("700x500")
root.resizable(False, False)

# --- Form nhập liệu ---
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Tên danh mục:").grid(row=0, column=0, padx=5, pady=5)
entry_ten = tk.Entry(frame_form, width=30)
entry_ten.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Mô tả:").grid(row=1, column=0, padx=5, pady=5)
entry_mota = tk.Entry(frame_form, width=30)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

# --- Các nút chức năng ---
frame_btn = tk.Frame(root)
frame_btn.pack(pady=5)

tk.Button(frame_btn, text="➕ Thêm", width=10, bg="#4CAF50", fg="white", command=insert_danhmuc).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="✏️ Sửa", width=10, bg="#2196F3", fg="white", command=update_danhmuc).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="❌ Xóa", width=10, bg="#f44336", fg="white", command=delete_danhmuc).grid(row=0, column=2, padx=5)
tk.Button(frame_btn, text="🔄 Tải lại", width=10, bg="#9C27B0", fg="white", command=load_danhmuc).grid(row=0, column=3, padx=5)

# --- Bảng hiển thị dữ liệu ---
frame_table = tk.Frame(root)
frame_table.pack(pady=10)

columns = ("MaDanhMuc", "TenDanhMuc", "MoTa", "TrangThai")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=15)

tree.heading("MaDanhMuc", text="Mã")
tree.heading("TenDanhMuc", text="Tên danh mục")
tree.heading("MoTa", text="Mô tả")
tree.heading("TrangThai", text="Trạng thái")

for col in columns:
    tree.column(col, width=150, anchor="center")

tree.pack()
tree.bind("<<TreeviewSelect>>", select_item)

# --- Gọi tải dữ liệu ban đầu ---
load_danhmuc()

root.mainloop()
