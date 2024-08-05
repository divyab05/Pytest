import time
from selenium.webdriver.common.by import By

from FrameWorkUtilities.common_utils import common_utils
from UIObjects.BaseObject import BasePage


class SP360CreateShipRequestObjectsClass(BasePage):
    address_book = (By.XPATH, "//button[@id='btnOpenAddressBook']")
    address_book_pop_up = (By.XPATH, "//h2[text()='Select Address']")
    first_address = (By.XPATH, "(//button[contains(@class,'mat-ripple btn btn-block text-start')])[1]")
    ship_request_header = (By.XPATH, "//*[contains(text(),'Create Ship Request')]")
    err_ship_request_header = (By.XPATH, "//*[contains(text(),'Create ERR Ship Request')]")
    print_options_btn = (By.XPATH, "(//button[@id ='btnPrintOption'])[1]")
    Label_successfully_printed = (By.XPATH, "//span[contains(text(),'Label Completed')]")
    sample_print_btn = (By.XPATH, "//*[contains(text(),'Print Sample')]")
    print_shipping_Request = (By.XPATH, "//button[contains(text(),'Print Ship Request')]")
    txt_print_shipping_request = (
        By.XPATH, "//span[contains(text(),'Print Ship Request') or contains(text(),'Label Completed')]")
    close_symbol = (By.XPATH, "//button[contains(@class,'mat-ripple btn-close')]")
    print_size_combobox_input = (By.XPATH, "//input[@id='printSize']")
    print_size_combobox = (
        By.XPATH, "//label[contains(text(),'Select Print Size')]//parent::div/child::ng-select[@bindlabel='name']")
    printer_combobox = (By.XPATH, "//ng-select[@bindlabel='printerName']")
    label_reprint_msg = (By.XPATH, "//span[contains(text(), 'Label Reprinted') or contains(text(),'Label Completed')]")
    roll_type_path_4X6 = (By.XPATH,
                          "//label[contains(text(),'Select Print Size')]//parent::div/child::ng-select[@bindlabel='name']/following::span[contains(text(),'Roll 4 x 8')]")
    roll_type_path_8X11 = (By.XPATH,
                           "//label[contains(text(),'Select Print Size')]//parent::div/child::ng-select[@bindlabel='name']/following::span[contains(text(),'Plain Paper - 8.5 x 11')]")
    roll_type_path_8_5X11 = (By.XPATH,
                             "(//span[contains(text(),'Plain Paper - 8.5')])[2]")
    print_btn = (By.XPATH, "//button[@class='btn btn-print']")
    close_btn = (By.XPATH, "//button[contains(text(),'Close')]")
    done_btn = (By.XPATH, "//button[contains(text(),'Done')]")
    ship_req_generated_txt = (By.XPATH, "//div[contains(text(),'Your ship request has been generated.')]")
    reprint_btn = (By.XPATH, "//button[contains(text(),'Cancel')]//preceding::button[1]")
    cancel_btn = (By.XPATH, "//button[contains(text(),'Cancel')]")
    cost_to_acnt_txt = (By.XPATH, "//*[@id='costAccounts' or @id ='costAccount']")
    choose_cost_acnt = (By.XPATH, "//*[@id='costAccount']//following::span[@class='mat-option-text'][1]")
    choose_cost_acnt_sso = (By.XPATH, "//*[@id='costAccounts']//following::ng-dropdown-panel/div/div[2]/div[1]")

    def __init__(self, app_config, driver, custom_logger):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(SP360CreateShipRequestObjectsClass, self).__init__(driver)

    def check_create_shipping_request_header(self):
        return self.wait_element(*self.ship_request_header)

    def check_print_options_btn_tobe_clickabe(self):
        return self.wait_for_element_to_be_clickable(*self.print_options_btn)

    def click_on_print_options_btn(self):
        self.click_using_js(*self.print_options_btn)

    def wait_for_label_printed_msg(self):
        return self.wait_element(*self.Label_successfully_printed)

    def click_on_sample_print(self):
        self.click_using_js(*self.sample_print_btn)
        self.custom_logger.info("Sample Print button is clicked")

    def wait_for_addressbook_pop_up(self):
        return self.wait_for_element_to_be_clickable(*self.address_book)

    def click_on_address_book_pop_up(self):
        self.click_using_js(*self.address_book)
        self.custom_logger.info("Clicked on address box popup")

    def wait_for_address_header_to_load(self):
        return self.wait_element(*self.address_book_pop_up)

    def wait_for_first_address_to_load(self):
        return self.wait_for_element_to_be_clickable(*self.first_address)

    def click_on_first_address_book(self):
        self.click_using_js(*self.first_address)
        self.custom_logger.info("Clicked on first Address")

    def click_on_print_option(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(2)
        self.click_using_js(*self.print_options_btn)
        self.custom_logger.info("click on Print Option button")

    def click_on_X_button(self):
        self.click_using_js(*self.close_symbol)
        self.custom_logger.info("Clicked on close symbol")

    def verify_txt_print_shipping_request(self):
        element_vis = self.wait_element_till_time_limit(41, *self.ship_req_generated_txt)
        if element_vis:
            self.click_using_js(*self.done_btn)
        time.sleep(2)
        element_visible = self.wait_element_till_time_limit(41, *self.txt_print_shipping_request)
        if element_visible:
            self.custom_logger.info("Shipping Request is printed successfully")
            return True
        else:
            try:
                self.click_on_X_button()
            except:
                self.click_cancel_btn()
            return False

    def check_print_size_is_enabled(self):
        return self.find_element(*self.print_size_combobox_input).is_enabled()

    def click_on_print_size_combo_box(self):
        self.wait_element(*self.print_size_combobox)
        self.find_element(*self.print_size_combobox).click()

    def get_printer_combo_box(self):
        return self.find_element(*self.printer_combobox)

    def verify_re_print_is_success(self, app_config, get_driver, custom_logger):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(5)
        element_visible = self.check_label_reprint_msg()
        if element_visible:
            self.custom_logger.info("Re print is success")
            return True
        else:
            self.click_on_close_btn()
            return False

    def check_label_reprint_msg(self):
        return self.wait_element(*self.label_reprint_msg)

    def check_printer_combo_box(self):
        flg = self.wait_element(*self.printer_combobox)
        return flg

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

            self.find_element(*printer_path).click()
            self.press_tab()
            self.custom_logger.info("Printer is selected and clicked")
            return True
        except:
            self.click_using_js(*self.close_symbol)
            self.custom_logger.info("Printer is not selected or Printer is not in the list")
            return False

    def select_roll_type_from_dropdown(self, roll_type):
        try:
            if roll_type == "4X6":
                self.find_element(*self.roll_type_path_4X6).click()
                self.custom_logger.info("4x8 roll type is selected")
            elif roll_type == "8x11":
                self.click_using_js(*self.roll_type_path_8X11)
                self.custom_logger.info("8.5x11 roll type is selected")
            elif roll_type == '8.5"x11"':
                self.click_using_js(*self.roll_type_path_8_5X11)
                self.custom_logger.info("8.5x11 roll type is selected")
            self.press_tab()
            return True
        except:
            return False

    def click_on_print_btn_on_print_options(self):
        self.wait_element(*self.print_btn)
        self.click_using_js(*self.print_btn)
        self.custom_logger.info("Clicked on print button")

    def click_on_close_btn(self):
        self.click_using_js(*self.close_btn)

    def click_reprint_btn(self):
        self.wait_element(*self.reprint_btn)
        self.click_using_js(*self.reprint_btn)

    def click_cancel_btn(self):
        self.wait_element(*self.cancel_btn)
        self.click_using_js(*self.cancel_btn)

    def enter_cost_to_acnt(self, test_data):
        acntname = test_data['costToAccount']
        print(acntname)
        if self.verify_if_element_is_visible(*self.cost_to_acnt_txt):
            self.wait_element(*self.cost_to_acnt_txt)
            self.find_element(*self.cost_to_acnt_txt).clear()
            self.find_element(*self.cost_to_acnt_txt).send_keys(acntname)
            time.sleep(3)
            if self.verify_if_element_is_visible(*self.choose_cost_acnt):
                self.wait_element(*self.choose_cost_acnt)
                self.click_using_js(*self.choose_cost_acnt)
            elif self.verify_if_element_is_visible(*self.choose_cost_acnt_sso):
                self.wait_element(*self.choose_cost_acnt_sso)
                self.click_using_js(*self.choose_cost_acnt_sso)

    def check_create_err_shipping_request_header(self):
        return self.wait_element(*self.err_ship_request_header)

    def select_address_from_address_book(self, test_data):
        self.wait_for_element_to_be_clickable(*self.address_book)
        self.click_on_address_book_pop_up()
        self.wait_element(*self.address_book_pop_up)
        self.wait_element(*self.first_address)
        self.click_on_first_address_book()
        self.wait_for_element_to_be_clickable(*self.print_options_btn)
        # self.enter_cost_to_acnt(test_data)

    def select_printer(self, test_data, get_env, roll_type):
        self.click_on_print_option()
        self.wait_element(*self.printer_combobox)
        self.click_on_printer_combo_box()
        selected_printer = self.select_printer_from_dropdown(common_utils.get_system_name(get_env), test_data)
        if selected_printer:
            flg = self.check_print_size_is_enabled()
            if flg:
                self.click_on_print_size_combo_box()
                self.select_roll_type_from_dropdown(roll_type)
                time.sleep(2)
            return True
        else:
            return False
