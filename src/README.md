# Budibase App Extract Files

## Giới thiệu
Đây là bộ tệp tin được trích xuất từ ứng dụng của chúng tôi trên nền tảng **Budibase**. Bộ tệp này bao gồm các file cần thiết để quản lý và cấu hình lại ứng dụng, giúp dễ dàng chia sẻ và tái sử dụng trong các dự án khác.

## Cấu trúc thư mục
- `budibase-client.js`: File JavaScript chính, chứa các logic xử lý của ứng dụng.
- `db.txt`: File cơ sở dữ liệu được xuất từ Budibase, chứa cấu trúc và dữ liệu mẫu.
- `manifest.json`: File định nghĩa metadata của ứng dụng, bao gồm thông tin cấu hình và tài nguyên sử dụng.
- `README.md`: Tài liệu hướng dẫn sử dụng và thông tin về dự án.

## Hướng dẫn sử dụng
1. **Nén file**
   - nén file thành file **.tar.gz**
   ```bash
    tar -czvf Vaccine.Control.Center-export.tar.gz budibase-client.js db.txt manifest.json
   ```
2. **Tải ứng dụng vào Budibase:**
   - Đăng nhập vào tài khoản **Budibase** của bạn.
   - Tạo một ứng dụng mới hoặc chọn ứng dụng hiện có.

3. **Import file vào app**
    - Vào phần ***Settings***, chọn ***Export/Import*** rồi chọn ***Import app*** 
    - Chọn file **Vaccine.Control.Center-export.tar.gz**
    - Chọn **Update**. Vậy là bạn đã hoàn thành Import app của chúng tôi
