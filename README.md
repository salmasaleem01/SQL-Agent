#AI Agents Demo Suite

This repository demonstrates the evolution of AI agents, starting from basic conversational agents to production-ready analytics agents with guardrails. Each script builds on the previous one, showing both capabilities and risks, while progressively introducing security measures and business intelligence logic.
# 📂 Project Structure
.
├── 00_simple_conversational_agent.py   # Agent with dummy tool (conversation only)
├── 01_simple_agent.py                  # Minimal agent demo
├── 02_risky_delete_demo.py             # Risk demo: unsafe, unconstrained agent
├── 03_guardrailed_agent.py             # Safe SQL agent with guardrails
├── 04_advanced_analytics_agent.py      # BI-ready analytics SQL agent
└── README.md                           # Project documentation

🚀 Scripts Overview
00. Simple Conversational Agent

Demonstrates a conversational agent using LangChain with a dummy tool.

No database or external logic — just shows the framework structure.

Educational focus: understanding agent scaffolding.

01. Simple Agent

Minimal example of a LangChain agent.

Foundation for adding tools and external integrations.

Educational focus: agent basics before introducing risks and safety.

02. Risky Delete Demo ⚠️

Shows what happens when agents are unconstrained.

Demonstrates unsafe file deletion to highlight potential dangers.

Educational focus: importance of guardrails and safety.

⚠️ Do not run on production machines.

03. Guardrailed Agent

Introduces security guardrails for SQL queries:

Only SELECT allowed

Regex-based validation

Prevention of destructive SQL commands

Result set limiting

Educational focus: how to safely integrate agents with databases.

04. Advanced Analytics SQL Agent

Production-style agent for business intelligence and analytics.

Features:

Revenue analysis, customer segmentation, lifetime value

Time-series trend analysis

Product rankings, aggregations, and multi-table joins

Multi-turn conversation for iterative queries

Security features inherited from Guardrailed Agent:

Read-only enforcement

Automatic LIMIT injection

SQL injection protection

Educational focus: scalable, production-ready analytics agents.

🛠️ Requirements

Python 3.9+

Dependencies (install via requirements.txt):

pip install -r requirements.txt


.env file containing your API key(s):

GOOGLE_API_KEY=your_api_key_here

▶️ Usage

Run scripts independently depending on what you want to explore:

# Conversational agent (framework only)
python 00_simple_conversational_agent.py

# Simple agent
python 01_simple_agent.py

# Risky demo (unsafe – be careful!)
python 02_risky_delete_demo.py

# Guardrailed SQL agent
python 03_guardrailed_agent.py

# Advanced analytics BI agent
python 04_advanced_analytics_agent.py

🎯 Learning Journey

This repo takes you step-by-step:

Basic agents → Understand framework.

Risk demonstration → See dangers of unconstrained automation.

Guardrails → Add safety and reliability.

Advanced BI logic → Apply agents to real-world analytics use cases.

📜 License

MIT License – free to use, adapt, and share with attribution.
