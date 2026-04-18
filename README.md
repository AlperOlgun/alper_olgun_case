# Alper Olgun – QA Automation Case Study

This repository contains UI, API, and basic performance test automation for a sample application.

---

## 📌 Scope

- UI Automation (Selenium)
- API Testing (Requests + Pytest)
- Performance Testing (Locust)

---

## 🧪 Test Coverage

### UI Tests
- Login page validation (positive & negative)
- QA Jobs flow:
  - Navigate to Careers
  - Select QA team
  - Verify job listings

### API Tests (Petstore)
- Create pet (positive & negative)
- Get pet by ID (valid / invalid)
- Update pet
- Delete pet (valid / invalid)

### Performance Tests
- Basic load test with Locust
- Endpoints:
  - GET /pet/findByStatus
  - GET /pet/{id}

---

## ⚙️ Tech Stack

- Python
- Pytest
- Selenium
- Requests
- Locust

---

## 🚀 Setup

```bash
pip install -r requirements.txt