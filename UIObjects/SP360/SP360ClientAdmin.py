import time
from selenium.webdriver.common.by import By
from UIObjects.BaseObject import BasePage


class SP360ClientAdmin(BasePage):
    device_hub_updates_tab = (By.XPATH, "//button[contains(text(),'DeviceHub Updates')]")
    dowload_mac_installer_btn = (By.XPATH, "//button[contains(text(),'Mac')]")
    dowload_windows_installer_btn = (By.XPATH, "//button[contains(text(),'Windows')]")
    save_btn = (By.XPATH, "//button[contains(text(),'Save')]")
    version_column = (By.XPATH, "//th[contains(text(),'Version')]")
    location_column = (By.XPATH, "//th[contains(text(),' Location ')]")
    view_release_notes_link = (By.XPATH, "//a[contains(text(),' View Release Notes')]")
    DH_update_txt = (By.XPATH, "//h2[contains(text(),'DeviceHub Updates')]")
    dh_current_version = (By.XPATH, "//h1[contains(@id,'mat-dialog-title')]")
    turnoff_updates_chkbox = (
        By.XPATH, "//*[contains(text(),'Turn off DeviceHub automatic update for all users')]//preceding::input[1]")
    dh_Release_notes_header = (By.XPATH, "//h1[contains(text(),'DeviceHub Release Notes')]")
    refresh_page = (By.XPATH, "//*[contains(text(), 'Refresh')]//ancestor::button")
    released_date = (By.XPATH, "//span[contains(text(),' Released')]//following-sibling::span")
    close_btn = (By.XPATH, "//button[@class='mat-ripple btn-close']")
    dh_update_text = (By.XPATH,
                      "//*[contains(text(),'Whenever a new version of DeviceHub is released, you have the option to either send updates automatically to the user or disable the automatic updates altogether.')]")
    show_mydevice_chkbox = (By.XPATH, "//*[contains(text(),'Show only my devices')]//preceding::input[1]")

    def __init__(self, app_config, driver, custom_logger):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(SP360ClientAdmin, self).__init__(driver)

    def check_device_hub_updates_tab(self):
        flg = self.wait_element(*self.device_hub_updates_tab)
        return flg

    def verify_location_column(self):
        flg = self.wait_element_till_time_limit(10, *self.location_column)
        return flg

    def verify_version_column(self):
        flg = self.wait_element_till_time_limit(10, *self.version_column)
        return flg

    def click_DH_updates_tab(self):
        self. wait_for_element_to_be_clickable(*self.device_hub_updates_tab)
        self.click_using_js(*self.device_hub_updates_tab)
        time.sleep(2)

    def verify_dh_update_popup_page(self):
        return self.wait_element(*self.DH_update_txt)

    def verify_current_version_dh_in_update_page(self, app_config):
        self.wait_element(*self.dh_current_version)
        config_dh_version = ((app_config.dh_common_config["DH_new_version"].split())[1]).replace('v', '')
        ui_dh_current_version = (
            By.XPATH, "//h1[contains(text(),'" + config_dh_version + "')]")
        return self.wait_element(*ui_dh_current_version)

    def click_windows_installer_button(self):
        self.custom_logger.info("windows installer button is displayed")
        self.wait_element(*self.dowload_windows_installer_btn)
        self.click_using_js(*self.dowload_windows_installer_btn)

    def click_mac_installer_button(self):
        self.custom_logger.info("MAC installer button is displayed")
        self.wait_element(*self.dowload_mac_installer_btn)
        self.click_using_js(*self.dowload_mac_installer_btn)

    def return_length_of_windows(self, driver):
        multi_windows = driver.window_handles
        return len(multi_windows)

    def click_release_notes_link(self):
        self.click_using_js(*self.view_release_notes_link)
        self.custom_logger.info("Release notes Link is clicked")

    def verify_release_notes_page(self):
        self.switch_to_first_child_window(*self.dh_Release_notes_header)
        return self.wait_element(*self.dh_Release_notes_header)

    def switch_to_first_child_window_and_close(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()

    def verify_turn_off_updates_check_Box_present(self):
        return self.wait_element(*self.turnoff_updates_chkbox)

    def click_turn_off_update(self):
        self.wait_element(*self.turnoff_updates_chkbox)
        if not self.find_element(*self.turnoff_updates_chkbox).is_selected():
            self.click_using_js(*self.turnoff_updates_chkbox)

    def verify_updates_turned_off(self):
        self.wait_element(*self.turnoff_updates_chkbox)
        turn_off_update_chk_box = self.find_element(*self.turnoff_updates_chkbox).is_selected()
        if not turn_off_update_chk_box:
            self.click_using_js(*self.turnoff_updates_chkbox)
        chkbox_selected = self.find_element(*self.turnoff_updates_chkbox).is_selected()
        if not turn_off_update_chk_box:
            self.click_save_btn()
        else:
            self.click_closeX()
        return chkbox_selected

    def verify_updates_turned_on(self):
        turn_off_update_chk_box = self.find_element(*self.turnoff_updates_chkbox).is_selected()
        if turn_off_update_chk_box:
            self.click_using_js(*self.turnoff_updates_chkbox)
        chkbox_selected = self.find_element(*self.turnoff_updates_chkbox).is_selected()
        if turn_off_update_chk_box:
            self.click_save_btn()
        else:
            self.click_closeX()
        return chkbox_selected

    def click_save_btn(self):
        self.wait_element(*self.released_date)
        self.click_using_js(*self.save_btn)
        self.custom_logger.info("updates turn off and clicked don save button")

    def click_turn_on_update(self):
        if self.find_element(*self.turnoff_updates_chkbox).is_selected():
            self.wait_element(*self.turnoff_updates_chkbox)
            self.click_using_js(*self.turnoff_updates_chkbox)

    def select_show_mydevice_chck_box(self):
        self.wait_element(*self.show_mydevice_chkbox)
        if not self.find_element(*self.show_mydevice_chkbox).is_selected():
            self.wait_element(*self.show_mydevice_chkbox)
            self.click_using_js(*self.show_mydevice_chkbox)
            return True

    def uncheck_show_mydevice_chck_box(self):
        self.wait_element(*self.show_mydevice_chkbox)
        if self.find_element(*self.show_mydevice_chkbox).is_selected():
            self.wait_element(*self.show_mydevice_chkbox)
            self.click_using_js(*self.show_mydevice_chkbox)
            return True

    def verify_release_update_date_present(self):
        self.wait_element(*self.released_date)
        released_date = self.find_element(*self.released_date).text
        if released_date != "":
            return True
        else:
            return False

    def click_closeX(self):
        try:
            self.wait_element(*self.close_btn)
            self.click_using_js(*self.close_btn)
        except:
            self.custom_logger("Close button is not present")

    def verify_dhupdate_text_visible(self):
        return self.wait_element(*self.dh_update_text)

    def check_download_status_and_close_the_open_child_window(self, my_device_page, length_window, installer_name):
        if length_window == 1:
            my_device_page.check_dh_download_status(self.app_config.dh_common_config[installer_name])
        elif length_window > 1:
            self.switch_to_first_child_window_and_close()
            self.switch_to_parent_window()
