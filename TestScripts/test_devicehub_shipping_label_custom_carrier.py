import time
import pytest
from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function import Test_common_function


class Test_DeviceHub_shipping_label_custom_carrier(Test_common_function):

    @pytest.mark.Shipping_label_fedex
    @pytest.mark.order(21)
    def test_verify_8X11_shipping_sample_label_print_fedex(self, get_env, setup_dh, app_config, custom_logger,
                                                           get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.verify_shipping_sample_label_print_with_custom_carrier(get_env, setup_dh, app_config, custom_logger,
                                                                    get_driver, test_data[0], roll_type="8x11",
                                                                    carrier="FEDEX")

    @pytest.mark.Shipping_label_fedex
    @pytest.mark.order(21)
    def test_verify_8X11_shipping_actual_label_print_fedex(self, get_env, setup_dh, app_config, custom_logger,
                                                           get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.verify_actual_shipping_label_print_with_custom_carrier(get_env, setup_dh, app_config, custom_logger,
                                                               get_driver, test_data[0],  roll_type="8x11",
                                                                    carrier="FEDEX")

    @pytest.mark.Shipping_label_fedex
    @pytest.mark.order(21)
    def test_verify_4x6_shipping_sample_label_print_fedex(self, get_env, setup_dh, app_config, custom_logger,
                                                           get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.verify_shipping_sample_label_print_with_custom_carrier(get_env, setup_dh, app_config, custom_logger,
                                                                    get_driver, test_data[0], roll_type="4x6",
                                                                    carrier="FEDEX")

    @pytest.mark.Shipping_label_fedex
    @pytest.mark.order(21)
    def test_verify_4x6_shipping_actual_label_print_fedex(self, get_env, setup_dh, app_config, custom_logger,
                                                           get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.verify_actual_shipping_label_print_with_custom_carrier(get_env, setup_dh, app_config, custom_logger,
                                                                    get_driver, test_data[0], roll_type="4x6",
                                                                    carrier="FEDEX")

    @pytest.mark.Shipping_label_ups
    @pytest.mark.order(21)
    def test_verify_4x6_shipping_sample_label_print_ups(self, get_env, setup_dh, app_config, custom_logger,
                                                          get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.verify_shipping_sample_label_print_with_custom_carrier(get_env, setup_dh, app_config, custom_logger,
                                                                    get_driver, test_data[0], roll_type="4x6",
                                                                    carrier="UPS")

    @pytest.mark.Shipping_label_ups
    @pytest.mark.order(21)
    def test_verify_4x6_shipping_actual_label_print_ups(self, get_env, setup_dh, app_config, custom_logger,
                                                          get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "4X6LabelPrinters")
        self.verify_actual_shipping_label_print_with_custom_carrier(get_env, setup_dh, app_config, custom_logger,
                                                                    get_driver, test_data[0], roll_type="4x6",
                                                                    carrier="UPS")

    @pytest.mark.Shipping_label_ups
    @pytest.mark.order(21)
    def test_verify_8x11_shipping_sample_label_print_ups(self, get_env, setup_dh, app_config, custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.verify_shipping_sample_label_print_with_custom_carrier(get_env, setup_dh, app_config, custom_logger,
                                                                    get_driver, test_data[0], roll_type="8x11",
                                                                    carrier="UPS")

    @pytest.mark.Shipping_label_ups
    @pytest.mark.order(21)
    def test_verify_8x11_shipping_actual_label_print_ups(self, get_env, setup_dh, app_config, custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "8X11LabelPrinters")
        self.verify_actual_shipping_label_print_with_custom_carrier(get_env, setup_dh, app_config, custom_logger,
                                                                    get_driver, test_data[0], roll_type="8x11",
                                                                    carrier="UPS")