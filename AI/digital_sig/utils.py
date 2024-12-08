import cv2
import numpy as np

def remove_background(image_path, img_out_path):
    """
    Tách nền khỏi hình ảnh và giữ lại độ trong suốt.

    Hàm này sử dụng phương pháp xử lý ảnh để loại bỏ nền của hình ảnh, chuyển nền thành trong suốt và lưu lại hình ảnh đã xử lý.

    Args:
        image_path (str): Đường dẫn đến tệp hình ảnh gốc cần loại bỏ nền.
        img_out_path (str): Đường dẫn nơi lưu tệp hình ảnh đã loại bỏ nền (định dạng PNG với độ trong suốt).

    Returns:
        numpy.ndarray: Hình ảnh đã loại bỏ nền, dưới dạng mảng NumPy với kênh alpha (trong suốt).

    Example:
        remove_background("input_image.png", "output_image.png")
    """
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    if img.shape[2] == 4:
        alpha_channel = img[:, :, 3]
        _, mask = cv2.threshold(alpha_channel, 0, 255, cv2.THRESH_BINARY)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    else:
        img_rgb = img

    hsv_img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)
    lower_bound = np.array([0, 0, 200])
    upper_bound = np.array([180, 30, 255])

    mask = cv2.inRange(hsv_img, lower_bound, upper_bound)
    mask_inv = cv2.bitwise_not(mask)
    img_no_bg = cv2.bitwise_and(img_rgb, img_rgb, mask=mask_inv)

    b, g, r = cv2.split(img_no_bg)
    alpha = mask_inv
    img_rgba = cv2.merge((b, g, r, alpha))

    cv2.imwrite(img_out_path, img_rgba)
    return img_rgba
