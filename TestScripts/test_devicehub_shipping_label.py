import time
import pytest
from hamcrest import assert_that
from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function import Test_common_function


class Test_DeviceHub_shipping_label(Test_common_function):

    @pytest.mark.scale_commercial_fedramp
    @pytest.mark.print_canada
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sanity_prod
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.canada_sanity_run
    @pytest.mark.canada_sanity_run_after_update
    @pytest.mark.sanity_prod_canada
    @pytest.mark.sanity_dev
    @pytest.mark.order(18)
    def test_verifyscale_functionality(self, get_env, setup_dh, app_config, custom_logger,
                                       get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Scale")
        self.click_on_header(setup_dh)
        setup_dh.click_on_shipping_label()
        assert_that(setup_dh.check_ship_another_label_btn_exists(), "Ship another link does not exist")
        setup_dh.scroll_to_ship_another_label()
        shipping_label_obj = setup_dh.click_on_ship_another_label()
        assert_that(shipping_label_obj.check_edit_rate_and_services_btn_loaded(),
                    "Edit Rate and Services Button is not Loaded")
        self.verify_scale_functionality(shipping_label_obj, get_env, test_data[0])

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sanity_prod
    @pytest.mark.shippingLabel
    @pytest.mark.canada_sanity_run
    @pytest.mark.canada_sanity_run_after_update
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_canada
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.sanity_prod_canada
    @pytest.mark.sanity_dev
    @pytest.mark.order(18)
    def test18_verify_4X6_shipping_sample_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                      get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.verify_shipping_sample_label_print(get_env, setup_dh, app_config, custom_logger,
                                                get_driver, test_data[0], get_product_name, roll_type="4x6",
                                                check_receipt="No")

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.shippingLabel
    @pytest.mark.canada_sanity_run
    @pytest.mark.canada_sanity_run_after_update
    @pytest.mark.print_canada
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.sanity_dev
    @pytest.mark.order(19)
    def test19_verify_4X6_shipping_actual_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                      get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.verify_shipping_actual_label_print(get_env, setup_dh, app_config, custom_logger,
                                                get_driver, test_data[0], get_product_name, roll_type="4x6",
                                                check_receipt="No")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sanity_prod
    @pytest.mark.shippingLabel
    @pytest.mark.canada_sanity_run
    @pytest.mark.print_canada
    @pytest.mark.canada_sanity_run_after_update
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.sanity_prod_canada
    @pytest.mark.sanity_dev
    @pytest.mark.order(20)
    def test20_verify_8X11_shipping_sample_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                       get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.verify_shipping_sample_label_print(get_env, setup_dh, app_config, custom_logger,
                                                get_driver, test_data[0], get_product_name, roll_type="8x11",
                                                check_receipt="No")

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.shippingLabel
    @pytest.mark.canada_sanity_run
    @pytest.mark.canada_sanity_run_after_update
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.sanity_dev
    @pytest.mark.print_canada
    @pytest.mark.order(21)
    def test21_verify_8X11_shipping_actual_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                       get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.verify_shipping_actual_label_print(get_env, setup_dh, app_config, custom_logger,
                                                get_driver, test_data[0], get_product_name, roll_type="8x11",
                                                check_receipt="No")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.shippingLabel
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(22)
    def test22_verify_8X11_shipping_sample_label_print_with_receipt(self, get_env, setup_dh, app_config,
                                                                    custom_logger,
                                                                    get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.verify_shipping_sample_label_print(get_env, setup_dh, app_config, custom_logger,
                                                get_driver, test_data[0], get_product_name, roll_type="8x11",
                                                check_receipt="Yes")

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.shippingLabel
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(23)
    def test23_verify_8X11_shipping_actual_label_print_with_receipt(self, get_env, setup_dh, app_config,
                                                                    custom_logger,
                                                                    get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.verify_shipping_actual_label_print(get_env, setup_dh, app_config, custom_logger,
                                                get_driver, test_data[0], get_product_name, roll_type="8x11",
                                                check_receipt="Yes")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.batchprint
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.order(23)
    def test_verify_8x11_shipping_batchprinting_label_print_with_summaryreceipt(self, get_env, app_config, setup_dh,
                                                                                custom_logger, get_driver,
                                                                                get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.selectMultipleRecipient(get_env, setup_dh, custom_logger, test_data[0], roll_type="8x11",
                                     check_summary_receipt="yes")

    @pytest.mark.batchprint
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.canada_batch_print
    @pytest.mark.canada_sanity_run
    @pytest.mark.print_canada
    @pytest.mark.order(24)
    def test_verify_8x11_shipping_batchprinting_label_print_without_summary_receipt(self, get_env, app_config, setup_dh,
                                                                                    custom_logger, get_driver,
                                                                                    get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.selectMultipleRecipient(get_env, setup_dh, custom_logger, test_data[0], roll_type="8x11",
                                     check_summary_receipt="no")

    @pytest.mark.batchprint
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.order(25)
    def test_verify_4X6_shipping_batchprinting_label_print_with_summaryreceipt(self, get_env, app_config, setup_dh,
                                                                               custom_logger, get_driver,
                                                                               get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.selectMultipleRecipient(get_env, setup_dh, custom_logger, test_data[0], roll_type="4x6",
                                     check_summary_receipt="yes")

    @pytest.mark.batchprint
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.canada_batch_print
    @pytest.mark.canada_sanity_run
    @pytest.mark.print_canada
    @pytest.mark.order(26)
    def test_verify_4X6_shipping_batchprinting_label_print_without_summary_receipt(self, get_env, app_config, setup_dh,
                                                                                   custom_logger, get_driver,
                                                                                   get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.selectMultipleRecipient(get_env, setup_dh, custom_logger, test_data[0], roll_type="4x6",
                                     check_summary_receipt="no")
