import cv2
import numpy as np

def overlay_stamp(image_path, stamp_path, output_path, position=(50, 50), transparency=1, scale=1):
    """
    Chèn con dấu lên ảnh.
    
    :param image_path: Đường dẫn đến ảnh chính (ảnh nền).
    :param stamp_path: Đường dẫn đến ảnh con dấu.
    :param output_path: Đường dẫn lưu ảnh đầu ra.
    :param position: Tọa độ (x, y) để chèn con dấu lên ảnh.
    :param transparency: Độ trong suốt của con dấu (0: hoàn toàn trong suốt, 1: hoàn toàn đậm).
    """
    # Đọc ảnh chính và con dấu
    image = cv2.imread(image_path)
    stamp = cv2.imread(stamp_path, cv2.IMREAD_UNCHANGED)
    print(image.shape)
    # Kiểm tra nếu con dấu có kênh alpha (định dạng PNG)
    if stamp.shape[2] == 4:  # Nếu con dấu có 4 kênh (RGBA)
        alpha = stamp[:, :, 3] / 255.0  # Kênh alpha (0-1)
        stamp = stamp[:, :, :3]  # Chỉ lấy kênh RGB
    else:
        alpha = np.ones(stamp.shape[:2], dtype=np.float32)  # Nếu không có alpha, đặt toàn bộ là 1 (đậm)

    # Resize con dấu nếu cần (ví dụ: giảm kích thước để phù hợp với ảnh chính)
    stamp_height, stamp_width = stamp.shape[:2]
    stamp = cv2.resize(stamp, (int(stamp_width * scale), int(stamp_height * scale)))
    alpha = cv2.resize(alpha, (int(stamp_width * scale), int(stamp_height * scale)))

    # Lấy kích thước ảnh chính và con dấu
    image_height, image_width = image.shape[:2]
    stamp_height, stamp_width = stamp.shape[:2]

    # Xác định vị trí để chèn con dấu (x, y)
    x, y = position

    # Đảm bảo con dấu không vượt quá biên ảnh chính
    x_end = min(x + stamp_width, image_width)
    y_end = min(y + stamp_height, image_height)
    x = max(x, 0)
    y = max(y, 0)

    # Chỉ lấy phần con dấu nằm trong biên ảnh
    stamp_width = x_end - x
    stamp_height = y_end - y
    stamp = stamp[:stamp_height, :stamp_width]
    alpha = alpha[:stamp_height, :stamp_width]

    # Chèn con dấu lên ảnh chính
    for c in range(3):  # Với mỗi kênh màu (B, G, R)
        image[y:y+stamp_height, x:x+stamp_width, c] = (
            image[y:y+stamp_height, x:x+stamp_width, c] * (1 - alpha * transparency) +
            stamp[:, :, c] * (alpha * transparency)
        )

    # Lưu ảnh kết quả
    cv2.imwrite(output_path, image)
    print(f"Ảnh đã được lưu tại: {output_path}")


# Đường dẫn ảnh và con dấu
image_path = "a49b12418b8c31d2689d12.jpg"  # Ảnh nền
stamp_path = "stamp_exc.png"  # Ảnh con dấu (nên dùng định dạng PNG có alpha)
output_path = f"../2_{image_path}"  # Ảnh kết quả

# Gọi hàm để chèn con dấu
overlay_stamp(image_path, stamp_path, output_path, position=(500, 1700), transparency=1, scale=1.4)
overlay_stamp(output_path, stamp_path, output_path, position=(1600, 1700), transparency=1, scale=1.4)

