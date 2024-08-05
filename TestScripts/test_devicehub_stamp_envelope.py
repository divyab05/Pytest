import time
import pytest
from hamcrest import assert_that
from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function import Test_common_function
from UIObjects.SP360.SP360MyDevicesPageObjects import SP360MyDevicesObjectsClass


class Test_DeviceHub_Stamp_Envelope(Test_common_function):

    # @pytest.mark.dh_autoactivationinstampPage
    # @pytest.mark.order(29)
    # def test_verify_activate_dh_in_stamp_envelope_page(self, get_env, setup_dh, app_config, custom_logger,
    #                                                    get_driver, get_product_name):
    #     myFile = app_config.dh_config["dhaMQTConfig_File"]
    #     self.replace_isGenerated_val_in_dhaMQTConfig(myFile, 'isGenerated": true', 'isGenerated": false')
    #     self.click_on_header(setup_dh)
    #     time.sleep(2)
    #     assert_that(setup_dh.check_stamps_links(), "Stamps link is not  present")
    #     setup_dh.click_on_stamps_link()
    #     assert_that(setup_dh.check_stamp_envelope_link_exists(), "Stamp Envelope link  is not present")
    #     setup_dh.click_on_stamp_envelope_link()
    #     time.sleep(5)
    #     my_device_page = SP360MyDevicesObjectsClass(app_config, get_driver, custom_logger)
    #     assert_that(my_device_page.verify_DH_regiestring_msg_roll_envelope(), "DH Registering message is not displayed")
    #     assert_that(my_device_page.verify_DH_auto_activated(), "DH is not Registered")
    #     assert_that(my_device_page.dh_registed_toastermsg(), "DH Registered Toaster message is not displayed")

    @pytest.mark.scale_commercial_fedramp
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.sanity_dev
    @pytest.mark.order(18)
    def test_verifyscale_functionality(self, get_env, setup_dh, app_config, custom_logger,
                                       get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx", "Scale")
        self.click_on_header(setup_dh)
        time.sleep(2)
        assert_that(setup_dh.check_stamps_links(), "Stamps link is not  present")
        setup_dh.click_on_stamps_link()
        assert_that(setup_dh.check_stamp_envelope_link_exists(), "Stamp Envelope link  is not present")
        print_stamp_obj = setup_dh.click_on_stamp_envelope_link()
        time.sleep(4)
        assert_that(print_stamp_obj.check_stamp_envelope_header_exists(), " Print Stamp Envelope header is not present")
        print_stamp_obj.click_on_custom_stamp()
        self.verify_scale_functionality(print_stamp_obj, get_env, test_data[0])

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sanity_prod
    @pytest.mark.stampenvelope
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.sanity_dev
    @pytest.mark.order(29)
    def test29_verify_stamp_envelope_size9_test_print(self, get_env, setup_dh, app_config, custom_logger,
                                                      get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        self.verify_stamp_envelope_size_test_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                                   size="9")

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.stampenvelope
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.sanity_dev
    @pytest.mark.order(30)
    def test30_verify_stamp_envelope_size9_actual_print(self, get_env, setup_dh, app_config, custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        self.verify_stamp_envelope_actual_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                                get_product_name, size="9", batchprint="no")

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.sanity_prod
    @pytest.mark.stampenvelope
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.sanity_dev
    @pytest.mark.order(31)
    def test31_verify_stamp_envelope_size10_test_print(self, get_env, setup_dh, app_config, custom_logger,
                                                       get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        self.verify_stamp_envelope_size_test_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                                   size="10")

    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.stampenvelope
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.sanity_dev
    @pytest.mark.order(32)
    def test32_verify_stamp_envelope_size10_actual_print(self, get_env, setup_dh, app_config, custom_logger,
                                                         get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        self.verify_stamp_envelope_actual_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                                get_product_name, size="10", batchprint="no")


    @pytest.mark.batchprint
    @pytest.mark.order(30)
    def test30_verify_stamp_envelope_size9_actual_print_batchprint(self, get_env, setup_dh, app_config,
                                                                   custom_logger,
                                                                   get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        self.verify_stamp_envelope_actual_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                                get_product_name, size="9", batchprint="yes")


    @pytest.mark.batchprint
    @pytest.mark.order(32)
    def test32_verify_stamp_envelope_size10_actual_print_batch_print(self, get_env, setup_dh, app_config,
                                                                     custom_logger,
                                                                     get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        self.verify_stamp_envelope_actual_print(get_env, setup_dh, test_data[0], app_config, custom_logger, get_driver,
                                                get_product_name,
                                                size="10", batchprint="yes")
