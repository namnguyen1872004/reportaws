---
title: "Worklog Tuần 4"
date: 2026-05-25
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu tuần 4:
* Tìm hiểu và triển khai ứng dụng container đơn giản với Amazon Lightsail Containers; cấu hình EC2 Auto Scaling Group.
* Thiết lập giám sát hệ thống bằng Amazon CloudWatch, quản lý DNS với Amazon Route 53 và tìm hiểu tổng quan DynamoDB, ElastiCache.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu / Công cụ |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu Amazon Lightsail Containers và quy trình đóng gói, triển khai một ứng dụng container đơn giản.<br> - Kiểm tra endpoint, log và trạng thái hoạt động của container sau khi triển khai. | 25/05/2026 | 25/05/2026 | Amazon Lightsail Containers |
| 3 | - Thiết lập Launch Template và EC2 Auto Scaling Group.<br> - Cấu hình số lượng instance tối thiểu, mong muốn, tối đa và kiểm tra khả năng tự động mở rộng. | 26/05/2026 | 26/05/2026 | EC2 Auto Scaling Docs |
| 4 | - Tìm hiểu Amazon CloudWatch Metrics, Logs và Dashboard.<br> - Tạo alarm theo dõi CPU/health và quan sát phản ứng của Auto Scaling trước thay đổi tải. | 27/05/2026 | 27/05/2026 | Amazon CloudWatch Docs |
| 5 | - Quản lý DNS bằng Amazon Route 53; tìm hiểu hosted zone, record và cơ chế định tuyến.<br> - Thực hành tạo bản ghi DNS cho tài nguyên ứng dụng. | 28/05/2026 | 28/05/2026 | Amazon Route 53 Docs |
| 6 | - Tìm hiểu tổng quan Amazon DynamoDB và Amazon ElastiCache.<br> - So sánh cơ sở dữ liệu NoSQL, caching và các tình huống sử dụng trong hệ thống web. | 29/05/2026 | 29/05/2026 | DynamoDB & ElastiCache Docs |

### Kết quả đạt được tuần 4:
* Triển khai ứng dụng container cơ bản với Amazon Lightsail Containers.
* Thiết lập EC2 Auto Scaling, theo dõi hệ thống bằng Amazon CloudWatch và tìm hiểu cơ chế mở rộng theo tải.
* Thực hành Amazon Route 53; có kiến thức tổng quan về Amazon DynamoDB và Amazon ElastiCache.

### Đánh giá tuần 4:
* **Mức độ hoàn thành:** Tốt. Hiểu được vai trò của container, Auto Scaling, monitoring và DNS trong vận hành hệ thống.
* **Ưu điểm:** Biết quan sát metric và liên hệ metric với hành vi mở rộng của hệ thống.
* **Điểm cần cải thiện:** Phần DynamoDB và ElastiCache mới ở mức nền tảng, cần thêm bài thực hành truy vấn và caching thực tế.