import pytest
from FrameWorkUtilities.common_utils import common_utils
from hamcrest import assert_that

from TestScripts.test_common_function import Test_common_function


class Test_DeviceHub_Stamp_Sheet(Test_common_function):

    @pytest.mark.scale_commercial_fedramp
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.stampsheet
    @pytest.mark.sanity_dev
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.order(18)
    def test_verifyscale_functionality(self, get_env, setup_dh, app_config, custom_logger):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx", "Scale")
        self.click_on_header(setup_dh)
        assert_that(setup_dh.check_stamps_links(), "Stamps link is not  present")
        setup_dh.click_on_stamps_link()
        assert_that(setup_dh.check_stamp_sheet_link_exists(), "Stamp sheet link  is not present")
        print_stamp_obj = setup_dh.click_on_stamp_sheet_link()
        assert_that(print_stamp_obj.check_stamp_sheet_header_exists(), " Print Stamp sheet header is not present")
        print_stamp_obj.click_on_custom_stamp()
        self.verify_scale_functionality(print_stamp_obj, get_env, test_data[0])

    @pytest.mark.stampsheet
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.sanity_prod
    @pytest.mark.sanity_dev
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(27)
    def test27_verify_8x11_stamp_sheet_test_print(self, get_env, setup_dh, app_config, get_driver,
                                                  custom_logger):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "StampSheet")
        print_stamp_obj = self.stamp_sheet_add_printer(get_env, setup_dh, test_data[0], app_config, get_driver,
                                                       custom_logger)
        print_stamp_obj.click_on_test_print_btn()
        selected_printer = print_stamp_obj.select_printer_after_clicking_print_btn(get_env, test_data[0])
        assert_that(selected_printer, "Printer is not selected or printer is not in the list")
        print_stamp_obj.click_done_or_test_print_btn()
        assert_that(print_stamp_obj.check_print_stamp_success_pop_up(), "Stamp is not printed successfully")
        assert_that(print_stamp_obj.check_done_button_is_clickable(), "Done button is not  present")
        print_stamp_obj.click_on_done_btn()

    @pytest.mark.stampsheet
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.sanity_dev
    @pytest.mark.order(28)
    def test28_verify_8x11_stamp_sheet_actual_print(self, get_env, setup_dh,
                                                     app_config, get_driver, custom_logger, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "StampSheet")
        print_stamp_obj = self.stamp_sheet_add_printer(get_env, setup_dh, test_data[0], app_config, get_driver,
                                                       custom_logger)
        assert_that(print_stamp_obj.check_actual_print_btn_is_enabled(), "Actual print button is not enabled")
        print_stamp_obj.click_cost_to_account(get_product_name, test_data[0])
        print_stamp_obj.click_on_print_btn()
        selected_printer = print_stamp_obj.select_printer_after_clicking_print_btn(get_env, test_data[0])
        assert_that(selected_printer, "Printer is not selected or printer is not in the list")
        print_stamp_obj.click_print_stamps_btn()
        assert_that(print_stamp_obj.check_stamp_print_success_message(), "Stamp print is not successful")
