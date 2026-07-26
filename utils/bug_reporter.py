import os
from datetime import datetime


def create_bug_report(
    module,
    title,
    test_case,
    url,
    actual_result,
    expected_result,
    username,
    password,
    screenshot_path=None,
    severity="Medium",
    priority="Medium",
    bug_type="Backend",
    browser="Chrome",
    automation_test="Unknown"
):
    bug_folder = f"bug_reports/{module}"
    os.makedirs(bug_folder, exist_ok=True)

    existing_bugs = [
        file
        for file in os.listdir(bug_folder)
        if file.endswith(".md")
    ]

    bug_number = len(existing_bugs) + 1
    bug_id = f"{module.upper()}-BUG-{bug_number:03d}"
    bug_file = os.path.join(bug_folder, f"{bug_id}.md")

    execution_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(bug_file, "w", encoding="utf-8") as file:
        file.write(
            f"# {bug_id}\n\n"
            f"Status:\nOpen\n\n"
            f"Bug Type:\n{bug_type}\n\n"
            f"Module:\n{module}\n\n"
            f"Title:\n{title}\n\n"
            f"Environment:\nTest\n\n"
            f"URL:\n{url}\n\n"
            f"Test User:\n{username}\n\n"
            f"Password:\n{password}\n\n"
            f"Test Case:\n{test_case}\n\n"
            f"Automation Test:\n{automation_test}\n\n"
            f"Browser:\n{browser}\n\n"
            f"Execution Date:\n{execution_date}\n\n"
            f"Severity:\n{severity}\n\n"
            f"Priority:\n{priority}\n\n"
            f"Actual Result:\n{actual_result}\n\n"
            f"Expected Result:\n{expected_result}\n\n"
            f"Screenshot:\n{screenshot_path or 'N/A'}\n\n"
            f"Assigned To:\nUnassigned\n\n"
            f"Comments:\nCreated automatically by Automation Framework\n"
        )

    return bug_file