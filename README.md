# 📦 platform_project_template

The `platform_project_template` is a **standardized project scaffold** designed for all AI and Vision-related applications running on Kubernetes under a unified Platform-as-Code framework. It ensures that every project in the team follows the same structure, logging, testing, configuration, and deployment standards, making it easier to maintain, deploy, and scale.

---

## ✅ Purpose

- Promote **consistency and reuse** across all team projects
- Enable **automated CI/CD and Dockerization** from day one
- Simplify integration into **Kubernetes** with standardized paths and outputs
- Track **Technology Readiness Level (TRL)** for maturity assessment

---

## 📁 Project Structure Overview

```
platform_project_template/
├── src/
│   ├── main.py
│   └── utils/
│       └── custom_log.py
├── config.yaml
├── test/
│   └── test_main.py
├── trl_checklist.yaml
├── requirements.txt
├── Dockerfile
├── .github/workflows/ci.yml
├── README.md
```

---

## ⚙️ Features

- **`config.yaml`**: Centralized configuration
- **`main.py`**: Runs fully from config (no hardcoded paths)
- **`custom_log.py`**: JSON logs for stdout and file logging
- **`test_main.py`**: Unit tests for core processing
- **CI/CD**: GitHub Actions pipeline runs tests, builds Docker image if successful
- **TRL Tracking**: Uses `trl_checklist.yaml` to track project maturity
- **Output Rules**:
  - Images → must use timestamp suffixes
  - Text/tabular → JSON only (no CSV)

---

## 🚀 Benefits

- Ready for **Docker + Kubernetes**
- Ensures all team projects are **testable, reproducible, and CI/CD integrated**
- Enforces a clear TRL roadmap for evaluating maturity
- Makes onboarding and project handoff easy

---

## 🧪 Quick Start

```bash
# Run the app
python src/main.py

# Run tests
PYTHONPATH=. pytest test/

# Build Docker image
docker build -t platform-demo .
```

---

## 📊 TRL Checklist Reference

See `trl_checklist.yaml` for assessing readiness from TRL 1 to TRL 9.