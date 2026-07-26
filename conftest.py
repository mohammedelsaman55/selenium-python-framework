import os
from datetime import datetime

import pytest

from utils.driver_factory import get_driver
from utils.bug_reporter import create_bug_report

from pages.login_page import LoginPage
from pages.otp_page import OtpPage

from data.test_data import (
    BASE_URL,
    VALID_EMAIL,
    VALID_PASSWORD,
    VALID_OTP
)

from utils.waits import wait_for_url_contains


@pytest.fixture
def driver():

    driver = get_driver()

    yield driver

    try:
        driver.quit()
    except Exception:
        pass


@pytest.fixture
def logged_in_user(driver):

    driver.get(
        BASE_URL + "/dashboard/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        VALID_EMAIL,
        VALID_PASSWORD
    )

    otp_page = OtpPage(driver)

    otp_page.enter_otp(
        VALID_OTP
    )

    otp_page.verify_code()

    wait_for_url_contains(
        driver,
        "/dashboard/profile"
    )

    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield

    report = outcome.get_result()

    if (
        report.when == "call"
        and
        report.failed
    ):

        driver = (
            item.funcargs.get("logged_in_user")
            or
            item.funcargs.get("driver")
        )

        if not driver:
            return

        os.makedirs(
            "reports/screenshots",
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        screenshot_path = (
            f"reports/screenshots/"
            f"{item.name}_{timestamp}.png"
        )

        try:
            driver.save_screenshot(
                screenshot_path
            )

            print(
                f"\nScreenshot saved: "
                f"{screenshot_path}"
            )

        except Exception as e:

            screenshot_path = None

            print(
                f"\nCould not save screenshot: {e}"
            )

        try:
            current_url = driver.current_url
        except Exception:
            current_url = "Browser Closed"

        if item.get_closest_marker(
                "bug_report"
        ):

            module = "general"

            test_path = str(
                item.fspath
            ).lower()

            if "profile" in test_path:
                module = "profile"

            elif "authentication" in test_path:
                module = "authentication"

            elif "users" in test_path:
                module = "users"

            elif "attendance" in test_path:
                module = "attendance"

            elif "payroll" in test_path:
                module = "payroll"

            elif "dashboard" in test_path:
                module = "dashboard"

            try:

                create_bug_report(
                    module=module,
                    title=f"Failed Test: {item.name}",
                    test_case=item.name,
                    url=current_url,
                    actual_result=str(
                        report.longrepr
                    ),
                    expected_result="Test should pass successfully",
                    username=VALID_EMAIL,
                    password=VALID_PASSWORD,
                    screenshot_path=screenshot_path,
                    automation_test=item.name
                )

                print(
                    "\nBug report created "
                    f"for {item.name}"
                )

            except Exception as e:

                print(
                    f"\nCould not create bug report: {e}"
                )