from selenium.webdriver.common.by import By


class LoginLocators:

    EMAIL = (
        By.ID,
        "email"
    )

    PASSWORD = (
        By.ID,
        "password"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    EMAIL_REQUIRED_MESSAGE = (
        By.XPATH,
        "//small[text()='Email is required.']"
    )

    PASSWORD_REQUIRED_MESSAGE = (
        By.XPATH,
        "//small[text()='Password is required.']"
    )

    INVALID_EMAIL_MESSAGE = (
        By.XPATH,
        "//small[text()='Please enter a valid email.']"
    )

    PAGE_TITLE = (
        By.XPATH,
        "//h2[text()='Login To Admin Panel']"
    )

    PASSWORD_VISIBILITY_BUTTON = (
        By.XPATH,
        "//button[@type='button']"
    )