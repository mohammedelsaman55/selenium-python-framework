from selenium.webdriver.common.by import By


class OtpLocators:

    OTP_INPUTS = (
        By.XPATH,
        "//input[@maxlength='1']"
    )

    VERIFY_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Verify Code')]"
    )

    OTP_TITLE = (
        By.XPATH,
        "//strong[text()=\"Verify it's you\"]"
    )

    EMPTY_OTP_MESSAGE = (
        By.XPATH,
        "//div[text()='Please enter the full 4-digit code']"
    )

    INVALID_OTP_MESSAGE = (
        By.XPATH,
        "//div[text()='Invalid verification code.']"
    )

    RESEND_CODE_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Resend code again')]"
    )

    OTP_TIMER = (
        By.XPATH,
        "//span[contains(text(), ':')]"
    )