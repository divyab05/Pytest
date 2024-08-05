import time
import pytest
from hamcrest import assert_that
from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function import Test_common_function


class Test_DeviceHub_shipping_label(Test_common_function):

    @pytest.mark.uk_scale
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(13)
    def test_verifyscale_functionality_label(self, get_env, setup_dh, app_config, custom_logger,
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

    @pytest.mark.label_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(14)
    def test18_verify_4X6_sendparcel_sample_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        shipping_label_obj = self.send_parcel_label_and_select_printer(get_env, setup_dh, app_config, custom_logger,
                                                                       get_driver, test_data[0], get_product_name,
                                                                       roll_type="4x6")
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_sample_print_is_success(),
                    "Test Print is not success")

    @pytest.mark.label_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(15)
    def test19_verify_4X6_sendparcel_actual_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        shipping_label_obj = self.send_parcel_label_and_select_printer(get_env, setup_dh, app_config, custom_logger,
                                                                       get_driver, test_data[0], get_product_name,
                                                                       roll_type="4x6")
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.label_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(16)
    def test18_verify_A4_sendparcel_sample_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                       get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "A4")
        shipping_label_obj = self.send_parcel_label_and_select_printer(get_env, setup_dh, app_config, custom_logger,
                                                                       get_driver, test_data[0], get_product_name,
                                                                       roll_type="A4")
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_sample_print_is_success(),
                    "Test Print is not success")

    @pytest.mark.label_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(17)
    def test19_verify_A4_sendparcel_actual_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                       get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "A4")
        shipping_label_obj = self.send_parcel_label_and_select_printer(get_env, setup_dh, app_config, custom_logger,
                                                                       get_driver, test_data[0], get_product_name,
                                                                       roll_type="A4")
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")

        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.label_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(18)
    def test18_verify_6x4_sendparcel_sample_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "6x4LabelPrinters")
        shipping_label_obj = self.send_parcel_label_and_select_printer(get_env, setup_dh, app_config, custom_logger,
                                                                       get_driver, test_data[0], get_product_name,
                                                                       roll_type="6x4")
        shipping_label_obj.click_on_sample_print()
        assert_that(shipping_label_obj.verify_sample_print_is_success(),
                    "Test Print is not success")

    @pytest.mark.label_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(19)
    def test19_verify_6x4_sendparcel_actual_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "6x4LabelPrinters")
        shipping_label_obj = self.send_parcel_label_and_select_printer(get_env, setup_dh, app_config, custom_logger,
                                                                       get_driver, test_data[0], get_product_name,
                                                                       roll_type="6x4")
        shipping_label_obj.click_on_print_btn_on_print_options()
        assert_that(shipping_label_obj.wait_for_label_printed_msg(), "Label is not printed successfully")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])
