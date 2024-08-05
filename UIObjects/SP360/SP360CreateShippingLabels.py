import time
from selenium.webdriver.common.by import By
from FrameWorkUtilities.common_utils import common_utils
from UIObjects.BaseObject import BasePage


class SP360CreateShippingLabelObjectsClass(BasePage):
    address_book = (By.XPATH, "//button[@id='btnOpenAddressBook']")
    address_book_pop_up = (By.XPATH, "//h2[text()='Select Address']")
    first_address = (By.XPATH, "(//button[contains(@class,'mat-ripple btn btn-block text-start')])[1]")
    shipping_label_header = (By.XPATH, "//h1[contains(text(),'Print Options')]")
    print_shipping_label = (
        By.XPATH, "//button[contains(text(),'Print Shipping Label')or contains(text(),'Print International')]")
    print_options_btn = (By.XPATH, "(//button[@id ='btnPrintOption' or @id ='btnPrintOptionBatch'])[1]")
    Label_successfully_printed = (
        By.XPATH, "//span[contains(text(),'Label Completed')or contains(text(),'Labels   Completed')]")
    sample_print_btn = (By.XPATH, "//button[contains(text(),'Print Sample')]")
    label_processing_dailog = (By.XPATH, "//*[text()='Label being processed']")
    close_symbol = (By.XPATH, "//button[contains(@class,'mat-ripple btn-close')]")
    re_print_link = (By.XPATH, "//button[contains(text(),'Reprint')]")
    label_reprint_msg = (By.XPATH, "//span[contains(text(), 'Label Reprinted')]")
    close_btn = (By.XPATH, "//button[contains(@class,'mat-ripple btn-close')]")
    button_ok = (By.XPATH, "//button[contains(text(),'OK')]")
    agreement_checkbox = (By.XPATH,
                          "//h2[contains(text(),' Reprint Label ')]//following::input[@type='checkbox']")
    reprint_btn = (By.XPATH, "//button[text()=' Reprint ']")
    print_size_combobox = (
        By.XPATH, "//label[contains(text(),'Select Print Size')]//parent::div/child::ng-select[@bindlabel='name']")
    printer_combobox = (By.XPATH, "//ng-select[@bindlabel='printerName']")
    print_size_combobox_input = (By.XPATH, "//input[@id='printSize']")
    chkbox_Receipt_with_shipping_label = (
        By.XPATH, "//div[contains(text(),'Receipt with Shipping Label')]//parent::div[1]//preceding::input[1]")
    print_btn = (By.XPATH, "//button[@class='btn btn-print']")
    ups_service = (By.XPATH, "//label[text()='Rates and Services']//following::div[contains(text(),'UPS')]")
    edit_rate_and_services_btn = (By.XPATH, "//span[text()='Edit Rates and Services']//parent::button")
    carrier_combo_box = (By.XPATH, "//select[@formcontrolname='subCarrier']/option")
    choose_service_apply_btn = (By.XPATH, "//button[contains(text(),'Choose Service') or contains(text(),'Apply')]")
    name_txt_box = (By.XPATH, "//input[@id='name']")
    select_rates_service_button = (By.ID, "btnShopRatesAndServices")
    new_cost_to_account = (By.XPATH, "//span[text()='new']")
    cost_account_input = (By.XPATH, "//ng-select[@formcontrolname='costAccount']")
    carrier_radio_btn = (By.XPATH, "(//input[contains(@id,'USPS') and @type='radio'])[1]")
    roll_type_path_4X6 = (By.XPATH,
                          "//label[contains(text(),'Select Print Size')]//following::ng-dropdown-panel/div/div/div/span[contains(text(),'Roll 4')]")
    roll_type_path_8X11 = (By.XPATH,
                           "//label[contains(text(),'Select Print Size')]//following::ng-dropdown-panel/div/div/div/span[contains(text(),'Plain Paper - 8.5')]")
    get_weight_btn = (By.XPATH, "//button[@class='btn btn-secondary btn-scale-with-text']")
    select_scale_drpdown = (By.XPATH, "//div[@aria-label='Scale options']/button")
    fetching_weight_txt = (By.XPATH, "//*[contains(text(), ' Fetching Weight.. ')]")
    set_scale_to_zero_btn = (By.XPATH, "//i[@class='pbi-icon-mini pbi-undo']//parent::button")
    zeroing_scale_txt = (By.XPATH, "//*[contains(text(),'Zeroing Scale')]")
    agreement_checkbox_ups_privacy_act = (By.XPATH,
                                          "//span[contains(text(),'By checking this box')]//preceding::span[@class='mat-checkbox-inner-container'][1]//input")
    multiple_recepient = (By.XPATH, "//span[contains(text(),'Multiple')]//parent::button")
    recipientList = (By.XPATH, "//ng-select[@id='recipientList']//div//input")
    address_validation = (By.XPATH, "//i[contains(@class,'pbi-icon-mini pbi-check-circle')]")

    length = (By.XPATH, "//input[@id='length' or @name='length']")
    width = (By.XPATH, "//input[@id='width' or @name='width']")
    height = (By.XPATH, "//input[@id='height' or @name='height']")
    weight = (By.XPATH, "//input[@id='pounds' or @name='pounds']")
    ounces = (By.XPATH, "//input[@id='ounces' or @name='ounces']")
    select_service_button = (By.XPATH, "//button[@id='btnSelectServices' or @id='btnShopRatesAndServices']")
    close_shipping_rates = (By.XPATH, "//button[contains(@class,'mat-ripple btn-close')]")
    cost_to_acnt_txt = (By.XPATH, "//*[@id='costAccounts' or @id ='costAccount']")
    choose_cost_acnt = (By.XPATH, "//*[@id='costAccount']//following::span[@class='mdc-list-item__primary-text'][1]")
    choose_cost_acnt_sso = (By.XPATH, "//*[@id='costAccounts']//following::ng-dropdown-panel/div/div[2]/div[1]")
    print_summary_receipt = (
        By.XPATH,
        "//*[contains(text(),'Summary Receipt')]//preceding::span[@class='mat-checkbox-background'][1]")

    use_preset = (By.XPATH, "//span[text()='Use a Preset']")
    txt_preset = (By.XPATH, "//ng-select[@formcontrolname ='selectedPreset']//input[1]")
    selected_preset = (By.XPATH, "//span[text()='Use a Preset']//following::div[@role='option'][1]")
    roll_type_path_6x4 = (By.XPATH,
                          "//label[contains(text(),'Select Print Size')]//following::ng-select/div/div/div/span[contains(text(),'Landscape - 6 X 4')]")
    roll_type_path_A4 = (By.XPATH,
                         "//label[contains(text(),'Select Print Size')]//following::ng-dropdown-panel/div/div/div/span[contains(text(),'Plain Paper')]")
    roll_type_path_21x27 = (By.XPATH,
                            "//label[contains(text(),'Select Print Size')]//following::ng-dropdown-panel/div/div/div/span[contains(text(),'Plain Paper - 21,59 X 27,94')]")
    roll_type_path_10x20 = (By.XPATH,
                            "//label[contains(text(),'Select Print Size')]//following::ng-dropdown-panel/div/div/div/span[contains(text(),'Roll 10,16 x 20,32')]")
    multipiece_label = (By.XPATH, "//label[contains(text(),'Multi-Piece')]")
    add_multipiece_label_icon = (By.XPATH, "//i[@class='pbi-icon-mini pbi-add']")
    certified_mail_header = (By.XPATH, "//h1[contains(text(),'Certified Mail')]")
    priority_mail = (By.XPATH, "//span[contains(text(),'Priority Mail')]")
    certified_label = (By.XPATH, "//span[contains(text(),'E-Certified')]")
    btn_preview_rates = (By.XPATH, "//button[contains(text(),'Preview Rates')]")
    done_btn = (By.XPATH, "//button[contains(text(),'Done')]")
    print_cover_sheet_stamp_btn = (By.XPATH, "//button[contains(text(),'Print Coversheet and Stamp')]")
    success_msg_cover_sheet = (By.XPATH, "//div[contains(text(), 'Your coversheet has been generated')]")
    btn_cancel = (By.XPATH, "//button[contains(text(),'Cancel')]")
    radiobtn_coversheet_certified10 = (By.XPATH, "//input[@value='10']")
    cubic_soft_pak_link = (By.XPATH,"//span[contains(text(), 'Cubic Soft Pack')]")
    Flat_link = (By.XPATH, "//span[contains(text(), 'Flat')]")

    def __init__(self, app_config, driver, custom_logger):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(SP360CreateShippingLabelObjectsClass, self).__init__(driver)

    def check_create_shipping_label_header(self):
        return self.wait_element(*self.shipping_label_header)

    def check_edit_rate_and_services_btn_loaded(self):
        return self.wait_element(*self.edit_rate_and_services_btn)

    def check_print_options_btn_tobe_clickable(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        return self.wait_for_element_to_be_clickable(*self.print_options_btn)

    def click_on_print_options_btn(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        self.click_using_js(*self.print_options_btn)

    def wait_for_label_printed_msg(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        if self.wait_element_till_time_limit(60, *self.Label_successfully_printed):
            self.custom_logger.info("Actual print is success")
            return True
        else:
            x_symbol_visible = self.wait_element_till_time_limit(2, *self.close_symbol)
            if x_symbol_visible:
                self.click_on_X_button()
                return False
            elif self.wait_element_till_time_limit(1, *self.button_ok):
                self.click_ok_btn()
                return False
            elif self.wait_element_till_time_limit(1, *self.btn_cancel):
                self.click_using_js(*self.btn_cancel)
                return False
            else:
                return False

    def click_on_X_button(self):
        self.click_using_js(*self.close_symbol)
        self.custom_logger.info("Clicked on close symbol")

    def check_label_processing_dialog(self):
        flg = self.wait_element(*self.label_processing_dailog)
        return flg

    def click_on_sample_print(self):
        self.wait_element(*self.sample_print_btn)
        self.click_using_js(*self.sample_print_btn)
        self.custom_logger.info("Sample Print button is clicked")

    def click_on_print_Shipping_label(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 1000)")
        self.click_using_js(*self.print_shipping_label)
        self.custom_logger.info("Clicked on print shipping label")

    def check_print_shipping_label_is_clickable(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        return self.wait_element_till_time_limit(50, *self.print_shipping_label)

    def verify_sample_print_is_success(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(2)
        try:
            element_visible = self.wait_for_element_not_present(*self.label_processing_dailog)
            if element_visible:
                self.custom_logger.info("Sample print is success")
                return True
        except:
            button_ok_visible = self.wait_element_till_time_limit(5, *self.button_ok)
            if button_ok_visible:
                self.click_ok_btn()
                return False
            else:
                self.click_on_X_button()
                return False

    def click_ok_btn(self):
        self.click_using_js(*self.button_ok)
        self.custom_logger.info("Clicked on OK Button")

    def click_re_print_link(self):
        self.click_using_js(*self.re_print_link)
        self.custom_logger.info("clicked on re print link")

    def check_re_print_link_present(self):
        return self.wait_element_till_time_limit(50, *self.re_print_link)

    def check_label_reprint_msg(self):
        time.sleep(10)
        return self.wait_element_till_time_limit(60, *self.label_reprint_msg)

    def click_on_close_btn(self):
        self.click_using_js(*self.close_btn)

    def verify_re_print_is_success(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        element_visible = self.check_label_reprint_msg()
        print(element_visible)
        if element_visible:
            self.custom_logger.info("Re print is success")
            return True
        else:
            self.click_on_close_btn()
            return False

    def check_printer_combo_box(self):
        flg = self.wait_element(*self.printer_combobox)
        return flg

    def click_on_printer_combo_box(self):
        self.get_printer_combo_box().click()
        self.custom_logger.info("Click on printer combo box")

    def select_printer_from_dropdown(self, device_name, test_data):
        printer_name = test_data['PrinterName']
        try:

            printer_path = (By.XPATH,
                            "//div[@role='group' and contains(text(),{arg1}{arg2}{arg3})]//following-sibling::div/span[text()={arg4}{arg5}{arg6}]"
                            .format(arg1="'", arg2=device_name, arg3="'", arg4="'", arg5=printer_name, arg6="'"))

            self.wait_element(*printer_path)
            self.scroll_to_element(*printer_path)
            time.sleep(2)
            self.click_using_js(*printer_path)
            self.press_tab()
            self.custom_logger.info("Printer " + printer_name + "is selected and clicked")
            return True
        except:
            self.click_using_js(*self.close_symbol)
            self.custom_logger.info("Printer" + printer_name + " is not selected")
            return False

    def click_agreement_checkbox(self):
        if self.wait_element_till_time_limit(4, *self.agreement_checkbox):
            self.click_using_js(*self.agreement_checkbox)
            self.custom_logger.info("Agreement checkbox is clicked ")

    def check_reprint_btn_is_enabled(self):
        return self.find_element(*self.reprint_btn).is_enabled()

    def click_on_reprint_buttton(self):
        self.click_using_js(*self.reprint_btn)

    def click_on_print_btn_on_print_options(self):
        self.wait_element(*self.print_btn)
        self.click_using_js(*self.print_btn)
        self.custom_logger.info("Clicked on print button")

    def check_receipt_shipping_label(self):
        is_selected = self.find_element(*self.chkbox_Receipt_with_shipping_label).is_selected()
        if is_selected == False:
            self.click_using_js(*self.chkbox_Receipt_with_shipping_label)
            self.custom_logger.info("Receipt with shipping label checkbox is checked")
            time.sleep(2)

    def select_roll_type_from_dropdown(self, roll_type):
        try:
            if roll_type == "4x6":
                self.find_element(*self.roll_type_path_4X6).click()
                self.custom_logger.info("4x6 roll type is selected")
            elif roll_type == "8x11":
                self.click_using_js(*self.roll_type_path_8X11)
                self.custom_logger.info("8.5x11 roll type is selected")
                self.press_tab()
            elif roll_type == "6x4":
                self.click_using_js(*self.roll_type_path_6x4)
                self.custom_logger.info("6x4 roll type is selected")
                self.press_tab()
            elif roll_type == "A4":
                self.click_using_js(*self.roll_type_path_A4)
                self.custom_logger.info("A4 roll type is selected")
                self.press_tab()
            elif roll_type == "21x27":
                self.click_using_js(*self.roll_type_path_21x27)
                self.custom_logger.info("21x27 roll type is selected")
                self.press_tab()
            elif roll_type == "10x20":
                self.click_using_js(*self.roll_type_path_10x20)
                self.custom_logger.info("21x27 roll type is selected")
                self.press_tab()
            return True
        except:
            self.click_on_X_button()
            return False

    def check_print_size_is_enabled(self):
        return self.find_element(*self.print_size_combobox_input).is_enabled()

    def click_on_print_size_combo_box(self):
        self.wait_element(*self.print_size_combobox)
        self.find_element(*self.print_size_combobox).click()

    def get_printer_combo_box(self):
        return self.find_element(*self.printer_combobox)

    def click_on_edit_rates_and_services(self):
        self.wait_element(*self.edit_rate_and_services_btn)
        self.click_using_js(*self.edit_rate_and_services_btn)

    def select_usps_carries(self):
        options = self.find_elements(*self.carrier_combo_box)
        text = 'USPS'
        for option in options:
            dropdown_txt = option.text
            if text in dropdown_txt:
                option.click()
                break
        time.sleep(5)

    def choose_service(self):
        time.sleep(5)
        self.wait_element(*self.carrier_radio_btn)
        self.find_element(*self.carrier_radio_btn).click()

    def click_choose_service_btn(self):
        self.wait_for_element_to_be_clickable(*self.choose_service_apply_btn)
        self.click_using_js(*self.choose_service_apply_btn)

    def selectUSPScarrier(self):
        self.select_usps_carries()
        self.wait_element(*self.select_rates_service_button)
        self.click_using_js(*self.select_rates_service_button)
        self.choose_service()
        self.click_choose_service_btn()

    def select_cost_Account(self):
        self.wait_element(*self.cost_account_input)
        self.find_element(*self.cost_account_input).click()
        if self.find_element(*self.new_cost_to_account).is_displayed():
            self.find_element(*self.new_cost_to_account).click()

    def click_on_print_option(self):
        self.wait_element(*self.print_options_btn)
        self.click_using_js(*self.print_options_btn)

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

    def click_if_agreement_box_is_present(self):
        value = self.wait_element_till_time_limit(10, *self.agreement_checkbox_ups_privacy_act)
        if value:
            self.click_using_js(*self.agreement_checkbox_ups_privacy_act)

    def click_multiple_recipient(self):
        self.wait_element(*self.multiple_recepient)
        self.click_using_js(*self.multiple_recepient)

    def select_recipient(self, recipient):
        self.wait_element(*self.recipientList)
        self.find_element(*self.recipientList).send_keys(recipient)
        time.sleep(4)
        print(recipient)
        self.wait_element(By.XPATH, "//span[text()='" + recipient + "']")
        self.click_using_js(By.XPATH, "//span[text()='" + recipient + "']")

    def verify_if_address_is_validated(self):
        return self.wait_element_till_time_limit(30, *self.address_validation)

    def enter_len_width_height_weight(self, test_data):
        length = test_data['Length']
        width =  test_data['Width']
        height = test_data['Height']
        weight = test_data['Weight']
        self.wait_element(*self.length)
        self.find_element(*self.length).send_keys(length)
        self.find_element(*self.width).send_keys(width)
        self.find_element(*self.height).send_keys(height)
        self.find_element(*self.weight).send_keys(weight)
        self.custom_logger.info("Lenght, Width, height and weight is entered")

    def enter_len_height_weight(self, test_data):
        length = test_data['Length']
        height = test_data['Height']
        weight = test_data['Weight']
        self.wait_element(*self.length)
        self.find_element(*self.length).send_keys(length)
        self.find_element(*self.height).send_keys(height)
        self.find_element(*self.weight).send_keys(weight)
        self.custom_logger.info("Length, height and weight is entered")
    def enter_ounces(self, test_data):
        ounces = test_data['Ounces']
        self.wait_element(*self.ounces)
        self.find_element(*self.ounces).send_keys(ounces)
        self.custom_logger.info("Ounces is entered")

    def selectcarrier(self, test_data):
        self.select_carrier(test_data)
        time.sleep(1)
        self.enter_len_width_height_weight(test_data)
        self.wait_for_element_to_be_clickable(*self.select_service_button)
        self.click_using_js(*self.select_service_button)
        self.select_service(test_data)
        self.click_choose_service_btn()

    def custom_selectcarrier(self, carrier,test_data):
        options = self.find_elements(*self.carrier_combo_box)
        text = carrier
        for option in options:
            dropdown_txt = option.text
            print(dropdown_txt)
            if text in dropdown_txt:
                option.click()
                break
        time.sleep(2)
        #self.enter_len_width_height_weight(test_data)
        self.wait_for_element_to_be_clickable(*self.select_service_button)
        self.click_using_js(*self.select_service_button)
        time.sleep(5)
        print(carrier)
        time.sleep(30)
        self.wait_element(By.XPATH,
                          "(//input[@type='radio']//parent::span)[1]")
        self.find_element(By.XPATH,
                          "(//input[@type='radio']//parent::span)[1]").click()
        self.click_choose_service_btn()

    def close_shipping_rates_page(self):
        time.sleep(2)
        self.wait_element(*self.close_shipping_rates)
        self.click_using_js(*self.close_shipping_rates)

    def wait_for_batch_print_label_printed_msg(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)
        element_visible = self.wait_element_till_time_limit(160, *self.Label_successfully_printed)
        if element_visible:
            self.custom_logger.info("Actual print is success")
            return True
        else:
            self.click_on_X_button()
            return False

    def enter_cost_to_acnt(self, test_data):
        acntname = test_data['costToAccount']
        cost_to_acnt_txt = self.wait_element_till_time_limit(10, *self.cost_to_acnt_txt)
        if cost_to_acnt_txt:
            self.wait_element_till_time_limit(5, *self.cost_to_acnt_txt)
            self.find_element(*self.cost_to_acnt_txt).clear()
            self.find_element(*self.cost_to_acnt_txt).send_keys(acntname)
            time.sleep(3)
            choose_cost_acnt = self.wait_element_till_time_limit(5, *self.choose_cost_acnt)
            if choose_cost_acnt:
                self.click_using_js(*self.choose_cost_acnt)
            elif self.verify_if_element_is_visible(*self.choose_cost_acnt_sso):
                self.wait_element_till_time_limit(5, *self.choose_cost_acnt_sso)
                self.click_using_js(*self.choose_cost_acnt_sso)
            self.custom_logger.info("Cost to Account is Entered")

    def select_summary_receipt(self):
        if self.verify_if_element_is_visible(*self.print_summary_receipt):
            if not self.find_element(*self.print_summary_receipt).is_selected():
                self.click_using_js(*self.print_summary_receipt)
                self.custom_logger.info("Summary Receipt is Clicked")
                print("Summary Receipt is Clicked")

    def select_carrier(self, test_data):
        carrier_name = test_data['carrierName']
        options = self.find_elements(*self.carrier_combo_box)
        text = carrier_name
        for option in options:
            dropdown_txt = option.text
            print(dropdown_txt)
            if text in dropdown_txt:
                option.click()
                break
        time.sleep(6)

    def select_service(self, test_data):
        time.sleep(5)
        carrier_name = test_data['carrierName']
        print(carrier_name)
        time.sleep(30)
        self.wait_element(By.XPATH,
                          "(//input[contains(@id,'" + carrier_name + "') and @type='radio'])[1]")
        self.find_element(By.XPATH,
                          "(//input[contains(@id,'" + carrier_name + "') and @type='radio'])[1]").click()

    def click_use_preset(self):
        self.wait_element(*self.use_preset)
        self.click_using_js(*self.use_preset)

    def select_preset(self, roll_type, test_data):
        presetData_Label = test_data['presetData_Label']
        self.click_use_preset()
        self.wait_element(*self.txt_preset)
        self.click_using_js(*self.txt_preset)
        self.find_element(*self.txt_preset).send_keys(presetData_Label)
        self.wait_element(*self.selected_preset)
        self.click_using_js(*self.selected_preset)

    def click_multi_piece_label(self):
        self.wait_element(*self.multipiece_label)
        self.click_using_js(*self.multipiece_label)

    def click_add_multipiece_label_icon(self):
        self.wait_element(*self.add_multipiece_label_icon)
        self.click_using_js(*self.add_multipiece_label_icon)

    def add_multipiece_label(self, test_data):
        self.click_multi_piece_label()
        time.sleep(2)
        self.selectcarrier(test_data)
        self.click_add_multipiece_label_icon()
        time.sleep(10)

        self.click_multi_piece_label()
        time.sleep(2)
        self.selectcarrier(test_data)
        self.click_add_multipiece_label_icon()
        time.sleep(10)

    def check_certified_mail_header(self):
        return self.wait_element(*self.certified_mail_header)

    def click_priority_mail_link(self):
        self.wait_element(*self.priority_mail)
        self.click_using_js(*self.priority_mail)
        self.custom_logger.info("Clicked on Priority Mail")

    def select_address_from_address_book(self, test_data):
        self.wait_element(*self.address_book)
        self.click_on_address_book_pop_up()
       # self.wait_element(*self.address_book_pop_up)
        self.wait_element(*self.first_address)
        self.click_on_first_address_book()

    # self.wait_for_element_to_be_clickable(*self.print_options_btn)
    #  self.enter_cost_to_acnt(test_data)

    def click_on_address_book_pop_up(self):
        self.find_element(*self.address_book).click()
        self.custom_logger.info("Clicked on address box popup")

    def click_on_first_address_book(self):
        self.click_using_js(*self.first_address)
        self.custom_logger.info("Clicked on first Address")

    def select_printer_and_roll(self, get_env, test_data, roll_type):
        self.wait_element(*self.printer_combobox)
        self.click_on_printer_combo_box()
        select_printer = self.select_printer_from_dropdown(common_utils.get_system_name(get_env),
                                                           test_data)
        if select_printer:
            flg = self.check_print_size_is_enabled()
            if flg:
                self.click_on_print_size_combo_box()
                time.sleep(2)
                roll_selected = self.select_roll_type_from_dropdown(roll_type)
                return roll_selected
            else:
                return False
        else:
            return False

    def click_on_preview_rates(self):
        self.wait_element(*self.btn_preview_rates)
        self.find_element(*self.btn_preview_rates).click()
        self.custom_logger.info("Preview rates are clicked")

    def check_done_button_is_clickable(self):
        flg = self.wait_for_element_to_be_clickable(*self.done_btn)
        return flg

    def click_on_done_btn(self):
        self.custom_logger.info("Click on done button")
        self.wait_element(*self.done_btn)
        self.find_element(*self.done_btn).click()

    def check_print_cover_sheet_stampbtn_is_clickable(self):
        self.wait_for_element_to_be_clickable(*self.print_cover_sheet_stamp_btn)
        return True

    def click_print_cover_sheet_stampbtn(self):
        self.wait_element(*self.print_cover_sheet_stamp_btn)
        self.click_using_js(*self.print_cover_sheet_stamp_btn)
        self.custom_logger.info("Clicked on Print Cover sheet")

    def verify_success_msg_cover_sheet(self):
        try:
            self.wait_for_element_to_be_clickable(*self.sample_print_btn)
            self.click_on_X_button()
            self.custom_logger.info("Cover sheet is printed successfully")
            return True
        except:
            self.click_on_X_button()
            return False

    def verify_success_msg_cover_sheet_actual_print(self):
        visible = self.wait_element_till_time_limit(50,*self.success_msg_cover_sheet)
        self.custom_logger.info("Cover sheet is printed successfully")
        if not visible:
            self.click_on_X_button()
        return visible

    def check_summary_receipt(self, summary_receipt):
        if summary_receipt == 'yes':
            self.select_summary_receipt()

    def click_Ecertified_link(self):
        self.wait_element(*self.certified_label)
        self.click_using_js(*self.certified_label)
        self.custom_logger.info("Clicked on ECertified Label")

    def verify_sample_print_is_success_err(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(2)
        try:
            self.wait_for_element_to_be_clickable(*self.sample_print_btn)
            self.click_on_X_button()
            self.custom_logger.info("Sample print is success")
            return True
        except:
            button_cancel_visible = self.wait_element_till_time_limit(5, *self.btn_cancel)
            if button_cancel_visible:
                self.click_using_js(*self.btn_cancel)
                return False
            else:
                self.click_on_X_button()
                return False

    def select_coversheet_withbarcode(self, size):
        coversheet_path = (By.XPATH, "//input[@value='"+size+"']")
        self.wait_for_element_to_be_clickable(*coversheet_path)
        self.click_using_js(*coversheet_path)

    def click_on_cubic_soft_pack(self):
        self.wait_element(*self.cubic_soft_pak_link)
        self.click_using_js(*self.cubic_soft_pak_link)
        self.custom_logger.info("Clicked on Cubic Soft pack")

    def click_on_Flat_sending_option(self):
        self.wait_element(*self.Flat_link)
        self.click_using_js(*self.Flat_link)
        self.custom_logger.info("Clicked on Flat")


