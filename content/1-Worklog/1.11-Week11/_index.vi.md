---
title: "Worklog Tuần 11"
date: 2026-07-13
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Mục tiêu tuần 11:

- Hoàn thiện các chức năng và giao diện chính của Hệ thống Quản lý Giao hàng NightFury Express.
- Tích hợp ứng dụng với các dịch vụ AWS phục vụ cơ sở dữ liệu, lưu trữ minh chứng, tìm kiếm địa chỉ, xử lý sự kiện và gửi thông báo.
- Xây dựng kế hoạch kiểm thử, thực hiện Black-box Testing và White-box Testing cho sáu luồng nghiệp vụ ưu tiên.
- Ghi nhận lỗi, phân tích nguyên nhân và chuẩn bị phiên bản ứng dụng để triển khai trên AWS.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc                                                                                                                                                                                                                                                                                                  | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu / Công cụ                     |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | -------------------------------------------- |
| 2   | - Hoàn thiện các giao diện chính dành cho Khách hàng, Tài xế và Quản trị viên.<br>- Kiểm tra tính nhất quán về bố cục, điều hướng, phân quyền và dữ liệu hiển thị trên các màn hình.                                                                                                                       | 13/07/2026   | 13/07/2026      | ASP.NET Core / Frontend Tools                |
| 3   | - Hoàn thiện các chức năng tạo đơn, phân công tài xế, cập nhật trạng thái, upload POD, ghi nhận chữ ký và minh chứng giao thất bại.<br>- Rà soát kiểm tra dữ liệu đầu vào, thông báo phản hồi và khả năng hiển thị trên các kích thước màn hình khác nhau.                                                 | 14/07/2026   | 14/07/2026      | UI/UX Testing Tools                          |
| 4   | - Xây dựng kế hoạch kiểm thử và bộ Test Case theo phương pháp Black-box Testing cho sáu luồng ưu tiên: tạo đơn, phân quyền, phân công tài xế, cập nhật trạng thái, upload POD và xử lý lỗi/ngoại lệ.<br>- Xác định điều kiện kiểm thử, bước thực hiện, dữ liệu đầu vào, kết quả mong đợi và mã minh chứng. | 15/07/2026   | 15/07/2026      | Playwright / Test Plan / Test Cases          |
| 5   | - Thực hiện White-box Testing cho các hàm và luồng xử lý nghiệp vụ quan trọng.<br>- Kiểm tra điều kiện phân quyền, chuyển trạng thái đơn hàng, validation file, transaction, xử lý ngoại lệ và tính toàn vẹn dữ liệu.                                                                                      | 16/07/2026   | 16/07/2026      | xUnit / Moq / SQLite In-Memory               |
| 6   | - Thực thi các bộ kiểm thử, ghi nhận Test Case đạt và chưa đạt, phân tích nguyên nhân lỗi và điều chỉnh mã nguồn hoặc kịch bản kiểm thử.<br>- Tổng hợp kết quả kiểm thử và chuẩn bị phiên bản ứng dụng để triển khai trên Amazon EC2.                                                                      | 17/07/2026   | 17/07/2026      | Bug Tracking / Test Report / Release Package |

### Kết quả đạt được tuần 11:

- Hoàn thiện các chức năng và giao diện chính dành cho Khách hàng, Tài xế và Quản trị viên.
- Hoàn thiện các luồng tạo đơn hàng, phân công tài xế, cập nhật trạng thái, giao hàng thành công, giao hàng thất bại, upload POD, ghi nhận chữ ký và lưu minh chứng giao hàng.
- Tích hợp ứng dụng với Amazon RDS for MySQL, AWS Secrets Manager, Amazon S3, Amazon SQS, AWS Lambda, Amazon SES và Amazon Location.
- Xây dựng và thực thi các Test Case Black-box cho sáu luồng nghiệp vụ ưu tiên.
- Thực hiện White-box Testing đối với các quy tắc phân quyền, chuyển trạng thái, validation dữ liệu, xử lý file, transaction và ngoại lệ.
- Ghi nhận các Test Case Black-box chưa đạt, phân tích nguyên nhân và phân biệt lỗi ứng dụng với lỗi selector, kết quả điều hướng mong đợi hoặc cấu hình dịch vụ bên ngoài.
- Hoàn thiện tài liệu kiểm thử và chuẩn bị phiên bản ứng dụng cho giai đoạn triển khai trên AWS.

### Đánh giá tuần 11:

- **Mức độ hoàn thành:** Tốt. Các chức năng nghiệp vụ chính, giao diện, tích hợp AWS và hoạt động kiểm thử đã được hoàn thiện ở mức đủ để chuyển sang giai đoạn triển khai.
- **Ưu điểm:** Kết hợp Black-box Testing và White-box Testing để đánh giá hệ thống ở cả góc độ người dùng và logic xử lý bên trong; các Test Case được liên kết với các luồng nghiệp vụ ưu tiên.
- **Điểm cần cải thiện:** Tiếp tục xử lý các Test Case Black-box chưa đạt, tăng mức độ tự động hóa kiểm thử, kiểm tra lại tích hợp Amazon Location và bổ sung kiểm thử hiệu năng, bảo mật và cơ sở dữ liệu MySQL thực tế.
