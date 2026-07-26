from pages.profile_page import ProfilePage


def test_save_button_disabled_without_changes(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    assert not profile_page.is_save_button_enabled()


def test_save_button_enabled_after_data_change(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    original_value = (
        profile_page.get_first_name_value()
    )

    profile_page.edit_first_name(
        original_value + "A"
    )

    assert profile_page.is_save_button_enabled()


def test_edit_first_name(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    original_value = (
        profile_page.get_first_name_value()
    )

    new_value = (
        original_value + "A"
    )

    profile_page.edit_first_name(
        new_value
    )

    assert (
        profile_page.get_first_name_value()
        == new_value
    )


def test_edit_last_name(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    original_value = (
        profile_page.get_last_name_value()
    )

    new_value = (
        original_value + "A"
    )

    profile_page.edit_last_name(
        new_value
    )

    assert (
        profile_page.get_last_name_value()
        == new_value
    )


def test_edit_address(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    original_value = (
        profile_page.get_address_value()
    )

    new_value = (
        original_value + " Test"
    )

    profile_page.edit_address(
        new_value
    )

    assert (
        profile_page.get_address_value()
        == new_value
    )


def test_success_message_displayed(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    original_value = (
        profile_page.get_first_name_value()
    )

    profile_page.edit_first_name(
        original_value + "A"
    )

    profile_page.click_save_changes()

    assert (
        profile_page.is_success_message_displayed()
    )


def test_edit_phone_number(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    original_value = (
        profile_page.get_phone_number_value()
    )

    new_value = (
        original_value + "1"
    )

    profile_page.edit_phone_number(
        new_value
    )

    assert (
        profile_page.is_save_button_enabled()
    )


def test_empty_first_name_validation(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.edit_first_name(
        ""
    )

    profile_page.click_save_changes()

    assert (
        profile_page.is_first_name_required_message_displayed()
    )


def test_empty_last_name_validation(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.edit_last_name(
        ""
    )

    profile_page.click_save_changes()

    assert (
        profile_page.is_last_name_required_message_displayed()
    )


def test_empty_phone_number_validation(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    profile_page.edit_phone_number(
        ""
    )

    profile_page.click_save_changes()

    assert (
        profile_page.is_phone_required_message_displayed()
    )


def test_address_maximum_length_validation(
        logged_in_user
):

    profile_page = ProfilePage(
        logged_in_user
    )

    long_address = (
        "A" * 500
    )

    profile_page.edit_address(
        long_address
    )

    profile_page.click_save_changes()

    assert (
        profile_page.is_address_maximum_length_message_displayed()
    )