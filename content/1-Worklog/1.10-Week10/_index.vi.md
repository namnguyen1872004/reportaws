---
title: "Worklog Tuần 10"
date: 2026-07-06
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Mục tiêu tuần 10:

- Thiết kế mô hình dữ liệu khái niệm và lược đồ cơ sở dữ liệu logic cho project Hệ thống Quản lý Giao hàng NightFury Express.
- Xác định các thực thể, thuộc tính, khóa chính, khóa ngoại, quan hệ và ràng buộc dữ liệu.
- Thiết kế wireframe và giao diện người dùng cho các luồng nghiệp vụ chính của Khách hàng, Tài xế và Quản trị viên.
- Bảo đảm sự thống nhất giữa cơ sở dữ liệu, Use Case, Business Rules, giao diện và Architecture Diagram.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc                                                                                                                                                                                                                                                  | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu / Công cụ              |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------- | ------------------------------------- |
| 2   | - Xác định các thực thể dữ liệu và thuộc tính chính của NightFury Express.<br>- Phác thảo mô hình dữ liệu tổng thể gồm người dùng, hồ sơ, hub, đơn hàng, lịch sử trạng thái, vị trí tài xế, thanh toán, đánh giá, POD, chữ ký và minh chứng giao thất bại. | 06/07/2026   | 06/07/2026      | Công cụ thiết kế cơ sở dữ liệu        |
| 3   | - Thiết kế quan hệ giữa người dùng, đơn hàng, tài xế, hub và lịch sử trạng thái.<br>- Xác định khóa chính, khóa ngoại, kiểu dữ liệu, bội số quan hệ và các ràng buộc toàn vẹn dữ liệu.                                                                     | 07/07/2026   | 07/07/2026      | Công cụ thiết kế ERD                  |
| 4   | - Hoàn thiện lược đồ cơ sở dữ liệu logic và rà soát việc chuẩn hóa các bảng.<br>- Kiểm tra khả năng đáp ứng các chức năng tạo đơn, phân công tài xế, cập nhật trạng thái, theo dõi giao hàng, lưu POD, chữ ký và minh chứng giao thất bại.                 | 08/07/2026   | 08/07/2026      | Tài liệu đặc tả lược đồ cơ sở dữ liệu |
| 5   | - Thiết kế wireframe cho các màn hình đăng nhập, đăng ký, tạo đơn hàng, theo dõi đơn, dashboard tài xế và dashboard quản trị viên.<br>- Xác định luồng thao tác của Khách hàng, Tài xế và Quản trị viên.                                                   | 09/07/2026   | 09/07/2026      | Figma / Công cụ thiết kế wireframe    |
| 6   | - Thiết kế giao diện cho tạo đơn, phân công tài xế, cập nhật trạng thái giao hàng, ghi nhận giao thành công, giao thất bại, upload POD và chữ ký.<br>- Đối chiếu giao diện với Use Case Diagram, Business Rules, cơ sở dữ liệu và Architecture Diagram.    | 10/07/2026   | 10/07/2026      | Tài liệu thiết kế UI/UX               |

### Kết quả đạt được tuần 10:

- Xác định các thực thể, thuộc tính, khóa chính, khóa ngoại và quan hệ cần thiết cho hệ thống NightFury Express.
- Hoàn thiện ERD khái niệm và lược đồ quan hệ logic gồm người dùng, hồ sơ, hub, đơn hàng, lịch sử trạng thái, vị trí tài xế, thanh toán và đánh giá.
- Xác định cách liên kết đơn hàng với các đối tượng media lưu trên Amazon S3; cơ sở dữ liệu chỉ lưu object key và metadata thay vì lưu trực tiếp file nhị phân.
- Kiểm tra lược đồ dữ liệu có khả năng hỗ trợ vòng đời đơn hàng: pending → assigned → shipping → done hoặc failed.
- Thiết kế wireframe và giao diện cho tạo đơn hàng, theo dõi đơn, phân công tài xế, cập nhật trạng thái, upload POD, ghi nhận chữ ký và minh chứng giao thất bại.
- Đối chiếu và bảo đảm sự thống nhất giữa Use Case, Business Rules, mô hình dữ liệu, giao diện và kiến trúc AWS.

### Đánh giá tuần 10:

- **Mức độ hoàn thành:** Tốt. Mô hình dữ liệu và giao diện đã được thiết kế phù hợp với các yêu cầu và luồng nghiệp vụ chính của NightFury Express.
- **Ưu điểm:** Có sự liên kết rõ ràng giữa quy trình nghiệp vụ, thực thể dữ liệu, vai trò người dùng, màn hình giao diện và chức năng hệ thống.
- **Điểm cần cải thiện:** Tiếp tục kiểm tra index, ràng buộc dữ liệu, transaction, các trường hợp biên, khả năng hiển thị responsive và sự nhất quán giữa object key trên Amazon S3 với dữ liệu đơn hàng.
