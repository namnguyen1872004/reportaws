---
title: "Week 2 Worklog"
date: 2026-05-11
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Week 2 Objectives:
* Understand and build a basic AWS networking foundation with Amazon VPC, Subnets, Route Tables, Internet Gateways, and NAT Gateways.
* Configure network security layers (Security Groups, Network ACLs) and launch an EC2 Instance to test connectivity.

### Tasks to Implement This Week:
| Day | Task | Start Date | End Date | Documentation / Tools |
| --- | --- | --- | --- | --- |
| Mon | - Learn the concept of Amazon VPC, CIDR addresses, and the role of virtual private networks in AWS architecture.<br> - Analyze the differences between public subnets, private subnets, and VPN connection models. | 11/05/2026 | 11/05/2026 | Amazon VPC Docs |
| Tue | - Create a practice VPC and divide subnets according to application tiers.<br> - Check address ranges, Availability Zones, and configure automatic public IPv4 assignment for appropriate subnets. | 12/05/2026 | 12/05/2026 | AWS Management Console |
| Wed | - Create a Route Table and Internet Gateway; configure routing for public subnets.<br> - Verify Internet access flows and the relationship between subnets, route tables, and gateways. | 13/05/2026 | 13/05/2026 | Amazon VPC Route Tables |
| Thu | - Create a NAT Gateway for private subnets; explore Security Groups and Network ACLs.<br> - Set up inbound/outbound rules following the principle of least privilege. | 14/05/2026 | 14/05/2026 | AWS Security Groups & NACLs |
| Fri | - Create a Key Pair and launch an EC2 Instance within the configured VPC.<br> - Perform connectivity testing between network components, log errors, and finalize the practice network diagram. | 15/05/2026 | 15/05/2026 | Amazon EC2 Docs |

### Week 2 Achieved Results:
* Understood the roles of Amazon VPC, CIDR, public subnets, private subnets, and VPN connection models.
* Practiced configuring Subnets, Route Tables, Internet Gateways, NAT Gateways, Security Groups, and Network ACLs.
* Created Key Pairs, launched EC2 Instances, and tested connectivity between network components.

### Week 2 Evaluation:
* **Completion Level:** Good. Built a basic AWS networking foundation and verified connection flows.
* **Strengths:** Understood the relationships between subnets, route tables, gateways, and access control layers.
* **Areas for Improvement:** Need to practice more on CIDR subnetting problems and troubleshooting routing or Security Group errors.