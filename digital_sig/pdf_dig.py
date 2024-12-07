import fitz  # PyMuPDF
import cv2
import numpy as np
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


def remove_background(image_path, img_out_path):
    """
    Tách nền của hình ảnh và giữ lại độ trong suốt.
    """
    # Đọc hình ảnh
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # Kiểm tra nếu ảnh có kênh alpha (để xử lý trong suốt)
    if img.shape[2] == 4:
        alpha_channel = img[:, :, 3]
        _, mask = cv2.threshold(alpha_channel, 0, 255, cv2.THRESH_BINARY)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    else:
        img_rgb = img

    # Chuyển đổi sang không gian màu HSV
    hsv_img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

    # Xác định phạm vi màu để tách nền (điều chỉnh tùy thuộc vào màu nền)
    lower_bound = np.array([0, 0, 200])  # Giới hạn dưới cho màu nền (ví dụ: màu trắng)
    upper_bound = np.array([180, 30, 255])  # Giới hạn trên cho màu nền

    # Tạo mặt nạ để tách nền
    mask = cv2.inRange(hsv_img, lower_bound, upper_bound)

    # Đảo ngược mặt nạ để giữ lại phần không phải nền
    mask_inv = cv2.bitwise_not(mask)

    # Tách nền ra khỏi hình ảnh bằng mặt nạ
    img_no_bg = cv2.bitwise_and(img_rgb, img_rgb, mask=mask_inv)

    # Thêm kênh alpha để giữ độ trong suốt
    b, g, r = cv2.split(img_no_bg)
    alpha = mask_inv  # Sử dụng mask_inv làm kênh alpha

    # Kết hợp các kênh BGR và alpha
    img_rgba = cv2.merge((b, g, r, alpha))

    with open(img_out_path, "w") as f:
        cv2.imwrite(img_out_path, img_rgba)
    
    return img_rgba
def insert_stamp(pdf_path, stamp_path, output_path, x, y, idx_page = 2):
    """
    Chèn con dấu vào file PDF.
    - pdf_path: Đường dẫn file PDF gốc.
    - stamp_path: Đường dẫn file ảnh con dấu.
    - output_path: Đường dẫn file PDF sau khi chèn dấu.
    - x, y: Tọa độ (x, y) chèn con dấu trên trang PDF.
    """
    # Mở file PDF
    pdf_document = fitz.open(pdf_path)
    
    # Đọc dữ liệu nhị phân từ file ảnh con dấu
    with open(stamp_path, "rb") as stamp_file:
        stamp_image = stamp_file.read()
    sd = 0
    for page in pdf_document:
        if sd == idx_page - 1:
                
            # Tính toán vị trí chèn dấu
            stamp_rect = fitz.Rect(x, y, x + 100, y + 100)  # Điều chỉnh kích thước con dấu

            # Chèn hình ảnh con dấu vào PDF
            page.insert_image(stamp_rect, stream=stamp_image)
            break
        else :
            sd += 1
            
    # Lưu file PDF đã chỉnh sửa
    pdf_document.save(output_path)
    print(f"File PDF đã chèn dấu được lưu tại: {output_path}")

def sign_pdf(pdf_path, private_key_path, signature_path):
    """
    Tạo chữ ký số cho file PDF.
    - pdf_path: Đường dẫn file PDF.
    - private_key_path: Đường dẫn file chứa khóa riêng.
    - signature_path: Đường dẫn file lưu chữ ký số.
    """
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    # Tạo hash của PDF
    pdf_hash = SHA256.new(pdf_data)

    # Đọc khóa riêng
    with open(private_key_path, "rb") as f:
        private_key = RSA.import_key(f.read())

    # Tạo chữ ký số
    signature = pkcs1_15.new(private_key).sign(pdf_hash)

    # Lưu chữ ký vào file
    with open(signature_path, "wb") as f:
        f.write(signature)
    print(f"Chữ ký số được lưu tại: {signature_path}")

def verify_pdf_signature(pdf_path, signature_path, public_key_path):
    """
    Xác minh chữ ký số của file PDF.
    - pdf_path: Đường dẫn file PDF.
    - signature_path: Đường dẫn file chữ ký số.
    - public_key_path: Đường dẫn file chứa khóa công khai.
    """
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    # Tạo hash của PDF
    pdf_hash = SHA256.new(pdf_data)

    # Đọc chữ ký
    with open(signature_path, "rb") as f:
        signature = f.read()

    # Đọc khóa công khai
    with open(public_key_path, "rb") as f:
        public_key = RSA.import_key(f.read())

    # Xác minh chữ ký
    try:
        pkcs1_15.new(public_key).verify(pdf_hash, signature)
        print("Chữ ký hợp lệ! PDF không bị thay đổi.")
    except (ValueError, TypeError):
        print("Chữ ký không hợp lệ! PDF có thể đã bị chỉnh sửa.")

a = remove_background('stamp.png', "stamp_exc.png")
insert_stamp("input_pdf.pdf", "stamp_exc.png", "stamped_output.pdf", x=350, y=500)
sign_pdf("stamped_output.pdf", "private.pem", "signature.sig")
verify_pdf_signature("stamped_output.pdf", "signature.sig", "public.pem")


