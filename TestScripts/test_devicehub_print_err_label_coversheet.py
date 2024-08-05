import time

import pytest
from hamcrest import assert_that

from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function import Test_common_function
from UIObjects.SP360.SP360CreateShippingLabels import SP360CreateShippingLabelObjectsClass


class Test_DeviceHub_shipping_label(Test_common_function):

    @pytest.mark.errlabel
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(22)
    def test_verify_8X11_shipping_sample_err_label_sample_print_with_receipt(self, get_env, setup_dh, app_config,
                                                                             custom_logger,
                                                                             get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.sample_print_err_shipping_label(setup_dh, test_data[0], get_env, roll_type='8x11',link="ERR link",sending_option="Package",summary_receipt="yes")


    @pytest.mark.errlabel
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(22)
    def test_verify_8X11_shipping_actual_err_label_print_with_receipt(self, get_env, setup_dh, app_config,
                                                                      custom_logger,
                                                                      get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.actual_print_err_shipping_label(setup_dh, test_data[0], get_env, roll_type='8x11',link="ERR link",sending_option="Package",summary_receipt="yes")

        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.errlabel
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(22)
    def test_verify_4x6_shipping_sample_err_label_sample_print_with_receipt(self, get_env, setup_dh, app_config,
                                                                            custom_logger,
                                                                            get_driver, get_product_name):

        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.sample_print_err_shipping_label(setup_dh, test_data[0], get_env,roll_type='4x6',link="ERR link",sending_option="Package",summary_receipt="yes")

    @pytest.mark.errlabel
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(22)
    def test_verify_4x6_shipping_actual_err_label_print_with_receipt(self, get_env, setup_dh, app_config,
                                                                     custom_logger,
                                                                     get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.actual_print_err_shipping_label(setup_dh, test_data[0], get_env, roll_type='4x6',link ="ERR link",sending_option="Package",summary_receipt="yes")

        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.errbatchprint
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(25)
    def test_verify_err_4X6_shipping_batchprinting_label_print(self, get_env, app_config, setup_dh,
                                                               custom_logger, get_driver,
                                                               get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        shipping_label_obj = self.select_err_batch_printing_details(setup_dh, test_data[0], app_config, get_driver,
                                                                    custom_logger,link="ERR link",sending_option="Package")
        assert_that(shipping_label_obj.check_print_shipping_label_is_clickable, "Shipping label is not clickable")
        shipping_label_obj.click_on_print_Shipping_label()
        shipping_label_obj.select_printer_and_roll(get_env, test_data[0], roll_type='4x6')
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.wait_for_batch_print_label_printed_msg(), "Label is not printed successfully")

    @pytest.mark.errbatchprint
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(25)
    def test_verify_err_8x11_shipping_batchprinting_label_print(self, get_env, app_config, setup_dh,
                                                                custom_logger, get_driver,
                                                                get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_err_batch_printing_details(setup_dh, test_data[0], app_config, get_driver,
                                                                    custom_logger,link="ERR link",sending_option="Package")
        assert_that(shipping_label_obj.check_print_shipping_label_is_clickable, "Shipping label is not clickable")
        shipping_label_obj.click_on_print_Shipping_label()
        shipping_label_obj.select_printer_and_roll(get_env, test_data[0], roll_type='8x11')
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.wait_for_batch_print_label_printed_msg(), "Label is not printed successfully")

    @pytest.mark.errcoversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(27)
    def test_verify_8x11_err_cover_sheet_test_print_certified_9_5x12(self, get_env, setup_dh, app_config, get_driver,
                                                    custom_logger):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh,test_data[0],get_env,link="ERR link",size="9.5X12",sending_option="Letter")
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet(), "Cover sheet is not printed")
        # assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        # shipping_label_obj.click_on_done_btn()

    @pytest.mark.errcoversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(28)
    def test_verify_8x11_err_cover_sheet_paid_print_certified_9_5x12(self, get_env, setup_dh,
                                                     app_config, get_driver, custom_logger, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh,test_data[0],get_env,link="ERR link",size="9.5X12",sending_option="Letter")
        shipping_label_obj.click_on_print_btn_on_print_options()
        time.sleep(2)
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet_actual_print(), "Cover sheet is not printed")
        assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        shipping_label_obj.click_on_done_btn()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.errcoversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(27)
    def test_verify_8x11_err_cover_sheet_test_print_certified_10(self, get_env, setup_dh, app_config, get_driver,
                                                                     custom_logger):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="ERR link",
                                                                 size="10",sending_option="Letter")
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet(), "Cover sheet is not printed")
        # assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        # shipping_label_obj.click_on_done_btn()

    @pytest.mark.errcoversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(28)
    def test_verify_8x11_err_cover_sheet_paid_print_certified_10(self, get_env, setup_dh,
                                                                     app_config, get_driver, custom_logger,
                                                                     get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="ERR link",
                                                                 size="10",sending_option="Letter")
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet_actual_print(), "Cover sheet is not printed")
        assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        shipping_label_obj.click_on_done_btn()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.errcoversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(27)
    def test_verify_8x11_err_cover_sheet_test_print_certified_6X9(self, get_env, setup_dh, app_config, get_driver,
                                                                     custom_logger):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="ERR link",
                                                                 size="6X9",sending_option="Letter")
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet(), "Cover sheet is not printed")
        # assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        # shipping_label_obj.click_on_done_btn()

    @pytest.mark.errcoversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(28)
    def test_verify_8x11_err_cover_sheet_paid_print_certified_6X9(self, get_env, setup_dh,
                                                                     app_config, get_driver, custom_logger,
                                                                     get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="ERR link",
                                                                 size="6X9",sending_option="Letter")
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet_actual_print(), "Cover sheet is not printed")
        assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        shipping_label_obj.click_on_done_btn()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.errcoversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(27)
    def test_verify_8x11_err_cover_sheet_test_print_certified_6X9_5(self, get_env, setup_dh, app_config, get_driver,
                                                                     custom_logger):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="ERR link",
                                                                 size="6X9.5",sending_option="Letter")
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet(), "Cover sheet is not printed")
        # assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        # shipping_label_obj.click_on_done_btn()

    @pytest.mark.errcoversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(28)
    def test_verify_8x11_err_cover_sheet_paid_print_certified_6x9_5(self, get_env, setup_dh,
                                                                     app_config, get_driver, custom_logger,
                                                                     get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="ERR link",
                                                                 size="6X9.5",sending_option="Letter")
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet_actual_print(), "Cover sheet is not printed")
        assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        shipping_label_obj.click_on_done_btn()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])



    @pytest.mark.shippingmultipieceLabel
    @pytest.mark.order(23)
    def test_verify_multipiece_label_print_with_receipt(self, get_env, setup_dh, app_config,
                                                        custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")

        roll_type = "8x11"
        self.click_on_header(setup_dh)
        setup_dh.click_on_shipping_label()
        assert_that(setup_dh.check_ship_another_label_btn_exists(), "Ship another link does not exist")
        setup_dh.scroll_to_ship_another_label()
        shipping_label_obj = setup_dh.click_on_ship_another_label()
        assert_that(shipping_label_obj.check_edit_rate_and_services_btn_loaded(),
                    "Edit Rate and Services Button is not Loaded")
        shipping_label_obj.add_multipiece_label(test_data[0])
        shipping_label_obj.click_on_print_option()
        assert_that(shipping_label_obj.check_printer_combo_box(), "Printer combo box is not present")
        shipping_label_obj.click_on_printer_combo_box()
        select_printer = shipping_label_obj.select_printer_from_dropdown(common_utils.get_system_name(get_env),
                                                                         test_data[0])
        if select_printer:
            flg = shipping_label_obj.check_print_size_is_enabled()
            if flg:
                shipping_label_obj.click_on_print_size_combo_box()
                time.sleep(2)
                if roll_type == "4x6":
                    shipping_label_obj.select_roll_type_from_dropdown("4x6")
                    time.sleep(2)
                elif roll_type == "8x11":
                    shipping_label_obj.select_roll_type_from_dropdown("8x11")
                    time.sleep(2)
        else:
            assert_that(select_printer, "Printer name is not present in the list")
        return SP360CreateShippingLabelObjectsClass(app_config, get_driver, custom_logger)

