import time
import pytest
from FrameWorkUtilities.common_utils import common_utils
from hamcrest import assert_that
from TestScripts.test_common_function import Test_common_function


class Test_DeviceHub_Postage_Envelope(Test_common_function):

    @pytest.mark.postageEnvelope
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(26)
    def test_1_verify_postage_envelope_test_print_standard_services_DL(self, get_env, setup_dh, app_config,
                                                                       get_driver,
                                                                       custom_logger, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        print_stamp_obj = self.verify_postage_envelope_header(setup_dh, get_product_name)
        postage_envelope_added = print_stamp_obj.postage_add_envelope()
        assert_that(postage_envelope_added, "Envelope is not added")
        test_print_clicked = print_stamp_obj.postage_click_test_print()
        assert_that(test_print_clicked, "Test print is not clicked")
        printer_selected = print_stamp_obj.select_printer(get_env, test_data[0])
        assert_that(printer_selected, "Printed is not Selected or not present in the list")
        custom_logger.info("printer is selected")
        print_stamp_obj.click_preview_test_print()
        custom_logger.info("Clicked of preview test Print")
        print_stamp_obj.click_Print_test_print_btn()
        print_stamp_obj.click_done_button()
        custom_logger.info("Clicked on Done Button")
        assert_that(print_stamp_obj.check_print_postage_envelope_header_exists(),
                    " Print Postage  sheet header is not present")

    @pytest.mark.postageEnvelope
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(27)
    def test_2_verify_postage_envelope_actual_print_standard_services_with_out_return_address_DL(self, get_env,
                                                                                                 setup_dh,
                                                                                                 app_config,
                                                                                                 get_driver,
                                                                                                 custom_logger,
                                                                                                 get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        print_stamp_obj = self.verify_postage_envelope_header(setup_dh, get_product_name)
        self.add_envelope_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.postageEnvelope
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(28)
    def test_3_verify_postage_envelope_actual_print_signed_services_with_return_address_DL(self, get_env, setup_dh,
                                                                                           app_config,
                                                                                           get_driver,
                                                                                           custom_logger,
                                                                                           get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        print_stamp_obj = self.verify_postage_envelope_header(setup_dh, get_product_name)
        print_stamp_obj.click_on_postage_signed_for_services_radio_btn()
        time.sleep(2)
        self.add_envelope_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.postageEnvelope
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(29)
    def test_4_verify_stamp_envelope_actual_print_standard_services_with_return_address_DL(self, get_env, setup_dh,
                                                                                           app_config,
                                                                                           get_driver,
                                                                                           custom_logger,
                                                                                           get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        print_stamp_obj = self.verify_postage_envelope_header(setup_dh, get_product_name)
        print_stamp_obj.click_on_postage_signed_for_services_radio_btn()
        time.sleep(2)
        print_stamp_obj.click_on_postage_standard_services_radio_btn()
        self.add_envelope_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.postageEnvelope
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(30)
    def test_5_verify_envelope_actual_print_signed_services_without_return_address_DL(self, get_env, setup_dh,
                                                                                      app_config,
                                                                                      get_driver,
                                                                                      custom_logger, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        print_stamp_obj = self.verify_postage_envelope_header(setup_dh, get_product_name)
        print_stamp_obj.click_on_postage_signed_for_services_radio_btn()
        time.sleep(2)
        print_stamp_obj.click_postage_delete_address()
        self.add_envelope_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.postageEnvelope
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(31)
    def test_6_verify_postage_envelope_test_print_standard_services_c5(self, get_env, setup_dh, app_config,
                                                                       get_driver,
                                                                       custom_logger, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        print_stamp_obj = self.verify_postage_envelope_header(setup_dh, get_product_name)
        print_stamp_obj.click_c5_envelope_size()
        postage_envelope_added = print_stamp_obj.postage_add_envelope()
        assert_that(postage_envelope_added, "Envelope is not added")
        test_print_clicked = print_stamp_obj.postage_click_test_print()
        assert_that(test_print_clicked, "Test print is not clicked")
        printer_selected = print_stamp_obj.select_printer(get_env, test_data[0])
        assert_that(printer_selected, "Printed is not Selected or not present in the list")
        custom_logger.info("printer is selected")
        print_stamp_obj.click_preview_test_print()
        custom_logger.info("Clicked of preview test Print")
        print_stamp_obj.click_c5_envelope_size_priewpage()
        custom_logger.info("Clicked on C5 size")
        print_stamp_obj.click_Print_test_print_btn()
        print_stamp_obj.click_done_button()
        custom_logger.info("Clicked on Done Button")
        assert_that(print_stamp_obj.check_print_postage_envelope_header_exists(),
                    " Print Postage  sheet header is not present")

    @pytest.mark.postageEnvelope
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(32)
    def test_7_verify_postage_envelope_actual_print_standard_services_with_out_return_address_c5(self, get_env,
                                                                                                 setup_dh,
                                                                                                 app_config,
                                                                                                 get_driver,
                                                                                                 custom_logger,
                                                                                                 get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        print_stamp_obj = self.verify_postage_envelope_header(setup_dh, get_product_name)
        print_stamp_obj.click_c5_envelope_size()
        self.add_envelope_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.postageEnvelope
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(33)
    def test_8_verify_postage_envelope_actual_print_signed_services_with_return_address_c5(self, get_env, setup_dh,
                                                                                           app_config,
                                                                                           get_driver,
                                                                                           custom_logger,
                                                                                           get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        print_stamp_obj = self.verify_postage_envelope_header(setup_dh, get_product_name)
        print_stamp_obj.click_c5_envelope_size()
        print_stamp_obj.click_on_postage_signed_for_services_radio_btn()
        time.sleep(2)
        self.add_envelope_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.postageEnvelope
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(34)
    def test_9_verify_stamp_envelope_actual_print_standard_services_with_return_address_c5(self, get_env, setup_dh,
                                                                                           app_config,
                                                                                           get_driver,
                                                                                           custom_logger,
                                                                                           get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        print_stamp_obj = self.verify_postage_envelope_header(setup_dh, get_product_name)
        print_stamp_obj.click_c5_envelope_size()
        print_stamp_obj.click_on_postage_signed_for_services_radio_btn()
        time.sleep(2)
        print_stamp_obj.click_on_postage_standard_services_radio_btn()
        self.add_envelope_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.postageEnvelope
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.uk_print
    @pytest.mark.order(35)
    def test_10_verify_envelope_actual_print_signed_services_without_return_address_c5(self, get_env, setup_dh,
                                                                                       app_config,
                                                                                       get_driver,
                                                                                       custom_logger, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Envelope")
        print_stamp_obj = self.verify_postage_envelope_header(setup_dh, get_product_name)
        print_stamp_obj.click_c5_envelope_size()
        print_stamp_obj.click_on_postage_signed_for_services_radio_btn()
        time.sleep(2)
        print_stamp_obj.click_postage_delete_address()
        self.add_envelope_and_verify_actual_print(print_stamp_obj, setup_dh, custom_logger, get_env, test_data[0])

    @pytest.mark.uk_scale
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.uk_sanity_test
    @pytest.mark.order(36)
    def test_verifyscale_functionality_envelope(self, get_env, setup_dh, app_config, custom_logger,
                                                get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Scale")
        print_stamp_obj = self.verify_postage_envelope_header(setup_dh, get_product_name)
        assert_that(print_stamp_obj.check_scale_btn_is_present(), "Scale button is not enabled")
        print_stamp_obj.click_on_get_Weight_from_scale_btn()
        assert_that(print_stamp_obj.verify_scale_is_connected(), "Scale is not connected")
        assert_that(print_stamp_obj.check_get_weight_btn_enabled(), "Get weight button is not enabled")
        time.sleep(1)
