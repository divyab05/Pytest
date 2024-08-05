import os
import time
import pytest
from pywinauto import Application
from hamcrest import assert_that, equal_to
from ConfigFiles import common_config
from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function_DH_app import Test_common_function_DH_app
from UIObjects.DeviceHubObjects import DeviceHubObjectsClass


@pytest.fixture()
def resource(app_config):
    req = DeviceHubObjectsClass(app_config)
    yield req


class Test_deviceHub_installation(Test_common_function_DH_app):

    @pytest.mark.uk_ui_installation1
    @pytest.mark.uk_sanity_test
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(1)
    def test01_verify_download_dh_from_my_devices_uk(self, setup_dh, app_config, custom_logger):
        assert_that(setup_dh.check_sp360_menu_item(), "Check PSPro UI menu item does exists")
        setup_dh.click_on_menu_item()
        custom_logger.info("Clicked on Settings")
        assert_that(setup_dh.check_my_device_link_exists(), "Check My Devices link is not present")
        my_device_page = setup_dh.click_on_my_device()
        custom_logger.info("Clicked on My Device Link")
        assert_that(my_device_page.check_my_device_header_exists(), "Check My Devices page header is not present")
        my_device_page.get_my_devices_header()
        assert_that(my_device_page.check_download_dh_btn_exists(), "Check Download DH button is not present")
        my_device_page.click_on_download_dh_installer()
        custom_logger.info("Download DH Button is Present")
        assert_that(my_device_page.check_DeviceHub_Installer_header_exists(),
                    "Check Devicehub installer page is not loaded")
        custom_logger.info("Device Hub Installer Text is Present in the DHI page")
        my_device_page.check_dh_download_status(app_config.dh_common_config['installer_name'])

    @pytest.mark.uk_ui_installation1
    @pytest.mark.uk_sanity_test
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(2)
    def test02_install_DeviceHub_uk(self, get_env, app_config, resource, custom_logger):
        installer_name = app_config.dh_common_config['installer_name']
        installer_path = os.getcwd() + "\\downloads\\" + installer_name
        Application().start('explorer.exe {arg1}'.format(arg1=installer_path))
        time.sleep(10)
        app = Application().connect(title_re="DeviceHub", class_name='#32770')
        app.DeviceHub.child_window(title='&' + app_config.dh_config["install_obj"], class_name="Button").click()
        custom_logger.info("Clicked on Install Button")
        self.wait_for_window_to_appear(
            app.DeviceHub.child_window(title='&' + app_config.dh_config["finish_obj"], class_name="Button"), 90)
        app.DeviceHub.child_window(title='&' + app_config.dh_config["finish_obj"], class_name="Button").click()
        custom_logger.info("Clicked on Finish Button")
        time.sleep(2)
        resource.wait_for_DH_to_be_online()
        resource.click_on_hidden_tray()

    @pytest.mark.uk_ui_installation1
    @pytest.mark.uk_sanity_test
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(3)
    def test03_activate_DH_uk(self, setup_dh, get_env, custom_logger, get_product_name):
        self.activate_DH(setup_dh, get_env, custom_logger, get_product_name)

    @pytest.mark.uk_ui_installation1
    @pytest.mark.uk_sanity_test
    @pytest.mark.sanity_prod_uk
    @pytest.mark.uk_print
    @pytest.mark.order(3)
    def test3_1_manual_activation_DH_uk(self, setup_dh, get_env, custom_logger, get_product_name):
        self.manual_activate_DH(setup_dh, get_env, custom_logger, get_product_name)

    @pytest.mark.uk_ui_installation1
    @pytest.mark.uk_sanity_test
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(4)
    def test04_check_deviceHub_context_menu_uk(self, resource, app_config, custom_logger):
        self.check_deviceHub_context_menu(resource, app_config, custom_logger)

    @pytest.mark.uk_ui_installation1
    @pytest.mark.uk_sanity_test
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(5)
    def test05_check_about_icon_uk(self, resource, app_config, custom_logger, get_driver, get_product_name):
        self.verify_About_context_menu(resource, app_config, custom_logger, get_product_name)

    @pytest.mark.uk_ui_installation1
    @pytest.mark.uk_sanity_test
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(6)
    def test06_check_log_icon_uk(self, resource, app_config, custom_logger):
        self.check_log_icon(resource, app_config, custom_logger)

    @pytest.mark.uk_ui_installation1
    @pytest.mark.uk_sanity_test
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(7)
    def test07_reconnect_device_hub_uk(self, app_config, resource, custom_logger):
        self.reconnect_device_hub(app_config, resource, custom_logger)

    @pytest.mark.uk_ui_installation1
    @pytest.mark.uk_sanity_test
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(100)
    def test14_check_exit_device_hub_uk(self, app_config, resource, custom_logger):
        self.check_exit_device_hub(app_config, resource, custom_logger)

    @pytest.mark.uk_ui_installation1
    @pytest.mark.order(102)
    def test_uninstall_uk(self, setup_dh, app_config, get_language, get_env, resource, custom_logger):
        path = app_config.dh_common_config['uninstallation_path']
        Application().start('explorer.exe {arg1}'.format(arg1=path))
        time.sleep(10)
        self.uninstall_DH(app_config, resource, custom_logger)
        isExist = os.path.exists(path)
        assert_that(isExist == False, 'DH is not uninstalled')

    @pytest.mark.uk_ui_installation1
    @pytest.mark.uk_sanity_test
    @pytest.mark.sanity_prod_uk
    @pytest.mark.order(101)
    def test15_checkDHStatus_is_offline_uk(self, setup_dh, get_env, custom_logger):
        sys_name = common_utils.get_system_name(get_env)
        assert_that(setup_dh.check_sp360_menu_item(), "Check PSPro UI menu item exists")
        setup_dh.click_on_menu_item()
        custom_logger.info("Clicked Settings Icon")
        assert_that(setup_dh.check_my_device_link_exists(), "My Device link is not present")
        my_device_page = setup_dh.click_on_my_device()
        custom_logger.info("My Device is clicked")
        assert_that(my_device_page.check_my_device_header_exists(), "My Device Text is not Displayed")
        custom_logger.info("My Device Text is Displayed")
        my_device_page.get_my_devices_header()
        my_device_page.refresh_manage_device_page()
        my_device_page.wait_for_first_device_after_refresh()
        dh_results = my_device_page.check_dh_name_in_table(sys_name)
        assert_that(dh_results['status'], "DH status is not present")
        assert_that(dh_results['dh_status'], equal_to("Offline"), 'DH status is not Offline')
        custom_logger.info("Device Hub status is Offline")

    @classmethod
    def teardown_class(cls):
        installer_path = os.getcwd() + "\\downloads\\" + common_config.dh_app_common_config_windows['installer_name']
        if os.path.exists(installer_path):
            os.remove(installer_path)
            print("DHUB installer deleted")
        else:
            print("No Installer is presents")
