from data.test_data import PROFILE_IMAGE
from pages.profile_page import ProfilePage


def test_upload_profile_photo_successfully(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.click_change_photo()

    profile_page.upload_profile_photo(
        PROFILE_IMAGE
    )

    assert (
        profile_page.is_image_uploaded_success_message_displayed()
    )


def test_save_button_enabled_after_uploading_photo(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.click_change_photo()

    profile_page.upload_profile_photo(
        PROFILE_IMAGE
    )

    # انتظر رسالة نجاح رفع الصورة
    assert (
        profile_page.is_image_uploaded_success_message_displayed()
    )

    # بعدها تحقق أن الزر أصبح Enabled
    assert (
        profile_page.is_save_button_enabled()
    )


def test_save_uploaded_profile_photo(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.click_change_photo()

    profile_page.upload_profile_photo(
        PROFILE_IMAGE
    )

    # انتظر رسالة نجاح رفع الصورة
    assert (
        profile_page.is_image_uploaded_success_message_displayed()
    )

    profile_page.click_save_changes()

    assert (
        profile_page.is_success_message_displayed()
    )