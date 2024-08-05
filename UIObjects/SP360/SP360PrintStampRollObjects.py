import time
from selenium.webdriver.common.by import By

from FrameWorkUtilities.common_utils import common_utils
from UIObjects.BaseObject import BasePage


class SP360PrintStampRollObjectsClass(BasePage):
    sp360_stamp_roll_header = (By.XPATH, "//h1[text()='Print Stamps: Roll']")
    sp360_add_to_roll_btn = (By.XPATH, "//button[contains(text(), 'Add to Roll')]")
    roll_quantity_txtbox = (By.XPATH, "//input[@id='quantity']")
    add_row = (By.XPATH, "//button[@aria-label='Delete Stamp']")
    test_print_btn = (By.XPATH, "//button[@id='test-print-btn']")
    printer_combobox = (By.XPATH, "//ng-select[@bindlabel='printerName']")
    done_btn = (By.XPATH, "//button[contains(text(),'Done')]")
    stamps_processed_pop_up = (By.XPATH, "//*[contains(text(), 'Stamps being processed...')]")
    success_print_msg = (By.XPATH, "//*[contains(text(), 'Print stamps completed')]")
    actual_print_btn = (By.XPATH, "//button[@id ='stamp-print-btn']")
    done_btn_on_pop_up = (By.XPATH, "//button[contains(text(),'Done')]")
    print_options_btn = (By.XPATH, "//button[@id ='print-option-btn']")
    stamps_print_completed_msg = (By.XPATH, "//*[text()='Stamp Completed']")
    printer_selection_txt = (By.XPATH, "//p[text()=' Brother QL-800 ']")
    print_size_combobox = (
        By.XPATH, "//label[contains(text(),'Select Print Size')]//parent::div/child::ng-select[@bindlabel='name']")
    print_btn = (By.XPATH, "//button[@class='btn btn-print']")
    print_size_combobox_input = (By.XPATH, "//input[@id='printSize']")
    sp360_stamp_roll_sheet = (By.XPATH, "//h1[text()='Print Stamps: Sheet']")
    select_quantity = (By.XPATH, "//select[@id='quantity']")
    add_to_sheet_btn = (By.XPATH, "//div[@class='addbutton']//button")
    close_symbol = (By.XPATH, "//button[contains(@class,'mat-ripple btn-close')]")
    agreement_checkbox = (By.XPATH,
                          "//span[contains(text(),'Refresh Printer List')]//following::span[@class='mat-checkbox-inner-container']/input")
    reprint_btn = (By.XPATH, "//button[text()=' Reprint ']")
    change_stamp_roll_layout_link = (By.XPATH, "//a[contains(text(),'Change Stamp Roll Layout')]")
    SPM12_layout = (By.XPATH, "//div[contains(text(),'SL-SPM12')]//ancestor::button")
    print_stamps_btn = (
    By.XPATH, "//h2[contains(text(),'Print Options')]//following::button[contains(text(),'Print Stamps')]")
    service_loaded = (By.XPATH,"//label[@id='mailTypeLabel']//following-sibling::div")
    test_print_btn_in_printer_page = (By.XPATH, "//h2[contains(text(),'Print Options')]//following::button[contains(text(),'Test Print')]")
    # scale
    custom_stamp = (By.XPATH, "//label[contains(text(),'Custom Stamp')]")
    get_weight_btn = (By.XPATH, "//button[@class='btn btn-secondary btn-scale-with-text']")
    select_scale_drpdown = (By.XPATH, "//div[@aria-label='Scale options']/button")
    fetching_weight_txt = (By.XPATH, "//*[contains(text(), ' Fetching Weight.. ')]")
    set_scale_to_zero_btn = (By.XPATH, "//i[@class='pbi-icon-mini pbi-undo']//parent::button")
    zeroing_scale_txt = (By.XPATH, "//*[contains(text(),'Zeroing Scale')]")

    def __init__(self, app_config, driver, custom_logger):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(SP360PrintStampRollObjectsClass, self).__init__(driver)

    def get_stamp_roll_header(self):
        return self.find_element(*self.sp360_stamp_roll_header)

    def check_stamp_roll_header_exists(self):
        flg = self.wait_element(*self.sp360_stamp_roll_header)
        return flg

    def get_add_to_roll_btn(self):
        return self.find_element(*self.sp360_add_to_roll_btn)

    def get_quantity_textbox(self):
        return self.find_element(*self.roll_quantity_txtbox)

    def check_enter_quantity_textbox_status(self):
        flg = self.wait_for_element_to_be_clickable(*self.roll_quantity_txtbox)
        return flg

    def enter_quantity(self, quantity):
        time.sleep(2)
        self.get_quantity_textbox().click()
        self.get_quantity_textbox().clear()
        self.get_quantity_textbox().send_keys(quantity)
        self.custom_logger.info("Quantity is Selected")

    def check_add_roll_btn_is_clickable(self):
        flg = self.wait_for_element_to_be_clickable(*self.sp360_stamp_roll_header)
        return flg

    def click_on_roll_btn(self):
        self.custom_logger.info("Click on Add to roll button icon")
        self.get_add_to_roll_btn().click()

    def check_row_added(self):
        self.custom_logger.info("Check Row exists")
        flg = self.wait_element(*self.add_row)
        return flg

    def check_printer_selection_displayed(self):
        return self.find_element(*self.printer_selection_txt).is_displayed()

    def get_test_print_btn(self):
        self.wait_element(*self.test_print_btn)
        return self.find_element(*self.test_print_btn)

    def check_test_print_btn_exists(self):
        self.custom_logger.info("Check Test print button exists")
        flg = self.wait_element(*self.test_print_btn)
        return flg

    def click_on_test_print_btn(self):
        self.custom_logger.info("Click on test print btn")
        self.get_test_print_btn().click()

    def get_printer_combo_box(self):
        return self.find_element(*self.printer_combobox)

    def check_printer_combo_box(self):
        flg = self.wait_element(*self.printer_combobox)
        return flg

    def verify_printer_combo_box_present(self):
        return self.verify_if_element_is_visible(*self.printer_combobox)

    def click_on_printStamps_btn(self):
        self.custom_logger.info("Click on Stamps button")
        self.find_element(*self.print_stamps_btn).click()

    def click_on_printer_combo_box(self):
        self.get_printer_combo_box().click()
        self.custom_logger.info("Click on printer combo box")

    def select_printer_from_dropdown(self, device_name, test_data):
        try:
            printer_name = test_data['PrinterName']
            printer_path = (By.XPATH,
                            "//div[@role='group' and contains(text(),{arg1}{arg2}{arg3})]//following-sibling::div/span[text()={arg4}{arg5}{arg6}]"
                            .format(arg1="'", arg2=device_name, arg3="'", arg4="'", arg5=printer_name, arg6="'"))
            time.sleep(2)
            self.scroll_to_element(*printer_path)
            self.click_using_js(*printer_path)
            self.press_tab()
            self.custom_logger.info("Printer is selected and clicked")
            return True
        except:
            self.click_using_js(*self.close_symbol)
            self.custom_logger.info("Printer is not selected or printer is not in the list")
            return False

    def check_done_button_is_clickable(self):
        flg = self.wait_for_element_to_be_clickable(*self.done_btn)
        return flg

    def click_on_done_btn(self):
        self.custom_logger.info("Click on done button")
        self.find_element(*self.done_btn).click()

    def check_stamp_processed_window(self):
        time.sleep(2)
        flg = self.pop_up_exists()
        return flg

    def check_print_stamp_success_pop_up(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        element_visible = self.wait_element(*self.success_print_msg)
        if element_visible:
            self.custom_logger.info("Actual print is success")
            return True
        else:
            self.click_on_X_button()
            return False

    def check_actual_print_btn_is_enabled(self):
        return self.wait_for_element_to_be_clickable(*self.actual_print_btn)

    def click_on_print_btn(self):
        self.custom_logger.info("Click on Print button")
        self.find_element(*self.actual_print_btn).click()

    def click_on_don_btn_after_print(self):
        self.find_element(*self.done_btn_on_pop_up).click()

    def check_print_options_btn(self):
        return self.wait_for_element_to_be_clickable(*self.print_options_btn)

    def click_on_print_options(self):
        self.click_using_js(*self.print_options_btn)
        self.custom_logger.info("Print Option link is clicked")

    def check_stamp_print_success_message(self, batchprint):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        if batchprint == 'yes':
            element_visible = self.wait_element_till_time_limit(200, *self.stamps_print_completed_msg)
        else:
            element_visible = self.wait_element_till_time_limit(90, *self.stamps_print_completed_msg)
        if element_visible:
            self.custom_logger.info("Actual print is success")
            return True
        else:
            self.click_on_X_button()
            return False

    def click_on_X_button(self):
        self.click_using_js(*self.close_symbol)
        self.custom_logger.info("Clicked on close symbol")

    def click_on_stamp_roll_layout(self):
        self.wait_element(*self.change_stamp_roll_layout_link)
        self.click_using_js(*self.change_stamp_roll_layout_link)
        self.custom_logger.info("Clicked on Stamp roll layout link")

    def click_spm12_roll_layout(self):
        self.wait_element(*self.SPM12_layout)
        self.click_using_js(*self.SPM12_layout)
        self.custom_logger.info("Clicked on SPM 12 layout")

    # scale

    def click_on_custom_stamp(self):
        try:
            self.wait_element_till_time_limit(5, *self.custom_stamp)
            self.click_using_js(*self.custom_stamp)
            return True
        except:
            return False

    def check_scale_btn_is_present(self):
        flg = self.wait_element(*self.get_weight_btn)
        return flg

    def click_on_get_Weight_from_scale_btn(self):
        self.click_using_js(*self.get_weight_btn)

    def check_get_weight_btn_enabled(self):
        flg = self.wait_for_element_to_be_clickable(*self.get_weight_btn)
        return flg

    def check_fetching_weight_txt(self):
        flg = self.wait_element(*self.fetching_weight_txt)
        return flg

    def check_set_scale_to_zero_btn(self):
        flg = self.wait_element(*self.set_scale_to_zero_btn)
        return flg

    def click_scale_set_to_zero_btn(self):
        self.click_using_js(*self.set_scale_to_zero_btn)

    def check_zeroing_scale_txt(self):
        flg = self.wait_element(*self.zeroing_scale_txt)
        return flg

    def check_select_scale_drpdwn_btn(self):
        flg = self.wait_element(*self.select_scale_drpdown)
        return flg

    def click_on_select_scale_drpdown(self):
        self.click_using_js(*self.select_scale_drpdown)
        time.sleep(2)

    def select_scale_from_dropdown(self, device_name, test_data):
        scale_name = test_data['scaleName']
        scale_path = (By.XPATH,
                      "//h6[contains(text() ,{arg1}{arg2}{arg3})]//parent::div//button[contains(text(), {arg4}{arg5}{arg6})]"
                      .format(arg1="'", arg2=device_name, arg3="'", arg4="'", arg5=scale_name, arg6="'"))
        self.wait_element(*scale_path)
        self.click_using_js(*scale_path)
        self.custom_logger.info("Scale " + scale_name + "is selected and clicked")

    def add_stamp_roll(self, setup_dh, test_data, custom_logger):
        try:
            quantity = test_data['Quantity']
            check_stamp_link = setup_dh.check_stamps_links()
            if check_stamp_link:
                custom_logger.info("Stamps link is present")
                setup_dh.click_on_stamps_link()
                custom_logger.info("Stamps link is present")
                print_stamp_obj = setup_dh.click_on_roll_btn()
                self.wait_element(*self.sp360_stamp_roll_header)
                time.sleep(2)
                self.wait_element(*self.service_loaded)
                print_stamp_obj.enter_quantity(quantity)
                print_stamp_obj.click_on_roll_btn()
                return True
        except:
            return False

    def select_layout(self, change_layout):
        try:
            if change_layout == 'yes':
                self.click_on_stamp_roll_layout()
                self.click_spm12_roll_layout()
                self.click_on_done_btn()
            return True
        except:
            self.click_on_X_button()
            return False

    def select_printer_for_roll(self, get_env, test_data):
        sys_name = common_utils.get_system_name(get_env)
        if self.check_printer_combo_box():
            self.click_on_printer_combo_box()
            printer_selected = self.select_printer_from_dropdown(sys_name, test_data)
            if printer_selected:
                self.click_on_done_btn()
                return True
            else:
                return False
        else:
            return False

    def select_printer_after_clicking_print_btn(self,get_env, test_data):
        sys_name = common_utils.get_system_name(get_env)
        if self.check_printer_combo_box():
            self.click_on_printer_combo_box()
            selected_printer = self.select_printer_from_dropdown(sys_name, test_data)
            if selected_printer:
                return True
            else:
                return False
        else:
            return True

    def click_done_or_test_print_btn(self):
        if self.verify_if_element_is_visible(*self.test_print_btn_in_printer_page):
            self.click_using_js(*self.test_print_btn_in_printer_page)
        else:
            self.click_on_done_btn()




