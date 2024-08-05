import os
import time
import pytest
from pytest_check import check

from ConfigFiles import common_config
from TestScripts.test_common_function import Test_common_function
from UIObjects.SP360.SP360ClientAdmin import SP360ClientAdmin
from hamcrest import assert_that
from UIObjects.SP360.SP360MyDevicesPageObjects import SP360MyDevicesObjectsClass


class Test_client_Admin(Test_common_function):

    @pytest.mark.clientAdmin
    @pytest.mark.order(34)
    def test35_verify_clientAdmin_device_page(self, get_env, app_config, setup_dh, custom_logger, get_driver):
        self.click_on_mydevice_header(setup_dh, custom_logger)
        obj_clientAdmin = SP360ClientAdmin(app_config, get_driver, custom_logger)
        assert_that(obj_clientAdmin.check_device_hub_updates_tab(),
                    "Device Hub Update Tab is not present for client Admin")
        custom_logger.info("DH update tab is present")
        obj_clientAdmin.uncheck_show_mydevice_chck_box()
        check.is_true(obj_clientAdmin.verify_version_column(), "Version Column is not Present")
        custom_logger.info("Version is present for client Admin in my device page")
        check.is_true(obj_clientAdmin.verify_location_column(), "Location Column is not Present")
        custom_logger.info("Location column is present for client Admin in my device page")

    @pytest.mark.clientAdmin
    @pytest.mark.order(36)
    def test_36_verify_clientAdmin_installer_is_downloadable(self, get_env, app_config, setup_dh, custom_logger,
                                                             get_driver):
        my_device_page = SP360MyDevicesObjectsClass(app_config, get_driver, custom_logger)
        self.click_on_mydevice_header(setup_dh, custom_logger)
        obj_clientAdmin = SP360ClientAdmin(app_config, get_driver, custom_logger)
        obj_clientAdmin.click_DH_updates_tab()
        custom_logger.info(" Clicked on DH update tab")
        assert_that(obj_clientAdmin.verify_dh_update_popup_page(), "DH Update popup page is not displayed")
        custom_logger.info("DH Update popup page is displayed")
        assert_that(obj_clientAdmin.verify_current_version_dh_in_update_page(app_config),
                    "Current version of Dh is not latest")
        obj_clientAdmin.click_windows_installer_button()
        time.sleep(2)
        length_window = obj_clientAdmin.return_length_of_windows(get_driver)
        check.is_false((length_window > 1), "Windows installer is not getting downloaded")
        obj_clientAdmin.check_download_status_and_close_the_open_child_window(my_device_page, length_window,
                                                                              "msi_windows_installer_name")
        installer_path = os.getcwd() + "\\downloads\\" + common_config.dh_app_common_config_windows[
            'msi_windows_installer_name']
        obj_clientAdmin.delete_installer(installer_path)
        obj_clientAdmin.click_mac_installer_button()
        time.sleep(2)
        length_window = obj_clientAdmin.return_length_of_windows(get_driver)
        check.is_false((length_window > 1), "Mac installer is not getting downloaded")
        obj_clientAdmin.check_download_status_and_close_the_open_child_window(my_device_page, length_window,
                                                                              "mac_installer_name")
        custom_logger.info("The MAC installer is downloaded successfully")
        installer_path = os.getcwd() + "\\downloads\\" + common_config.dh_app_common_config_windows[
            'mac_installer_name']
        obj_clientAdmin.delete_installer(installer_path)
        obj_clientAdmin.click_closeX()

    @pytest.mark.clientAdmin
    @pytest.mark.order(37)
    def test37_verify_clientAdmin_dhupdate_popup(self, get_env, app_config, setup_dh, custom_logger, get_driver):
        self.click_on_mydevice_header(setup_dh, custom_logger)
        obj_clientAdmin = SP360ClientAdmin(app_config, get_driver, custom_logger)
        obj_clientAdmin.click_DH_updates_tab()
        custom_logger.info(" Clicked on DH update tab")
        assert_that(obj_clientAdmin.verify_dh_update_popup_page(), "DH Update popup page is not displayed")
        custom_logger.info("DH Update popup page is displayed")
        check.is_true(obj_clientAdmin.verify_current_version_dh_in_update_page(app_config),
                      "Current version of Dh is not latest")
        custom_logger.info("current dh version is displayed")
        check.is_true(obj_clientAdmin.verify_release_update_date_present(), "Release date is Present")
        custom_logger.info("Released date is present")
        check.is_true(obj_clientAdmin.verify_turn_off_updates_check_Box_present(),
                      "Turn off DH update check box is not present")
        custom_logger.info("Turn off updates check box is displayed")
        check.is_true(obj_clientAdmin.verify_dhupdate_text_visible(), "Dh update text is not present as expected")
        obj_clientAdmin.click_release_notes_link()
        check.is_true(obj_clientAdmin.verify_release_notes_page(), "Release notes page is not displayed")
        custom_logger.info("Release notes page is displayed")
        obj_clientAdmin.close_current_window()
        obj_clientAdmin.switch_to_parent_window()
        obj_clientAdmin.click_closeX()

    @pytest.mark.clientAdmin
    @pytest.mark.order(38)
    def test38_verify_clientAdmin_turnoff_turnon_updates(self, get_env, app_config, setup_dh, custom_logger,
                                                         get_driver):
        self.click_on_mydevice_header(setup_dh, custom_logger)
        obj_clientAdmin = SP360ClientAdmin(app_config, get_driver, custom_logger)
        obj_clientAdmin.click_DH_updates_tab()
        custom_logger.info(" Clicked on DH update tab")
        assert_that(obj_clientAdmin.verify_dh_update_popup_page(), "DH Update popup page is not displayed")
        custom_logger.info("DH Update popup page is displayed")
        check.is_true(obj_clientAdmin.verify_current_version_dh_in_update_page(app_config),
                      "Current version of Dh is not latest")
        check.is_true(obj_clientAdmin.verify_turn_off_updates_check_Box_present(),
                      "Turn off DH update check box is not present")
        custom_logger.info("Turn off updates check box is displayed")
        check.is_true(obj_clientAdmin.verify_updates_turned_off(), "DH Updates are not turned off")
        obj_clientAdmin.click_DH_updates_tab()
        check.is_true(obj_clientAdmin.verify_current_version_dh_in_update_page(app_config),
                      "Current version of Dh is not latest")
        check.is_false(obj_clientAdmin.verify_updates_turned_on(), "DH Updates are not turned on")
        obj_clientAdmin.click_closeX()

    @pytest.mark.clientAdmin
    @pytest.mark.order(38)
    def test_verify_show_my_device_functionality(self, get_env, app_config, setup_dh, custom_logger,
                                                 get_driver):
        self.click_on_mydevice_header(setup_dh, custom_logger)
        obj_clientAdmin = SP360ClientAdmin(app_config, get_driver, custom_logger)
        obj_clientAdmin.select_show_mydevice_chck_box()
        time.sleep(5)
        check.is_false(obj_clientAdmin.verify_version_column(),
                       "Version Column is Present when show my device check box is clicked")
        custom_logger.info("Version is present for client Admin in my device page")
        check.is_false(obj_clientAdmin.verify_location_column(),
                       "Location Column is not Present when show my device check box is clicked")
        custom_logger.info("Location column is present for client Admin in my device page")
        obj_clientAdmin.uncheck_show_mydevice_chck_box()



