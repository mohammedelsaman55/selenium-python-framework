from selenium.webdriver.common.by import By


class UsersLocators:

    # ==========================================
    # Users Page
    # ==========================================

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
        "//div[@role='menuitem'][.//strong[normalize-space()='Details']]"
    )

    ACTIVATE_OPTION = (
        By.XPATH,
        "//strong[normalize-space()='Activate']"
    )

    DEACTIVATE_OPTION = (
        By.XPATH,
        "//strong[normalize-space()='Deactivate']"
    )

    # ==========================================
    # Create User
    # ==========================================

    ADD_USER_MODAL_TITLE = (
        By.XPATH,
        "//strong[text()='Add New User']"
    )

    FIRST_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter first name']"
    )

    LAST_NAME_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter last name']"
    )

    EMAIL_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter email address']"
    )

    PHONE_INPUT = (
        By.NAME,
        "phoneNumber"
    )

    TEAM_DROPDOWN = (
        By.XPATH,
        "//label[contains(.,'Team')]/following::div[contains(@class,'react-select__control')][1]"
    )

    TEAM_INPUT = (
        By.XPATH,
        "//label[contains(.,'Team')]/following::input[@role='combobox'][1]"
    )

    COUNTRY_DROPDOWN = (
        By.XPATH,
        "//label[contains(.,'Country')]/following::div[contains(@class,'select__control')][1]"
    )

    COUNTRY_INPUT = (
        By.XPATH,
        "//label[contains(.,'Country')]/following::input[@role='combobox'][1]"
    )

    PROVINCE_DROPDOWN = (
        By.XPATH,
        "//label[contains(.,'Province')]/following::div[contains(@class,'select__control')][1]"
    )

    PROVINCE_INPUT = (
        By.XPATH,
        "//label[contains(.,'Province')]/following::input[@role='combobox'][1]"
    )

    CITY_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter city']"
    )

    POSTAL_CODE_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter postal code']"
    )

    ADDRESS_INPUT = (
        By.XPATH,
        "//input[@placeholder='Street name, building number']"
    )

    STATUS_VALUE = (
        By.XPATH,
        "//div[contains(@class,'single-value') and normalize-space()='Active']"
    )

    SAVE_BUTTON = (
        By.XPATH,
        "//button[@type='submit']"
    )

    CLOSE_BUTTON = (
        By.XPATH,
        "//button[@data-slot='dialog-close']"
    )

    CREATE_USER_MODAL = (
        By.XPATH,
        "//div[@role='dialog']"
    )

    FIRST_NAME_REQUIRED = (
        By.XPATH,
        "//small[text()='First Name is required.']"
    )

    LAST_NAME_REQUIRED = (
        By.XPATH,
        "//small[text()='Last Name is required.']"
    )

    EMAIL_REQUIRED = (
        By.XPATH,
        "//small[text()='Email Address is required.']"
    )

    CREATE_USER_SUCCESS_MESSAGE = (
        By.XPATH,
        "//h4/strong[normalize-space()='User Created']"
    )

    VIEW_USERS_LIST_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='View users list']"
    )

    EMAIL_ALREADY_EXISTS = (
        By.XPATH,
        "//small[normalize-space()='The email has already been taken.']"
    )

    INVALID_EMAIL_MESSAGE = (
        By.XPATH,
        "//small[normalize-space()='The email field format is invalid.']"
    )

    # ==========================================
    # User Details (Used for Edit User)
    # ==========================================

    DETAILS_PAGE_TITLE = (
        By.XPATH,
        "//strong[normalize-space()='User Details']"
    )

    FIRST_NAME_DETAILS_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter first name']"
    )

    LAST_NAME_DETAILS_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter last name']"
    )

    EMAIL_DETAILS_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter email address']"
    )

    PHONE_DETAILS_INPUT = (
        By.NAME,
        "phoneNumber"
    )

    CITY_DETAILS_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter city']"
    )

    POSTAL_CODE_DETAILS_INPUT = (
        By.XPATH,
        "//input[@placeholder='Enter postal code']"
    )

    ADDRESS_DETAILS_INPUT = (
        By.XPATH,
        "//textarea[@placeholder='Enter address'] | //input[@placeholder='Street name, building number']"
    )

    SAVE_CHANGES_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and .//strong[normalize-space()='Save Changes']] | //button[normalize-space()='Save Changes']"
    )

    USER_UPDATED_SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'User updated successfully')]"
    )

    BACK_BUTTON = (
        By.XPATH,
        "//button[@type='button'][.//*[name()='svg']]"
    )

    # ==========================================
    # User Actions
    # ==========================================

    ACTIVATE_DIALOG_TITLE = (
        By.XPATH,
        "//strong[normalize-space()='Activate User']"
    )

    DEACTIVATE_DIALOG_TITLE = (
        By.XPATH,
        "//strong[normalize-space()='Deactivate User']"
    )

    CONFIRM_ACTION_BUTTON = (
        By.XPATH,
        "//button[contains(.,\"Yes, I'm Sure\")]"
    )

    CANCEL_ACTION_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Cancel']"
    )

    ACTION_SUCCESS_MESSAGE = (
        By.XPATH,
        "//*[contains(text(),'successfully')]"
    )