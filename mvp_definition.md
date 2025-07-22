## AlchemyOS MVP Definition

### Goal

The goal of the MVP is to validate the core functionality of AlchemyOS with a limited set of features. This will allow for early feedback from users and help to guide the future development of the product.

### Core Features

The MVP will include the following core features:

- **Left-Brain:**
  - Input connector for Slack.
  - AI generator for micro-articles.
- **Middle-Brain:**
  - Dynamic tagging of artifacts with "topic" and "vibe".
  - Workflow engine to manage artifact status (draft, in_review, approved).
  - Basic dashboard to view and approve artifacts.
- **Right-Brain:**
  - Distribution to a single Slack channel.

### User Roles

The MVP will support two user roles:

- **Admin:** Can do everything.
- **Approver:** Can approve or veto artifacts.

### Technology Stack

The MVP will be built using the following technology stack:

- **Backend:** Python FastAPI
- **Frontend:** React + Next.js + Tailwind CSS
- **Database:** Postgres + pgvector
- **AI Engine:** OpenAI
- **Orchestration:** LangChain, Temporal
- **Hosting:** Vercel for UI, AWS for backend

### Success Metrics

The success of the MVP will be measured by the following metrics:

- Number of knowledge artifacts created.
- Number of knowledge artifacts approved.
- Number of knowledge artifacts distributed.
- User feedback.
