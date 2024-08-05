import time

import pytest
from FrameWorkUtilities.common_utils import common_utils
from hamcrest import assert_that
from TestScripts.test_common_function import Test_common_function


class Test_DeviceHub_Postage_Roll(Test_common_function):

    @pytest.mark.postageroll
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(8)
    def test_verify_postage_roll_test_print_standard_services(self, get_env, setup_dh, app_config,
                                                              get_driver,
                                                              custom_logger, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "2x1RollPRinters")
        print_stamp_obj = self.verify_postage_roll_header(setup_dh, get_product_name)
        postage_roll_added = print_stamp_obj.postage_add_roll()
        assert_that(postage_roll_added, "Postage roll is not added")
        print_stamp_obj.postage_click_test_print()
        printer_selected = print_stamp_obj.select_printer(get_env, test_data[0])
        assert_that(printer_selected, "Printed is not Selected or not present in the list")
        print_stamp_obj.postage_click_print_option_print_button()
        assert_that(print_stamp_obj.check_print_postage_roll_header_exists(),
                    " Print Postage  sheet header is not present")

    @pytest.mark.postageroll
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(9)
    def test_verify_postage_roll_actual_print_standard_services_with_out_return_address(self, get_env, setup_dh,
                                                                                         app_config,
                                                                                        get_driver,
                                                                                        custom_logger,
                                                                                        get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "2x1RollPRinters")
        print_stamp_obj = self.verify_postage_roll_header(setup_dh, get_product_name)
        self.add_postageroll_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.postageroll
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(10)
    def test_verify_postage_roll_actual_print_signed_services_with_return_address(self, get_env, setup_dh,
                                                                                  app_config,
                                                                                  get_driver,
                                                                                  custom_logger, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "2x1RollPRinters")
        print_stamp_obj = self.verify_postage_roll_header(setup_dh, get_product_name)
        print_stamp_obj.click_on_postage_signed_for_services_radio_btn()
        self.add_postageroll_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.postageroll
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(11)
    def test_verify_stamp_roll_actual_print_standard_services_with_return_address(self, get_env, setup_dh,
                                                                                  app_config,
                                                                                  get_driver,
                                                                                  custom_logger, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "2x1RollPRinters")
        print_stamp_obj = self.verify_postage_roll_header(setup_dh, get_product_name)
        print_stamp_obj.click_on_postage_signed_for_services_radio_btn()
        print_stamp_obj.click_on_postage_standard_services_radio_btn()
        self.add_postageroll_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.postageroll
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(12)
    def test_verify_stamp_roll_actual_print_signed_services_without_return_address(self, get_env, setup_dh,
                                                                                   app_config,
                                                                                   get_driver,
                                                                                   custom_logger, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "2x1RollPRinters")
        print_stamp_obj = self.verify_postage_roll_header(setup_dh, get_product_name)
        print_stamp_obj.click_on_postage_signed_for_services_radio_btn()
        print_stamp_obj.click_postage_delete_address()
        self.add_postageroll_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.uk_scale
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.order(13)
    def test_verifyscale_functionality_roll(self, get_env, setup_dh, app_config, custom_logger,
                                             get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Scale")
        print_stamp_obj = self.verify_postage_roll_header(setup_dh, get_product_name)
        assert_that(print_stamp_obj.check_scale_btn_is_present(), "Scale button is not enabled")
        print_stamp_obj.click_on_get_Weight_from_scale_btn()
        assert_that(print_stamp_obj.verify_scale_is_connected(), "Scale is not connected")
        assert_that(print_stamp_obj.check_get_weight_btn_enabled(), "Get weight button is not enabled")
        time.sleep(7)
