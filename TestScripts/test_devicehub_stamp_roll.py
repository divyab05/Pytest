import time
import pytest
from hamcrest import assert_that
from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function import Test_common_function

class Test_DeviceHub_stamp_roll(Test_common_function):

    @pytest.mark.scale_commercial_fedramp
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sanity_prodnorun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.stamp_roll
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.order(18)

    def test_verifyscale_functionality(self, get_env, setup_dh, app_config, custom_logger):

        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Scale")
        self.click_on_header(setup_dh)
        setup_dh.click_on_stamps_link()
        assert_that(setup_dh.check_roll_btn_exists(), "Roll Button is not present")
        print_stamp_obj = setup_dh.click_on_roll_btn()
        assert_that(print_stamp_obj.check_stamp_roll_header_exists(), " Print Stamp Roll header is not present")
        print_stamp_obj.click_on_custom_stamp()
        self.verify_scale_functionality(print_stamp_obj, get_env, test_data[0])

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sanity_prod
    @pytest.mark.stamp_roll
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(14)
    def test14_verify_2X1_stamp_roll_test_print(self, get_env, setup_dh, app_config, custom_logger,
                                                get_driver):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "2x1RollPRinters")
        self.verify_2X1_stamp_roll_test_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                              change_layout='No')

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.stamp_roll
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(15)
    def test15_verify_2X1_stamp_roll_print(self, get_env, setup_dh,  app_config, custom_logger, get_driver):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "2x1RollPRinters")
        self.verify_2X1_stamp_roll_actual_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                                change_layout='No', batchprint="no")

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.sanity_prodnorun
    @pytest.mark.stamp_roll
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(16)
    def test16_verify_2X1_stamp_roll_test_print(self, get_env, setup_dh, app_config, custom_logger,
                                                get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "2x1RollPRinters")
        self.verify_2X1_stamp_roll_test_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                              change_layout='yes')

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.stamp_roll
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(17)
    def test17_verify_2X1_stamp_roll_print(self, get_env, setup_dh, app_config, custom_logger, get_driver,
                                           get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "2x1RollPRinters")
        self.verify_2X1_stamp_roll_actual_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                                change_layout='yes', batchprint="no")


    @pytest.mark.batchprint
    @pytest.mark.order(17)
    def test17_verify_2X1_stamp_roll_print_batchprint(self, get_env, setup_dh, app_config, custom_logger,
                                                      get_driver):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "2x1RollPRinters")
        self.verify_2X1_stamp_roll_actual_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                                change_layout='yes', batchprint="yes")


    @pytest.mark.batchprint
    @pytest.mark.order(15)
    def test15_verify_2X1_stamp_roll_print_batchprint(self, get_env, setup_dh, app_config, custom_logger,
                                                      get_driver):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "2x1RollPRinters")
        self.verify_2X1_stamp_roll_actual_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                                change_layout='No', batchprint="yes")
