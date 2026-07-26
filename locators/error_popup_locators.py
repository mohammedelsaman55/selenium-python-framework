from selenium.webdriver.common.by import By


class ErrorPopupLocators:

    LOGIN_ERROR_TITLE = (
        By.XPATH,
        "//strong[text()='Login Error']"
    )

    DISMISS_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Dissmis')]"
    )