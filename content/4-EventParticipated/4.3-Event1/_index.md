---
title: "Event 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 4.3. </b> "
---


# Workshop Report: AWS Vietnam Community Day

### Event Purpose

- Gain up-to-date perspectives from the AWS and FCAJ community on the technology landscape in the AI era.
- Understand the role of Context Engineering when running AI solutions at production scale.
- Explore how Amazon CloudFront can serve as a foundation layer for performance, security, and reliability.
- Learn from a real hackathon journey (UTMorpho at LotusHacks) - from idea to demo in 36 hours.
- Analyze the non-determinism of LLM settings and how to design Multi-Agent systems that meet enterprise requirements.

### Speakers

- **Tinh Truong** - Platform Engineer, GoTymeX (Context Engineering with AI)
- **Team VIB** (Thao Nguyen, Mai Nguyen, Uyen Le) - GenAI Engineers, VIB (LotusHacks with UTMorpho)
- **Thinh Nguyen** - DevOps Engineer, FCAJ (CloudFront Foundation)
- **Anh Pham** - Cloud Consultant, G-AsiaPacific Vietnam (Amazon Quick)
- **Duc Dao** - Solutions Architect, Cloud Kinetics (LLM Non-Determinism)
- **Vy Lam** - Senior Business Systems Analyst, VPBank (Multi-Agent System)
- **Anh Hung** - Mentor, opening the session

### Schedule

- **08:30 - 09:00:** Seating at the 36th floor
- **09:00 - 09:30:** Context Is Everything - Making AI Actually Work for You
- **09:30 - 10:00:** 36 hrs with LotusHacks - Building UTMorpho from Idea to Reality
- **10:00 - 10:40:** From Edge To Origin - CloudFront as Your Foundation
- **10:40 - 10:55:** Friendly AI Assistant with Amazon Quick
- **10:55 - 11:00:** Break
- **11:00 - 11:30:** Non-Determinism of "Deterministic" LLM Settings
- **11:30 - 12:00:** Enterprise-Grade Multi-Agent System - The Case of Startup Credit Scoring

### Opening Session

#### Career Direction in the AI Era (Anh Hung)

The opening session painted an overall picture of the job market as AI reshapes software development. A key takeaway was that AI does not eliminate demand for software engineers - it actually pushes the volume of technology products higher, which in turn creates more engineering opportunities.

Anh Hung stressed that students and interns cannot rely solely on technical foundations and university knowledge. They also need business domain understanding, the ability to ship real products (not just demos), soft skills, English proficiency, and personal branding. The core lesson: stay proactive, keep learning continuously, and adapt quickly to evolving market requirements.

### Key Highlights

#### Context Is Everything (Tinh Truong)

The session highlighted Context as the deciding factor when running AI in production. While large language models carry massive knowledge, output quality drops sharply when the model lacks context about the goal, audience, project, or working process.

A few common anti-patterns were discussed: stuffing many unrelated topics into a single chat session dilutes the context window, and the "internet puller" habit of grabbing every shiny tool/plugin without evaluating fit. The talk also touched on broader ideas like AI mindset, AI adoption, and building a second brain to organize personal knowledge when working with AI.

#### Building UTMorpho in 36 Hours (Team VIB)

The UTMorpho team walked through their LotusHacks 2026 journey, where the product came together in just 36 hours. The motivation was practical: when using AI to generate UI, developers usually want to edit the interface directly rather than going back and forth tweaking prompts.

Architecturally, the project uses a coordinated agent system to handle image input, analyze layout, generate JSON/layer, auto-produce HTML/CSS, and support visual UI editing. Core features include template upload, UI generation, source code view, component editing, edit history, and public share link. The team was candid about challenges: token exhaustion, AI over-generation, deadline pressure, and prepping demo/video while exhausted.

#### CloudFront as a Foundation (Thinh Nguyen)

Anh Thinh reframed Amazon CloudFront beyond the usual CDN definition - it is a foundation layer for performance, security, and reliability of web applications.

Highlights covered the new CloudFront pricing model (Free/Pro/Business/Premium) with bill-spike control strategies, edge-to-origin request flow optimization using the AWS backbone and edge locations, and deep integration with AWS WAF and Shield to absorb DDoS and volumetric attacks before they reach the origin. The lesson for interns: treat CloudFront as a core platform rather than just a CDN.

#### Amazon Quick - Friendly AI Assistant (Anh Pham)

The session introduced Amazon Quick as an end-user-oriented AI assistant that integrates into daily workflows. It reduces time spent on repetitive tasks like data aggregation, file analysis, dashboard creation, meeting summaries, and next-step recommendations.

A notable point is the flexible integration with third-party ecosystems (Microsoft, Google, email, calendar, team collaboration tools). Anh Pham also clarified that an Agent is essentially an LLM combined with actions/functions that can perform real tasks. The lesson: when designing an AI assistant, prioritize actual workflows and user experience over technical sophistication.

#### Non-Determinism of LLM Settings (Duc Dao)

This talk unpacked a common misconception: setting `temperature = 0` does not guarantee identical LLM outputs across runs. LLMs are probabilistic engines - they generate tokens based on probability distributions and are influenced by technical factors like floating point rounding, GPU parallelism, and inference optimization on the hosting provider side.

Anh Duc did a live demo showing the difference between model output via provider API and locally self-hosted model. Mitigation strategies include: running prompts multiple times and picking common answers, self-hosting when high control is needed, using JSON mode/structured output, designing downstream services to handle malformed outputs, and testing many cases.

#### Enterprise-Grade Multi-Agent System (Vy Lam)

Ch Vy presented a case study on building a multi-agent system for startup credit scoring. The challenge: startups often lack long-term financial reports, credit history, or collateral - but they have other valuable signals (traction, team, market, intellectual property).

The architecture uses specialized roles: credit committee/orchestrator, financial analyst, market researcher, team evaluator, risk assessor, and report generator. She emphasized that "enterprise-grade" goes far beyond working code - it requires security, compliance, guardrails, prompt injection protection, output filtering, API key rotation, audit trail, human review, and high standards for reliability and scalability.

### Key Learnings

- **Job market in the AI era:** Students/interns need both technical foundations and soft skills, especially the ability to ship real products.
- **Context is foundational:** Output quality depends heavily on the quality of context provided to the model.
- **Hackathon experience:** Builds teamwork, shipping speed, product thinking, and the ability to focus on core features.
- **CloudFront as a foundation:** More than a CDN - it plays a central role in cost control, security, and reliability.
- **AI assistant in workflow:** Integrating AI into daily workflows significantly boosts individual and team productivity.
- **LLM non-determinism:** Always need logging, testing, monitoring, and systems that can tolerate output variation.
- **Multi-Agent systems:** Suitable for complex enterprise problems, but require guardrails, security, and a clear link to business value.

### Application to Internship

- Be more proactive in learning; ship real products instead of stopping at demos.
- Apply clear, focused context when using AI for AWS learning, report writing, or debugging.
- When working on team projects, decompose tasks, focus on core features, and allocate work based on each member's strengths.
- Relate CloudFront's role to the web/cloud architectures being built in the internship project.
- Use AI-assistant thinking to automate repetitive tasks in personal and team workflows.
- When using LLMs, always verify, compare outputs across runs, and log for quality evaluation.
- When exploring multi-agent systems, pay attention to workflow, risk control, security, compliance, and practical applicability.

### Personal Experience

Attending AWS Vietnam Community Day gave me a deeper view of both the AWS ecosystem and the AI trends reshaping the industry. The diversity of topics - from context engineering and hackathon lessons to CloudFront, AI assistants, LLM non-determinism, and multi-agent systems - created a comprehensive picture of the challenges and opportunities in this era.

The opening session from Anh Hung was particularly valuable, helping me become more aware of real market demands: not just technical skills, but also domain understanding, the ability to ship working products, and responsible AI usage.

I was also impressed by Ch Vy - young but already serving as Senior Business Systems Analyst, designing complex enterprise systems. It is clear evidence that with the right direction and strong capability, young people can grow fast in tech. The event reinforced that I need to keep learning beyond AWS services: product thinking, business value, security/reliability standards, and responsible AI usage.

### Event Photos

![AWS Community Day Poster](/reportaws/images/4-EventParticipated/4.3-Event3/poster.png)

![Anh Hung opening the session](/reportaws/images/4-EventParticipated/4.3-Event3/hung-opening.png)

![Anh Tinh sharing about Context Engineering](/reportaws/images/4-EventParticipated/4.3-Event3/tinh-session.png)

![Team VIB sharing the UTMorpho journey](/reportaws/images/4-EventParticipated/4.3-Event3/teamVIB-session.png)

![Anh Thinh presenting CloudFront](/reportaws/images/4-EventParticipated/4.3-Event3/thinh-session.png)

![Anh Pham introducing Amazon Quick](/reportaws/images/4-EventParticipated/4.3-Event3/haianh-session.png)

![Anh Duc explaining LLM Non-Determinism](/reportaws/images/4-EventParticipated/4.3-Event3/duc-session.png)

![Ch Vy presenting the Multi-Agent System](/reportaws/images/4-EventParticipated/4.3-Event3/vy-session.png)

![Group photo at AWS Vietnam Community Day](/reportaws/images/4-EventParticipated/4.3-Event3/group_photo.png)