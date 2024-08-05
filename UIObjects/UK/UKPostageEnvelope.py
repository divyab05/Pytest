import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from FrameWorkUtilities.common_utils import common_utils
from UIObjects.BaseObject import BasePage


class UKPostageEnvelope(BasePage):
    # scale
    custom_stamp = (By.XPATH, "//label[contains(text(),'Custom Stamp')]")
    get_weight_btn = (By.XPATH, "//i[@class='pbi-icon-mini pbi-scale custom-size']")
    select_scale_drpdown = (By.XPATH, "//div[@aria-label='Scale options']/button")
    fetching_weight_txt = (By.XPATH, "//*[contains(text(), ' Fetching Weight.. ')]")
    set_scale_to_zero_btn = (By.XPATH, "//i[@class='pbi-icon-mini pbi-undo']//parent::button")
    zeroing_scale_txt = (By.XPATH, "//*[contains(text(),'Zeroing Scale')]")

    # UK
    postage_envelope = (By.XPATH, "//h1[contains(text(),'Print Postage')]")
    postage_add_to_envelope_btn = (By.XPATH, "//button[contains(text(),'Add to Envelope')]")
    postage_delete_envelope = (By.XPATH, "//button[contains(text(),'Delete All')]")
    postage_print_options_btn = (By.XPATH, "//button[contains(text(),'Print Options')]")
    postage_print_combo_box = (
        By.XPATH, "//h2[contains(text(),'Check printer compatibility') or contains(text(),'Print Options')]//following::input[1]")
    postage_test_print_btn = (By.XPATH, "//button[contains(text(),'Test Print')]")
    postage_print_btn = (By.XPATH, "//h2[contains(text(),'Print Options')]//following::button[contains(text(),'Print')]")
    postage_print_option_print_btn = (
        By.XPATH, "//h2[contains(text(), 'Print Options')] // following::button[contains(text(), 'Print')]")
    postage_toaster_msg = (
        By.XPATH,
        "//div[contains(@aria-label,'Selected postage have been removed due to change in postage type')] | //p[contains(text(),'Processing postage')]")
    # postage_toaster_msg_processing_postage = (By.XPATH, "//p[contains(text(),'Processing postage')]")
    postage_print_postage_btn = (By.XPATH, "//button[contains(text(),'Print Postage')]")
    postage_signed_for_services_radio_btn = (
        By.XPATH, "//span[contains(text(),'Signed For Services')]//preceding::input[1]")

    postage_standard_services_radio_btn = (
        By.XPATH, "//span[contains(text(),'Standard Services')]//preceding::input[1]")
    postage_delete_address = (By.XPATH, "//i[@class='pbi-icon-mini pbi-trash']")
    close_symbol = (By.XPATH, "//button[contains(@class,'mat-ripple close')]")
    select_quantity = (By.XPATH, "//select[@id='quantity']")
    preview_test_print = (By.XPATH, "//button[contains(text(),' Preview Test Print')]")
    print_test_print_btn = (By.XPATH, "//button[contains(text(),' Print Test Print')]")
    done_button = (By.XPATH, "//button[contains(text(),'Done')]")
    c5_envelope_size = (By.XPATH, "//button/span[contains(text(),'C5')]")  # Updated
    c5_envelope_size_priewpage = (By.XPATH, "//div/input[@id='mat-radio-13-input']")  # Updated
    txt_no_scale_found_msg = (By.XPATH, "//h2[contains(text(),'No scale driver found')]")

    def __init__(self, app_config, driver, custom_logger):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(UKPostageEnvelope, self).__init__(driver)

    ####################UK#####################

    def check_print_postage_envelope_header_exists(self):
        flg = self.wait_element_till_time_limit(34, *self.postage_add_to_envelope_btn)
        return flg

    def select_postage_envelope_quantity(self):
        self.wait_element_till_time_limit(40, *self.select_quantity)
        Select(self.find_element(*self.select_quantity)).select_by_value("1")
        self.custom_logger.info("Quantity is selected")

    def check_postage_add_to_envelope_btn_exists(self):
        self.wait_element_till_time_limit(30, *self.postage_add_to_envelope_btn)

    def click_on_postage_add_to_envelope_btn(self):
        self.click_using_js(*self.postage_add_to_envelope_btn)
        self.custom_logger.info("Add to sheet button is clicked")

    def click_preview_test_print(self):
        self.wait_element(*self.preview_test_print)
        self.click_using_js(*self.preview_test_print)

    def click_Print_test_print_btn(self):
        self.wait_element(*self.print_test_print_btn)
        self.click_using_js(*self.print_test_print_btn)

    def check_postage_row_added(self):
        self.custom_logger.info("Check Row exists")
        flg = self.wait_element(*self.postage_delete_envelope)
        return flg

    def postage_check_print_options_btn(self):
        return self.wait_for_element_to_be_clickable(*self.postage_print_options_btn)

    def postage_click_on_print_options(self):
        self.click_using_js(*self.postage_print_options_btn)
        self.custom_logger.info("Print Option link is clicked")

    def postage_check_printer_combo_box(self):
        flg = self.wait_element_till_time_limit(30, *self.postage_print_combo_box)
        return flg

    def postage_click_on_printer_combo_box(self):
        self.click_using_js(*self.postage_print_combo_box)
        self.custom_logger.info("Click on printer combo box")

    def enter_printer_name(self, test_data):
        printer_name = test_data['PrinterName']
        self.wait_element(*self.postage_print_combo_box)
        self.find_element(*self.postage_print_combo_box).click()
        self.find_element(*self.postage_print_combo_box).send_keys(printer_name)

    def postage_click_on_test_print_btn(self):
        self.custom_logger.info("Click on test print btn")
        self.wait_element(*self.postage_test_print_btn)
        self.click_using_js(*self.postage_test_print_btn)

    def click_print_postage_button(self):
        self.custom_logger.info("Click on Postage print Button")
        self.wait_element(*self.postage_print_postage_btn)
        self.click_using_js(*self.postage_print_postage_btn)

    def postage_click_on_print_button(self):
        self.wait_element(*self.postage_print_btn)
        self.click_using_js(*self.postage_print_btn)

    def postage_click_print_option_print_button(self):
        self.wait_element(*self.postage_print_option_print_btn)
        self.click_using_js(*self.postage_print_option_print_btn)

    def verify_toaster_message(self):
        return self.wait_element_till_time_limit(40, *self.postage_toaster_msg)

    def click_on_postage_signed_for_services_radio_btn(self):
        self.wait_element(*self.postage_signed_for_services_radio_btn)
        self.click_using_js(*self.postage_signed_for_services_radio_btn)

    def click_on_postage_standard_services_radio_btn(self):
        self.wait_element(*self.postage_standard_services_radio_btn)
        self.click_using_js(*self.postage_standard_services_radio_btn)

    def click_postage_delete_address(self):
        self.wait_element(*self.postage_delete_address)
        self.click_using_js(*self.postage_delete_address)

    def postage_select_printer_from_dropdown(self, device_name, test_data):
        try:
            printer_name = test_data['PrinterName']
            printer_path = (By.XPATH,
                            "//div[@role='group']/span[contains(text(),{arg1}{arg2}{arg3})]//parent::div//following-sibling::div/span[text()={arg4}{arg5}{arg6}]"
                            .format(arg1="'", arg2=device_name, arg3="'", arg4="'", arg5=printer_name, arg6="'"))
            time.sleep(3)
            self.scroll_to_element(*printer_path)
            self.click_using_js(*printer_path)
            self.press_tab()
            self.custom_logger.info("Printer is selected and clicked")
            return True
        except:
            self.click_using_js(*self.close_symbol)
            self.custom_logger.info("Printer is not selected or not in the list")
            return False

    def postage_click_test_print(self):
        flg = self.postage_check_print_options_btn()
        if flg:
            self.postage_click_on_test_print_btn()
            return flg
        else:
            return flg

    def select_printer(self, get_env, test_data):
        sys_name = common_utils.get_system_name(get_env)
        self.postage_check_printer_combo_box()
        self.enter_printer_name(test_data)
        selected_printer = self.postage_select_printer_from_dropdown(sys_name, test_data)
        if selected_printer:
            return True
        else:
            return False

    def postage_click_actual_print(self):
        self.postage_check_print_options_btn()
        self.click_print_postage_button()
        self.postage_check_printer_combo_box()

    def postage_add_envelope(self):
        self.select_postage_envelope_quantity()
        self.check_postage_add_to_envelope_btn_exists()
        self.click_on_postage_add_to_envelope_btn()
        return self.check_postage_row_added()

    def click_done_button(self):
        self.wait_element(*self.done_button)
        self.click_using_js(*self.done_button)

    def click_c5_envelope_size(self):
        self.wait_element(*self.c5_envelope_size)
        self.click_using_js(*self.c5_envelope_size)

    def click_c5_envelope_size_priewpage(self):
        self.wait_element(*self.c5_envelope_size_priewpage)
        self.click_using_js(*self.c5_envelope_size_priewpage)

    def check_scale_btn_is_present(self):
        flg = self.wait_element(*self.get_weight_btn)
        return flg

    def click_on_get_Weight_from_scale_btn(self):
        self.click_using_js(*self.get_weight_btn)

    def check_get_weight_btn_enabled(self):
        flg = self.wait_for_element_to_be_clickable(*self.get_weight_btn)
        return flg

    def verify_scale_is_connected(self):
        scale_not_connected = self.verify_if_element_is_visible(*self.txt_no_scale_found_msg)
        if scale_not_connected:
            self.click_using_js(*self.close_symbol)
            return False
        else:
            return True