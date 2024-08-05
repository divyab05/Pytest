import time
import pytest
from hamcrest import assert_that, equal_to
from FrameWorkUtilities.common_utils import common_utils
from UIObjects.DeviceHubObjects import DeviceHubObjectsClass
from UIObjects.SP360.SP360CreateShipRequestPageObjects import SP360CreateShipRequestObjectsClass
from UIObjects.SP360.SP360CreateShippingLabels import SP360CreateShippingLabelObjectsClass
from UIObjects.SP360.SP360PrintStampRollObjects import SP360PrintStampRollObjectsClass
from UIObjects.SP360.SP360StampEnvelope import SP360StampEnvelopeClass
from UIObjects.SP360.SP360StampSheets import SP360StampSheets
from UIObjects.UK.UKStampSheets import UKStampSheets


@pytest.fixture()
def resource(app_config):
    req = DeviceHubObjectsClass(app_config)
    yield req


class Test_common_function(common_utils):

    def click_on_header(self, setup_dh):
        assert_that(setup_dh.check_header_exists(), "Login Page is not Loaded")
        setup_dh.click_on_header()

    def add_stamp_roll_2x1_print(self, get_env, setup_dh, test_data, app_config, custom_logger, get_driver,
                                 change_layout):
        print_stamp_obj = SP360PrintStampRollObjectsClass(app_config, get_driver, custom_logger)
        self.click_on_header(setup_dh)
        stamp_roll_added = print_stamp_obj.add_stamp_roll(setup_dh, test_data, custom_logger)
        assert_that(stamp_roll_added, "StampRoll is not added")
        assert_that(print_stamp_obj.check_row_added(), "row is not added")
        assert_that(print_stamp_obj.check_print_options_btn(), "Print Option button is not present")
        print_stamp_obj.click_on_print_options()
        layout_selected = print_stamp_obj.select_layout(change_layout)
        assert_that(layout_selected, "The layout option is not available")
        printer_selected = print_stamp_obj.select_printer_for_roll(get_env, test_data)
        assert_that(printer_selected, "Printer name is not present in the list")
        return SP360PrintStampRollObjectsClass(app_config, get_driver, custom_logger)

        # This function is used to Test print Roll

    def verify_2X1_stamp_roll_test_print(self, get_env, setup_dh, test_data, app_config, custom_logger, get_driver,
                                         change_layout):
        print_stamp_obj = self.add_stamp_roll_2x1_print(get_env, setup_dh, test_data, app_config, custom_logger,
                                                        get_driver, change_layout)
        print_stamp_obj.click_on_test_print_btn()
        printer_selected = print_stamp_obj.select_printer_after_clicking_print_btn(get_env, test_data)
        assert_that(printer_selected, "Printer is not selected or printer is not in the list")
        print_stamp_obj.click_done_or_test_print_btn()
        assert_that(print_stamp_obj.check_print_stamp_success_pop_up(), "Stamp is not printed successfully")
        assert_that(print_stamp_obj.check_done_button_is_clickable(), "Done button is not  present")
        print_stamp_obj.click_on_done_btn()

        # This function is used to print Roll

    def verify_2X1_stamp_roll_actual_print(self, get_env, setup_dh, test_data, app_config, custom_logger, get_driver,
                                           change_layout, batchprint):
        print_stamp_obj = self.add_stamp_roll_2x1_print(get_env, setup_dh, test_data, app_config, custom_logger,
                                                        get_driver, change_layout)
        assert_that(print_stamp_obj.check_actual_print_btn_is_enabled(), "Actual print button is not enabled")
        print_stamp_obj.click_on_print_btn()
        printer_selected = print_stamp_obj.select_printer_after_clicking_print_btn(get_env, test_data)
        assert_that(printer_selected, "Printer is not selected or printer is not in the list")
        print_stamp_obj.click_on_printStamps_btn()
        assert_that(print_stamp_obj.check_stamp_print_success_message(batchprint), "Stamp Roll print is not successful")

    def stamp_sheet_add_printer(self, get_env, setup_dh, test_data, app_config, get_driver, custom_logger):
        print_stamp_obj = SP360StampSheets(app_config, get_driver, custom_logger)
        self.click_on_header(setup_dh)
        stamp_sheet_added = print_stamp_obj.add_stamp_sheet(setup_dh, custom_logger)
        assert_that(stamp_sheet_added, "row is not added")
        assert_that(print_stamp_obj.check_print_options_btn(), "Print Option button is not present")
        print_stamp_obj.click_on_print_options()
        time.sleep(2)
        printer_selected = print_stamp_obj.select_printer_for_sheet(get_env, test_data)
        assert_that(printer_selected, "Printer name is not present in the list")
        return SP360StampSheets(app_config, get_driver, custom_logger)

    def add_envelope_for_print(self, setup_dh, test_data, app_config, custom_logger, get_driver,
                               size):
        print_stamp_obj = SP360StampEnvelopeClass(app_config, custom_logger, get_driver)
        self.click_on_header(setup_dh)
        print_stamp_obj.add_stamp_envelope(setup_dh, size, test_data, custom_logger)
        assert_that(print_stamp_obj.check_row_added(), "row is not added")
        return SP360StampEnvelopeClass(app_config, custom_logger, get_driver)

    # This function is used to Test print envelope
    def verify_stamp_envelope_size_test_print(self, get_env, setup_dh, test_data, app_config, custom_logger, get_driver,
                                              size):
        print_stamp_obj = self.add_envelope_for_print(setup_dh, test_data, app_config, custom_logger, get_driver,
                                                      size)
        assert_that(print_stamp_obj.get_envelope_test_print_btn(), "Test Print button is not present")
        print_stamp_obj.click_test_envelope_btn()
        if print_stamp_obj.verify_preview_test_print_visible():
            printer_selected = print_stamp_obj.select_printer_for_envelope(get_env, test_data)
            assert_that(printer_selected, "Printer name is not present in the list or printer combo box is not present")
            print_stamp_obj.click_preview_test_print()
        print_stamp_obj.click_test_print_test_btn()
        assert_that(print_stamp_obj.verify_test_print(), "Test Print for Envelope is not success")

        # This function is used to print envelope

    def verify_stamp_envelope_actual_print(self, get_env, setup_dh, test_data, app_config, custom_logger, get_driver,
                                           get_product_name,
                                           size, batchprint):
        sys_name = common_utils.get_system_name(get_env)
        print_stamp_obj = self.add_envelope_for_print(setup_dh, test_data, app_config, custom_logger, get_driver,
                                                      size)
        print_stamp_obj.click_cost_to_account(get_product_name, test_data)
        assert_that(print_stamp_obj.check_actual_envelope_print(), "Actual print button is not enabled")
        time.sleep(1)
        print_stamp_obj.click_actual_envelope_print()
        assert_that(print_stamp_obj.check_actual_envelope_print_printoption(),
                    "Actual print button in print option page is not enabled")
        print_stamp_obj.click_on_printer_combo_box()
        printer_selected = print_stamp_obj.select_printer_from_dropdown(sys_name, test_data)
        assert_that(printer_selected, "Printer name is not present in the list or printer combo box is not present")
        print_stamp_obj.click_actual_envelope_print_printoption()
        assert_that(print_stamp_obj.check_stamp_print_success_message(batchprint),
                    "Envelope print is not successful")

    # this function is used to activate DH from UI and verify if Device is online
    def activate_DH(self, setup_dh, get_env, custom_logger, get_product_name):
        sys_name = common_utils.get_system_name(get_env)
        self.click_on_header(setup_dh)
        setup_dh.click_on_menu_item()
        custom_logger.info("Clicked Settings Icon")
        assert_that(setup_dh.check_my_device_link_exists(), "My Device Link is not Present")
        my_device_page = setup_dh.click_on_my_device()
        custom_logger.info("My Device is clicked")
        assert_that(my_device_page.check_my_device_header_exists(), "My Device Text is not Displayed")
        custom_logger.info("My Device Text is Displayed")
        my_device_page.get_my_devices_header()
        assert_that(my_device_page.check_activate_dh_btn_exists(), "Activate Dh button is not present")
        assert_that(my_device_page.verify_DH_regiestring_msg(), "DH Registration message is not displayed")
        #assert_that(my_device_page.verify_DH_auto_activated(), "DH is not Registered")
        assert_that(my_device_page.dh_registed_toastermsg(), "DH Registered Toaster message is not displayed")
        custom_logger.info("DH Registered toaster message is displayed")
        assert_that(my_device_page.check_my_device_header_exists(), "Device Header is not present")
        time.sleep(5)
        my_device_page.refresh_manage_device_page()
        custom_logger.info("Clicked on refresh")
        my_device_page.wait_for_first_device_after_refresh()
        dh_results = my_device_page.check_dh_name_in_table(sys_name)
        assert_that(dh_results['status'], "DH status is not present")
        assert_that(dh_results['dh_status'], equal_to("Online"), 'DH status is not online')
        custom_logger.info("Device Hub status is online")

    def manual_activate_DH(self, setup_dh, get_env, custom_logger, get_product_name):
        sys_name = common_utils.get_system_name(get_env)
        self.click_on_header(setup_dh)
        setup_dh.click_on_menu_item()
        custom_logger.info("Clicked Settings Icon")
        assert_that(setup_dh.check_my_device_link_exists(), "My Device Link is not Present")
        my_device_page = setup_dh.click_on_my_device()
        custom_logger.info("My Device is clicked")
        assert_that(my_device_page.check_my_device_header_exists(), "My Device Text is not Displayed")
        custom_logger.info("My Device Text is Displayed")
        my_device_page.get_my_devices_header()
        assert_that(my_device_page.check_activate_dh_btn_exists(), "Activate Dh button is not present")
        my_device_page.click_on_activate_dh()
        custom_logger.info("Activate Device button is clicked")
        if get_product_name == 'fedramp':
            assert_that(my_device_page.check_activate_button_on_dh_pop_up(), "Activate Dh button on popup is not present")
            assert_that(my_device_page.check_downloadDH_button_on_dh_pop_up(), "Download DH button is not Present")
            my_device_page.click_activate_dh_pop_up()
            my_device_page.check_dh_activated()
            assert_that(my_device_page.verify_DH_RegistrationMsg(), "DH is not Registered")
            assert_that(my_device_page.verify_CloseAndContinue_button(), "Close and Continue button is not present")
            my_device_page.clickon_close_and_continue_button()
            custom_logger.info("Click and close button is clicked")
        else :
            assert_that(my_device_page.dh_registed_toastermsg(), "DH Registered Toaster message is not displayed")
        assert_that(my_device_page.check_my_device_header_exists(), "Device Header is not present")
        time.sleep(5)
        my_device_page.refresh_manage_device_page()
        custom_logger.info("Clicked on refresh")
        my_device_page.wait_for_first_device_after_refresh()
        dh_results = my_device_page.check_dh_name_in_table(sys_name)
        assert_that(dh_results['status'], "DH status is not present")
        assert_that(dh_results['dh_status'], equal_to("Online"), 'DH status is not online')
        custom_logger.info("Device Hub status is online")

    # This Function is to only verify the device is online in UI
    def verify_DH_is_Online(self, setup_dh, get_env, custom_logger):
        sys_name = common_utils.get_system_name(get_env)
        assert_that(setup_dh.check_sp360_menu_item(), "Check PSPro UI menu item exists")
        setup_dh.click_on_menu_item()
        custom_logger.info("Clicked Settings Icon")
        my_device_page = setup_dh.click_on_my_device()
        custom_logger.info("My Device is clicked")
        my_device_page.refresh_manage_device_page()
        custom_logger.info("Clicked on refresh")
        my_device_page.wait_for_first_device_after_refresh()
        dh_results = my_device_page.check_dh_name_in_table(sys_name)
        assert_that(dh_results['status'], "DH status is not present")
        assert_that(dh_results['dh_status'], equal_to("Online"), 'DH status is not online')
        custom_logger.info("Device Hub status is online")

    # This function is used to Test print Label
    def verify_shipping_sample_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                           get_driver, test_data, get_product_name, roll_type, check_receipt):
        shipping_label_obj = self.select_printer(get_env, setup_dh, app_config, custom_logger,
                                                 get_driver, test_data, get_product_name, roll_type, check_receipt)
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_sample_print_is_success(),
                    "Test Print is not success")

    def select_printer(self, get_env, setup_dh, app_config, custom_logger,
                       get_driver, test_data, get_product_name, roll_type, check_receipt):
        self.click_on_header(setup_dh)
        setup_dh.click_on_shipping_label()
        assert_that(setup_dh.check_ship_another_label_btn_exists(), "Ship another link does not exist")
        setup_dh.scroll_to_ship_another_label()
        shipping_label_obj = setup_dh.click_on_ship_another_label()
        assert_that(shipping_label_obj.check_edit_rate_and_services_btn_loaded(),
                    "Edit Rate and Services Button is not Loaded")
        time.sleep(2)
        if check_receipt == "Yes":
            shipping_label_obj.selectUSPScarrier()
        shipping_label_obj.click_if_agreement_box_is_present()
        assert_that(shipping_label_obj.check_print_shipping_label_is_clickable(), "Print Shipping label is not present")
        shipping_label_obj.click_on_print_option()
        assert_that(shipping_label_obj.check_printer_combo_box(), "Printer combo box is not present")
        printer_selected = shipping_label_obj.select_printer_and_roll(get_env, test_data, roll_type)
        assert_that(printer_selected, "Printer name  or Roll type is not present in the list")
        if check_receipt == "Yes":
            shipping_label_obj.check_receipt_shipping_label()
        return SP360CreateShippingLabelObjectsClass(app_config, get_driver, custom_logger)

    def click_on_print_options_and_select_printer(self, shipping_label_obj, get_env, test_data, roll_type,
                                                  check_receipt):
        assert_that(shipping_label_obj.check_print_shipping_label_is_clickable(), "Print Shipping label is not present")
        shipping_label_obj.click_on_print_option()
        assert_that(shipping_label_obj.check_printer_combo_box(), "Printer combo box is not present")
        shipping_label_obj.click_on_printer_combo_box()
        printer_selected = shipping_label_obj.select_printer_and_roll(get_env, test_data, roll_type)
        assert_that(printer_selected, "Printer name  or Roll type is not present in the list")
        if check_receipt == "Yes":
             shipping_label_obj.check_receipt_shipping_label()

    # This function is used to  print Label
    def verify_shipping_actual_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                           get_driver, test_data, get_product_name, roll_type, check_receipt):

        shipping_label_obj = self.select_printer(get_env, setup_dh, app_config, custom_logger,
                                                 get_driver, test_data, get_product_name, roll_type, check_receipt)
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")

    # This function is used to Re print Label
    def click_and_verify_reprint(self, app_config, get_driver, custom_logger, get_env, test_data):
        time.sleep(2)
        shipping_label_obj = SP360CreateShippingLabelObjectsClass(app_config, get_driver, custom_logger)
        assert_that(shipping_label_obj.check_re_print_link_present(),
                    "RePrint link is not present")
        shipping_label_obj.click_re_print_link()
        printer_combobox_present = shipping_label_obj.check_printer_combo_box()
        if printer_combobox_present:
            # assert_that(shipping_label_obj.check_printer_combo_box(), "Printer combo box is not present")
            shipping_label_obj.click_on_printer_combo_box()
            shipping_label_obj.select_printer_from_dropdown(common_utils.get_system_name(get_env), test_data)
        shipping_label_obj.click_agreement_checkbox()
        assert_that(shipping_label_obj.check_reprint_btn_is_enabled(), "Reprint button is not enabled")
        shipping_label_obj.click_on_reprint_buttton()
        assert_that(shipping_label_obj.verify_re_print_is_success(),
                    "Label is not re printed successfully")

    def print_shipping_req(self, get_env, app_config, custom_logger,
                           get_driver, test_data, roll_type):
        ship_request_obj = SP360CreateShipRequestObjectsClass(app_config, get_driver, custom_logger)
        ship_request_obj.select_address_from_address_book(test_data)
        selected_printer = ship_request_obj.select_printer(test_data, get_env, roll_type)
        assert_that(selected_printer, "Printer is not selected or printer is not in the list")
        ship_request_obj.click_on_print_btn_on_print_options()
        assert_that(ship_request_obj.verify_txt_print_shipping_request(),
                    "Shipping request is not  printed successfully")
        shipping_label_obj = SP360CreateShippingLabelObjectsClass(app_config, get_driver, custom_logger)
        assert_that(shipping_label_obj.check_re_print_link_present(),
                    "RePrint link is not present")
        shipping_label_obj.click_re_print_link()
        assert_that(ship_request_obj.check_printer_combo_box(), "Printer is not present")
        ship_request_obj.click_on_printer_combo_box()
        selected_printer = ship_request_obj.select_printer_from_dropdown(common_utils.get_system_name(get_env),
                                                                         test_data)
        if selected_printer:
            ship_request_obj.click_reprint_btn()
        else:
            assert_that(selected_printer, "Printer is not selected or printer is not in the list")
        assert_that(shipping_label_obj.verify_re_print_is_success(),
                    "Label is not re printed successfully")

    def click_on_mydevice_header(self, setup_dh, custom_logger):
        assert_that(setup_dh.check_sp360_menu_item(), "Check PSPro UI menu item does exists")
        setup_dh.click_on_menu_item()
        custom_logger.info("Clicked on Settings")
        assert_that(setup_dh.check_my_device_link_exists(), "Check My Devices link is not present")
        my_device_page = setup_dh.click_on_my_device()
        custom_logger.info("Clicked on My Device Link")
        assert_that(my_device_page.check_my_device_header_exists(), "Check My Devices page header is not present")
        my_device_page.get_my_devices_header()

    def selectMultipleRecipient(self, get_env, setup_dh, custom_logger, test_data, roll_type,
                                 check_summary_receipt):
        recipient = test_data['Recipient']
        self.click_on_header(setup_dh)
        shipping_label_obj = setup_dh.click_shipping_label()
        shipping_label_obj.click_multiple_recipient()
        time.sleep(2)
        shipping_label_obj.select_recipient(recipient)
        assert_that(shipping_label_obj.verify_if_address_is_validated,
                    "multiple recipients list is selected and address is validated")
        time.sleep(2)
        shipping_label_obj.enter_cost_to_acnt(test_data)
        shipping_label_obj.selectcarrier(test_data)
        shipping_label_obj.close_shipping_rates_page()
        time.sleep(3)
        self.click_on_print_options_and_select_printer_label(shipping_label_obj, get_env, test_data, roll_type)
        if check_summary_receipt == 'yes':
            shipping_label_obj.select_summary_receipt()
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.wait_for_batch_print_label_printed_msg(), "Label is not printed successfully")

    def click_on_print_options_and_select_printer_label(self, shipping_label_obj, get_env, test_data, roll_type):

        assert_that(shipping_label_obj.check_print_shipping_label_is_clickable(), "Print Shipping label is not present")
        shipping_label_obj.click_on_print_option()
        assert_that(shipping_label_obj.check_printer_combo_box(), "Printer combo box is not present")
        printer_roll_selected = shipping_label_obj.select_printer_and_roll(get_env, test_data, roll_type)
        assert_that(printer_roll_selected, "Printer name or Roll is not present in the list")

    def send_parcel_label_and_select_printer(self, get_env, setup_dh, app_config, custom_logger,
                                             get_driver, test_data, get_product_name, roll_type):
        self.click_on_header(setup_dh)
        setup_dh.click_on_shipping_label()
        assert_that(setup_dh.check_create_shipping_label_btn(), "Create Shipping label button  does not exist")
        shipping_label_obj = setup_dh.click_on_create_label_btn()
        shipping_label_obj.select_preset(roll_type, test_data)
        assert_that(shipping_label_obj.check_edit_rate_and_services_btn_loaded(),
                    "Edit Rate and Services Button is not Loaded")
        assert_that(shipping_label_obj.check_print_shipping_label_is_clickable(),
                    "Print Shipping label is not present")
        shipping_label_obj.click_on_print_option()
        assert_that(shipping_label_obj.check_printer_combo_box(), "Printer combo box is not present")
        shipping_label_obj.click_on_printer_combo_box()
        select_printer = shipping_label_obj.select_printer_from_dropdown(common_utils.get_system_name(get_env),
                                                                         test_data)
        if select_printer:
            flg = shipping_label_obj.check_print_size_is_enabled()
            if flg:
                shipping_label_obj.click_on_print_size_combo_box()
                assert_that(shipping_label_obj.select_roll_type_from_dropdown(roll_type),
                            "Roll is not Selected or not present")
        else:
            assert_that(select_printer, "Printer name is not present in the list")
        return SP360CreateShippingLabelObjectsClass(app_config, get_driver, custom_logger)

    def verify_postage_stampsheet_header(self, setup_dh, get_product_name):
        self.click_on_header(setup_dh)
        assert_that(setup_dh.check_send_a_letter_link(), "Send a letter link is not  present")
        time.sleep(2)
        setup_dh.click_send_a_letter_link()
        assert_that(setup_dh.check_postage_sheet_link_exists(), "Postage sheet link  is not present")
        print_stamp_obj = setup_dh.click_on_postage_sheet_link()
        assert_that(print_stamp_obj.check_print_postage_sheet_header_exists(),
                    " Print Postage  sheet header is not present")
        return print_stamp_obj

    def postage_click_actual_print(self, get_env, test_data, app_config, get_driver, custom_logger):
        sys_name = common_utils.get_system_name(get_env)
        print_stamp_obj = UKStampSheets(app_config, get_driver, custom_logger)
        assert_that(print_stamp_obj.postage_check_print_options_btn(), "Print Option button is not present")
        print_stamp_obj.click_print_postage_button()
        assert_that(print_stamp_obj.postage_check_printer_combo_box(), "printer combo box is not present")
        print_stamp_obj.enter_printer_name(test_data)
        selected_printer = print_stamp_obj.postage_select_printer_from_dropdown(sys_name, test_data)
        if selected_printer:
            print_stamp_obj.postage_click_print_option_print_button()
        else:
            assert_that(selected_printer, "Printer is not selected or printer is not in the list")
        return UKStampSheets(app_config, get_driver, custom_logger)

    def verify_postage_roll_header(self, setup_dh, get_product_name):
        self.click_on_header(setup_dh)
        assert_that(setup_dh.check_send_a_letter_link(), "Send a letter link is not  present")
        setup_dh.click_send_a_letter_link()
        assert_that(setup_dh.check_postage_roll_btn_exists(), "Postage Roll link  is not present")
        print_stamp_obj = setup_dh.click_on_postage_roll_btn()
        assert_that(print_stamp_obj.check_print_postage_roll_header_exists(),
                    "Print Postage Roll header is not present")
        return print_stamp_obj

    def verify_postage_envelope_header(self, setup_dh, get_product_name):
        self.click_on_header(setup_dh)
        assert_that(setup_dh.check_send_a_letter_link(), "Send a letter link is not  present")
        time.sleep(2)
        setup_dh.click_send_a_letter_link()
        assert_that(setup_dh.check_postage_envelope_link_exists(), "Postage Envelope link  is not present")
        print_stamp_obj = setup_dh.click_on_postage_envelope_link()
        assert_that(print_stamp_obj.check_print_postage_envelope_header_exists(),
                    "Print Postage envelope header is not present")
        return print_stamp_obj

    def verify_scale_functionality(self, print_stamp_obj, get_env, test_data):
        assert_that(print_stamp_obj.check_scale_btn_is_present(), "Scale button is not enabled")
        assert_that(print_stamp_obj.check_select_scale_drpdwn_btn(), "Scale dropdown is not clickable")
        print_stamp_obj.click_on_select_scale_drpdown()
        print_stamp_obj.select_scale_from_dropdown(common_utils.get_system_name(get_env), test_data)
        print_stamp_obj.click_on_get_Weight_from_scale_btn()
        assert_that(print_stamp_obj.check_fetching_weight_txt(), "Fetching Weight test is not present")
        assert_that(print_stamp_obj.check_get_weight_btn_enabled(), "Get weight button is not enabled")
        time.sleep(1)
        assert_that(print_stamp_obj.check_set_scale_to_zero_btn(), "Scale set to zero button is not present")
        print_stamp_obj.click_scale_set_to_zero_btn()
        assert_that(print_stamp_obj.check_zeroing_scale_txt(), "Zeroing scale text is not present")
        assert_that(print_stamp_obj.check_get_weight_btn_enabled(), "Get weight button is not enabled")
        time.sleep(1)

    def actual_print_err_shipping_label(self, setup_dh, test_data, get_env, roll_type, link,sending_option, summary_receipt):
        assert (setup_dh.check_err_or_certifiedmail_link(link), "ERR or Certified mail link is not present")
        shipping_label_obj = self.verify_certified_mail_header(setup_dh, link)
        shipping_label_obj.click_priority_mail_link()
        shipping_label_obj.select_address_from_address_book(test_data)
        if sending_option == "Cubic Soft Pack":
            shipping_label_obj.click_on_cubic_soft_pack()
            shipping_label_obj.enter_len_height_weight(test_data)
        else:
            shipping_label_obj.enter_len_width_height_weight(test_data)
        assert_that(shipping_label_obj.check_print_shipping_label_is_clickable(), "Shipping label is not cickable")
        shipping_label_obj.click_on_print_Shipping_label()
        shipping_label_obj.check_summary_receipt(summary_receipt)
        shipping_label_obj.select_printer_and_roll(get_env, test_data, roll_type)
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")

    def sample_print_err_shipping_label(self, setup_dh, test_data, get_env, roll_type, link,sending_option, summary_receipt):
        assert (setup_dh.check_err_or_certifiedmail_link(link), "ERR or Certified mail link is not present")
        shipping_label_obj = self.verify_certified_mail_header(setup_dh, link)
        shipping_label_obj.click_priority_mail_link()
        shipping_label_obj.select_address_from_address_book(test_data)
        time.sleep(2)
        if sending_option == "Cubic Soft Pack":
            shipping_label_obj.click_on_cubic_soft_pack()
            shipping_label_obj.enter_len_height_weight(test_data)

        else:
            shipping_label_obj.enter_len_width_height_weight(test_data)
        assert_that(shipping_label_obj.check_print_shipping_label_is_clickable(), "Shipping label is not cickable")
        shipping_label_obj.click_on_print_Shipping_label()
        shipping_label_obj.check_summary_receipt(summary_receipt)
        shipping_label_obj.select_printer_and_roll(get_env, test_data, roll_type)
        shipping_label_obj.click_on_sample_print()
        time.sleep(3)
        assert_that(shipping_label_obj.verify_sample_print_is_success_err(),
                    "Test Print is not success")



    def select_err_batch_printing_details(self, setup_dh, test_data, app_config, get_driver, custom_logger, link,sending_option):
        recipient = test_data['Recipient']
        shipping_label_obj = self.verify_certified_mail_header(setup_dh, link)
        shipping_label_obj.click_multiple_recipient()
        time.sleep(1)
        shipping_label_obj.click_priority_mail_link()
        time.sleep(1)
        shipping_label_obj.select_recipient(recipient)
        assert_that(shipping_label_obj.verify_if_address_is_validated(),
                    "multiple recipients list is selected and address is validated")
        time.sleep(1)
        shipping_label_obj.enter_cost_to_acnt(test_data)
        if sending_option == "Cubic Soft Pack":
            shipping_label_obj.click_on_cubic_soft_pack()
            shipping_label_obj.enter_len_height_weight(test_data)

        else:
            shipping_label_obj.enter_len_width_height_weight(test_data)
        #shipping_label_obj.enter_len_width_height_weight(test_data)
        time.sleep(2)
        shipping_label_obj.click_on_preview_rates()
        assert (shipping_label_obj.check_done_button_is_clickable, "Done Button is not clickable")
        shipping_label_obj.click_on_done_btn()
        return SP360CreateShippingLabelObjectsClass(app_config, get_driver, custom_logger)

    def select_certifiedmail_batch_printing_details(self, setup_dh, test_data, app_config, get_driver, custom_logger,
                                                    link):
        recipient = test_data['Recipient']
        shipping_label_obj = self.verify_certified_mail_header(setup_dh, link)
        shipping_label_obj.click_multiple_recipient()
        time.sleep(1)
        shipping_label_obj.click_Ecertified_link()
        time.sleep(1)
        shipping_label_obj.click_priority_mail_link()
        shipping_label_obj.select_recipient(recipient)
        assert_that(shipping_label_obj.verify_if_address_is_validated(),
                    "multiple recipients list is selected and address is not validated")
        time.sleep(1)
        shipping_label_obj.enter_cost_to_acnt(test_data)
        shipping_label_obj.enter_len_width_height_weight(test_data)
        time.sleep(2)
        shipping_label_obj.click_on_preview_rates()
        assert (shipping_label_obj.check_done_button_is_clickable, "Done Button is not clickable")
        shipping_label_obj.click_on_done_btn()
        return SP360CreateShippingLabelObjectsClass(app_config, get_driver, custom_logger)

    def verify_certified_mail_header(self, setup_dh, link):
        self.click_on_header(setup_dh)
        setup_dh.click_on_shipping_and_mailing()
        if link == "Certified Mail":
            shipping_label_obj = setup_dh.click_on_certified_mail_link()
        else:
            shipping_label_obj = setup_dh.click_on_create_err_link()
        assert_that(shipping_label_obj.check_certified_mail_header(), "Certified mail Header is not present")
        return shipping_label_obj

    def select_printer_for_cover_sheet(self, setup_dh, test_data, get_env, link,size,sending_option):
        shipping_label_obj = self.verify_certified_mail_header(setup_dh, link)
        shipping_label_obj.select_address_from_address_book(test_data)
        if sending_option == "Flat":
            shipping_label_obj.click_on_Flat_sending_option()
            time.sleep(2)
        shipping_label_obj.enter_ounces(test_data)
        assert_that(shipping_label_obj.check_print_cover_sheet_stampbtn_is_clickable(),
                    "Shipping label is not clickable")
        shipping_label_obj.select_coversheet_withbarcode(size)
        shipping_label_obj.click_print_cover_sheet_stampbtn()
        shipping_label_obj.select_printer_and_roll(get_env, test_data, roll_type='8x11')
        return shipping_label_obj

    def add_sheet_and_verify_actual_print_uk(self, print_stamp_obj, setup_dh, custom_logger, get_env, test_data):
        postage_sheet_added = print_stamp_obj.postage_add_sheet()
        assert_that(postage_sheet_added, "Postage Sheet is not added")
        print_stamp_obj.postage_click_actual_print()
        custom_logger.info("Clicked on Actual Print")
        printer_selected = print_stamp_obj.select_printer(get_env, test_data)
        assert_that(printer_selected, "Printed is not Selected or not present in the list")
        print_stamp_obj.postage_click_print_option_print_button()
        custom_logger.info("Clicked on Print Option Button")
        assert_that(print_stamp_obj.verify_toaster_message(), "Stamp Sheet is not Printed")
        assert_that(setup_dh.check_postage_sheet_link_exists(),
                    "Postage  sheet Link is not present")

    def add_envelope_and_verify_actual_print(self, print_stamp_obj, setup_dh, custom_logger, get_env, test_data):
        postage_envelope_added = print_stamp_obj.postage_add_envelope()
        assert_that(postage_envelope_added, "Envelope is not added")
        print_stamp_obj.postage_click_actual_print()
        custom_logger.info("Clicked on Actual Print")
        printer_selected = print_stamp_obj.select_printer(get_env, test_data)
        assert_that(printer_selected, "Printed is not Selected or not present in the list")
        print_stamp_obj.postage_click_on_print_button()
        custom_logger.info("Clicked on Print Option Button")
        assert_that(print_stamp_obj.verify_toaster_message())
        assert_that(setup_dh.check_postage_envelope_link_exists(),
                    "Postage Envelope link is not Present")

    def add_postageroll_and_verify_actual_print(self, print_stamp_obj, setup_dh, custom_logger, get_env, test_data):
        postage_roll_added = print_stamp_obj.postage_add_roll()
        assert_that(postage_roll_added, "Postage roll is not added")
        print_stamp_obj.postage_click_actual_print()
        custom_logger.info("Clicked on Actual Print")
        printer_selected = print_stamp_obj.select_printer(get_env, test_data)
        assert_that(printer_selected, "Printed is not Selected or not present in the list")
        print_stamp_obj.postage_click_print_option_print_button()
        custom_logger.info("Clicked on Print Option Button")
        assert_that(print_stamp_obj.verify_toaster_message())
        assert_that(setup_dh.check_postage_roll_btn_exists(),
                    " Print Postage sheet links is not present")

    def verify_shipping_sample_label_print_with_custom_carrier(self, get_env, setup_dh, app_config, custom_logger,
                                           get_driver, test_data,roll_type,carrier):
        shipping_label_obj = self.create_shipping_label_with_custom_carrier_and_select_printer(app_config, get_driver, setup_dh, custom_logger, get_env, test_data,roll_type,carrier)
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_sample_print_is_success(),
                    "Test Print is not success")
    def verify_actual_shipping_label_print_with_custom_carrier(self, get_env, setup_dh, app_config, custom_logger,
                                           get_driver, test_data,roll_type,carrier):
        shipping_label_obj = self.create_shipping_label_with_custom_carrier_and_select_printer(app_config, get_driver,
                                                                                               setup_dh, custom_logger,
                                                                                               get_env, test_data,roll_type, carrier)
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")

    def create_shipping_label_with_custom_carrier_and_select_printer(self,app_config, get_driver, setup_dh, custom_logger, get_env, test_data,roll_type,carrier):

        self.click_on_header(setup_dh)
        setup_dh.click_on_shipping_label()
        assert_that(setup_dh.check_ship_another_label_btn_exists(), "Ship another link does not exist")
        setup_dh.scroll_to_ship_another_label()
        shipping_label_obj = setup_dh.click_on_ship_another_label()
        time.sleep(2)
        shipping_label_obj.custom_selectcarrier(carrier,test_data)
        shipping_label_obj.enter_cost_to_acnt(test_data)
        shipping_label_obj.click_if_agreement_box_is_present()
        assert_that(shipping_label_obj.check_print_shipping_label_is_clickable(), "Print Shipping label is not present")
        shipping_label_obj.click_on_print_option()
        assert_that(shipping_label_obj.check_printer_combo_box(), "Printer combo box is not present")
        printer_selected = shipping_label_obj.select_printer_and_roll(get_env, test_data, roll_type)
        assert_that(printer_selected, "Printer name  or Roll type is not present in the list")
        return SP360CreateShippingLabelObjectsClass(app_config, get_driver, custom_logger)





