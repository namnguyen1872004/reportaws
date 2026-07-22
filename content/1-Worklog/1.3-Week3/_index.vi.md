---
title: "Worklog Tuần 3"
date: 2026-05-18
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu tuần 3:
* Thực hành chuyên sâu về Amazon EC2, lưu trữ Amazon S3, phân quyền IAM theo nguyên tắc least privilege và làm quen AWS Cloud9.
* Triển khai Static Website Hosting trên S3, kết hợp CDN Amazon CloudFront và cấu hình cơ sở dữ liệu Amazon RDS.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu / Công cụ |
| --- | --- | --- | --- | --- |
| 2 | - Khởi tạo Amazon EC2, lựa chọn AMI, instance type và cấu hình lưu trữ phù hợp.<br> - Tạo IAM User/Role phục vụ thao tác quản trị và cấp quyền truy cập theo nguyên tắc least privilege. | 18/05/2026 | 18/05/2026 | Amazon EC2 & IAM Docs |
| 3 | - Tạo Amazon S3 bucket; tìm hiểu bucket policy, object ownership và Block Public Access.<br> - Bật Versioning và kiểm tra thao tác tải lên, tải xuống, khôi phục phiên bản object. | 19/05/2026 | 19/05/2026 | Amazon S3 Docs |
| 4 | - Làm quen với môi trường lập trình AWS Cloud9.<br> - Triển khai Static Website Hosting trên Amazon S3 và kiểm tra truy cập nội dung tĩnh. | 20/05/2026 | 20/05/2026 | AWS Cloud9 & S3 Hosting |
| 5 | - Kết hợp Amazon CloudFront với S3 để phân phối nội dung; tìm hiểu cache và invalidation.<br> - Thực hành sao chép dữ liệu sang Region khác và đánh giá phương án dự phòng dữ liệu. | 21/05/2026 | 21/05/2026 | Amazon CloudFront Docs |
| 6 | - Khởi tạo Amazon RDS, cấu hình kết nối từ EC2 đến RDS và kiểm tra truy vấn dữ liệu.<br> - Thực hành sao lưu/khôi phục; tìm hiểu Lightsail Database, snapshot và các ứng dụng mẫu như WordPress, PrestaShop, Akaunting. | 22/05/2026 | 22/05/2026 | Amazon RDS & Lightsail Docs |

### Kết quả đạt được tuần 3:
* Thực hành Amazon EC2, Amazon S3 và IAM User/Role theo nguyên tắc phân quyền phù hợp.
* Triển khai Static Website Hosting trên S3, kết hợp Amazon CloudFront, Versioning và sao chép dữ liệu sang Region khác.
* Khởi tạo Amazon RDS, kết nối ứng dụng từ EC2 và thực hành sao lưu/khôi phục; tìm hiểu Lightsail Database và snapshot.

### Đánh giá tuần 3:
* **Mức độ hoàn thành:** Tốt. Hoàn thành nhiều bài thực hành liên kết compute, storage, CDN và database.
* **Ưu điểm:** Có khả năng kết nối nhiều dịch vụ AWS thành một luồng triển khai hoàn chỉnh.
* **Điểm cần cải thiện:** Cần hệ thống hóa lại quyền IAM, bảo mật dữ liệu và chi phí của từng phương án triển khai.