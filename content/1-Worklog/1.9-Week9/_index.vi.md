---
title: "Worklog Tuần 9"
date: 2026-06-29
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Mục tiêu tuần 9:

- Thiết kế kiến trúc tổng thể cho project Hệ thống Quản lý Giao hàng NightFury Express.
- Xác định các thành phần ứng dụng, cơ sở dữ liệu, lưu trữ, xử lý sự kiện, bảo mật và giám sát.
- Ánh xạ các thành phần hệ thống với dịch vụ AWS phù hợp và xây dựng Architecture Diagram.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc                                                                                                                                                                                                                                                                                              | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu / Công cụ                  |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | --------------- | ----------------------------------------- |
| 2   | - Rà soát yêu cầu nghiệp vụ và các luồng chính của NightFury Express đã xác định trong tuần 8.<br>- Xác định các tiêu chí thiết kế kiến trúc gồm bảo mật, khả năng mở rộng, khả năng bảo trì, tính sẵn sàng và chi phí triển khai.                                                                     | 29/06/2026   | 29/06/2026      | AWS Architecture Best Practices           |
| 3   | - Xác định các thành phần chính gồm ứng dụng ASP.NET Core, cơ sở dữ liệu MySQL, lưu trữ POD và chữ ký, dịch vụ địa chỉ, xử lý sự kiện đơn hàng, gửi email và giám sát hệ thống.<br>- Mô tả trách nhiệm và phương thức giao tiếp giữa các thành phần.                                                   | 30/06/2026   | 30/06/2026      | Tài liệu kiến trúc hệ thống               |
| 4   | - Ánh xạ các thành phần hệ thống với Amazon EC2, Application Load Balancer, Amazon RDS for MySQL, AWS Secrets Manager, Amazon S3, Amazon SQS, AWS Lambda, Amazon SES, Amazon Location, AWS IAM và Amazon CloudWatch.<br>- Xây dựng phiên bản đầu của Architecture Diagram bằng AWS Architecture Icons. | 01/07/2026   | 01/07/2026      | AWS Architecture Icons / Diagram Tools    |
| 5   | - Bổ sung luồng request, luồng dữ liệu, IAM Role, Security Group, public subnet, private subnet và các điểm kiểm soát bảo mật vào sơ đồ.<br>- Kiểm tra tính hợp lý của kiến trúc và khả năng triển khai trên môi trường AWS.                                                                           | 02/07/2026   | 02/07/2026      | Security and Data Flow Specifications     |
| 6   | - Đối chiếu kiến trúc với các luồng nghiệp vụ tạo đơn, phân công tài xế, cập nhật trạng thái, lưu POD, chữ ký, minh chứng thất bại và gửi thông báo.<br>- Hoàn thiện Architecture Diagram và cập nhật tài liệu thiết kế theo góp ý của người hướng dẫn.                                                | 03/07/2026   | 03/07/2026      | Tài liệu kiến trúc và thiết kế hoàn chỉnh |

### Kết quả đạt được tuần 9:

- Xác định kiến trúc tổng thể của NightFury Express gồm lớp truy cập, mạng, ứng dụng, dữ liệu, lưu trữ media, xử lý sự kiện và giám sát.
- Ánh xạ các thành phần của hệ thống với những dịch vụ AWS phù hợp.
- Hoàn thiện Architecture Diagram thể hiện luồng request từ người dùng qua Amazon CloudFront, AWS WAF, Application Load Balancer đến ứng dụng ASP.NET Core trên Amazon EC2.
- Xác định luồng dữ liệu và tích hợp giữa Amazon EC2, Amazon RDS for MySQL, Amazon S3, Amazon Location, Amazon SQS, AWS Lambda và Amazon SES.
- Xác định yêu cầu về IAM Role, Security Group, subnet và AWS Secrets Manager nhằm bảo đảm kết nối an toàn giữa các dịch vụ.
- Phân biệt các thành phần được triển khai trong phạm vi Workshop với EC2 Auto Scaling và cơ chế sao lưu, phục hồi RDS là các nội dung chưa triển khai hoàn chỉnh.

### Đánh giá tuần 9:

- **Mức độ hoàn thành:** Tốt. Kiến trúc đã thể hiện được các thành phần chính, luồng request, luồng dữ liệu, ranh giới mạng và các điểm kiểm soát bảo mật của hệ thống.
- **Ưu điểm:** Liên kết được yêu cầu nghiệp vụ của NightFury Express với giải pháp kỹ thuật và các dịch vụ AWS phù hợp.
- **Điểm cần cải thiện:** Tiếp tục đối chiếu sơ đồ với kết quả triển khai thực tế, bổ sung phân tích chi phí và làm rõ các thành phần định hướng như EC2 Auto Scaling, sao lưu và phục hồi RDS.
