import time
from selenium.webdriver.common.by import By
from FrameWorkUtilities.common_utils import common_utils
from UIObjects.BaseObject import BasePage


class FedrampMyDevicesPageObjects(BasePage):
    my_devices_header = (By.XPATH, "//h1[contains(text(), 'My Devices')]")
    device_name = (By.XPATH, "//p-table[@datakey ='devicehubName']/div/div/table/tbody/tr/td[2]")
    download_dh = (By.XPATH, "//button[contains(text(), 'Download DeviceHub Installer')]")
    Windows_installer = (By.XPATH, "//a[contains(text(), 'Windows')]")
    Mac_installer = (By.XPATH, "//a[contains(text(),'Mac')]")
    activate_dh = (By.XPATH, "//button[contains(text(),'Activate DeviceHub')]")
    activate_dh_pop_up_btn = (By.XPATH, "//mat-dialog-actions/button[contains(text(),'Activate')]")
    download_dh_pop_up_Btn = (By.XPATH, "//mat-dialog-actions/button[contains(text(),' Download DeviceHub ')]")
    successful_dh_msg = (By.XPATH, "//*[contains(text(),'DeviceHub registered successfully!')]")
    refresh_page = (By.XPATH, "//*[contains(text(), 'Refresh')]//ancestor::button")
    first_row_under_devices = (By.XPATH, "//table[@role='table']/tbody/tr[1]")
    close_and_continue_Btn = (By.XPATH, "//button[text()='Close And Continue']")

    def __init__(self, app_config, driver, custom_logger):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(FedrampMyDevicesPageObjects, self).__init__(driver)

    def check_my_device_header_exists(self):
        flg = self.wait_element(*self.my_devices_header)
        return flg

    def get_my_devices_header(self):
        time.sleep(2)
        return self.find_element(*self.my_devices_header)

    def check_activate_dh_btn_exists(self):
        flg = self.wait_for_element_to_be_clickable(*self.activate_dh)
        return flg

    def click_on_activate_dh(self):
        self.click_using_js(*self.activate_dh)

    def check_activate_button_on_dh_pop_up(self):
        flg = self.wait_element(*self.activate_dh_pop_up_btn)
        return flg

    def check_downloadDH_button_on_dh_pop_up(self):
        flg = self.wait_element(*self.download_dh_pop_up_Btn)
        return flg

    def click_activate_dh_pop_up(self):
        self.click_using_js(*self.activate_dh_pop_up_btn)

    def check_dh_name_in_table(self, dh_name):
        results = {}
        device_nm = self.find_elements(*self.device_name)
        for index in range(0, len(device_nm)):
            if device_nm[index].text == dh_name:
                status_xpath = (By.XPATH,
                                "(//p-table[@datakey ='devicehubName']/div/div/table/tbody/tr/td[2])[{arg1}]//ancestor::tr/td["
                                "6]/span".format(arg1=index + 1))

                dh_status = self.find_element(*status_xpath)
                results['status'] = True
                results['dh_status'] = dh_status.text
                self.scroll_to_element(*status_xpath)
                time.sleep(2)
                return results

        results['status'] = False
        results['dh_status'] = "Not Present"

    def check_download_dh_btn_exists(self):
        flg = self.wait_for_element_to_be_clickable(*self.download_dh)
        return flg

    def click_on_download_dh_installer(self):
        self.click_using_js(*self.download_dh)

    def wait_for_devichub_installer_page(self):
        flg = self.wait_element(*self.Windows_installer)
        return flg

    def click_on_windows_installer(self):
        self.click_using_js(*self.Windows_installer)
        self.custom_logger.info("Windows Installer is Clicked")
        time.sleep(5)

    def check_dh_download_status(self, file_name):
        common_utils.check_download_complete(file_name)

    def check_dh_activated(self):
        self.switch_to_first_child_window(*self.successful_dh_msg)

    def refresh_manage_device_page(self):
        self.wait_element_till_time_limit(60,*self.refresh_page)
        self.click_using_js(*self.refresh_page)

    def wait_for_first_device_after_refresh(self):
        self.wait_element(*self.first_row_under_devices)

    def check_DeviceHub_Installer_header_exists(self):
        flg = self.wait_element(*self.my_devices_header)
        return flg

    def check_windows_installer_Button_exists(self):
        flg = self.wait_element(*self.Windows_installer)
        return flg

    def check_mac_installer_Button_exists(self):
        flg = self.wait_element(*self.Mac_installer)
        return flg

    def verify_DH_RegistrationMsg(self):
        return self.verify_if_element_is_visible(*self.successful_dh_msg)

    def verify_CloseAndContinue_button(self):
        return self.verify_if_element_is_visible(*self.close_and_continue_Btn)

    def clickon_close_and_continue_button(self):
        self.click_using_js(*self.close_and_continue_Btn)
        self.switch_to_parent_window()
