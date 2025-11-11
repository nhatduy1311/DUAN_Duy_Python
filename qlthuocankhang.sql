-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 04, 2025 lúc 03:47 AM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `qlthuocankhang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `danhmuc`
--

CREATE TABLE `danhmuc` (
  `MaDanhMuc` int(11) NOT NULL,
  `TenDanhMuc` varchar(100) NOT NULL,
  `MoTa` text DEFAULT NULL,
  `TrangThai` tinyint(4) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `danhmuc`
--

INSERT INTO `danhmuc` (`MaDanhMuc`, `TenDanhMuc`, `MoTa`, `TrangThai`) VALUES
(1, 'Bán chạy', NULL, 1),
(2, 'Thuốc', NULL, 1),
(3, 'Thực phẩm chức năng', NULL, 1),
(4, 'Thiết bị, công cụ y tế', NULL, 1),
(5, 'Dược mỹ phẩm', NULL, 1),
(6, 'Chăm sóc cá nhân', NULL, 1),
(7, 'Chăm sóc trẻ em', NULL, 1);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `sanpham`
--

CREATE TABLE `sanpham` (
  `MaSanPham` int(11) NOT NULL,
  `TenSanPham` varchar(200) NOT NULL,
  `GiaGoc` decimal(10,0) DEFAULT NULL,
  `GiaBan` decimal(10,0) DEFAULT NULL,
  `GiamGia` int(11) DEFAULT NULL,
  `DungTich` varchar(50) DEFAULT NULL,
  `MoTa` text DEFAULT NULL,
  `HinhAnh` varchar(255) DEFAULT NULL,
  `MaDanhMuc` int(11) DEFAULT NULL,
  `TrangThai` tinyint(4) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `sanpham`
--

INSERT INTO `sanpham` (`MaSanPham`, `TenSanPham`, `GiaGoc`, `GiaBan`, `GiamGia`, `DungTich`, `MoTa`, `HinhAnh`, `MaDanhMuc`, `TrangThai`) VALUES
(1, 'Nước muối Việt sát khuẩn, bướu miệng', 7000, 4900, 30, '500ml', NULL, 'viettrue.png', 3, 1),
(2, 'Thực phẩm dinh dưỡng Y Học Ensure Gold', 932000, 845000, 9, '800g', NULL, 'ensure_gold.png', 3, 1),
(3, 'Sữa bột Anlene Gold hương Vani', 555000, 480000, 13, '800g', NULL, 'anlene_gold.png', 3, 1),
(4, 'Costar Omega 3', 972000, 729000, 25, '365 viên', NULL, 'costar_omega3.png', 3, 1);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  ADD PRIMARY KEY (`MaDanhMuc`);

--
-- Chỉ mục cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD PRIMARY KEY (`MaSanPham`),
  ADD KEY `MaDanhMuc` (`MaDanhMuc`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `danhmuc`
--
ALTER TABLE `danhmuc`
  MODIFY `MaDanhMuc` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  MODIFY `MaSanPham` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `sanpham`
--
ALTER TABLE `sanpham`
  ADD CONSTRAINT `sanpham_ibfk_1` FOREIGN KEY (`MaDanhMuc`) REFERENCES `danhmuc` (`MaDanhMuc`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
