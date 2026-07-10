# TerraGuard

Infrastructure Change Intelligence Engine
Correlates Terraform dependency graphs with security analysis to produce explainable deployment decisions.

TerraGuard is an infrastructure intelligence engine that analyzes Terraform infrastructure changes and correlates graph-based dependency analysis with security findings to produce deployment recommendations.

Traditional Infrastructure-as-Code scanners identify policy violations independently for each resource. TerraGuard extends this by understanding the structure of the infrastructure, determining how critical each resource is within the dependency graph, and combining that information with security findings to provide actionable deployment decisions.

---

## Motivation

Modern Infrastructure-as-Code workflows generate large amounts of information:

- Terraform describes what will change.
- Security scanners report policy violations.
- Engineers must manually determine which findings actually matter.

Not every failed security check carries the same operational risk.

A security issue on a foundational VPC is significantly more important than the same issue on an isolated resource.

TerraGuard bridges this gap by combining infrastructure topology with security analysis to prioritize risk and support deployment decisions.

---

## Features

Current capabilities include:

- Terraform Plan Parser
- Infrastructure Blueprint Generation
- Infrastructure Dependency Graph Construction
- Dependency Analysis
- Blast Radius Calculation
- Infrastructure Criticality Scoring
- Checkov Integration
- Security Finding Parsing
- Resource Risk Correlation
- Deterministic Deployment Decision Engine
- Human-readable Infrastructure Risk Reports

---

## Architecture

```
Terraform Plan
       │
       ▼
Terraform Parser
       │
       ▼
Infrastructure Blueprint
       │
       ▼
Infrastructure Graph
       │
       ▼
Graph Intelligence
(Criticality & Blast Radius)
       │
       ├──────────────┐
       │              │
       ▼              ▼
Checkov Scan    Security Findings
       │              │
       └──────┬───────┘
              ▼
      Resource Correlation
              │
              ▼
      Resource Risk Report
              │
              ▼
       Decision Engine
              │
              ▼
APPROVE • WARN • BLOCK
```

---

## Example Output

```
Resource
--------
aws_vpc.main

Infrastructure
--------------
Criticality Score : 100
Graph Level       : Critical
Blast Radius      : 4

Security
--------
Failed Checks : 2

Resource Risk
-------------
Critical

Insights
--------
• Forms the networking foundation of the infrastructure.
• Security policy violations should be reviewed before deployment.
• Changes may affect dependent infrastructure resources.

Decision
--------
BLOCK

Reason
------
aws_vpc.main is operationally important and contains unresolved security findings.
```

---

## Project Structure

```
app/
├── analyzers/
├── correlation/
├── decision/
├── engine/
├── graph/
├── knowledge/
├── models/
├── parser/
├── renderers/
└── main.py

tests/
terraform_examples/
docs/
```

---

## Running TerraGuard

Clone the repository:

```bash
git clone <repository-url>
cd infrastructure-change-intelligence-engine
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run TerraGuard:

```bash
python -m app.main
```

---

## Running Tests

Execute the complete test suite:

```bash
python -m pytest
```

---

## Current Tech Stack

- Python
- Terraform
- Checkov
- Pydantic
- Graph-based Infrastructure Analysis
- DevSecOps

---

## Roadmap

### Phase 1 — Infrastructure Intelligence
- [x] Terraform Parser
- [x] Infrastructure Graph
- [x] Criticality Analysis
- [x] Blast Radius Analysis
- [x] Checkov Integration
- [x] Resource Risk Correlation
- [x] Decision Engine

### Phase 2 — DevSecOps Integration
- [ ] GitHub Pull Request Comments
- [ ] GitHub Actions Integration
- [ ] Docker Support
- [ ] CI/CD Pipeline

### Phase 3 — Infrastructure Intelligence Expansion
- [ ] Infracost Integration
- [ ] OPA Integration
- [ ] tfsec Integration
- [ ] Drift Detection

### Phase 4 — AI-Assisted Infrastructure Analysis
- [ ] Natural Language Risk Explanations
- [ ] Historical Change Intelligence
- [ ] Incident Knowledge Integration

---

## Design Principles

TerraGuard is built around a few core principles:

- Deterministic infrastructure analysis before AI assistance.
- Graph intelligence over isolated resource analysis.
- Explainable deployment decisions.
- Production-oriented software engineering.
- Practical DevSecOps integration.

---

## Development

This branch is used to validate TerraGuard's GitHub Pull Request integration.

## License

This project is licensed under the MIT License.