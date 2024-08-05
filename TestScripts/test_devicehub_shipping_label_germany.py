import pytest
from hamcrest import assert_that
from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function import Test_common_function


class Test_DeviceHub_shipping_label(Test_common_function):

    @pytest.mark.scale_germany
    @pytest.mark.germany_sanity_run
    @pytest.mark.germany_sanity_run_afterupdate
    @pytest.mark.sanity_prod_germany
    @pytest.mark.print_germany
    @pytest.mark.order(18)
    def test_verifyscale_functionality(self, get_env, setup_dh, app_config, custom_logger, get_product_name):
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

    @pytest.mark.shippingLabel_germany
    @pytest.mark.germany_sanity_run
    @pytest.mark.germany_sanity_run_afterupdate
    @pytest.mark.print_germany
    @pytest.mark.sanity_prod_germany
    @pytest.mark.order(18)
    def test18_verify_21x27_shipping_sample_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx", "21x27LabelPrinters")
        self.verify_shipping_sample_label_print(get_env, setup_dh, app_config, custom_logger,
                                                get_driver, test_data[0], get_product_name, roll_type="21x27",
                                                check_receipt="No")

    @pytest.mark.shippingLabel_germany
    @pytest.mark.germany_sanity_run
    @pytest.mark.germany_sanity_run_afterupdate
    @pytest.mark.print_germany
    @pytest.mark.order(19)
    def test19_verify_21x27_shipping_actual_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx", "21x27LabelPrinters")
        self.verify_shipping_actual_label_print(get_env, setup_dh, app_config, custom_logger,
                                                get_driver, test_data[0], get_product_name, roll_type="21x27",
                                                check_receipt="No")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.shippingLabel_germany
    @pytest.mark.germany_sanity_run
    @pytest.mark.germany_sanity_run_afterupdate
    @pytest.mark.sanity_prod_germany
    @pytest.mark.print_germany
    @pytest.mark.order(20)
    def test20_verify_10x20_shipping_sample_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx", "10x20LabelPrinters")
        self.verify_shipping_sample_label_print(get_env, setup_dh, app_config, custom_logger,
                                                get_driver, test_data[0], get_product_name, roll_type="10x20",
                                                check_receipt="No")

    @pytest.mark.shippingLabel_germany
    @pytest.mark.germany_sanity_run
    @pytest.mark.germany_sanity_run_afterupdate
    @pytest.mark.print_germany
    @pytest.mark.order(21)
    def test21_verify_10x20_shipping_actual_label_print(self, get_env, setup_dh, app_config, custom_logger,
                                                        get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx", "10x20LabelPrinters")
        self.verify_shipping_actual_label_print(get_env, setup_dh, app_config, custom_logger,
                                                get_driver, test_data[0], get_product_name, roll_type="10x20",
                                                check_receipt="No")
        self.click_and_verify_reprint(app_config, get_driver, custom_logger, get_env, test_data[0])

    @pytest.mark.shippingLabel_germany
    @pytest.mark.germany_sanity_run
    @pytest.mark.germany_sanity_run_afterupdate
    @pytest.mark.print_germany
    @pytest.mark.batchprint_germany
    @pytest.mark.order(22)
    def test_verify_10x20_batchPrint_shipping_label_without_SummaryReceipt(self, get_env, setup_dh, app_config, custom_logger,
                                                    get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "10x20LabelPrinters")
        self.selectMultipleRecipient(get_env, setup_dh, custom_logger, test_data[0], roll_type="10x20",
                                     check_summary_receipt="no")

    @pytest.mark.shippingLabel_germany
    @pytest.mark.germany_sanity_run
    @pytest.mark.germany_sanity_run_afterupdate
    @pytest.mark.print_germany
    @pytest.mark.batchprint_germany
    @pytest.mark.order(22)
    def test_verify_21x27_batchPrint_shipping_label_without_SummaryReceipt(self, get_env, setup_dh, app_config, custom_logger,
                                                    get_driver, get_product_name):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "21x27LabelPrinters")
        self.selectMultipleRecipient(get_env, setup_dh, custom_logger, test_data[0],
                                     roll_type="21x27", check_summary_receipt="no")