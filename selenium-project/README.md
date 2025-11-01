# Install dependencies

pip install -r requirements.txt

# Run all tests

pytest

# Run in headless mode

pytest --headless

# Run specific test suite

pytest tests/test_register.py

# Run with markers

pytest -m positive # Positive test cases
pytest -m negative # Negative test cases

## Reports

View test results in `reports/report.html`. Screenshots on failures are saved in `screenshots/` directory.
