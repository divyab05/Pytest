import time
from selenium.webdriver.common.by import By

from FrameWorkUtilities.common_utils import common_utils
from UIObjects.BaseObject import BasePage


class SP360StampEnvelopeClass(BasePage):
    envelope_quantity_txtbox = (By.XPATH, "//input[@id='quantity']")
    add_row = (By.XPATH, "//button[@aria-label='Delete Stamp']")
    sp360_stamp_envelope = (By.XPATH, "//h1[text()='Print Stamps: Envelope']")
    envelope_size9 = (By.XPATH, "//button/span[contains(text(),'#9')]")
    envelope_size10 = (By.XPATH, "//button/span[contains(text(),'#10')]")
    done_btn = (By.XPATH, "//button[contains(text(),'Done')]")
    add_to_envelope_btn = (By.XPATH, "//button[@id='addMailServices']")
    print_option_envelope = (By.XPATH, "//button[contains(text(),'Print Options')]")
    preview_test_print = (By.XPATH, "//button[contains(text(),'Preview Test Print')]")
    test_print_test_btn = (By.XPATH, "//button[contains(text(),'Print Test Print')]")
    success_envelope_test_print_mgs = (By.XPATH, "//p[contains(text(),'Good test print')]")
    test_print_envelope = (By.XPATH, "//button[contains(text(),'Test Print')]")
    actual_envelope_print = (By.XPATH, "//button[contains(text(),'Print Stamps')]")
    actual_envelope_print_printoption = (
        By.XPATH, "//mat-dialog-actions/button[contains(text(),'Print Stamps')]")
    button_ok = (By.XPATH, "//button[contains(text(),'OK')]")
    close_symbol = (By.XPATH, "//button[contains(@class,'mat-ripple btn-close')]")
    agreement_checkbox = (By.XPATH,
                          "//span[contains(text(),'Refresh Printer List')]//following::span[@class='mat-checkbox-inner-container']/input")
    reprint_btn = (By.XPATH, "//button[text()=' Reprint ']")
    printer_combobox = (By.XPATH, "//ng-select[@bindlabel='printerName']")
    stamps_print_completed_msg = (
        By.XPATH, "//*[contains(text(),'Stamp Completed') or contains(text(),'Stamps Completed')]")
    cancel_link = (By.XPATH, "//a[text()='Cancel']")
    ok_cancel_transaction_btn = (By.ID, "cancel-transaction")
    cost_to_acnt = (By.XPATH, "//i[@class='pbi-icon-mini pbi-search']")
    account_txt = (By.XPATH, "//span[contains(text(),'List by Name')]//following::div[1]/button[1]")
    cost_to_acnt_commercial = (By.XPATH, "//input[@id='costAccounts']")
    account_txt_commercial = (By.XPATH, "//ng-dropdown-panel[@role='listbox']/div/div[2]/div[1]")
    search_cost_to_acnt = (By.XPATH, "//input[@aria-label='Search for a cost account']")

    # scale
    custom_stamp = (By.XPATH, "//label[contains(text(),'Custom Stamp')]")
    get_weight_btn = (By.XPATH, "//button[@class='btn btn-secondary btn-scale-with-text']")
    select_scale_drpdown = (By.XPATH, "//div[@aria-label='Scale options']/button")
    fetching_weight_txt = (By.XPATH, "//*[contains(text(), ' Fetching Weight.. ')]")
    set_scale_to_zero_btn = (By.XPATH, "//i[@class='pbi-icon-mini pbi-undo']//parent::button")
    zeroing_scale_txt = (By.XPATH, "//*[contains(text(),'Zeroing Scale')]")

    sender_address_link = (By.XPATH, "//button[contains(text(),'Add Sender Address')]")
    recipient_address_link = (By.XPATH, "//button[contains(text(),'Add Recipient Address')]")
    button_apply = (By.XPATH, "//button[contains(text(),'Apply')]")
    select_address = (By.XPATH, "//ul[@class='list-unstyled ng-star-inserted']/li[1]/div/button")
    address_book_icon = (By.XPATH, "//i[@class='pbi-icon-mini pbi-address-book']")
    test_print_good_label =(By.XPATH,"//h2[contains(text(),'Is the test print good?')]")

    def __init__(self, app_config, custom_logger, driver):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(SP360StampEnvelopeClass, self).__init__(driver)

    def get_quantity_textbox(self):
        return self.find_element(*self.envelope_quantity_txtbox)

    def enter_quantity(self, quantity):
        time.sleep(2)
        self.get_quantity_textbox().click()
        self.get_quantity_textbox().clear()
        self.get_quantity_textbox().send_keys(quantity)
        self.custom_logger.info("Quantity is Selected")
        time.sleep(3)

    def check_stamp_envelope_header_exists(self):
        flg = self.wait_element_till_time_limit(30, *self.sp360_stamp_envelope)
        return flg

    def select_envelope_size9(self):
        self.click_using_js(*self.envelope_size9)

    def select_envelope_size10(self):
        self.click_using_js(*self.envelope_size10)

    def check_add_to_envelope_btn_exists(self):
        flg = self.wait_element(*self.add_to_envelope_btn)
        return flg

    def click_on_add_to_envelope_btn(self):
        self.wait_for_element_to_be_clickable(*self.add_to_envelope_btn)
        self.click_using_js(*self.add_to_envelope_btn)
        self.custom_logger.info("Add to Envelope button is clicked")

    def check_print_options_envelope_btn(self):
        return self.wait_element(*self.print_option_envelope)

    def click_print_options_envelope_btn(self):
        self.click_using_js(*self.print_option_envelope)

    def click_preview_test_print(self):
        self.click_using_js(*self.preview_test_print)
        self.custom_logger.info("Click preview test Button")

    def verify_preview_test_print_visible(self):
        return self.verify_if_element_is_visible(*self.preview_test_print)

    def click_test_print_test_btn(self):
        self.wait_element(*self.test_print_test_btn)
        self.click_using_js(*self.test_print_test_btn)
        self.custom_logger.info("Click on print test Button")

    def check_done_button_is_clickable(self):
        flg = self.wait_for_element_to_be_clickable(*self.done_btn)
        return flg

    def click_on_X_button(self):
        self.click_using_js(*self.close_symbol)
        self.custom_logger.info("Clicked on close symbol")

    def verify_success_envelope_test_print_mgs(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        element_visible = self.wait_element_till_time_limit(90, *self.success_envelope_test_print_mgs)
        if element_visible:
            self.custom_logger.info("Actual print is success")
            return True
        else:
            self.click_on_X_button()
            return False

    def get_envelope_test_print_btn(self):
        self.scroll_to_element(*self.test_print_envelope)
        return self.wait_element_till_time_limit(30, *self.test_print_envelope)

    def click_test_envelope_btn(self):
        self.click_using_js(*self.test_print_envelope)
        self.custom_logger.info("Test Print Button is clicked")

    def check_actual_envelope_print(self):
        return self.wait_element(*self.actual_envelope_print)

    def click_actual_envelope_print(self):
        self.click_using_js(*self.actual_envelope_print)
        self.custom_logger.info("Print button is clicked")

    def click_actual_envelope_print_printoption(self):
        time.sleep(2)
        self.click_using_js(*self.actual_envelope_print_printoption)
        self.custom_logger.info("Print button is clicked")

    def check_actual_envelope_print_printoption(self):
        return self.wait_element_till_time_limit(40, *self.actual_envelope_print_printoption)

    def click_ok_btn(self):
        self.click_using_js(*self.button_ok)
        self.custom_logger.info("Clicked on OK Button")

    def verify_printer_combo_box_present(self):
        return self.verify_if_element_is_visible(*self.printer_combobox)

    def get_printer_combo_box(self):
        return self.find_element(*self.printer_combobox)

    def click_on_printer_combo_box(self):
        self.find_element(*self.printer_combobox).click()
        self.custom_logger.info("Click on printer combo box")

    def check_printer_combo_box(self):
        flg = self.wait_element(*self.printer_combobox)
        return flg

    def select_printer_from_dropdown(self, device_name, test_data):
        try:
            printer_name = test_data['PrinterName']
            print(printer_name)

            printer_path = (By.XPATH,
                            "//div[@role='group' and contains(text(),{arg1}{arg2}{arg3})]//following-sibling::div/span[text()={arg4}{arg5}{arg6}]"
                            .format(arg1="'", arg2=device_name, arg3="'", arg4="'", arg5=printer_name, arg6="'"))
            print(printer_path)
            self.wait_element(*printer_path)
            self.click_using_js(*printer_path)
            self.custom_logger.info("Printer is selected and clicked")
            return True
        except:
            self.click_using_js(*self.close_symbol)
            self.custom_logger.info("Printer is not selected")
            return False

    def check_stamp_print_success_message(self, batchprint):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        if batchprint == 'yes':
            print('inside batch print')
            element_visible = self.wait_element_till_time_limit(200, *self.stamps_print_completed_msg)
        else:
            element_visible = self.wait_element_till_time_limit(90, *self.stamps_print_completed_msg)
        print(element_visible)
        if element_visible:
            self.custom_logger.info("Actual print is success")
            return True
        else:
            self.click_on_X_button()
            self.recover_transcation()
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

    def check_enter_quantity_textbox_status(self):
        flg = self.wait_for_element_to_be_clickable(*self.envelope_quantity_txtbox)
        return flg

    def check_row_added(self):
        flg = self.wait_element(*self.add_row)
        self.custom_logger.info("Check Row exists")
        return flg

    def click_on_done_btn(self):
        self.wait_element(*self.done_btn)
        self.custom_logger.info("Click on done button")
        self.find_element(*self.done_btn).click()

    def recover_transcation(self):
        element_visible = self.verify_if_element_is_visible(*self.cancel_link)
        if element_visible:
            self.click_using_js(*self.cancel_link)
            self.custom_logger.info("Click on Cancel Link")
            self.wait_element_till_time_limit(10, *self.ok_cancel_transaction_btn)
            self.click_using_js(*self.ok_cancel_transaction_btn)
            self.wait_for_element_to_be_clickable(*self.print_option_envelope)

        # scale

    def click_on_custom_stamp(self):
        try:
            self.wait_element_till_time_limit(5,*self.custom_stamp)
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

    def select_sender_recipient_address(self):

        senderAddress = self.wait_element_till_time_limit(5, *self.sender_address_link)
        if senderAddress:
            self.click_using_js(*self.sender_address_link)
            self.wait_for_element_to_be_clickable(*self.button_apply)
            self.click_using_js(*self.button_apply)

        self.click_using_js(*self.recipient_address_link)
        self.wait_element(*self.address_book_icon)
        self.click_using_js(*self.address_book_icon)

        self.wait_element(*self.select_address)
        self.click_using_js(*self.select_address)

        self.wait_for_element_to_be_clickable(*self.button_apply)
        self.click_using_js(*self.button_apply)

    def add_stamp_envelope(self, setup_dh, size, test_data, custom_logger):
        try:
            quantity = test_data['Quantity']
            time.sleep(4)
            check_stamp_link = setup_dh.check_stamps_links()
            if check_stamp_link:
                custom_logger.info("Stamps link is present")
                setup_dh.click_on_stamps_link()
                custom_logger.info("Stamps Envelope link is present")
                setup_dh.click_on_stamp_envelope_link()
                self.wait_element(*self.sp360_stamp_envelope)
                self.select_envelope_size(size)
                self.select_sender_recipient_address()
                time.sleep(4)
                self.enter_quantity(quantity)
                self.wait_for_element_to_be_clickable(*self.add_to_envelope_btn)
                self.click_on_add_to_envelope_btn()
                return self.check_row_added()
        except:
            return False

    def select_envelope_size(self, size):
        if size == "9":
            self.select_envelope_size9()
        else:
            self.select_envelope_size10()

    def select_printer_for_envelope(self, get_env, test_data):
        sys_name = common_utils.get_system_name(get_env)
      #  if self.check_printer_combo_box():
        self.click_on_printer_combo_box()
        printer_selected = self.select_printer_from_dropdown(sys_name, test_data)
        if printer_selected:
            return True
        else:
            return False
       # else:
           # return False

    def select_printer_after_clicking_print_btn(self, get_env, test_data):
        sys_name = common_utils.get_system_name(get_env)
        if self.check_printer_combo_box():
            self.click_on_printer_combo_box()
            selected_printer = self.select_printer_from_dropdown(sys_name, test_data)
            if selected_printer:
                self.click_on_done_btn()
                return True
            else:
                return False
        else:
            return True

    def click_test_print_envelope(self):
        self.click_test_envelope_btn()
        time.sleep(2)
        if self.verify_preview_test_print_visible():
            self.click_preview_test_print()
            self.click_test_print_test_btn()
        else :
            self.click_test_print_test_btn()

    def verify_test_print(self):
        if self.verify_if_element_is_visible(*self.test_print_good_label):
            self.click_on_X_button()
            return True
        elif self.verify_if_element_is_visible(*self.done_btn):
             self.click_on_done_btn()
             return True
        else:
            return False


