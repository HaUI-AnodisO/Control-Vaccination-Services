# Sử dụng image Python chính thức làm base image
FROM python:3.11-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Copy file requirements.txt vào container
COPY requirements.txt /app/

# Cài đặt các dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . /app/

# Mở cổng 8000 cho FastAPI
EXPOSE 8000

# Lệnh để chạy FastAPI với Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
