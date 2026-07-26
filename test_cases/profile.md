# Profile Test Cases

---

# Profile View

| ID | Test Case | Status |
|----|-----------|---------|
| PROFILE-001 | Profile Page Title Displayed | Passed ✅ |
| PROFILE-002 | Profile Name Displayed | Passed ✅ |
| PROFILE-003 | First Name Field Displayed | Passed ✅ |
| PROFILE-004 | Last Name Field Displayed | Passed ✅ |
| PROFILE-005 | Email Field Displayed | Passed ✅ |
| PROFILE-006 | Phone Number Component Displayed | Passed ✅ |
| PROFILE-007 | Country Selector Dropdown Displayed | Passed ✅ |
| PROFILE-008 | Password Field Displayed | Passed ✅ |
| PROFILE-009 | Address Field Displayed | Passed ✅ |
| PROFILE-010 | Team Dropdown Displayed | Passed ✅ |
| PROFILE-011 | Save Changes Button Displayed | Passed ✅ |
| PROFILE-012 | Change Photo Link Displayed | Passed ✅ |
| PROFILE-013 | Change Email Link Displayed | Passed ✅ |
| PROFILE-014 | Change Password Link Displayed | Passed ✅ |

---

# Data Validation

| ID | Test Case | Status |
|----|-----------|---------|
| PROFILE-015 | First Name Value Loaded | Passed ✅ |
| PROFILE-016 | Last Name Value Loaded | Passed ✅ |
| PROFILE-017 | Email Value Loaded | Passed ✅ |
| PROFILE-018 | Phone Number Value Loaded | Passed ✅ |
| PROFILE-019 | Selected Country Value Loaded | Passed ✅ |
| PROFILE-020 | Address Value Loaded | Passed ✅ |
| PROFILE-021 | Team Value Loaded | Passed ✅ |

---

# Edit Profile

| ID | Test Case | Status |
|----|-----------|---------|
| PROFILE-022 | Edit First Name | Passed ✅ |
| PROFILE-023 | Edit Last Name | Passed ✅ |
| PROFILE-024 | Edit Address | Passed ✅ |
| PROFILE-025 | Edit Phone Number | Passed ✅ |
| PROFILE-026 | Country Dropdown Opens | Passed ✅ |
| PROFILE-027 | Search Country In Dropdown | Passed ✅ |
| PROFILE-028 | Select Country From Dropdown | Passed ✅ |
| PROFILE-029 | Save Button Disabled Without Changes | Passed ✅ |
| PROFILE-030 | Save Button Enabled After Data Change | Passed ✅ |
| PROFILE-031 | Save Profile Successfully | Passed ✅ |
| PROFILE-032 | Success Message Displayed | Passed ✅ |
| PROFILE-033 | Updated Data Persist After Refresh | Passed ✅ |

---

# Validation Scenarios

| ID | Test Case | Status |
|----|-----------|---------|
| PROFILE-034 | Empty First Name Validation | Passed ✅ |
| PROFILE-035 | Empty Last Name Validation | Passed ✅ |
| PROFILE-036 | Invalid Phone Number Validation (Bug Detected) | Passed ✅ |
| PROFILE-037 | Address Maximum Length Validation (Bug Detected) | Passed ✅ |

---

# Change Email

| ID | Test Case | Status |
|----|-----------|---------|
| PROFILE-038 | Open Change Email Popup | Deferred ⏸️ |
| PROFILE-039 | Change Email Successfully | Deferred ⏸️ |
| PROFILE-040 | Email Validation Message Displayed | Deferred ⏸️ |

---

# Change Password

| ID | Test Case | Status |
|----|-----------|---------|
| PROFILE-041 | Open Change Password Popup | Passed ✅ |
| PROFILE-042 | Change Password Successfully | Passed ✅ |
| PROFILE-043 | Invalid Password Validation Displayed | Passed ✅ |

---

# Profile Photo

| ID | Test Case | Status |
|----|-----------|---------|
| PROFILE-044 | Upload Valid Profile Photo | Passed ✅ |
| PROFILE-045 | Image Upload Success Message Displayed | Passed ✅ |
| PROFILE-046 | Save Button Enabled After Successful Upload | Passed ✅ |
| PROFILE-047 | Save Profile Photo Successfully | Passed ✅ |
| PROFILE-048 | Profile Photo Persists After Refresh | Deferred ⏸️ |

---

# Automation Progress

## Completed

### Profile View
- PROFILE-001 → PROFILE-014 ✅

### Data Validation
- PROFILE-015 → PROFILE-021 ✅

### Edit Profile
- PROFILE-022 → PROFILE-033 ✅

### Validation Scenarios
- PROFILE-034 → PROFILE-037 ✅

### Change Password
- PROFILE-041 → PROFILE-043 ✅

### Profile Photo
- PROFILE-044 → PROFILE-047 ✅

---

# Pending

### Change Email
- PROFILE-038
- PROFILE-039
- PROFILE-040

### Profile Photo
- PROFILE-048

---

# Execution Summary

| Metric | Value |
|----------|------:|
| Total Test Cases | 48 |
| Automated | 42 |
| Passed | 42 |
| Failed | 0 |
| Deferred | 4 |

---

# Current Coverage

| Module | Automated | Total |
|----------|----------:|------:|
| Profile | 42 | 48 |

Coverage: **87.5%**

---

# Latest Execution Result

```bash
42 passed
0 failed