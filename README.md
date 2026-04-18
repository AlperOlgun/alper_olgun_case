# Alper Olgun – Case Study

This repository includes UI, API, and basic performance tests.

## Structure
- **api_tests/**: Petstore CRUD tests (positive & negative) using requests + pytest
- **ui_tests/**: Selenium-based UI tests (login + QA jobs flow)
- **performance_tests/**: Locust scenarios for basic load observation

## Tech Stack
Python, Pytest, Selenium, Requests, Locust

## How to Run

### API
```bash
cd api_tests
python -m pytest -v