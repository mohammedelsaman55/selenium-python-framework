from utils.bug_reporter import create_bug_report


def test_create_bug_report():

    bug_file = create_bug_report(
        module="profile",
        title="Address field validation failed",
        test_case="PROFILE-037",
        url="https://sub6-test.togetherapps.ca/dashboard/profile",
        actual_result="Validation message not displayed",
        expected_result="Validation message should be displayed",
        username="samanauto@gmail.com",
        password="123@123Mm",
        screenshot_path="reports/screenshots/test.png",
        severity="Medium",
        priority="High",
        bug_type="Backend",
        browser="Chrome",
        automation_test="test_address_maximum_length_validation"
    )

    print(
        "Bug Report Created:",
        bug_file
    )

    assert bug_file is not None