<div align="center">

# 🚀 Selenium Python Automation Framework

### Professional UI Test Automation Framework

Built with **Python**, **Selenium WebDriver**, **Pytest**, and the **Page Object Model (POM)**.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)]()
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)]()
[![Pytest](https://img.shields.io/badge/Pytest-Testing-orange.svg)]()
[![POM](https://img.shields.io/badge/Design-Page%20Object%20Model-red.svg)]()

</div>

---

# 📖 Overview

This project is a professional UI Automation Testing Framework developed using **Python**, **Selenium WebDriver**, and **Pytest**.

The framework follows the **Page Object Model (POM)** design pattern to separate page actions from test logic, making the project easier to maintain, extend, and reuse.

The framework automates major workflows of the Together SaaS Admin Dashboard and includes reusable utilities, structured test cases, HTML reporting, screenshot capture, and automatic bug report generation.

---

# ✨ Key Features

- Selenium WebDriver
- Python
- Pytest
- Page Object Model (POM)
- Explicit Waits
- HTML Test Reports
- Screenshot on Test Failure
- Automatic Bug Report Generation
- Modular Test Structure
- Reusable Utilities
- Clean Project Architecture
- Easy Maintenance
- Scalable Design

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Selenium WebDriver | Browser Automation |
| Pytest | Test Framework |
| ChromeDriver | Browser Driver |
| Pytest HTML | HTML Reports |
| Git | Version Control |
| GitHub | Source Code Hosting |

---

# 🏗 Framework Architecture

```text
                    Test Cases
                         │
                         ▼
                   Page Objects
                         │
                         ▼
                     Locators
                         │
                         ▼
                  Selenium WebDriver
                         │
                         ▼
                     Chrome Browser
```

---

# 📂 Project Structure

```text
PythonProject
│
├── data/
├── pages/
├── locators/
├── utils/
├── tests/
│   ├── authentication/
│   ├── profile/
│   └── users/
│
├── test_cases/
├── reports/
├── bug_reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
├── main.py
└── .gitignore
```

# 📁 Project Components

This framework is organized using the **Page Object Model (POM)** to improve readability, maintainability, and scalability.

---

# 📂 data/

The `data` folder contains reusable test data and configuration values shared across the entire framework.

### Files

### 📄 test_data.py

Stores all reusable test data, including:

- Base URL
- Valid Email
- Valid Password
- Valid OTP
- Invalid Test Data
- Reusable Constants

Separating test data from test logic makes maintenance much easier.

---

# 📂 pages/

The `pages` folder contains all Page Object classes.

Each file represents one page or reusable component of the application.

---

### 📄 login_page.py

Handles all Login page actions.

Responsibilities include:

- Enter Email
- Enter Password
- Login
- Toggle Password Visibility
- Read Placeholders
- Read Validation Messages

---

### 📄 otp_page.py

Handles the OTP verification page.

Responsibilities include:

- Enter OTP Code
- Verify OTP
- Resend OTP
- Read OTP Validation Messages

---

### 📄 profile_page.py

Handles all Profile page operations.

Responsibilities include:

- View Profile Information
- Edit Profile
- Change Password
- Save Changes
- Logout

---

### 📄 users_page.py

Handles the Users module.

Responsibilities include:

- Open Users Page
- Search Users
- Read Users Table
- Navigate Between Users

---

### 📄 error_popup_page.py

Handles reusable popup dialogs and error messages that appear throughout the application.

---

# 📂 locators/

Contains all Selenium locators.

Each page has its own locator file to keep Page Objects clean.

### Files

- 📄 login_locators.py
- 📄 otp_locators.py
- 📄 profile_locators.py
- 📄 users_locators.py
- 📄 error_popup_locators.py

Each locator file stores:

- Buttons
- Text Fields
- Labels
- Validation Messages
- Tables
- Links
- Icons

---

# 📂 utils/

The `utils` folder contains reusable helper methods shared across the framework.

### 📄 waits.py

Provides reusable Explicit Wait methods.

Examples:

- Wait for Element
- Wait for Clickable Element
- Wait for URL
- Wait for Visibility

---

### 📄 driver_factory.py

Responsible for browser initialization.

Responsibilities include:

- Chrome Driver Creation
- Browser Configuration
- Driver Setup
- Browser Lifecycle Management

---

### 📄 bug_reporter.py

Automatically generates structured bug reports whenever a test is configured for bug reporting.

Generated reports include:

- Bug ID
- Module
- Severity
- Priority
- Environment
- URL
- Expected Result
- Actual Result
- Screenshot
- Execution Date & Time

---

# 📄 conftest.py

The central configuration file for the Pytest framework.

Responsibilities include:

- Shared Fixtures
- Browser Setup
- Browser Cleanup
- Login Fixtures
- Screenshot on Failure
- Bug Report Integration
- Shared Test Configuration

---

# 📄 pytest.ini

Contains the global Pytest configuration.

Examples include:

- Test Discovery
- Default Test Paths
- HTML Report Configuration
- Pytest Settings

---

# 📄 requirements.txt

Contains all required Python packages.

Typical packages include:

- selenium
- pytest
- pytest-html
- webdriver-manager

Installing these packages prepares the project for execution.

---

# 📄 .gitignore

Defines files and folders ignored by Git.

Examples:

- .venv
- reports
- .pytest_cache
- __pycache__
- .idea

Keeping these files out of Git keeps the repository clean and lightweight.

# 🧪 Test Modules

The automated tests are organized by business module to improve readability, maintenance, and scalability.

---

# 📂 tests/

Contains all automated test scripts.

---

## 📂 authentication/

This module verifies the complete authentication workflow.

### Test Files

### 📄 test_login.py

Covers login functionality, including:

- Login Page Display
- Email Validation
- Password Validation
- Login Button
- Password Visibility Toggle
- Valid Login
- Invalid Login

---

### 📄 test_otp.py

Tests the One-Time Password (OTP) verification process.

Covered scenarios include:

- OTP Verification
- Invalid OTP
- OTP Validation Messages

---

### 📄 test_session.py

Validates user session behavior.

Examples include:

- Session Persistence
- Authentication State
- Session Validation

---

## 📂 profile/

This module verifies all Profile features.

### Test Files

### 📄 test_profile_view.py

Verifies that profile information is displayed correctly.

---

### 📄 test_profile_edit.py

Tests profile editing functionality.

Examples include:

- Edit First Name
- Edit Last Name
- Edit Phone Number
- Save Changes
- Field Validations

---

### 📄 test_profile_data_validation.py

Validates profile form inputs.

Examples include:

- Required Fields
- Maximum Length
- Input Validation

---

### 📄 test_change_password.py

Tests the complete Change Password workflow.

Examples include:

- Successful Password Change
- Incorrect Current Password
- Password Validation

---

### 📄 test_change_password_elements.py

Verifies Change Password page UI elements.

Examples include:

- Labels
- Buttons
- Input Fields
- Visibility

---

### 📄 test_profile_country_dropdown.py

Tests Country dropdown functionality.

Examples include:

- Dropdown Display
- Country Selection
- Search
- Selection Validation

---

## 📂 users/

Tests the Users Management module.

### Test Files

### 📄 test_users_view.py

Verifies Users page functionality.

Examples include:

- Users Page Loading
- Navigation
- User Details

---

### 📄 test_users_table.py

Tests the Users table.

Examples include:

- Table Visibility
- Columns
- Search
- Data Display
- Pagination (if available)

---

### 📄 test_bug_reporter.py

Verifies the Automatic Bug Report Generator.

Examples include:

- Bug Report Creation
- Markdown File Generation
- Report Structure
- Bug Information Validation

---

# 📄 test_cases/

Contains manual documentation for automated scenarios.

### Files

- authentication.md
- profile.md
- users.md

These documents describe the manual test cases implemented by the automation framework.

# 🚀 Getting Started

Follow the steps below to set up and run the automation framework on your local machine.

---

# 1️⃣ Clone the Repository

```bash
git clone https://github.com/mohammedelsaman55/selenium-python-framework.git
```

---

# 2️⃣ Navigate to the Project Folder

```bash
cd selenium-python-framework
```

---

# 3️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

### macOS / Linux

```bash
python3 -m venv .venv
```

---

# 4️⃣ Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

# 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Tests

## Run All Tests

```bash
pytest
```

---

## Run Authentication Tests

```bash
pytest tests/authentication
```

---

## Run Profile Tests

```bash
pytest tests/profile
```

---

## Run Users Tests

```bash
pytest tests/users
```

---

## Run the Bug Reporter Tests

```bash
pytest tests/test_bug_reporter.py
```

---

## Run a Specific Test File

Example:

```bash
pytest tests/profile/test_profile_edit.py
```

---

## Run a Specific Test Function

Example:

```bash
pytest tests/profile/test_profile_edit.py::test_edit_profile
```

---

## Run Tests with Verbose Output

```bash
pytest -v
```

---

# 📊 HTML Test Reports

The framework automatically generates an HTML execution report.

Example location:

```text
reports/html/report.html
```

The report includes:

- Test Summary
- Passed Tests
- Failed Tests
- Execution Time
- Error Details
- Stack Trace

This makes reviewing test execution simple and efficient.

---

# 📸 Screenshot on Failure

Whenever a test fails, the framework automatically captures a screenshot.

Screenshots are saved in:

```text
reports/screenshots/
```

Screenshots help developers and testers quickly identify the cause of failures.

---

# 🐞 Automatic Bug Reports

When configured, failed tests automatically generate a structured bug report.

Bug reports are stored inside:

```text
bug_reports/
```

Each report contains:

- Bug ID
- Module
- Severity
- Priority
- Environment
- URL
- Expected Result
- Actual Result
- Screenshot Reference
- Execution Date
- Execution Time

---

# 📄 Manual Test Cases

Manual test documentation is available in:

```text
test_cases/
```

Available documents include:

- authentication.md
- profile.md
- users.md

These files describe the manual test scenarios implemented by the automation framework.

---

# 💡 Best Practices Used

This framework follows industry-standard automation testing practices, including:

- ✅ Page Object Model (POM)
- ✅ Reusable Test Data
- ✅ Reusable Locators
- ✅ Explicit Waits
- ✅ Modular Test Design
- ✅ Automatic HTML Reports
- ✅ Screenshot Capture
- ✅ Automatic Bug Reporting
- ✅ Git Version Control
- ✅ Clean Code Structure
- ✅ Easy Maintenance
- ✅ Scalable Framework Design

# 📊 Project Highlights

This framework includes:

- Organized Page Object Model (POM)
- Modular Test Architecture
- Authentication Module Automation
- Profile Module Automation
- Users Module Automation
- Reusable Test Data
- Reusable Locators
- Explicit Wait Utilities
- HTML Test Reports
- Automatic Screenshot Capture
- Automatic Bug Report Generation
- Clean Folder Structure
- Git Version Control
- GitHub Repository

---

# 📈 Future Enhancements

Planned improvements include:

- Cross Browser Testing (Firefox & Edge)
- Parallel Test Execution
- Jenkins CI/CD Integration
- GitHub Actions Pipeline
- Docker Support
- Allure Reports
- API Testing Integration
- Database Validation
- Data-Driven Testing
- Excel & JSON Test Data Support
- Environment Configuration (.env)
- Logging Improvements

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📜 License

This project is created for learning, demonstration, and portfolio purposes.

Feel free to use or extend it for educational and personal projects.

---

# 👨‍💻 Author

**Mohamed Elsaman**

QA Engineer

Specialized in:

- Manual Testing
- Automation Testing
- Selenium WebDriver
- Python
- Pytest
- Software Quality Assurance

GitHub Repository:

https://github.com/mohammedelsaman55/selenium-python-framework

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

💡 Share your feedback

Every contribution and suggestion is appreciated.

---

<div align="center">

### Thank you for visiting this repository ❤️

Happy Testing 🚀

</div>