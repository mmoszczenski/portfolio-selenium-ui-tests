# Selenium UI Automation Test Suite

A comprehensive UI automation test suite for [AutomationExercise.com](https://automationexercise.com/) built with Selenium, Python, and pytest.

## Features

- **Page Object Model (POM)** architecture
- **Test data factories** using Faker for dynamic data generation
- **Comprehensive coverage**: Registration, Login, Shopping Cart, Checkout, Product Search, Contact Form
- **HTML report** with automatic screenshot capture on failures

## Technologies

- Python 3.x
- Selenium WebDriver 4.35.0
- pytest 8.4.1
- Faker
- webdriver-manager

## Quick Start

### Installation

    cd selenium-project
    pip install -r requirements.txt

### Run Tests

# Run all tests

    pytest

# Run in headless mode

    pytest --headless

# Run specific test file

    pytest tests/test_register.py

### View Reports

HTML report is generated in `reports/report.html` after test execution.

## Project Structure

```
selenium-project/
├── pages/ # Page Object Model classes
├── tests/ # Test files (register, login, cart, checkout, etc.)
├── utils/ # Test data factories and utilities
├── test_data/ # Product data definitions
└── reports/ # HTML test report
```

## Test Coverage

- ✅ User registration (positive & negative cases)
- ✅ User login (positive & negative cases)
- ✅ Shopping cart operations
- ✅ Complete checkout flow
- ✅ Product search and filtering
- ✅ Contact form submission

**Purpose**: Portfolio project demonstrating Selenium test automation best practices

```

```
