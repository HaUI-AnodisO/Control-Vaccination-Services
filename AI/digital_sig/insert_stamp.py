import fitz

def insert_stamp(pdf_path, stamp_path, output_path, x, y, idx_page=2):
    """
    Chèn một hình ảnh con dấu vào một trang cụ thể trong tài liệu PDF.

    Args:
        pdf_path (str): Đường dẫn đến tệp PDF mà bạn muốn chèn con dấu vào.
        stamp_path (str): Đường dẫn đến tệp hình ảnh con dấu (hỗ trợ các định dạng hình ảnh như PNG, JPG).
        output_path (str): Đường dẫn nơi lưu tệp PDF mới sau khi đã chèn con dấu.
        x (int): Tọa độ x của góc trên bên trái của vùng chèn dấu.
        y (int): Tọa độ y của góc trên bên trái của vùng chèn dấu.
        idx_page (int, optional): Số trang cần chèn dấu (mặc định là trang thứ 2). Trang được đánh số từ 1.

    Returns:
        None: Hàm này không trả về giá trị mà chỉ lưu tệp PDF đã được chèn dấu vào đường dẫn `output_path`.

    Raises:
        Exception: Nếu gặp lỗi trong quá trình chèn dấu hoặc lưu tệp PDF, sẽ ném ra ngoại lệ.

    Example:
        insert_stamp("input.pdf", "stamp.png", "output_stamped.pdf", 350, 500, 2)

    Ghi chú:
        - Hàm này chỉ chèn dấu vào trang cụ thể (chỉ định bởi `idx_page`).
        - Vị trí của dấu được xác định bởi tọa độ (x, y), với kích thước mặc định là 100x100 px.
        - Tệp PDF mới sau khi chèn dấu sẽ được lưu tại `output_path`.
    """
    pdf_document = fitz.open(pdf_path)
    with open(stamp_path, "rb") as stamp_file:
        stamp_image = stamp_file.read()
    sd = 0
    for page in pdf_document:
        if sd == idx_page - 1:
            stamp_rect = fitz.Rect(x, y, x + 100, y + 100)
            page.insert_image(stamp_rect, stream=stamp_image)
            break
        else:
            sd += 1
    pdf_document.save(output_path)
    print(f"File PDF đã chèn dấu được lưu tại: {output_path}")
