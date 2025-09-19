# SQL-Agent Demo Suite

_A collection of agent demos evolving from simple conversational assistants to secure, analytics-oriented agents for BI and reporting._

---

## 🔍 Table of Contents

1. [Project Overview](#project-overview)  
2. [Scripts & Progression](#scripts-&-progression)  
3. [Key Features](#key-features)  
4. [Requirements](#requirements)  
5. [Usage](#usage)  
6. [Security / Safety Considerations](#security-/-safety-considerations)  
7. [How to Contribute or Extend](#how-to-contribute-or-extend)  

---

## Project Overview

This repository showcases the step-by-step development of AI agents using LangChain, focusing on:

- Understanding agent architectures  
- Highlighting risks of unsupervised autonomous actions  
- Introducing guardrails for database security  
- Building advanced analytics capabilities for business intelligence

---

## Scripts & Progression

| Script | Purpose | Highlights |
|---|---|---|
| `00_simple_conversational_agent.py` | Introductory conversational agent. No tools or SQL — just core agent framework. | Shows how agents are structured, system messages, conversation loops. |
| `01_simple_agent.py` | Basic agent usage. Starting to use the agent framework. | Formalizes agent setup before adding external tools. |
| `02_risky_delete_demo.py` | Demonstrates danger of unconstrained actions, especially file deletions. | Helps understand why guardrails are necessary. ⚠️ |
| `03_guardrailed_agent.py` | Safe SQL agent: only read operations, validated inputs, protection against unsafe SQL. | Introduces security checks, regex validation, etc. |
| `04_advanced_analytics_agent.py` | Full-blown analytics / BI agent with secure SQL, joins, aggregation, trends, segmentation, multi-turn queries. | Combining rich business logic and analytics with safety. |

---

## Key Features

- Secure SQL execution: only `SELECT`, no writes/updates/deletes.  
- Input validation: regex patterns, single statement enforcement.  
- Automatic limits on result sets when needed.  
- Support for advanced SQL constructs: JOINs, window functions, CTEs, historical trends.  
- Multi-turn interaction for iterative analysis.  
- Clear system message context with schema, business logic (e.g., revenue, refunds, etc.).  

---

## Requirements

- Python 3.9+  
- A `.env` file containing necessary environment variables (e.g. `GOOGLE_API_KEY`)  
- Dependencies listed in `requirements.txt` (ensure they match your versions)  
- A working SQLite file (or your choice of SQL database) configured appropriately  

---
## Security / Safety Considerations

- Do not run risky deletion scripts (like 02_risky_delete_demo.py) on machines with important data.
- Always double check input SQL when allowed — even with guardrails.
- Guardrails include: only SELECT, limit injection, no multiple statements.
- Ensure schema whitelist is up to date (if using additional tables).
___

## How to Contribute or Extend

- Add additional analytics reports or metrics (e.g., churn rate, cohort analysis).
- Support more databases (PostgreSQL, MySQL) with similar safety checks.
- Improve performance for large data queries or integrate caching.
- Add user authentication / access control if sharing across users.

## Usage

```bash
# Clone repository
git clone https://github.com/salmasaleem01/SQL-Agent.git
cd SQL-Agent

# (If needed) create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
Then run individual scripts as needed:
# Conversational agent only
python 00_simple_conversational_agent.py

# Basic agent
python 01_simple_agent.py

# Risky behavior demo
python 02_risky_delete_demo.py

# Guardrailed (safe) SQL agent
python 03_guardrailed_agent.py

# Advanced analytics / BI-oriented agent
python 04_advanced_analytics_agent.py 

