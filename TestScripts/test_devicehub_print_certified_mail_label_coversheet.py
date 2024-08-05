import pytest
from hamcrest import assert_that
from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function import Test_common_function


class Test_DeviceHub_shipping_label(Test_common_function):

    @pytest.mark.certifiedmail_label
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(22)
    def test_verify_8X11_shipping_sample_certifiedmail_label_sample_print_with_receipt(self, get_env, setup_dh, app_config,
                                                                             custom_logger,
                                                                             get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.sample_print_err_shipping_label(setup_dh, test_data[0], get_env, roll_type='8x11', link="Certified Mail",sending_option="Package",summary_receipt="yes")

    @pytest.mark.certifiedmail_label
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(22)
    def test_verify_8X11_shipping_actual_certifiedmail_label_print_with_receipt(self, get_env, setup_dh, app_config,
                                                                      custom_logger,
                                                                      get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.actual_print_err_shipping_label(setup_dh, test_data[0], get_env, roll_type='8x11', link="Certified Mail",sending_option="Package",summary_receipt="yes")

        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.certifiedmail_label
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(22)
    def test_verify_4x6_shipping_sample_certifiedmail_label_sample_print_with_receipt(self, get_env, setup_dh, app_config,
                                                                            custom_logger,
                                                                            get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.sample_print_err_shipping_label(setup_dh, test_data[0], get_env, roll_type='4x6', link="Certified Mail",sending_option="Package",summary_receipt="yes")

    @pytest.mark.certifiedmail_label
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(22)
    def test_verify_4x6_shipping_actual_certifiedmail_label_print_with_receipt(self, get_env, setup_dh, app_config,
                                                                     custom_logger,
                                                                     get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.actual_print_err_shipping_label(setup_dh, test_data[0], get_env, roll_type='4x6', link="Certified Mail",sending_option="Package",summary_receipt="yes")

        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.certifiedmail_batchprint
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(25)
    def test_verify_certifiedmail_4X6_shipping_batchprinting_label_print(self, get_env, app_config, setup_dh,
                                                               custom_logger, get_driver,
                                                               get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        shipping_label_obj = self.select_certifiedmail_batch_printing_details(setup_dh, test_data[0], app_config, get_driver,
                                                                    custom_logger, link="Certified Mail")
        assert_that(shipping_label_obj.check_print_shipping_label_is_clickable, "Shipping label is not clickable")
        shipping_label_obj.click_on_print_Shipping_label()
        shipping_label_obj.select_printer_and_roll(get_env, test_data[0], roll_type='4x6')
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.wait_for_batch_print_label_printed_msg(), "Label is not printed successfully")

    @pytest.mark.certifiedmail_batchprint
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(25)
    def test_verify_certifiedmail_8x11_shipping_batchprinting_label_print(self, get_env, app_config, setup_dh,
                                                                custom_logger, get_driver,
                                                                get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_certifiedmail_batch_printing_details(setup_dh, test_data[0], app_config, get_driver,
                                                                    custom_logger, link="Certified Mail")
        assert_that(shipping_label_obj.check_print_shipping_label_is_clickable, "Shipping label is not clickable")
        shipping_label_obj.click_on_print_Shipping_label()
        shipping_label_obj.select_printer_and_roll(get_env, test_data[0], roll_type='8x11')
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.wait_for_batch_print_label_printed_msg(), "Label is not printed successfully")

    @pytest.mark.certifiedmail_coversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(27)
    def test_verify_8x11_certifiedmail_cover_sheet_test_print_certified_10(self, get_env, setup_dh, app_config, get_driver,
                                                    custom_logger):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="Certified Mail",size ="10",sending_option="Letter")
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet(), "Cover sheet is not printed")
        # assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        # shipping_label_obj.click_on_done_btn()

    @pytest.mark.certifiedmail_coversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(28)
    def test_verify_8x11_certifiedmail_cover_sheet_paid_print_certified_10(self, get_env, setup_dh,
                                                     app_config, get_driver, custom_logger, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="Certified Mail",size="10",sending_option="Letter")
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet_actual_print(), "Cover sheet is not printed")
        assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        shipping_label_obj.click_on_done_btn()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.certifiedmail_coversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(27)
    def test_verify_8x11_certifiedmail_cover_sheet_test_print_certified_6X9(self, get_env, setup_dh, app_config,
                                                                           get_driver,
                                                                           custom_logger):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="Certified Mail",
                                                                 size="6X9",sending_option="Letter")
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet(), "Cover sheet is not printed")
        # assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        # shipping_label_obj.click_on_done_btn()

    @pytest.mark.certifiedmail_coversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(28)
    def test_verify_8x11_certifiedmail_cover_sheet_paid_print_certified_6X9(self, get_env, setup_dh,
                                                                           app_config, get_driver, custom_logger,
                                                                           get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="Certified Mail",
                                                                 size="6X9",sending_option="Letter")
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet_actual_print(), "Cover sheet is not printed")
        assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        shipping_label_obj.click_on_done_btn()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])


    @pytest.mark.certifiedmail_coversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(27)
    def test_verify_8x11_certifiedmail_cover_sheet_test_print_certified_6x9_5(self, get_env, setup_dh, app_config,
                                                                           get_driver,
                                                                           custom_logger):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="Certified Mail",
                                                                 size="6X9.5",sending_option="Letter")
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet(), "Cover sheet is not printed")
        # assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        # shipping_label_obj.click_on_done_btn()


    @pytest.mark.certifiedmail_coversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(28)
    def test_verify_8x11_certifiedmail_cover_sheet_paid_print_certified_6x9_5(self, get_env, setup_dh,
                                                                           app_config, get_driver, custom_logger,
                                                                           get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="Certified Mail",
                                                                 size="6X9.5",sending_option="Letter")
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet_actual_print(), "Cover sheet is not printed")
        assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        shipping_label_obj.click_on_done_btn()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])


    @pytest.mark.certifiedmail_coversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(27)
    def test_verify_8x11_certifiedmail_cover_sheet_test_print_certified_9_5x12(self, get_env, setup_dh, app_config, get_driver,
                                                                           custom_logger):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="Certified Mail",
                                                                 size="9.5X12",sending_option="Letter")
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet(), "Cover sheet is not printed")
        # assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        # shipping_label_obj.click_on_done_btn()


    @pytest.mark.certifiedmail_coversheet
    @pytest.mark.sp360_sanityrun
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(28)
    def test_verify_8x11_certifiedmail_cover_sheet_paid_print_certified_9_5x12(self, get_env, setup_dh,
                                                                           app_config, get_driver, custom_logger,
                                                                           get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        shipping_label_obj = self.select_printer_for_cover_sheet(setup_dh, test_data[0], get_env, link="Certified Mail",
                                                                 size="9.5X12",sending_option="Letter")
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.verify_success_msg_cover_sheet_actual_print(), "Cover sheet is not printed")
        assert_that(shipping_label_obj.check_done_button_is_clickable(), "Done button is not  present")
        shipping_label_obj.click_on_done_btn()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])


