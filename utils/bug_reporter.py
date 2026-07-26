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

    bug_folder = (
        f"bug_reports/{module}"
    )

    os.makedirs(
        bug_folder,
        exist_ok=True
    )

    existing_bugs = [
        file
        for file in os.listdir(
            bug_folder
        )
        if file.endswith(".md")
    ]

    bug_number = (
        len(existing_bugs) + 1
    )

    bug_id = (
        f"{module.upper()}-BUG-{bug_number:03d}"
    )

    bug_file = (
        f"{bug_folder}/{bug_id}.md"
    )

    with open(
            bug_file,
            "w",
            encoding="utf-8"
    ) as file:

        file.write(
            f"# {bug_id}\n\n"

            f"Status:\n"
            f"Open\n\n"

            f"Bug Type:\n"
            f"{bug_type}\n\n"

            f"Module:\n"
            f"{module}\n\n"

            f"Title:\n"
            f"{title}\n\n"

            f"Environment:\n"
            f"Test\n\n"

            f"URL:\n"
            f"{url}\n\n"

            f"Test User:\n"
            f"{username}\n\n"

            f"Password:\n"
            f"{password}\n\n"

            f"Test Case:\n"
            f"{test_case}\n\n"

            f"Automation Test:\n"
            f"{automation_test}\n\n"

            f"Browser:\n"
            f"{browser}\n\n"

            f"Execution Date:\n"
            f"{datetime.now()}\n\n"

            f"Severity:\n"
            f"{severity}\n\n"

            f"Priority:\n"
            f"{priority}\n\n"

            f"Actual Result:\n"
            f"{actual_result}\n\n"

            f"Expected Result:\n"
            f"{expected_result}\n\n"

            f"Screenshot:\n"
            f"{screenshot_path}\n\n"

            f"Assigned To:\n"
            f"Unassigned\n\n"

            f"Comments:\n"
            f"Created automatically by Automation Framework\n"
        )

    return bug_file