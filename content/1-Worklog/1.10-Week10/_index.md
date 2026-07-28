---
title: "Week 10 Worklog"
date: 2026-07-06
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

### Week 10 Objectives:

- Design the conceptual data model and logical database schema for the NightFury Express Delivery Management System.
- Identify the main entities, attributes, primary keys, foreign keys, relationships, and data constraints.
- Design wireframes and user interfaces for the main Customer, Driver, and Administrator workflows.
- Ensure consistency between the database design, Use Cases, business rules, user interfaces, and AWS architecture.

### Tasks to Implement This Week:

| Day | Task                                                                                                                                                                                                                                                                                                    | Start Date | End Date   | Documentation / Tools         |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- | ----------------------------- |
| Mon | - Identify the main business entities and attributes of NightFury Express.<br>- Define the initial conceptual data model for users, profiles, hubs, orders, order tracking events, driver locations, payments, ratings, POD, signatures, and failed-delivery evidence.                                  | 06/07/2026 | 06/07/2026 | Database Design Tools         |
| Tue | - Design relationships among users, orders, hubs, drivers, and order tracking events.<br>- Define primary keys, foreign keys, cardinalities, data types, and integrity constraints.                                                                                                                     | 07/07/2026 | 07/07/2026 | ERD Tools                     |
| Wed | - Finalize the logical database schema and review table normalization.<br>- Verify that the schema supports order creation, driver assignment, status transitions, delivery tracking, POD, signatures, failed-delivery evidence, and notifications.                                                     | 08/07/2026 | 08/07/2026 | Database Schema Specification |
| Thu | - Design wireframes for login, registration, Customer order creation, order tracking, Driver dashboard, and Administrator dashboard.<br>- Map the interaction workflows for Customers, Drivers, and Administrators.                                                                                     | 09/07/2026 | 09/07/2026 | Figma / Wireframing Tools     |
| Fri | - Design the main interfaces for order creation, driver assignment, delivery status updates, successful delivery, failed delivery, POD upload, and signature capture.<br>- Cross-check the UI designs against Use Case Diagrams, Business Rules, the database schema, and the AWS Architecture Diagram. | 10/07/2026 | 10/07/2026 | UI/UX Design Documents        |

### Week 10 Achieved Results:

- Identified the main entities, attributes, primary keys, foreign keys, and relationships required for NightFury Express.
- Completed the conceptual ERD and logical relational schema for users, profiles, hubs, orders, order tracking events, driver locations, payments, and ratings.
- Defined the relationship between orders and media objects stored on Amazon S3, where the database stores object keys and metadata instead of binary files.
- Verified that the database schema supports the core delivery lifecycle: pending → assigned → shipping → done or failed.
- Designed wireframes and interfaces for Customer order creation, order tracking, Administrator driver assignment, Driver delivery updates, POD upload, signature capture, and failed-delivery evidence.
- Reviewed consistency among the Use Cases, Business Rules, database schema, user interfaces, and AWS architecture.

### Week 10 Evaluation:

- **Completion Level:** Good. The database and interface designs were aligned with the main business requirements and delivery workflows of NightFury Express.
- **Strengths:** Established clear relationships among business processes, data entities, user roles, interface screens, and system functions.
- **Areas for Improvement:** Continue reviewing database indexes, validation constraints, transaction handling, exceptional cases, responsive interface behavior, and the consistency of S3 object keys with order data.
