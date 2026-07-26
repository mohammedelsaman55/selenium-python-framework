from selenium.webdriver.common.by import By


class ProfileLocators:

    PROFILE_AVATAR = (
        By.XPATH,
        "//img[@alt='User Avatar']"
    )

    LOGOUT_BUTTON = (
        By.XPATH,
        "//div[text()='Logout']"
    )

    CONFIRM_LOGOUT_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Yes, Log me Out')]"
    )

    PAGE_TITLE = (
        By.XPATH,
        "//strong[text()='Profile']"
    )

    PROFILE_NAME = (
        By.XPATH,
        "//h5[contains(@class,'text-gray-800')]"
    )

    FIRST_NAME_INPUT = (
        By.ID,
        "first_name"
    )

    LAST_NAME_INPUT = (
        By.ID,
        "last_name"
    )

    EMAIL_INPUT = (
        By.ID,
        "email_address"
    )

    PASSWORD_INPUT = (
        By.ID,
        "password"
    )

    COUNTRY_CODE_INPUT = (
        By.XPATH,
        "//input[@aria-label='Country code']"
    )

    PHONE_NUMBER_INPUT = (
        By.XPATH,
        "//input[@name='phoneNumber']"
    )

    ADDRESS_INPUT = (
        By.ID,
        "address"
    )

    TEAM_DROPDOWN = (
        By.XPATH,
        "//div[contains(@class,'react-select__control')]"
    )

    SAVE_CHANGES_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    CHANGE_PHOTO_LINK = (
        By.XPATH,
        "//span[text()='Change photo']"
    )

    CHANGE_EMAIL_LINK = (
        By.XPATH,
        "//label[@for='email_address']/following::small[text()='Change'][1]"
    )

    CHANGE_PASSWORD_LINK = (
        By.XPATH,
        "//label[@for='password']/following::small[text()='Change'][1]"
    )

    COUNTRY_SELECTOR_DROPDOWN = (
        By.XPATH,
        "//div[contains(@class,'selected-flag')]"
    )

    SELECTED_COUNTRY = (
        By.XPATH,
        "//div[contains(@class,'selected-flag')]"
    )

    TEAM_VALUE = (
        By.XPATH,
        "//div[contains(@class,'react-select__multi-value__label')]"
    )

    COUNTRY_SEARCH_INPUT = (
        By.XPATH,
        "//input[@placeholder='Search country...']"
    )

    COUNTRY_EGYPT_OPTION = (
        By.XPATH,
        "//li[@data-country-code='eg']"
    )

    FIRST_NAME_REQUIRED_MESSAGE = (
        By.XPATH,
        "//small[text()='First name is required.']"
    )

    LAST_NAME_REQUIRED_MESSAGE = (
        By.XPATH,
        "//small[text()='Last name is required.']"
    )

    PHONE_REQUIRED_MESSAGE = (
        By.XPATH,
        "//div[text()='Phone is required.']"
    )

    SUCCESS_TOAST_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Profile updated successfully')]"
    )

    CHANGE_PASSWORD_POPUP_TITLE = (
        By.XPATH,
        "//strong[text()='Change Password']"
    )

    CURRENT_PASSWORD_INPUT = (
        By.XPATH,
        "//input[@placeholder='Current Password']"
    )

    NEW_PASSWORD_INPUT = (
        By.XPATH,
        "//input[@placeholder='New Password']"
    )

    CONFIRM_PASSWORD_INPUT = (
        By.XPATH,
        "//input[@placeholder='Confirm Password']"
    )

    SAVE_PASSWORD_BUTTON = (
        By.XPATH,
        "//button[@type='submit']//strong[text()='Save']"
    )

    PASSWORD_CHANGED_SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Password updated successfully')]"
    )

    PASSWORDS_DO_NOT_MATCH_MESSAGE = (
        By.XPATH,
        "//small[text()='Passwords do not match.']"
    )

    GENERIC_ERROR_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'Something went wrong')]"
    )

    ADDRESS_MAXIMUM_LENGTH_MESSAGE = (
        By.XPATH,
        "//small[text()='The Address field must not be greater than 250 characters.']"
    )