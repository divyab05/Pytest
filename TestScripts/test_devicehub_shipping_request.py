import time
import pytest
from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function import Test_common_function
from TestScripts.test_common_function_DH_app import Test_common_function_DH_app
from UIObjects.SP360.SP360CreateShipRequestPageObjects import SP360CreateShipRequestObjectsClass
from UIObjects.SP360.SP360CreateShippingLabels import SP360CreateShippingLabelObjectsClass
from hamcrest import assert_that

from UIObjects.SP360.SP360MyDevicesPageObjects import SP360MyDevicesObjectsClass


class Test_DeviceHub_shipping_request(Test_common_function_DH_app):

    @pytest.mark.canada_sanity_run
    @pytest.mark.canada_sanity_run_after_update
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.shippingRequest
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(24)
    def test24_verify_8x11_ship_request_print(self, get_env, setup_dh, app_config, custom_logger,
                                              get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        ship_request_obj = SP360CreateShipRequestObjectsClass(app_config, get_driver, custom_logger)
        self.click_on_header(setup_dh)
        setup_dh.click_on_shipping_and_mailing()
        setup_dh.click_on_shipping_request()
        assert_that(ship_request_obj.check_create_shipping_request_header(),
                    "Ship Request header is not present")
        self.print_shipping_req(get_env, app_config, custom_logger,
                                get_driver, test_data[0], roll_type="8x11")

    @pytest.mark.canada_sanity_run
    @pytest.mark.canada_sanity_run_after_update
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.sp360_sanityrun
    @pytest.mark.shippingRequest
    @pytest.mark.sp360_sanity_run_afterUpdate
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(24)
    def test_verify_4x6_ship_request_print(self, get_env, setup_dh, app_config, custom_logger,
                                              get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        ship_request_obj = SP360CreateShipRequestObjectsClass(app_config, get_driver, custom_logger)
        self.click_on_header(setup_dh)
        setup_dh.click_on_shipping_and_mailing()
        setup_dh.click_on_shipping_request()
        assert_that(ship_request_obj.check_create_shipping_request_header(),
                    "Ship Request header is not present")
        self.print_shipping_req(get_env, app_config, custom_logger,
                                get_driver, test_data[0], roll_type="4x6")

    @pytest.mark.shippingRequest
    @pytest.mark.order(24)
    def test_verify_ERR_request_print(self, get_env, setup_dh, app_config, custom_logger,
                                      get_driver, get_product_name, ):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        ship_request_obj = SP360CreateShipRequestObjectsClass(app_config, get_driver, custom_logger)
        self.click_on_header(setup_dh)
        setup_dh.click_on_shipping_and_mailing()
        setup_dh.click_on_Err_ship_Request()
        assert_that(ship_request_obj.check_create_err_shipping_request_header(),
                    "ERR Ship Request header is not present")
        self.print_shipping_req(get_env, app_config, custom_logger,
                                get_driver, test_data[0], roll_type='8.5"x11"')
