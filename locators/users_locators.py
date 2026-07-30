from selenium.webdriver.common.by import By


class UsersLocators:

    PAGE_TITLE = (
        By.XPATH,
        "//strong[text()='Users']"
    )

    TOTAL_USERS_COUNTER = (
        By.XPATH,
        "(//div[contains(@class,'rounded') and .//strong])[1]//strong"
    )

    ACTIVE_USERS_COUNTER = (
        By.XPATH,
        "(//div[contains(@class,'rounded') and .//strong])[2]//strong"
    )

    INACTIVE_USERS_COUNTER = (
        By.XPATH,
        "(//div[contains(@class,'rounded') and .//strong])[3]//strong"
    )

    CREATE_NEW_USER_BUTTON = (
        By.XPATH,
        "//strong[text()='Create New User']/ancestor::button"
    )

    SEARCH_INPUT = (
        By.XPATH,
        "//input[@placeholder='Search']"
    )

    BULK_ACTIONS_DROPDOWN = (
        By.XPATH,
        "//span[text()='Bulk']/ancestor::button"
    )

    ADD_FILTER_BUTTON = (
        By.XPATH,
        "//div[text()='Add Filter']"
    )

    RESET_FILTER_BUTTON = (
        By.XPATH,
        "//span[text()='Reset']"
    )

    RESET_SORTING_BUTTON = (
        By.XPATH,
        "//div[contains(text(),'Reset Sorting')]"
    )

    EXPORT_PDF_BUTTON = (
        By.XPATH,
        "//span[contains(.,'Export As PDF')]"
    )

    EXPORT_CSV_BUTTON = (
        By.XPATH,
        "//span[contains(.,'Export As CSV')]"
    )

    USERS_TABLE = (
        By.XPATH,
        "//table"
    )

    SELECT_ALL_CHECKBOX = (
        By.XPATH,
        "//strong[text()='All']"
    )

    USER_NAME_HEADER = (
        By.XPATH,
        "//strong[text()='User name']"
    )

    TEAM_HEADER = (
        By.XPATH,
        "//strong[text()='Team']"
    )

    EMAIL_HEADER = (
        By.XPATH,
        "//strong[text()='Email']"
    )

    COUNTRY_HEADER = (
        By.XPATH,
        "//strong[text()='Country']"
    )

    PROVINCE_HEADER = (
        By.XPATH,
        "//strong[text()='Province']"
    )

    PAYMENTS_HEADER = (
        By.XPATH,
        "//strong[text()='Payments']"
    )

    PHONE_NUMBER_HEADER = (
        By.XPATH,
        "//strong[text()='Phone number']"
    )

    STATUS_HEADER = (
        By.XPATH,
        "//strong[text()='Status']"
    )

    ACTIONS_HEADER = (
        By.XPATH,
        "//strong[text()='Actions']"
    )

    USER_ROWS = (
        By.XPATH,
        "//tbody/tr"
    )

    SEARCH_ICON = (
        By.XPATH,
        "//img[@alt='search']"
    )

    FIRST_USER_NAME = (
        By.XPATH,
        "//tbody/tr[1]/td[2]//p"
    )

    NO_RESULTS_MESSAGE = (
        By.XPATH,
        "//strong[text()='No Results Found']"
    )

    PREVIOUS_BUTTON = (
        By.XPATH,
        "//button[text()='Prev']"
    )

    NEXT_BUTTON = (
        By.XPATH,
        "//button[text()='Next']"
    )

    PAGE_SIZE_VALUE = (
        By.XPATH,
        "//div[contains(@class,'single-value') and text()='15']"
    )

    SHOWING_RECORDS_TEXT = (
        By.XPATH,
        "//div[contains(text(),'Showing')]"
    )

    FIRST_USER_ACTIONS_BUTTON = (
        By.XPATH,
        "//tbody/tr[1]//img[@alt='actions']/parent::button"
    )

    DETAILS_OPTION = (
        By.XPATH,
        "//div[@role='menuitem'][.//strong[text()='Details']]"
    )
    
    ACTIVATE_OPTION = (
        By.XPATH,
        "//strong[text()='Activate']"
    )

    DEACTIVATE_OPTION = (
        By.XPATH,
        "//strong[text()='Deactivate']"
    )

    FIRST_NAME_INPUT = (
        By.XPATH,
        "//label[contains(.,'First Name')]/following::input[1]"
    )

    SAVE_CHANGES_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and contains(.,'Save Changes')]"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'User updated successfully')]"
    )