---
title: "Week 5 Worklog"
date: 2026-06-01
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Week 5 Objectives:
* Deeply configure Amazon ElastiCache for Redis, multi-AZ Cache Subnet Groups, and experiment with Cluster Modes.
* Optimize content delivery with CloudFront Origin Groups, Failover mechanisms, cache policies, and practice edge programming with Lambda@Edge.

### Tasks to Implement This Week:
| Day | Task | Start Date | End Date | Documentation / Tools |
| --- | --- | --- | --- | --- |
| Mon | - Install and configure AWS CLI for ElastiCache practice labs.<br> - Understand Amazon ElastiCache for Redis architecture and core components. | 01/06/2026 | 01/06/2026 | AWS CLI & ElastiCache Docs |
| Tue | - Create Cache Subnet Groups across multiple Availability Zones.<br> - Verify Security Groups and connection flows from applications to Redis. | 02/06/2026 | 02/06/2026 | ElastiCache Redis Subnets |
| Wed | - Experiment with Cluster Mode Enabled/Disabled and analyze differences in sharding, scaling, and availability.<br> - Integrate AWS SDK to verify cache read/write operations. | 03/06/2026 | 03/06/2026 | AWS SDK & ElastiCache |
| Thu | - Configure CloudFront Origin Groups and Failover mechanisms.<br> - Customize cache policies, origin request policies, and response headers tailored to content types. | 04/06/2026 | 04/06/2026 | Amazon CloudFront Advanced |
| Fri | - Explore Lambda@Edge and execution stages: Viewer Request, Origin Request, Origin Response, Viewer Response.<br> - Write and test a simple handler function on HTTP workflows, documenting lab results. | 05/06/2026 | 05/06/2026 | AWS Lambda@Edge Docs |

### Week 5 Achieved Results:
* Configured Amazon ElastiCache for Redis, multi-AZ Cache Subnet Groups, and experimented with cluster modes.
* Integrated AWS SDK to verify cache read/write operations.
* Optimized Amazon CloudFront with Origin Groups, Failover, cache policies, response headers, and practiced Lambda@Edge.

### Week 5 Evaluation:
* **Completion Level:** Good. Completed advanced topics on caching and content distribution.
* **Strengths:** Understood failover mechanisms, caching policies, and Lambda@Edge intervention points.
* **Areas for Improvement:** Need to supplement cache performance measurement and practice error handling when deploying edge functions.