[![Github license](https://img.shields.io/github/license/HaUI-AnodisO/Control-Vaccination-Services 'Github license')](https://github.com/HaUI-AnodisO/Control-Vaccination-Services/blob/develop/LICENSE)
[![Open issues](https://img.shields.io/github/issues/HaUI-AnodisO/Control-Vaccination-Services 'Open issues')](https://github.com/HaUI-AnodisO/Control-Vaccination-Services/issues)
[![Open Pull Requests](https://img.shields.io/github/issues-pr/HaUI-AnodisO/Control-Vaccination-Services 'Open Pull Requests')](https://github.com/HaUI-AnodisO/Control-Vaccination-Services/pulls)
[![Commit activity](https://img.shields.io/github/commit-activity/m/HaUI-AnodisO/Control-Vaccination-Services 'Commit activity')](https://github.com/HaUI-AnodisO/Control-Vaccination-Services/graphs/commit-activity)
[![GitHub contributors](https://img.shields.io/github/contributors/HaUI-AnodisO/Control-Vaccination-Services 'Github contributors')](https://github.com/HaUI-AnodisO/Control-Vaccination-Services/graphs/contributors)
![](./docs/images/banner.png)

# Control-Vaccination-Services

<a href="https://github.com/HaUI-AnodisO/Control-Vaccination-Services/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=">Bug Report ⚠️</a>
<a href="https://github.com/HaUI-AnodisO/Control-Vaccination-Services/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=">Request Feature 👩‍💻</a>
 
![Trang chủ](docs/images/trang_chu.png)


Ứng dụng quản lý tiêm chủng, phát triển trên nền tảng Budibase để tối ưu quy trình và giảm thao tác thủ công.

Mục tiêu phát triển ứng dụng quản lý tiêm chủng, phát triển trên nền tảng LCDP Budibase kết hợp với AI, tự động hóa quy trình để giảm thao tác thủ công và nâng cao hiệu quả quản lý.  

Dự án được thực hiện trong cuộc thi [Phần Mềm Nguồn Mở-Olympic Tin học Sinh viên Việt Nam 2024](https://www.olp.vn/procon-pmmn/ph%E1%BA%A7n-m%E1%BB%81m-ngu%E1%BB%93n-m%E1%BB%9F). Được open source theo giấy phép [Apache License, Version 2.0](https://opensource.org/license/apache-2-0) bởi đội tác giả HaUI-AnodisO.

Để biết thêm chi tiết về cuộc thi, bạn có thể xem tại [đây](https://vfossa.vn/tin-tuc/gioi-thieu-chu-de-cuoc-thi-phan-mem-nguon-mo-olp-2024-709.html).

Link thuyết trình Canva tại cuộc thi [link](https://www.canva.com/design/DAGY-gPSgIw/az2fo9xRoZm0WQ4q92iTyA/edit?utm_content=DAGY-gPSgIw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

Slide bài thuyết trình tại cuộc thi dưới dạng PDF có thể được truy cập tại đây: [Slide](docs/pdf/slinde.pdf)

---
## 🔎 Danh Mục

1. [Giới Thiệu](#Giới-Thiệu)
2. [Chức Năng Chính](#chức-năng-chính)
3. [Tổng Quan Hệ Thống](#-tổng-quan-hệ-thống)
4. [Cấu Trúc Thư Mục](#cấu-trúc-thư-mục)
5. [Thiết kế Database](#thiết-kế-database)
6. [Hướng Dẫn Cài Đặt](#hướng-dẫn-cài-đặt)
    - [📋 Yêu Cầu - Prerequisites](#yêu-cầu-📋)
    - [🔨 Cài Đặt](#🔨-cài-đặt)
7. [CI/CD](#cicd)
8. [🙌 Đóng Góp](#-đóng-góp-cho-dự-án)
9. [📝 License](#-license)


---


## Giới Thiệu

- [Công nghệ LCDP](https://vfossa.vn/tin-tuc/gioi-thieu-chu-de-cuoc-thi-phan-mem-nguon-mo-olp-2024-709.html) cho phép các công cụ cấu hình dễ dàng và triển khai nhanh chóng mà không cần phải lập trình nhiều.
- [Budibase](https://docs.budibase.com/docs/what-is-budibase)Budibase là nền tảng phát triển ứng dụng Low-Code, cho phép tạo nhanh các ứng dụng nội bộ với giao diện trực quan, tích hợp linh hoạt và khả năng triển khai dễ dàng.
---


## Chức Năng 
Dự án tập trung vào các chức năng chính sau:
- Đăng ký lịch tiêm chủng
- Thông báo lịch tiêm tự động
- Chatbot hỗ trợ thông minh
- Cấp giấy xác nhận tiêm chủng
- Xử lý phản hồi đăng ký nhanh chóng

Link đặc tả usecase [link](https://docs.google.com/document/d/1W7d9Jv12tFRPOvTuHa_aR0t0nrU0JI6fVPU96vjWVeA/edit?usp=sharing)

Document đặc tả usecase: [Doc](docs/pdf/usecase.pdf)


---

## 👩‍💻 Tổng Quan Hệ Thống

Mô hình hệ thống bao gồm các công nghệ:  
- [Docker](https://www.docker.com/): Containerize các service.
- [Nginx](https://nginx.org/en/): Reverse proxy server, load balancer, và web server cho các dịch vụ.
- [Budibase](https://budibase.com/): Nền tảng low-code để xây dựng và triển khai ứng dụng  nhanh chóng.
- [FastAPI](https://fastapi.tiangolo.com/): Framework web để xây dựng API nhanh chóng và hiệu quả với Python.
- [GeminiAI](https://aistudio.google.com/): tạo API hỗ trợ các mô hình trí tuệ nhân tạo và học máy
<img loading="lazy" src="docs/images/sysyem_architecture.svg" alt="System Architecture" width="100%" height=600>


## CI/CD

Project CI/CD sử dụng Github và [Github Actions](https://github.com/Anodis108/HAUI-HITAnodisO/tree/develop/.github/workflows) để tự động hóa quá trình build và deploy. Quy trình như hình vẽ sau:
![CI/CD](docs/images/ci_cd.svg)

- [commitlint.yml](https://github.com/HaUI-AnodisO/Control-Vaccination-Services/blob/develop/.github/workflows/commitlint.yml): Lint các commit message của các nhánh




## Cấu trúc thư mục
- [src](src/README.md): Các tệp export của budibase
- [Docs](docs): Tài liệu về hệ thống, cuộc thi, sử dụng.
- [AI](AI/README.md): Tài liệu về module ocr và OpenAPI AI Key

## Thiết kế Database
![alt text](docs/images/database.png)

---

## Hướng Dẫn Cài Đặt

### Yêu Cầu 📋
Trước khi cài đặt, bạn cần cài đặt các công cụ sau:

- [Docker](https://www.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)


### 🔨 Cài Đặt
---
#### Cài đặt budibase
Đầu tiên, ta cần cài đặt ứng dụng budibase về self-host, hoặc có thể sử dụng luôn chính website trang chủ budibase chính thức tại [đây](https://budibase.com/)

#### Để cài đặt budibase selfhost, ta thực hiện các bước như sau:
Bước 1. clone dự án budibase về máy của bạn:
```bash
git clone https://github.com/Budibase/budibase.git
```
Bước 2. cd vào thư mục hosting 
```bash
cd budibase/hosting/
```
Bước 3: Tạo tài khoản admin
- Bạn vào file .env, tìm đến và điền thông tin của mình ở phần này 
```bash
# An admin user can be automatically created initially if these are set
BB_ADMIN_USER_EMAIL=
BB_ADMIN_USER_PASSWORD=
```
Bước 4: chạy lệnh docker-compose
```bash
docker-compose --env-file hosting.properties up
```
Ứng dụng budibase của bạn sẽ chạy trên địa chỉ http://localhost:10000

--- 
#### Cài đặt AI
Trước hết, hãy cd vào thư mục AI
```bash
cd AI/
```
Sau đó, thực hiện các bước theo [hướng dẫn này](AI/README.md)

---
#### Import dự án của chúng tôi
Trước hết, hãy clone dự án về máy tính của bạn:

```bash
git clone https://github.com/HaUI-AnodisO/Control-Vaccination-Services.git
```
cd vào thư mục Control-Vaccination-Services/src:

```bash
cd Control-Vaccination-Services/src
```
Bạn sẽ thấy các file đã được giải nén ra. Việc cần làm là nén chúng lại giống như [hướng dẫn](src/README.md) để tạo file nén.   

---
Bây giờ, bạn hãy import thư mục nén này vào app budibase như sau họăc dựa theo [hướng dẫn này](https://docs.budibase.com/docs/export-and-import-apps#:~:text=Within%20the%20Apps%20screen%2C%20click,click%20Import%20app%20to%20finish.):  
## Hướng dẫn Cài đặt và Sử dụng

### Bước 1: Tải tệp nén
- Nếu bạn đã có tệp nén sau bước nén trên thì sẽ không cần thực hiện bước ày nữa, ta sẽ sử dụng luôn file nén đó.  

Truy cập vào phần **Release** trên GitHub, tìm tệp nén có tên `Vaccine.Control.Center-export-###.tar.gz`, đây là phần **Export app** của chúng tôi. Hãy tải tệp đó về máy.

### Bước 2: Đăng nhập vào ứng dụng
Mở ứng dụng và đăng nhập vào tài khoản của bạn.

### Bước 3: Tạo ứng dụng mới
Chọn **Create new app** để tạo một ứng dụng mới, sau đó chọn ứng dụng mới vừa tạo.

### Bước 4: Nhập ứng dụng
Vào phần **Settings**, chọn **Export/Import**, sau đó nhấn **Import app**  
![Import App](docs/images/budibase.png)

### Bước 5: Hoàn tất
Chọn tệp `Vaccine.Control.Center-export-###.tar.gz` mà bạn đã tải về, rồi nhấn **Update**. Vậy là bạn đã có thể sử dụng dịch vụ của chúng tôi ngay bây giờ!



---
## 🙌 Đóng góp cho dự án

<a href="https://github.com/Anodis108/HAUI-HITAnodisO/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=">Bug Report ⚠️
</a>

<a href="https://github.com/Anodis108/HAUI-HITAnodisO/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=">Feature Request 👩‍💻</a>

Nếu bạn muốn đóng góp cho dự án, hãy đọc [CONTRIBUTING.md](.github/CONTRIBUTING.md) để biết thêm chi tiết.

Mọi đóng góp của các bạn đều được trân trọng, đừng ngần ngại gửi pull request cho dự án.

## Liên hệ 

-   Phạm Đăng Đông: dong10082003@gmail.com
-   Nguyễn Thị Trang: nguyenthitrang.ttd@gmail.com
-   Đỗ Trung Hòa: trunghoa2k4@gmail.com


## 📝 License

This project is licensed under the terms of the [APACHE V2](LICENSE) license.