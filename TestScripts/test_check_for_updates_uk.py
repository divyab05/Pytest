import os
import time
import pytest
from pywinauto import Application
from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function_DH_app import Test_common_function_DH_app
from UIObjects.DeviceHubObjects import DeviceHubObjectsClass


@pytest.fixture()
def resource(app_config):
    req = DeviceHubObjectsClass(app_config)
    yield req


class Test_check_for_updates(Test_common_function_DH_app):
    @pytest.mark.check_for_update_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.sanity_prod_uk_update
    @pytest.mark.order(1)
    def test08_install_DeviceHub_old_version_uk(self, get_env, app_config, resource, custom_logger, setup_dh, get_product_name,
                             get_language):
        old_version_installer_name = app_config.dh_common_config['old_version_installer_name']
        installer_path = os.getcwd() + "\\old_version_DH\\" + old_version_installer_name
        Application().start('explorer.exe {arg1}'.format(arg1=installer_path))
        time.sleep(3)
        if resource.get_check_for_update_dialog().exists():
            resource.click_check_for_update_ok_btn()
            time.sleep(7)
            self.uninstall_DH(app_config,resource, custom_logger)
        app = Application().connect(title_re="DeviceHub", class_name='#32770')
        app.DeviceHub.child_window(title='&'+app_config.dh_config['install_obj'], class_name="Button").click()
        custom_logger.info("Clicked on Install Button")
        dh_obj = app.DeviceHub
        resource.get_dh_installation_progress_window(dh_obj)
        self.wait_for_window_to_appear(app.DeviceHub.child_window(title='&'+app_config.dh_config['finish_obj'], class_name="Button"), 90)
        app.DeviceHub.child_window(title='&'+app_config.dh_config['finish_obj'], class_name="Button").click()
        custom_logger.info("Clicked on Finish Button")
        time.sleep(2)
        resource.wait_for_DH_to_be_online()
        resource.click_on_hidden_tray()
        # self.verify_startingDH_DH_is_online_notification(get_env, resource, custom_logger)
        # self.activate_DH(setup_dh, get_env, custom_logger,get_product_name)
        self.manual_activate_DH(setup_dh, get_env, custom_logger, get_product_name)

    @pytest.mark.check_for_update_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.sanity_prod_uk_update
    @pytest.mark.order(2)
    def test09_validate_cancel_update_uk(self, resource, custom_logger, app_config):
        self.validate_cancel_update(resource, custom_logger, app_config)

    @pytest.mark.check_for_update_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.sanity_prod_uk_update
    @pytest.mark.order(3)
    def test10_click_check_for_update_uk(self, resource, app_config, get_env, custom_logger, get_driver):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Recovery_mechanishm")
        self.click_check_for_update(resource, app_config, get_env, custom_logger, get_driver,
                                    test_data[0])

    @pytest.mark.check_for_update_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.sanity_prod_uk_update
    @pytest.mark.order(4)
    def test11_verify_DH_Version_is_updated_from_old_to_new_uk(self, resource, app_config, custom_logger):
        self.verify_DH_Version_is_updated_from_old_to_new(resource, app_config, custom_logger)

    @pytest.mark.check_for_update_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.sanity_prod_uk_update
    @pytest.mark.order(5)
    def test12_verify_DH_is_online_uk(self, setup_dh, get_env, custom_logger, app_config, get_product_name):
        self.manual_activate_DH(setup_dh, get_env, custom_logger, get_product_name)

    @pytest.mark.check_for_update_uk
    @pytest.mark.uk_update_sanity_test
    @pytest.mark.sanity_prod_uk_update
    @pytest.mark.order(6)
    def test13_validate_check_for_update_uk(self, resource, custom_logger, app_config):
        self.validate_check_for_update(resource, custom_logger, app_config)

    @pytest.mark.check_for_update_uk
    @pytest.mark.order(99)
    def test_update_from_update_xml_uk(self, resource, custom_logger, app_config, get_env,get_driver):
        test_data = common_utils.read_excel_data_store("DeviceHubTestData.xlsx",
                                                       "Recovery_mechanishm")
        filepath = app_config.dh_common_config['update_xml_file_path']
        newDHVersion = app_config.dh_common_config['DH_new_version'].split("v1")
        oldDHVersion = app_config.dh_common_config['DH_old_version'].split("v1")
        txt_to_replace = str(newDHVersion[1])
        txt_replaced = str(oldDHVersion[1])
        self.replace_txt_in_a_file(filepath, txt_to_replace, txt_replaced)
        time.sleep(5)
        self.reconnect_device_hub(app_config, resource, custom_logger)
        time.sleep(7)
        resource.move_cursor()
        self.validate_cancel_update(resource, custom_logger, app_config)
        self.click_check_for_update(resource, app_config, get_env, custom_logger, get_driver,
                                    test_data[0])
        self.verify_DH_Version_is_updated_from_old_to_new(resource, app_config, custom_logger)


