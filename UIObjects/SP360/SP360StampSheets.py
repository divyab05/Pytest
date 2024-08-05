import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from FrameWorkUtilities.common_utils import common_utils
from UIObjects.BaseObject import BasePage


class SP360StampSheets(BasePage):

   # print_btn = (By.XPATH, "//button[@class='btn btn-print']")
    actual_print_btn_in_option_page = (
        By.XPATH, "//button[contains(text(),'Print Stamps') and (@class='btn btn-print ng-star-inserted')]")
    print_size_combobox_input = (By.XPATH, "//input[@id='printSize']")
    sp360_stamp_roll_sheet = (By.XPATH, "//h1[contains(text(),'Print Stamps: Sheet')]")
    select_quantity = (By.XPATH, "//select[@id='quantity']")
    add_to_sheet_btn = (By.XPATH, "//div[@class='addbutton']//button")
    done_btn = (By.XPATH, "//button[contains(text(),'Done')]")
    success_print_msg = (By.XPATH, "//*[contains(text(), 'Print stamps completed')]")
    actual_print_btn = (By.XPATH, "//button[contains(text(),'Print Stamps')]")
    add_row = (By.XPATH, "//button[@aria-label='Delete Stamp']")
    close_symbol = (By.XPATH, "//button[contains(@class,'mat-ripple btn-close')]")
    print_options_btn = (By.XPATH, "//button[@id ='print-option-btn']")
    printer_combobox = (By.XPATH, "//ng-select[@bindlabel='printerName']")
    test_print_btn = (By.XPATH, "//button[@id='test-print-btn']")
    stamps_print_completed_msg = (By.XPATH, "//*[text()='Stamp Completed']")
    cancel_link = (By.XPATH, "//a[text()='Cancel']")
    ok_cancel_transaction_btn = (By.ID, "cancel-transaction")
    cost_to_acnt = (By.XPATH, "//i[@class='pbi-icon-mini pbi-search']")
    account_txt = (By.XPATH, "//span[contains(text(),'List by Name')]//following::div[1]/button[1]")
    print_stamp_btn = (
        By.XPATH, "//button[@id='stamp-print-btn' and contains(text(),'Print Stamps')]")
    cost_to_acnt_commercial = (By.XPATH, "//input[@id='costAccounts']")
    search_cost_to_acnt = (By.XPATH, "//input[@aria-label='Search for a cost account']")
    #account_txt_commercial = (By.XPATH, "//ng-dropdown-panel[@role='listbox']/div/div[2]/div[1]")
    test_print_btn_in_printer_page = (By.XPATH, "//h2[contains(text(),'Print Options')]//following::button[contains(text(),'Test Print')]")
    print_stamps_btn = (By.XPATH, "//h2[contains(text(),'Print Options')]//following::button[contains(text(),'Print Stamps')]")
    # scale
    custom_stamp = (By.XPATH, "//label[contains(text(),'Custom Stamp')]")
    get_weight_btn = (By.XPATH, "//button[@class='btn btn-secondary btn-scale-with-text']")
    select_scale_drpdown = (By.XPATH, "//div[@aria-label='Scale options']/button")
    fetching_weight_txt = (By.XPATH, "//*[contains(text(), ' Fetching Weight.. ')]")
    set_scale_to_zero_btn = (By.XPATH, "//i[@class='pbi-icon-mini pbi-undo']//parent::button")
    zeroing_scale_txt = (By.XPATH, "//*[contains(text(),'Zeroing Scale')]")
    certified_mail_header = (By.XPATH, "//h1[contains(text(),'Certified Mail')]")
    priority_mail = (By.XPATH, "//label[contains(text(),'Priority Mail')]")
    btn_preview_rates = (By.XPATH, "//button[contains(text(),'Preview Rates')]")
    ounces = (By.XPATH, "//input[@id='ounces']")
    address_book = (By.XPATH, "//button[@id='btnOpenAddressBook']")
    address_book_pop_up = (By.XPATH, "//h2[@id='mat-dialog-title-0'and text()='Select Address']")
    Label_successfully_printed = (
        By.XPATH, "//span[contains(text(),'Label Completed')or contains(text(),'Labels   Completed')]")
    first_address = (By.XPATH, "(//button[@class='mat-ripple btn btn-block text-left ml-2'])[1]")
    service_loaded = (By.XPATH, "//label[@id='mailTypeLabel']//following-sibling::div")
    def __init__(self, app_config, driver, custom_logger):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(SP360StampSheets, self).__init__(driver)

    def check_stamp_sheet_header_exists(self):
        flg = self.wait_element_till_time_limit(34, *self.sp360_stamp_roll_sheet)
        return flg

    def select_stamp_sheet_quantity(self):
        time.sleep(2)
        self.wait_element_till_time_limit(40, *self.select_quantity)
        Select(self.find_element(*self.select_quantity)).select_by_value("1")
        self.custom_logger.info("Quantity is selected")

    def check_add_to_sheet_btn_exists(self):
        flg = self.wait_element_till_time_limit(30, *self.add_to_sheet_btn)
        return flg

    def click_on_print_btn(self):
        self.custom_logger.info("Click on Print button")
        time.sleep(3)
        self.wait_element(*self.actual_print_btn)
        self.find_element(*self.actual_print_btn).click()

    def click_print_stamp_sheet(self):
        self.custom_logger.info("Click on Print button")
        time.sleep(3)
        self.wait_element(*self.actual_print_btn)
        self.find_element(*self.actual_print_btn).click()

    def recover_transcation(self):
        element_visible = self.verify_if_element_is_visible(*self.cancel_link)
        if element_visible:
            self.click_using_js(*self.cancel_link)
            self.custom_logger.info("Click on Cancel Link")
            self.wait_element_till_time_limit(10, *self.ok_cancel_transaction_btn)
            self.click_using_js(*self.ok_cancel_transaction_btn)
            self.wait_for_element_to_be_clickable(*self.print_options_btn)

    def click_on_add_to_sheet_btn(self):
        self.click_using_js(*self.add_to_sheet_btn)
        self.custom_logger.info("Add to sheet button is clicked")

    def check_row_added(self):
        self.custom_logger.info("Check Row exists")
        flg = self.wait_element(*self.add_row)
        return flg

    def check_print_options_btn(self):
        return self.wait_for_element_to_be_clickable(*self.print_options_btn)

    def click_on_print_options(self):
        self.click_using_js(*self.print_options_btn)
        self.custom_logger.info("Print Option link is clicked")

    def check_printer_combo_box(self):
        flg = self.wait_element_till_time_limit(30, *self.printer_combobox)
        return flg

    def click_on_printer_combo_box(self):
        self.get_printer_combo_box().click()
        self.custom_logger.info("Click on printer combo box")

    def get_printer_combo_box(self):
        return self.find_element(*self.printer_combobox)

    def select_printer_from_dropdown(self, device_name, test_data):
        try:
            printer_name = test_data['PrinterName']
            printer_path = (By.XPATH,
                            "//div[@role='group' and contains(text(),{arg1}{arg2}{arg3})]//following-sibling::div/span[text()={arg4}{arg5}{arg6}]"
                            .format(arg1="'", arg2=device_name, arg3="'", arg4="'", arg5=printer_name, arg6="'"))
            self.wait_element_till_time_limit(40, *printer_path)
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

    def check_done_button_is_clickable(self):
        flg = self.wait_for_element_to_be_clickable(*self.done_btn)
        return flg

    def click_on_done_btn(self):
        self.custom_logger.info("Click on done button")
        self.find_element(*self.done_btn).click()

    def click_on_test_print_btn(self):
        self.custom_logger.info("Click on test print btn")
        self.scroll_to_element(*self.test_print_btn)
        self.click_using_js(*self.test_print_btn)

    def get_test_print_btn(self):
        self.wait_element(*self.test_print_btn)
        return self.find_element(*self.test_print_btn)

    def check_print_stamp_success_pop_up(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        element_visible = self.wait_element(*self.success_print_msg)
        if element_visible:
            self.custom_logger.info("Test print is success")
            return True
        else:
            self.click_on_X_button()
            return False

    def click_cost_to_account(self, get_product_name, test_data):
        try:
            cost_to_acnt = test_data['costToAccount']
            if self.verify_if_element_is_visible(*self.cost_to_acnt_commercial):
                self.find_element(*self.cost_to_acnt_commercial).send_keys(cost_to_acnt)
                time.sleep(3)
                self.wait_element_till_time_limit(5, *self.account_txt_commercial)
                self.click_using_js(*self.account_txt_commercial)
            elif self.verify_if_element_is_visible(*self.cost_to_acnt):
                self.click_using_js(*self.cost_to_acnt)
                self.wait_element_till_time_limit(5, *self.search_cost_to_acnt)
                self.find_element(*self.search_cost_to_acnt).send_keys(cost_to_acnt)
                time.sleep(3)
                self.wait_element_till_time_limit(5, *self.account_txt)
                self.click_using_js(*self.account_txt)
        except:
            return False

    def check_actual_print_btn_is_enabled(self):
        return self.wait_for_element_to_be_clickable(*self.actual_print_btn)

    def check_stamp_print_success_message(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        element_visible = self.wait_element_till_time_limit(70, *self.stamps_print_completed_msg)
        if element_visible:
            self.custom_logger.info("Actual print is success")
            return True
        else:
            self.click_on_X_button()
            self.recover_transcation()
            return False

    def click_on_X_button(self):
        self.click_using_js(*self.close_symbol)
        self.custom_logger.info("Clicked on close symbol")

    def click_actual_print_btn_in_option_page(self):
        element_visible = self.wait_element_till_time_limit(10, *self.actual_print_btn_in_option_page)
        if element_visible:
            self.click_using_js(*self.actual_print_btn_in_option_page)
            self.custom_logger.info("Actual Print in option page is clicked")
        else:
            self.click_on_X_button()

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
        # scale_name = test_data

        scale_path = (By.XPATH,
                      "//h6[contains(text() ,{arg1}{arg2}{arg3})]//parent::div//button[contains(text(), {arg4}{arg5}{arg6})]"
                      .format(arg1="'", arg2=device_name, arg3="'", arg4="'", arg5=scale_name, arg6="'"))

        self.wait_element(*scale_path)
        self.click_using_js(*scale_path)
        self.custom_logger.info("Scale " + scale_name + "is selected and clicked")

    def add_stamp_sheet(self, setup_dh, custom_logger):
        try:
            time.sleep(3)
            check_stamp_link = setup_dh.check_stamps_links()
            if check_stamp_link:
                custom_logger.info("Stamps link is present")
                setup_dh.click_on_stamps_link()
                custom_logger.info("Stamps sheet link is present")
                setup_dh.click_on_stamp_sheet_link()
                self.wait_element(*self.sp360_stamp_roll_sheet)
                self.wait_element(*self.service_loaded)
                time.sleep(2)
                self.select_stamp_sheet_quantity()
                self.click_on_add_to_sheet_btn()
                return self.check_row_added()
        except:
              return False

    def select_printer_for_sheet(self, get_env, test_data):
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

    def select_printer_after_clicking_print_btn(self, get_env, test_data):
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

    def click_print_stamps_btn(self):
        self.custom_logger.info("Click on Print button")
        time.sleep(3)
        self.wait_element(*self.print_stamps_btn)
        self.find_element(*self.print_stamps_btn).click()









