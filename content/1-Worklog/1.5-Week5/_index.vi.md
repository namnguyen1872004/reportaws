---
title: "Worklog Tuần 5"
date: 2026-06-01
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Mục tiêu tuần 5:
* Cấu hình chuyên sâu Amazon ElastiCache for Redis, Cache Subnet Group trên nhiều Availability Zone và thử nghiệm Cluster Mode.
* Tối ưu hóa phân phối nội dung với CloudFront Origin Group, Failover, cache policy và thực hành lập trình tại biên với Lambda@Edge.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu / Công cụ |
| --- | --- | --- | --- | --- |
| 2 | - Cài đặt và cấu hình AWS CLI phục vụ bài thực hành ElastiCache.<br> - Tìm hiểu kiến trúc Amazon ElastiCache for Redis và các thành phần chính. | 01/06/2026 | 01/06/2026 | AWS CLI & ElastiCache Docs |
| 3 | - Tạo Cache Subnet Group trên nhiều Availability Zone.<br> - Kiểm tra Security Group và luồng kết nối từ ứng dụng đến Redis. | 02/06/2026 | 02/06/2026 | ElastiCache Redis Subnets |
| 4 | - Thử nghiệm Cluster Mode Enabled/Disabled và phân tích sự khác nhau về phân mảnh, mở rộng và tính sẵn sàng.<br> - Tích hợp AWS SDK để kiểm tra thao tác đọc/ghi dữ liệu cache. | 03/06/2026 | 03/06/2026 | AWS SDK & ElastiCache |
| 5 | - Cấu hình CloudFront Origin Group và cơ chế Failover.<br> - Tùy chỉnh cache policy, origin request policy và response headers phù hợp từng loại nội dung. | 04/06/2026 | 04/06/2026 | Amazon CloudFront Advanced |
| 6 | - Tìm hiểu Lambda@Edge và các giai đoạn Viewer Request, Origin Request, Origin Response, Viewer Response.<br> - Viết và kiểm thử một hàm xử lý đơn giản trên luồng HTTP, ghi nhận kết quả thực hành. | 05/06/2026 | 05/06/2026 | AWS Lambda@Edge Docs |

### Kết quả đạt được tuần 5:
* Cấu hình Amazon ElastiCache for Redis, Cache Subnet Group đa vùng và thử nghiệm các chế độ cluster.
* Tích hợp AWS SDK để kiểm tra thao tác đọc/ghi cache.
* Tối ưu Amazon CloudFront với Origin Group, Failover, cache policy, response headers và thực hành Lambda@Edge.

### Đánh giá tuần 5:
* **Mức độ hoàn thành:** Tốt. Hoàn thành các nội dung nâng cao về caching và phân phối nội dung.
* **Ưu điểm:** Hiểu được cơ chế failover, chính sách cache và các điểm can thiệp của Lambda@Edge.
* **Điểm cần cải thiện:** Cần bổ sung đo lường hiệu năng cache và rèn luyện xử lý lỗi khi triển khai hàm ở edge.