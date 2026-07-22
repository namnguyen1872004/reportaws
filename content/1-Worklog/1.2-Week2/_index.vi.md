---
title: "Worklog Tuần 2"
date: 2026-05-11
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu tuần 2:
* Tìm hiểu và xây dựng nền tảng mạng AWS cơ bản với Amazon VPC, Subnet, Route Table, Internet Gateway, NAT Gateway.
* Cấu hình các lớp bảo mật mạng (Security Group, Network ACL) và khởi tạo EC2 Instance để kiểm tra kết nối.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu / Công cụ |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu khái niệm Amazon VPC, địa chỉ CIDR và vai trò của mạng riêng ảo trong kiến trúc AWS.<br> - Phân tích sự khác nhau giữa public subnet, private subnet và mô hình kết nối VPN. | 11/05/2026 | 11/05/2026 | Amazon VPC Docs |
| 3 | - Tạo VPC thực hành và phân chia các subnet theo từng lớp ứng dụng.<br> - Kiểm tra dải địa chỉ, Availability Zone và thiết lập tự động cấp public IPv4 cho subnet phù hợp. | 12/05/2026 | 12/05/2026 | AWS Management Console |
| 4 | - Tạo Route Table và Internet Gateway; cấu hình định tuyến cho public subnet.<br> - Kiểm tra luồng truy cập Internet và mối liên hệ giữa subnet, route table và gateway. | 13/05/2026 | 13/05/2026 | Amazon VPC Route Tables |
| 5 | - Tạo NAT Gateway cho private subnet; tìm hiểu Security Group và Network ACL.<br> - Thiết lập các quy tắc inbound/outbound theo nguyên tắc quyền tối thiểu. | 14/05/2026 | 14/05/2026 | AWS Security Groups & NACLs |
| 6 | - Tạo Key Pair và khởi tạo EC2 Instance trong VPC đã cấu hình.<br> - Thực hiện kiểm tra kết nối giữa các thành phần mạng, ghi nhận lỗi và hoàn thiện sơ đồ mạng thực hành. | 15/05/2026 | 15/05/2026 | Amazon EC2 Docs |

### Kết quả đạt được tuần 2:
* Hiểu vai trò của Amazon VPC, CIDR, public subnet, private subnet và mô hình kết nối VPN.
* Thực hành cấu hình Subnet, Route Table, Internet Gateway, NAT Gateway, Security Group và Network ACL.
* Tạo Key Pair, khởi tạo EC2 Instance và kiểm tra kết nối giữa các thành phần mạng.

### Đánh giá tuần 2:
* **Mức độ hoàn thành:** Tốt. Đã xây dựng được nền tảng mạng AWS cơ bản và kiểm tra được luồng kết nối.
* **Ưu điểm:** Nắm được mối liên hệ giữa subnet, route table, gateway và các lớp kiểm soát truy cập.
* **Điểm cần cải thiện:** Cần luyện thêm bài toán chia CIDR và kỹ năng xử lý lỗi định tuyến hoặc Security Group.