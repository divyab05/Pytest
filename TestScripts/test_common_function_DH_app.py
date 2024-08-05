import os
import sys
import time
import pyautogui
import pytest
from hamcrest import assert_that, equal_to
from pywinauto import Application
from TestScripts.test_common_function import Test_common_function
from UIObjects.DeviceHubObjects import DeviceHubObjectsClass


@pytest.fixture()
def resource(app_config):
    req = DeviceHubObjectsClass(app_config)
    yield req


class Test_common_function_DH_app(Test_common_function):

    # This Function is used to verify Context Menu Option
    def verify_About_context_menu(self, resource, app_config, custom_logger, get_product_name):
        get_pop_up_text = resource.get_about_popup_text(custom_logger)
        if get_product_name == 'fedramp':
            DH_version_text = app_config.dh_common_config["Fedramp_DH_version"]
        else:
            DH_version_text = app_config.dh_common_config["DH_version"]
        copy_right_text = app_config.dh_config["copy_right_text"]
        assert_that(get_pop_up_text.__contains__(DH_version_text), DH_version_text + " is not displayed as version")
        custom_logger.info(DH_version_text + "is displayed as version")
        assert_that(get_pop_up_text.__contains__(copy_right_text), copy_right_text + " is not displayed")
        custom_logger.info(copy_right_text + "is displayed")
        DH_text = app_config.dh_config["DH_descriptive_text"]
        assert_that(get_pop_up_text.__contains__(DH_text), DH_text + " is not displayed")
        custom_logger.info(DH_text + "is displayed")
        assert_that(resource.get_about_menu_Ok_button(), "Ok button is not present")
        resource.get_about_menu_Ok_button().click_input(button='left')
        custom_logger.info("Ok button is clicked to close the popup")

    # This function is used to Verify DH logs
    def check_log_icon(self, resource, app_config, custom_logger):
        curr_date = resource.click_on_logs_return_current_date(custom_logger)
        logs_explorer_window = resource.get_logs_explorer_window()
        assert_that(logs_explorer_window.exists(), "Not Navigated to logs folder")
        custom_logger.info("Navigated to logs folder")
        assert_that((os.path.isfile(app_config.dh_common_config['log_file_path'] + '\\dha-' + curr_date + '.log')),
                    "Dha file is not displayed")
        custom_logger.info("Dha file is displayed in logs")
        resource.get_close_button().click()
        if sys.getwindowsversion().build < 22000:
            resource.click_on_hidden_tray()

    # This function is used to Reconnect DH
    def reconnect_device_hub(self, app_config, resource, custom_logger):
        resource.right_click_notification_tray()
        custom_logger.info("Context menu is displayed")
        context_menu = resource.get_device_hub_context_menu_obj()
        resource.get_context_menu_options(app_config.dh_config["DH_object_Reconnect"], context_menu).click_input(
            button='left')
        custom_logger.info("Reconnect menu is Clicked")
        resource.click_on_hidden_tray()
        time.sleep(3)
        resource.wait_for_DH_to_be_online()
        resource.click_on_hidden_tray()

    # This function is used to Exit DH
    def check_exit_device_hub(self, app_config, resource, custom_logger):
        resource.click_exit_from_context_menu(custom_logger)
        self.wait_for_window_to_appear(resource.get_device_hub_offline_notification(), 20)
        assert_that(resource.get_device_hub_offline_notification().exists(),
                    "DH is Offline notification is not displayed")
        custom_logger.info("DH is Offline notification is displayed")
        resource.click_on_hidden_tray()

    def replace_isGenerated_val_in_dhaMQTConfig(self, filepath, txt_to_replace, txt_replaced):
        self.replace_txt_in_a_file(filepath, txt_to_replace, txt_replaced)

    def check_deviceHub_context_menu(self, resource, app_config, custom_logger):
        resource.right_click_notification_tray()
        custom_logger.info("Context menu is displayed")
        time.sleep(2)
        context_menu_array = app_config.dh_config["context_menu_array"]
        context_menu = resource.get_device_hub_context_menu_obj()
        for menu_options in context_menu_array:
            assert_that(resource.get_context_menu_options(menu_options, context_menu),
                        menu_options + " is not present in context menu")
            custom_logger.info(menu_options + " exist in context menu")
        resource.click_on_hidden_tray()

    def validate_check_for_update(self, resource, custom_logger, app_config):
        check_for_update_dialog = resource.get_check_for_update_popup(custom_logger)
        self.wait_for_window_to_appear(resource.get_check_for_update_dialog(), 20)
        assert_that(check_for_update_dialog.exists(), "Update dialog box is not  present")
        text_update = check_for_update_dialog.window_text()
        assert_that(text_update.__contains__(app_config.dh_config["check_update_dlg_text"]),
                    text_update + " is not displayed as expected")
        custom_logger.info(text_update + " is not displayed as expected")
        resource.click_check_for_update_ok_btn()

    def verify_DH_Version_is_updated_from_old_to_new(self, resource, app_config, custom_logger):
        get_pop_up_text = resource.get_about_popup_text(custom_logger)
        DH_version_text = app_config.dh_common_config["DH_new_version"]
        copy_right_text = app_config.dh_config["copy_right_text"]
        assert_that(get_pop_up_text.__contains__(DH_version_text), DH_version_text + " is displayed as version")
        custom_logger.info(DH_version_text + "is displayed as version")
        assert_that(get_pop_up_text.__contains__(copy_right_text), copy_right_text + " is displayed")
        custom_logger.info(copy_right_text + "is displayed")
        assert_that(resource.get_about_menu_Ok_button(), "Ok button is present")
        resource.get_about_menu_Ok_button().click_input(button='left')
        custom_logger.info("Ok button is clicked to close the popup")

    def install_deviceHub(self, get_env, app_config, resource, custom_logger, get_product_name, get_language):
        app = ""
        installer_name = app_config.dh_config['installer_name']
        installer_path = os.getcwd() + "\\downloads\\" + installer_name
        Application().start('explorer.exe {arg1}'.format(arg1=installer_path))
        time.sleep(10)
        if get_product_name == "sp360canada":
            app = Application().connect(title_re="Installer Language", class_name='#32770')
            if get_language == "french":
                pyautogui.keyDown('down')
            self.wait_for_window_to_appear(app.DeviceHub.child_window(title="OK", class_name="Button"), 60)
            resource.click_ok_btn_installer_lang_popup()
            time.sleep(5)
        elif get_product_name == "sp360commercial":
            app = Application().connect(title_re="DeviceHub", class_name='#32770')

        if get_language == "french":
            dhapp = Application().connect(title_re="DeviceHub", class_name='#32770')
            self.wait_for_window_to_appear(app.DeviceHub.child_window(title="&Installer", class_name="Button"), 30)
            # app.window(title_re="Installer Language", class_name='#32770').print_control_identifiers()
            dhapp.DeviceHub.child_window(title='&Installer', class_name="Button").click()
            custom_logger.info("Clicked on Install Button")
            self.wait_for_window_to_appear(app.DeviceHub.child_window(title="&Fermer", class_name="Button"), 90)
            dhapp.DeviceHub.child_window(title="&Fermer", class_name="Button").click()
            custom_logger.info("Clicked on Finish Button")
            time.sleep(2)
            resource.wait_for_DH_to_be_online()
            resource.click_on_hidden_tray()
        elif get_language == "english":
            dhapp = Application().connect(title_re="DeviceHub", class_name='#32770')
            self.wait_for_window_to_appear(app.DeviceHub.child_window(title="&Install", class_name="Button"), 30)
            # app.window(title_re="Installer Language", class_name='#32770').print_control_identifiers()
            dhapp.DeviceHub.child_window(title='&Install', class_name="Button").click()
            custom_logger.info("Clicked on Install Button")
            self.wait_for_window_to_appear(app.DeviceHub.child_window(title="&Finish", class_name="Button"), 90)
            dhapp.DeviceHub.child_window(title="&Finish", class_name="Button").click()
            custom_logger.info("Clicked on Finish Button")
            time.sleep(2)
            resource.wait_for_DH_to_be_online()
            resource.click_on_hidden_tray()

    def click_check_for_update(self, resource, app_config, get_env, custom_logger, get_driver,
                               test_data):
        recovery_mechanism_update = test_data['Recovery_mechanism_update']
        # note to run recovery mechanism update the column Recovery_mechanism_update in the excel sheet
        resource.move_cursor()
        if recovery_mechanism_update == 'no':
            update_txt = app_config.dh_config["DH_object_check_for_update"]  # Check for Update
        else:
            update_txt = app_config.dh_config["update_txt_recovery_mechanism"]  # New DeviceHub version available.

        resource.click_notification_tray_update(app_config)
        custom_logger.info("Context menu is displayed")
        context_menu = resource.get_device_hub_context_menu_obj()
        resource.get_context_menu_options(update_txt, context_menu).click_input(button='left')
        custom_logger.info("Check for update menu is clicked")

        check_for_update_dialog = resource.get_check_for_update_dialog()
        self.wait_for_window_to_appear(resource.get_check_for_update_dialog(), 20)
        assert_that(check_for_update_dialog.exists(), "Update DH Dialog is not  present")
        text_update = check_for_update_dialog.window_text()
        assert_that(text_update.__contains__(app_config.dh_config["check_update_dlg_latest_version"]),
                    text_update + " is not displayed as expected")
        custom_logger.info(text_update + " is  displayed as expected")
        resource.click_check_for_update_ok_btn()
        win_notification = resource.get_system_notification_obj()
        time.sleep(5)
        self.wait_for_window_to_appear(resource.get_dh_update_in_progress_norification(win_notification),
                                       60)
        assert_that(resource.get_dh_update_in_progress_norification(win_notification).exists(),
                    "DH update failed")
        custom_logger.info("DeviceHub updates are in progress")
        time.sleep(4)
        text_update = resource.get_successful_update_dialog().window_text()
        assert_that(text_update.__contains__(app_config.dh_config["successful_updation_msg"]),
                    "Update is not completed")
        resource.click_ok_btn_after_update()
        resource.wait_for_DH_to_be_online()
        resource.click_on_hidden_tray()

    def validate_cancel_update(self, resource, custom_logger, app_config):
       # check_for_update_dialog = resource.get_check_for_update_popup(custom_logger)
        resource.click_notification_tray_update(app_config)
        custom_logger.info("Context menu is displayed")
        context_menu = resource.get_device_hub_context_menu_obj()
        resource.get_context_menu_options(app_config.dh_config["DH_object_check_for_update"],
                                          context_menu).click_input(button='left')
        check_for_update_dialog = resource.get_check_for_update_dialog()
        self.wait_for_window_to_appear(resource.get_check_for_update_dialog(), 20)
        assert_that(check_for_update_dialog.exists(), "Update Dialog box is not present")
        text_update = check_for_update_dialog.window_text()
        assert_that(text_update.__contains__(app_config.dh_config["check_update_dlg_latest_version"]),
                    text_update + " is not displayed as expected")
        custom_logger.info(text_update + " is displayed as expected")
        resource.click_cancel_update_dialog()
        custom_logger.info("Cancel button is clicked")
        win_notification = resource.get_system_notification_obj()
        assert_that(not resource.get_dh_update_in_progress_norification(win_notification).exists(),
                    "DH Updates failed notification is not displayed")

    def uninstall_DH(self, app_config, resource, custom_logger):
        try:
            app = Application().connect(title_re=app_config.dh_config["DH_uninstaller_window_obj"], class_name='#32770')
            uninstall = app.window(title_re=app_config.dh_config["DH_uninstaller_window_obj"], class_name='#32770')
            uninstall.child_window(title='&' + app_config.dh_config["Uninstall_obj"], class_name="Button").click()
            custom_logger.info("Clicked on UnInstall Button")
            dh_obj = app.DeviceHub
            resource.get_dh_uninstallation_progress_window(dh_obj)
            self.wait_for_window_to_appear(
                uninstall.child_window(title='&' + app_config.dh_config["finish_obj"], class_name="Button"), 90)
            uninstall.child_window(title='&' + app_config.dh_config["finish_obj"], class_name="Button").click()
            custom_logger.info("Clicked on Finish Button")
            time.sleep(3)
        except:
            if resource.check_installer_window_exists():
                resource.click_ok_btn_installer_lang_popup()
                time.sleep(4)
            app = Application().connect(title_re=app_config.dh_config["DH_uninstaller_window_obj"], class_name='#32770')
            app.DeviceHub.child_window(title='&' + app_config.dh_config["Uninstall_obj"], class_name="Button").click()
            custom_logger.info("Clicked on UnInstall Button")
            dh_obj = app.DeviceHub
            resource.get_dh_uninstallation_progress_window(dh_obj)
            self.wait_for_window_to_appear(
                app.DeviceHub.child_window(title='&' + app_config.dh_config["finish_obj"], class_name="Button"), 120)
            app.DeviceHub.child_window(title='&' + app_config.dh_config["finish_obj"], class_name="Button").click()
            custom_logger.info("Clicked on Finish Button")
            time.sleep(3)
