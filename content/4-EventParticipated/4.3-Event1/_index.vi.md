---
title: "Event 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 4.3. </b> "
---


# Bài thu hoạch Hội thảo AWS Vietnam Community Day

### Mục Đích Của Sự Kiện

- Cập nhật góc nhìn thực tế từ cộng đồng AWS và FCAJ về bức tranh công nghệ trong kỷ nguyên AI.
- Hiểu rõ vai trò của Context Engineering trong việc vận hành các giải pháp AI ở quy mô thực tế.
- Khám phá cách xây dựng hệ thống CloudFront như một nền tảng nền tảng vững chắc cho performance, security và reliability.
- Trải nghiệm thực tế hành trình phát triển sản phẩm hackathon (UTMorpho) trong khoảng thời gian 36 giờ.
- Phân tích đặc tính bất định của LLM và cách thiết kế hệ thống Multi-Agent đáp ứng yêu cầu doanh nghiệp.

### Danh Sách Diễn Giả

- **Tịnh Trương** - Platform Engineer, GoTymeX (chuyên đề Context Engineering với AI)
- **Team VIB** (Thảo Nguyen, Mai Nguyen, Uyen Le) - GenAI Engineers, VIB (hành trình LotusHacks với UTMorpho)
- **Thịnh Nguyen** - DevOps Engineer, FCAJ (chuyên đề CloudFront Foundation)
- **Anh Pham** - Cloud Consultant, G-AsiaPacific Vietnam (Amazon Quick)
- **Đức Dao** - Solutions Architect, Cloud Kinetics (LLM Non-Determinism)
- **Vy Lam** - Senior Business Systems Analyst, VPBank (Multi-Agent System)
- **Anh Hưng** - Mentor chia sẻ định hướng đầu buổi

### Thông Tin Chương Trình

- **08:30 - 09:00:** Ổn định chỗ ngồi tại tầng 36
- **09:00 - 09:30:** Context Is Everything - Making AI Actually Work for You
- **09:30 - 10:00:** 36 hrs with LotusHacks - Building UTMorpho from Idea to Reality
- **10:00 - 10:40:** From Edge To Origin - CloudFront as Your Foundation
- **10:40 - 10:55:** Friendly AI Assistant with Amazon Quick
- **10:55 - 11:00:** Nghỉ giữa giờ
- **11:00 - 11:30:** Non-Determinism of "Deterministic" LLM Settings
- **11:30 - 12:00:** Enterprise-Grade Multi-Agent System - The Case of Startup Credit Scoring

### Phần Định Hướng Mở Đầu

#### Anh Hưng - Chia sẻ định hướng đầu buổi

Phần mở đầu của anh Hưng đặt ra bức tranh tổng quan về thị trường việc làm trong giai đoạn AI đang thay đổi mạnh mẽ cách thức phát triển phần mềm. Điểm nhấn đáng chú ý là mặc dù AI giúp tăng tốc độ phát triển, nhu cầu về kỹ sư phần mềm không hề giảm đi mà còn được kỳ vọng tăng theo số lượng sản phẩm công nghệ.

Qua phần chia sẻ, anh Hưng nhấn mạnh rằng sinh viên và intern không thể chỉ dựa vào nền tảng kỹ thuật và kiến thức đại học. Các yếu tố cần bổ sung gồm: hiểu biết về business domain thực tế, khả năng xây dựng sản phẩm chạy được thay vì chỉ dừng ở mức demo, cùng với kỹ năng mềm, tiếng Anh và khả năng tự xây dựng personal branding. Bài học cốt lõi là tinh thần chủ động học hỏi liên tục và chấp nhận thích ứng nhanh với yêu cầu mới của thị trường.

### Nội Dung Nổi Bật

#### Context Is Everything - Making AI Actually Work for You (Tịnh Trương)

Phần chia sẻ của anh Tịnh xoay quanh vai trò quyết định của Context (ngữ cảnh) khi vận hành AI trong thực tế. Mặc dù các mô hình AI có lượng tri thức lớn, output trả về chỉ đáp ứng đúng nhu cầu khi được cung cấp đầy đủ ngữ cảnh cụ thể về mục tiêu, đối tượng, dự án và quy trình làm việc.

Anh Tịnh cảnh báo về một số thói quen phổ biến gây giảm chất lượng output: gom quá nhiều chủ đề khác nhau vào cùng một phiên chat làm AI liên tục thay đổi context, hoặc hiện tượng "internet puller" - copy mọi rule/plugin hay vào project mà không đánh giá tính phù hợp. Ngoài ra, anh cũng giới thiệu các khái niệm mở rộng như AI mindset, AI adoption và tư duy xây dựng second brain để tổ chức tri thức cá nhân khi làm việc với AI.

#### 36 giờ với LotusHacks - Hành trình UTMorpho (Team VIB)

Nhóm UTMorpho từ Team VIB chia sẻ lại hành trình tham gia cuộc thi hackathon LotusHacks 2026, trong đó sản phẩm được hình thành chỉ trong 36 giờ. Ý tưởng UTMorpho xuất phát từ một bài toán thực tế khi làm việc với AI để generate UI: người dùng muốn chỉnh sửa trực tiếp trên giao diện thay vì phải sửa prompt nhiều lần.

Về kiến trúc, dự án sử dụng hệ thống các agent phối hợp để xử lý ảnh đầu vào, phân tích layout, sinh JSON/layer, tự động tạo HTML/CSS và hỗ trợ chỉnh sửa UI trực quan. Các tính năng chính bao gồm upload template, generate UI, xem source code, chỉnh sửa component, lưu lịch sử và xuất public link. Đội cũng chia sẻ thẳng thắn về các thách thức gặp phải như cạn token, AI over-generation, áp lực deadline và việc chuẩn bị demo trong trạng thái mệt mỏi.

#### From Edge To Origin - CloudFront như một nền tảng (Thịnh Nguyen)

Anh Thịnh mở rộng góc nhìn về Amazon CloudFront vượt khỏi định nghĩa CDN thông thường. Theo đó, CloudFront thực sự đóng vai trò là lớp nền tảng cho cả performance, security và reliability của web application.

Các điểm chính trong phần chia sẻ gồm: cơ chế pricing mới với các gói Free/Pro/Business/Premium cùng cách kiểm soát bill spike; tối ưu request flow từ edge đến origin thông qua AWS backbone và edge locations để giảm latency; tích hợp sâu với AWS WAF và Shield giúp giảm tải cho origin trước các cuộc tấn công DDoS. Bài học cho intern là cần nhìn CloudFront như một nền tảng cốt lõi chứ không chỉ là CDN đơn thuần.

#### Friendly AI Assistant với Amazon Quick (Anh Pham)

Phần chia sẻ tập trung giới thiệu Amazon Quick - AI assistant hướng đến người dùng cuối với khả năng tích hợp sâu vào workflow hàng ngày. Công cụ này giúp giảm đáng kể thời gian xử lý các tác vụ lặp lại như tổng hợp dữ liệu, phân tích file, tạo dashboard, tóm tắt meeting và đề xuất next steps.

Điểm đáng chú ý là Amazon Quick có khả năng tích hợp linh hoạt với hệ sinh thái bên thứ ba (Microsoft, Google, email, calendar, công cụ cộng tác). Anh Pham cũng làm rõ khái niệm Agent là sự kết hợp giữa LLM và các action/function để thực thi hành động thực tế. Bài học cho intern là khi thiết kế AI assistant, cần ưu tiên workflow thực tế và trải nghiệm người dùng thay vì chỉ tập trung vào kỹ thuật.

#### Non-Determinism của LLM Settings (Đức Dao)

Phần chia sẻ của anh Đức giải mã một quan niệm thường gặp: cho rằng việc đặt `temperature = 0` đảm bảo LLM cho ra kết quả hoàn toàn giống nhau giữa các lần chạy. Thực tế, LLM là probabilistic engine, sinh token dựa trên xác suất và chịu ảnh hưởng bởi nhiều yếu tố kỹ thuật như floating point rounding, GPU parallelism và các cơ chế inference optimization từ hosting provider.

Anh Đức cũng thực hiện live demo cho thấy sự khác biệt giữa model qua API của provider và model tự host ở local. Các chiến lược giảm thiểu rủi ro bao gồm: chạy prompt nhiều lần chọn câu trả lời chung, self-host model khi cần kiểm soát cao, sử dụng JSON mode/structured output, thiết kế downstream service đủ robust và test nhiều trường hợp.

#### Multi-Agent System cấp doanh nghiệp - Credit Scoring (Vy Lam)

Chị Vy trình bày case study xây dựng hệ thống multi-agent cho bài toán đánh giá tín dụng startup. Đặc thù của bài toán là startup thường thiếu báo cáo tài chính dài hạn, credit history hay tài sản thế chấp, nhưng lại có dữ liệu giá trị khác (traction, team, market, intellectual property).

Kiến trúc multi-agent trong case study này gồm các vai trò chuyên biệt: credit committee/orchestrator, financial analyst, market researcher, team evaluator, risk assessor và report generator. Chị Vy cũng nhấn mạnh rằng "Enterprise-grade" không chỉ là code chạy được, mà còn đòi hỏi security, compliance, guardrails, chống prompt injection, audit trail, human review cùng yêu cầu cao về reliability và scalability.

### Những Gì Học Được

- **Thị trường việc làm trong kỷ nguyên AI:** Sinh viên/intern cần chuẩn bị cả nền tảng kỹ thuật lẫn kỹ năng mềm, đặc biệt là khả năng xây dựng sản phẩm thực tế.
- **Context là cốt lõi:** Chất lượng output AI phụ thuộc phần lớn vào chất lượng ngữ cảnh được cung cấp.
- **Kinh nghiệm Hackathon:** Rèn luyện tinh thần teamwork, tốc độ triển khai, tư duy sản phẩm và khả năng chọn lọc core feature.
- **CloudFront là nền tảng:** Không chỉ là CDN, CloudFront đóng vai trò then chốt trong cost control, security và reliability.
- **AI assistant và workflow:** Tích hợp AI vào quy trình làm việc giúp tăng đáng kể hiệu suất cá nhân và đội ngũ.
- **LLM không hoàn toàn deterministic:** Cần logging, testing, monitoring và thiết kế hệ thống chịu được output variation.
- **Multi-Agent System:** Phù hợp cho bài toán enterprise phức tạp, nhưng đòi hỏi guardrails, security và gắn liền với business value.

### Ứng Dụng Vào Quá Trình Internship

- Chủ động xây dựng sản phẩm thực tế thay vì chỉ dừng ở demo, tránh tư duy trì hoãn trong học tập.
- Áp dụng cách cung cấp context rõ ràng, có chọn lọc khi sử dụng AI để học AWS, viết báo cáo và debug.
- Học cách chia nhỏ task, tập trung vào core feature và phân chia công việc theo thế mạnh từng thành viên khi làm project nhóm.
- Liên hệ vai trò của CloudFront với các kiến trúc web/cloud đang triển khai trong project thực tập.
- Ứng dụng tư duy AI assistant để tự động hóa các tác vụ lặp lại trong workflow cá nhân và nhóm.
- Khi dùng LLM, luôn kiểm tra, so sánh output giữa các lần chạy và ghi nhận log để đánh giá chất lượng.
- Khi nghiên cứu multi-agent, quan tâm đến workflow, kiểm soát rủi ro, security, compliance và khả năng áp dụng thực tế.

### Trải nghiệm trong event

Tham gia AWS Vietnam Community Day là một trải nghiệm giúp tôi nhìn nhận sâu sắc hơn về cả hệ sinh thái AWS lẫn các xu hướng AI đang định hình lại ngành. Sự đa dạng của các topic - từ context engineering, hackathon thực chiến, CloudFront, AI assistant, LLM non-determinism đến multi-agent system - đã tạo ra một bức tranh toàn diện về những thách thức và cơ hội trong giai đoạn hiện nay.

Phần chia sẻ đầu buổi của anh Hưng đặc biệt có giá trị, giúp tôi ý thức rõ hơn về yêu cầu thực tế của thị trường: không chỉ cần kỹ năng kỹ thuật mà còn phải thấu hiểu domain, xây dựng được sản phẩm chạy được và phát triển tư duy sử dụng AI có trách nhiệm.

Tôi cũng ấn tượng với phần trình bày của chị Vy - dù tuổi đời còn trẻ nhưng đã đảm nhận vai trò Senior Business Systems Analyst và thiết kế các hệ thống enterprise phức tạp. Đây là minh chứng rõ ràng cho thấy với định hướng đúng đắn và năng lực vững vàng, người trẻ hoàn toàn có thể phát triển nhanh trong ngành công nghệ. Qua event, tôi nhận ra bản thân cần học thêm không chỉ về AWS service mà còn về tư duy sản phẩm, business value, security/reliability và đặc biệt là cách sử dụng AI có trách nhiệm.

### Một số hình ảnh khi tham gia sự kiện

![Poster AWS Community Day](/reportaws/images/4-EventParticipated/4.3-Event3/poster.png)

![Anh Hưng chia sẻ định hướng đầu buổi](/reportaws/images/4-EventParticipated/4.3-Event3/hung-opening.png)

![Anh Tịnh chia sẻ về Context Engineering](/reportaws/images/4-EventParticipated/4.3-Event3/tinh-session.png)

![Team VIB chia sẻ hành trình UTMorpho](/reportaws/images/4-EventParticipated/4.3-Event3/teamVIB-session.png)

![Anh Thịnh chia sẻ về CloudFront](/reportaws/images/4-EventParticipated/4.3-Event3/thinh-session.png)

![Anh Pham giới thiệu Amazon Quick](/reportaws/images/4-EventParticipated/4.3-Event3/haianh-session.png)

![Anh Đức giải thích LLM Non-Determinism](/reportaws/images/4-EventParticipated/4.3-Event3/duc-session.png)

![Chị Vy chia sẻ về Multi-Agent System](/reportaws/images/4-EventParticipated/4.3-Event3/vy-session.png)

![Ảnh tập thể tại AWS Vietnam Community Day](/reportaws/images/4-EventParticipated/4.3-Event3/group_photo.png)