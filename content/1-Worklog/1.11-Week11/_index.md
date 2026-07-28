---
title: "Week 11 Worklog"
date: 2026-07-13
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

### Week 11 Objectives:

- Complete the main features and user interfaces of the NightFury Express Delivery Management System.
- Integrate the application with the required AWS services for data storage, media storage, address lookup, order events, and email notifications.
- Develop test plans and execute Black-box and White-box testing for the six priority business workflows.
- Record defects, analyze their causes, and prepare the application for AWS deployment.

### Tasks to Implement This Week:

| Day | Task                                                                                                                                                                                                                                                                           | Start Date | End Date   | Documentation / Tools                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ---------- | -------------------------------------------- |
| Mon | - Complete the main interfaces for Customers, Drivers, and Administrators.<br>- Review navigation, role-based access, data presentation, and consistency among the main screens.                                                                                               | 13/07/2026 | 13/07/2026 | ASP.NET Core / Frontend Tools                |
| Tue | - Finalize order creation, driver assignment, delivery status updates, POD upload, signature capture, failed-delivery evidence, search functions, and user notifications.<br>- Review input validation and responsive display on different screen sizes.                       | 14/07/2026 | 14/07/2026 | UI/UX Testing Tools                          |
| Wed | - Develop the Black-box test plan and representative Test Cases for order creation, authorization, driver assignment, status updates, POD upload, and error handling.<br>- Define preconditions, test steps, input data, expected results, actual results, and evidence codes. | 15/07/2026 | 15/07/2026 | Playwright / Test Plan / Test Cases          |
| Thu | - Perform White-box testing on critical business logic using unit and integration tests.<br>- Verify authorization conditions, status transition rules, exception handling, transactions, data integrity, and file validation.                                                 | 16/07/2026 | 16/07/2026 | xUnit / Moq / SQLite In-Memory               |
| Fri | - Execute the test suites, record passed and failed Test Cases, analyze software defects, and update the relevant code or test scripts.<br>- Summarize testing results and prepare the application package for deployment on Amazon EC2.                                       | 17/07/2026 | 17/07/2026 | Bug Tracking / Test Report / Release Package |

### Week 11 Achieved Results:

- Completed the main interfaces and business functions for Customers, Drivers, and Administrators.
- Finalized the workflows for order creation, driver assignment, delivery status updates, successful delivery, failed delivery, POD upload, signature capture, and delivery evidence management.
- Integrated the application with Amazon RDS for MySQL, AWS Secrets Manager, Amazon S3, Amazon SQS, AWS Lambda, Amazon SES, and Amazon Location.
- Created and executed Black-box Test Cases for the six priority workflows: order creation, authorization, driver assignment, status updates, POD upload, and error handling.
- Performed White-box testing on critical business logic, including authorization rules, status transitions, file validation, transactions, and exception handling.
- Recorded the failed Black-box Test Cases, analyzed their causes, and distinguished application defects from issues related to test selectors, expected navigation behavior, and external service configuration.
- Prepared the application and test documentation for the AWS deployment phase.

### Week 11 Evaluation:

- **Completion Level:** Good. The main business functions, interfaces, AWS integrations, and planned testing activities were completed sufficiently to support deployment.
- **Strengths:** Effectively combined Black-box and White-box testing to evaluate the system at both user-interaction and internal business-logic levels.
- **Areas for Improvement:** Continue correcting the remaining failed Black-box Test Cases, increase automated test coverage, verify Amazon Location integration, and add performance, security, and production database testing.
