# Muhammad Ahmad — AI Agent Engineer & Digital Supply Chain Architect

[![Live Portfolio](https://img.shields.io/badge/Portfolio-Live--DigiSuite-007ACC?style=for-the-badge&logo=googlechrome&logoColor=white)](https://emadaed.github.io/digisuite/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/muhammad-ahmad-scm)
[![GitHub](https://img.shields.io/badge/GitHub-emadaed-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/emadaed)
[![Certifications](https://img.shields.io/badge/Certifications-PMP%C2%AE%20%7C%20RMP%C2%AE-2E7D32?style=for-the-badge)](https://emadaed.github.io/digisuite/#expertise)

---

## 🌐 Live Systems Hub & Engineering Documentation

Welcome to my digital systems hub. I bring **15+ years of hands-on operations leadership** in telecom and supply chain management, paired with modern **Agentic AI Engineering** (LangGraph, RAG, WebSockets, deterministic safety guardrails).

Below are the direct engineering deep-dives, architecture logs, and production-grade case studies available in the **[DigiSuite Portfolio Hub](https://emadaed.github.io/digisuite/)**:

### 🔎 Verification Log — Times the Machine Was Wrong and I Caught It

* 🧾 **[Verification Log](https://emadaed.github.io/digisuite/verification-log.html)**  
  *Five entries across four systems: a live LLM summary that passed my checker while containing an unverified ranking claim, a forecast model that beat a naive baseline on pair count and lost 3× on volume-weighted WAPE, a validator that scored 14.8% precision on a hard test set before the fix, an n8n retry setting that did not rescue a lost lead, and a prose payload typed as a number. What was wrong, how I noticed, and what I changed.*

### 📘 Engineering Logs & Architecture Deep-Dives

* 📗 **[Engineering Log 01: Guardrails & Hallucination Prevention](https://emadaed.github.io/digisuite/engineering-log.html)**  
  *Building a deterministic safety layer around an LLM agent with live SQL tool-calling and strict citation verification.*
* 📙 **[Engineering Log 02: Multilingual Semantic Search & Shamela Integration](https://emadaed.github.io/digisuite/engineering-log-2.html)**  
  *Scaling Ahmad-AI to 113,842 indexed Islamic records using two-stage retrieval (`MiniLM-L12` + `GATE-Reranker-V1`).*
* 🎙️ **[Engineering Log 03: Real-Time Voice AI Agent System](https://emadaed.github.io/digisuite/engineering-log-3.html)**  
  *Full-duplex continuous voice assistant built on WebSockets, Deepgram Nova-3, GPT-4o-mini, and Aura-2 TTS.*
* 📈 **[Engineering Log 04: Production Demand Forecasting Engine](https://emadaed.github.io/digisuite/engineering-log-4.html)**  
  *Multi-model wholesale ERP demand forecasting (Naive, Seasonal Naive, ETS) evaluated across 84,741 real order lines.*
* 📖 **[Engineering Log 05: Building a Quran Retrieval Benchmark From Scratch](https://emadaed.github.io/digisuite/engineering-log-5.html)**  
  *68 hand-labeled questions, three rejected datasets, and the counter-intuitive finding that translating the corpus beats translating the query for cross-lingual retrieval.*
* 🧪 **[Engineering Log 06: Scaling Ahmad-Eval to 196 Hand-Reviewed Questions](https://emadaed.github.io/digisuite/engineering-log-6.html)**  
  *Growing the benchmark 3x, hand-verifying every gold verse against the Quranic text, fixing a qid collision bug, and re-evaluating the retriever on the cleaned gold.*
* 🔍 **[Engineering Log 07: The Reranker Was Hurting, and the Metric Was Wrong](https://emadaed.github.io/digisuite/engineering-log-7.html)**  
  *A corpus-wide indexing bug found by a diagnostic built for another purpose, a 12-point reranker regression hidden behind an auto-selector, and a 40-minute failure read showing the 19% metric was measuring gold-set specificity, not retriever quality.*
* 🚪 **[Engineering Log 08: The LLM Selector Failed; the Gate Ships](https://emadaed.github.io/digisuite/engineering-log-8.html)**  
  *Four local models tested as Quranic abstainers. Zero correct abstentions across 24 draws. A two-layer scope-routing gate replaced the failed hypothesis and shipped at the pre-registered threshold: 8/10 out-of-scope catches, 0/4 answerable false positives.*
* 📕 **[Engineering Log 09: The Pipeline Does Not Generalize — and That's the Finding](https://emadaed.github.io/digisuite/engineering-log-9.html)**  
  *196 calibration questions pass. 36 fresh questions fail the pre-registered thresholds on both conditions. The 232-question benchmark is published on Hugging Face with both the passing and the failing numbers, and the four-tier promise from Chapter 03 is checked against what was actually built.*
* 🧾 **[Engineering Log 10: The Lead I Lost — Building an Intake Pipeline and Finding Where It Breaks](https://emadaed.github.io/digisuite/engineering-log-10.html)**  
  *Failing tests, a join that could silently inflate spend, a lead lost when the API was down, a retry setting that did not rescue it, a reporting copy because Metabase would not read SQLite, and an assistant that quotes instead of writing.*
* 🧾 **[Engineering Log: Healthcare Data Quality Engine](https://emadaed.github.io/digisuite/engineering-log-healthcare-dq.html)**  
  *A phase-by-phase build log: a validator that scored 14.8% precision on a deliberately messy test set, the 925 false alarms behind it, and the cleaning layer and rule that fixed it. Same 12 rules verified across Python, SQLite and Azure SQL. Synthetic data.*

### 📊 Case Studies

* 📊 **[Case Study: Wholesale ERP Demand Forecasting Validation](https://emadaed.github.io/digisuite/case-study-forecasting.html)**  
  *12-month backtested evaluation, WAPE analysis, lumpy order detection, and automated Excel worklist generation.*
* 🛡️ **[Case Study: Healthcare Revenue Cycle Data Quality Engine](https://emadaed.github.io/digisuite/case-study-healthcare-dq.html)**  
  *Twelve documented validation rules, a ground-truth answer key, a four-page Power BI scorecard with row-level security, and an honest account of what the results do and do not prove. Source: [GitHub repo](https://github.com/emadaed/healthcare-data-ops).*
* 🧾 **[Case Study: Intake-to-Booking Attribution Pipeline](https://emadaed.github.io/digisuite/case-study-intake-booking.html)**  
  *A synthetic-data pipeline from ad spend to occurred appointments: an n8n intake workflow, a strict Flask API with a field allowlist, a Postgres reporting copy, a four-chart Metabase dashboard, four engineering specs and 71 automated tests. The problem is real; the data is not, and every page says so.*

---

## 👨‍💻 Operations Built, Then Coded

I build and optimize operational ecosystems that work — combining 15+ years of senior operations leadership with production-grade software development.

### Core Leadership Highlights:
* **Ericsson BSA (Saudi Arabia):** Founding operational lead for one of the largest telecom managed services contracts in KSA (STC). Built vendor ecosystems from scratch, engineered SLA/WLA governance frameworks saving **SAR 100,000+/month**, and led zero-disruption warehouse migrations.
* **Blue Light LLC (Pakistan):** Restructured manual supply chain operations, cut FedEx logistics delivery cycle time by **50%**, reduced shipment costs by **20%**, and managed a $10M+ logistics portfolio.

---

## 🚀 Featured Software & AI Systems

| System | Description | Primary Tech Stack | Links |
| :--- | :--- | :--- | :--- |
| **GrowEasy ERP** | Full-stack SaaS ERP for SMEs (Inventory, Invoicing, Finance) with live SCM agent data layer. | Python, Flask, Postgres, Redis, Docker | [GrowEasy Site](https://groweasycloud.github.io/groweasy-site) |
| **Demand Forecasting Engine** | Multi-model B2B demand forecasting engine analyzing 84,741 order lines & 4,307 SKUs. | Python, Pandas, Statsmodels, Streamlit | [Read Log 04](https://emadaed.github.io/digisuite/engineering-log-4.html) \| [Case Study](https://emadaed.github.io/digisuite/case-study-forecasting.html) |
| **Healthcare Data Quality Engine** | 12-rule validation engine for synthetic healthcare claims. The same rules run in Python, SQLite and Azure SQL and flag identical records; a four-page Power BI report adds a data quality scorecard and row-level security. Synthetic data, measured against its own generator. | Python, pandas, SQL / T-SQL, Azure SQL, Power BI, DAX, pytest | [Case Study](https://emadaed.github.io/digisuite/case-study-healthcare-dq.html) \| [Engineering Log](https://emadaed.github.io/digisuite/engineering-log-healthcare-dq.html) \| [GitHub](https://github.com/emadaed/healthcare-data-ops) |
| **Intake-to-Booking Pipeline** | End-to-end synthetic-data pipeline from ad spend to occurred appointments: n8n intake, strict Flask API, Postgres reporting copy, four-chart Metabase dashboard, 71 automated tests. The problem is real; the data is simulated and labelled. | Python, Flask, SQL (SQLite, PostgreSQL), n8n, Docker, Metabase, pytest | [Case Study](https://emadaed.github.io/digisuite/case-study-intake-booking.html) \| [Log 10](https://emadaed.github.io/digisuite/engineering-log-10.html) \| [GitHub](https://github.com/emadaed/intake-to-booking) |
| **Ahmad-AI (RAG Agent)** | Offline multi-turn research agent with hybrid cross-encoder reranking over 113k records; 232-question hand-reviewed Quran retrieval benchmark published on Hugging Face, with its documented failure to generalize; per-bucket routing; two-layer scope-routing gate (LLM intent classifier + keyword backstop) that catches 8/10 out-of-scope questions without showing a wrong verse. | LangGraph, ChromaDB, GATE-Reranker, Ollama, camel-tools, BGE-reranker-v2-m3, command-r7b-arabic | [Log 01](https://emadaed.github.io/digisuite/engineering-log.html) \| [Log 02](https://emadaed.github.io/digisuite/engineering-log-2.html) \| [Log 05](https://emadaed.github.io/digisuite/engineering-log-5.html) \| [Log 06](https://emadaed.github.io/digisuite/engineering-log-6.html) \| [Log 07](https://emadaed.github.io/digisuite/engineering-log-7.html) \| [Log 08](https://emadaed.github.io/digisuite/engineering-log-8.html) \| [Log 09](https://emadaed.github.io/digisuite/engineering-log-9.html) \| [Benchmark on Hugging Face](https://huggingface.co/datasets/ahmad1979/ahmad-eval-v1) |
| **Verification Log** | Five entries across four systems: a live LLM summary that passed its own checker while containing an unverified ranking claim; a forecast that beat naive on pair count and lost 3× on volume-weighted WAPE; a validator that scored 14.8% precision before the fix; an n8n retry setting that did not rescue a lost lead; a prose payload typed as a number. | — | [Verification Log](https://emadaed.github.io/digisuite/verification-log.html) |
| **Serverless WMS** | Enterprise fulfillment & order processing platform running inside Google Workspace. | Google Apps Script, Google Sheets | [Source Code](https://emadaed.github.io/digisuite/WH_AppScript.txt) \| [Live Demo](https://docs.google.com/spreadsheets/d/1fFstQ3d4r4HCv1KGCzoLjWhiuZZMQisxaD9OyMWfgXA/edit?usp=sharing) |
| **Learn With Misham** | Scalable CRM & Learning Management System actively used by education providers. | JavaScript, Google Apps Script, LocalStorage | [Live Platform](https://emadaed.github.io/LearnWithMisham/) |

---

## 🛠️ Technical Capabilities

* **AI Systems & Agents:** LangGraph, RAG (ChromaDB), Cross-Encoder Reranking (`GATE-Reranker-V1`), WebSockets, Speech-to-Text (Nova-3), Text-to-Speech (Aura-2), Deterministic Guardrails.
* **Backend & Systems:** Python, Flask, FastAPI, PostgreSQL, Redis, Celery, Docker, Google Apps Script, n8n.
* **Data & BI:** Power BI (DAX, row-level security), T-SQL, Azure SQL Database, SQLite, pandas, data validation and reconciliation, star-schema modelling, pytest, Metabase.
* **Supply Chain & Management:** Digital Transformation, Demand Forecasting (ETS/Naive), Warehouse Management (WMS), SLA/WLA Governance, PMP®, RMP®.

---

## 📬 Contact & Collaboration

Open to global roles and consulting in **Agentic AI Systems Engineering**, **Digital Supply Chain Architecture**, and **Operations Automation**.

* 📧 **Email:** [muhammad.a.ahmed@gmail.com](mailto:muhammad.a.ahmed@gmail.com)
* 💼 **LinkedIn:** [linkedin.com/in/muhammad-ahmad-scm](https://linkedin.com/in/muhammad-ahmad-scm)
* 💬 **WhatsApp:** [+92 309 5222202](https://wa.me/923095222202)
* 🌐 **Portfolio Hub:** [https://emadaed.github.io/digisuite/](https://emadaed.github.io/digisuite/)

---
*License: MIT — Feel free to explore, learn from, or build upon the open-source architecture components.*