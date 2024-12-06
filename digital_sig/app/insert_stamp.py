import fitz

def insert_stamp(pdf_path, stamp_path, output_path, x, y, idx_page=2):
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
