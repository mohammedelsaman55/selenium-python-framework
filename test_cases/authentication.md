# Authentication Test Cases

## Login Screen

| ID | Test Case | Status |
|----|-----------|---------|
| AUTH-001 | Page Title Displayed | Passed ✅ |
| AUTH-002 | Email Placeholder | Passed ✅ |
| AUTH-003 | Password Placeholder | Passed ✅ |
| AUTH-004 | Login Button Text | Passed ✅ |
| AUTH-005 | Password Hidden By Default | Passed ✅ |
| AUTH-006 | Password Visibility Toggle | Passed ✅ |
| AUTH-007 | Invalid Email Format | Passed ✅ |
| AUTH-008 | Empty Email | Passed ✅ |
| AUTH-009 | Empty Password | Passed ✅ |
| AUTH-010 | Invalid Login | Passed ✅ |
| AUTH-011 | Valid Login | Passed ✅ |

---

## OTP Verification

| ID | Test Case | Status |
|----|-----------|---------|
| AUTH-012 | OTP Popup Title | Passed ✅ |
| AUTH-013 | Empty OTP | Passed ✅ |
| AUTH-014 | Invalid OTP | Passed ✅ |
| AUTH-015 | Resend OTP | Passed ✅ |
| AUTH-016 | Valid OTP | Passed ✅ |

---

## Post Login

| ID | Test Case | Status |
|----|-----------|---------|
| AUTH-017 | Access Login Page While Already Logged In | Passed ✅ |
| AUTH-018 | Session Timeout | Passed ✅ |

---

## Logout

| ID | Test Case | Status |
|----|-----------|---------|
| AUTH-019 | Logout | Passed ✅ |
| AUTH-020 | Access Dashboard After Logout | Passed ✅ |

---

## Additional Scenarios

| ID | Test Case | Status |
|----|-----------|---------|
| AUTH-021 | Login Using Enter Key | Passed ✅ |
| AUTH-022 | Email With Leading Spaces | Passed ✅ |
| AUTH-023 | Email With Trailing Spaces | Passed ✅ |

---

# Automation Progress

## Completed

- AUTH-001 - Page Title Displayed ✅
- AUTH-002 - Email Placeholder ✅
- AUTH-003 - Password Placeholder ✅
- AUTH-004 - Login Button Text ✅
- AUTH-005 - Password Hidden By Default ✅
- AUTH-006 - Password Visibility Toggle ✅
- AUTH-007 - Invalid Email Format ✅
- AUTH-008 - Empty Email ✅
- AUTH-009 - Empty Password ✅
- AUTH-010 - Invalid Login ✅
- AUTH-011 - Valid Login ✅
- AUTH-012 - OTP Popup Title ✅
- AUTH-013 - Empty OTP ✅
- AUTH-014 - Invalid OTP ✅
- AUTH-015 - Resend OTP ✅
- AUTH-016 - Valid OTP ✅
- AUTH-017 - Access Login Page While Already Logged In ✅
- AUTH-018 - Session Timeout ✅
- AUTH-019 - Logout ✅
- AUTH-020 - Access Dashboard After Logout ✅
- AUTH-021 - Login Using Enter Key ✅
- AUTH-022 - Email With Leading Spaces ✅
- AUTH-023 - Email With Trailing Spaces ✅

---

# Execution Summary

| Metric | Value |
|----------|----------|
| Total Test Cases | 23 |
| Automated | 23 |
| Passed | 23 |
| Failed | 0 |
| Pending | 0 |

---

# Current Automation Coverage

| Module | Automated | Total |
|----------|----------|----------|
| Authentication | 23 | 23 |

## Coverage

```text
100%
```

---

# Latest Execution Result

```bash
23 passed
0 failed
```

---

# Framework Improvements

- Implemented Page Object Model (POM).
- Centralized Locators.
- Created reusable Wait utilities.
- Added `wait_for_clickable_element()`.
- Improved Logout stability.
- Removed duplicated methods.
- Added reusable OTP workflows.
- Improved framework maintainability and readability.

---

# Observations

## OBS-001
Leading spaces in email addresses are not automatically trimmed before validation.

## OBS-002
Trailing spaces in email addresses are not automatically trimmed before validation.

## OBS-003
A loading overlay may temporarily block profile actions immediately after login and requires proper synchronization.

---

# Module Status

✅ Authentication Module Completed

Ready for:

- Profile Module Automation
- Regression Execution
- CI/CD Integration
- Future Framework Enhancements