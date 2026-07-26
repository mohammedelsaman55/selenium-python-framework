from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


DEFAULT_TIMEOUT = 15


def wait_for_element(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_clickable_element(driver, locator, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_url_contains(driver, text, timeout=DEFAULT_TIMEOUT):
    return WebDriverWait(driver, timeout).until(
        EC.url_contains(text)
    )

def wait_for_overlay_to_disappear(driver, timeout=DEFAULT_TIMEOUT):
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located(
            (
                By.CSS_SELECTOR,
                "div.fixed.inset-0.flex.items-center.justify-center.bg-transparent.bg-opacity-30.z-50"
            )
        )
    )