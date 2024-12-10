# Sử dụng image Python chính thức làm base image
FROM python:3.11-slim

# Cài đặt thư viện OpenGL và các thư viện phụ thuộc
RUN apt-get update && apt-get install -y libgl1-mesa-glx

RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/
# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Copy file requirements.txt vào container
COPY requirements.txt /app/

# Cài đặt các dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . /app/

# Mở cổng 8000 cho FastAPI
EXPOSE 8001

# Lệnh để chạy FastAPI với Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
