---
title: "Week 9 Worklog"
date: 2026-06-29
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

### Week 9 Objectives:

- Design the overall system architecture for the NightFury Express Delivery Management System.
- Identify the main application, data, storage, integration, security, and monitoring components.
- Map system components to appropriate AWS services and develop the initial Architecture Diagram.

### Tasks to Implement This Week:

| Day | Task                                                                                                                                                                                                                                                                                                               | Start Date | End Date   | Documentation / Tools                      |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ---------- | ------------------------------------------ |
| Mon | - Review the business requirements and core delivery workflows defined in Week 8.<br>- Establish architectural design criteria based on security, scalability, maintainability, availability, and Workshop cost constraints.                                                                                       | 29/06/2026 | 29/06/2026 | AWS Architecture Best Practices            |
| Tue | - Identify the main system components: ASP.NET Core web application, MySQL database, media storage, address service, order event processing, email notification, load balancing, and monitoring.<br>- Describe the responsibilities and communication between components.                                          | 30/06/2026 | 30/06/2026 | System Architecture Document               |
| Wed | - Map the system components to AWS services, including Amazon EC2, Application Load Balancer, Amazon RDS for MySQL, AWS Secrets Manager, Amazon S3, Amazon SQS, AWS Lambda, Amazon SES, Amazon Location, AWS IAM, and Amazon CloudWatch.<br>- Build the initial Architecture Diagram using AWS Architecture Icons. | 01/07/2026 | 01/07/2026 | AWS Architecture Icons / Diagram Tools     |
| Thu | - Add request flows, data flows, IAM access paths, Security Groups, public/private subnets, and external service interactions to the diagram.<br>- Review the deployment feasibility and verify that the architecture follows the defined business workflows.                                                      | 02/07/2026 | 02/07/2026 | Security and Data Flow Specifications      |
| Fri | - Review the architecture against the NightFury Express delivery workflows, including order creation, driver assignment, delivery status updates, POD storage, and email notifications.<br>- Finalize the Architecture Diagram and update the design documentation based on mentor feedback.                       | 03/07/2026 | 03/07/2026 | Finalized Architecture and Design Document |

### Week 9 Achieved Results:

- Defined the overall NightFury Express architecture, including the web application, database, private media storage, address lookup, event processing, email notification, load balancing, and monitoring components.
- Mapped the main system components to appropriate AWS services.
- Completed the initial Architecture Diagram showing the request flow from the user through CloudFront, AWS WAF, Application Load Balancer, and Amazon EC2.
- Defined the data and integration flows between Amazon EC2, Amazon RDS for MySQL, Amazon S3, Amazon Location, Amazon SQS, AWS Lambda, and Amazon SES.
- Identified IAM Role, Security Group, subnet, and Secrets Manager requirements for secure communication between services.
- Updated the architecture and supporting documentation based on feedback from the mentor.

### Week 9 Evaluation:

- **Completion Level:** Good. The architecture clearly represented the main system components, AWS services, request flows, data flows, and security boundaries.
- **Strengths:** Successfully linked the NightFury Express business requirements and delivery workflows with suitable technical solutions and AWS services.
- **Areas for Improvement:** Continue reviewing the architecture based on actual implementation results, clearly distinguish deployed services from production-oriented components, and further evaluate cost, scalability, backup, and recovery requirements.
