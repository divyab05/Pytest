import os
import subprocess
import time
import pytest
from hamcrest import assert_that, equal_to
from pywinauto import Application, Desktop

from ConfigFiles import common_config
from ConfigFiles.Fedramp import fedramp_config
from FrameWorkUtilities.common_utils import common_utils
from TestScripts.test_common_function import Test_common_function
from TestScripts.test_common_function_DH_app import Test_common_function_DH_app
from UIObjects.DeviceHubObjects import DeviceHubObjectsClass


@pytest.fixture()
def resource(app_config):
    req = DeviceHubObjectsClass(app_config)
    yield req


class Test_deviceHub_installation_fedramp(Test_common_function_DH_app):

    @pytest.mark.fedrampui_installation1
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.order(1)
    def test01_verify_download_dh_from_my_devices_fedrampp(self, get_env, setup_dh, app_config, custom_logger):
        assert_that(setup_dh.check_fedramp_menu_item(), "Login Page is not Loaded")
        setup_dh.click_on_menu_item()
        assert_that(setup_dh.check_my_device_link_exists(), "My Device Link is not Present")
        my_device_page = setup_dh.click_on_my_device()
        custom_logger.info("My Device is clicked")
        assert_that(my_device_page.check_my_device_header_exists(), "Check My Devices page header is not present")
        my_device_page.get_my_devices_header()
        assert_that(my_device_page.check_download_dh_btn_exists(), "Check Download DH button is not present")
        my_device_page.click_on_download_dh_installer()
        custom_logger.info("Download DH Button is Present")
        assert_that(my_device_page.check_DeviceHub_Installer_header_exists(),
                    "Check Devicehub installer page is not loaded")
        custom_logger.info("Device Hub Installer Text is Present in the DHI page")
        my_device_page.check_dh_download_status(app_config.dh_common_config['installer_name'])

    @pytest.mark.fedrampui_installation1
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.order(2)
    def test02_install_DeviceHub_fedramp(self, get_env, app_config, resource, custom_logger):
        installer_name = app_config.dh_common_config['Fedramp_installer_name']
        installer_path = os.getcwd() + "\\downloads\\" + installer_name
        time.sleep(15)
        ##os.system('msiexec /i %s /qn' % installer_path)
        Application().start('explorer.exe {arg1}'.format(arg1=installer_path))
        dh_object = DeviceHubObjectsClass(app_config)
        dh_object.wait_for_DH_explorer_window()
        path = app_config.dh_common_config['dh_app_path']
        subprocess.Popen(path, shell=True)
        # app = Desktop(backend="uia").DeviceHub
        resource.wait_for_DH_to_be_online()
        resource.click_on_hidden_tray()

    @pytest.mark.fedrampui_installation1
    @pytest.mark.fedramp_sanityrunxx
    @pytest.mark.print_commercial_fedramp
    @pytest.mark.order(3)
    def test03_activate_DH_fedramp(self, setup_dh, get_env, custom_logger, get_product_name):
        self.manual_activate_DH(setup_dh, get_env, custom_logger, get_product_name)

    @pytest.mark.fedrampui_installation1
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.order(4)
    def test04_check_deviceHub_context_menu_fedramp(self, resource, app_config, custom_logger):
        self.check_deviceHub_context_menu(resource, app_config, custom_logger)

    @pytest.mark.fedrampui_installation1
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.order(5)
    def test05_check_about_icon_fedramp(self, resource, app_config, custom_logger, get_driver, get_product_name):
        self.verify_About_context_menu(resource, app_config, custom_logger, get_product_name)

    @pytest.mark.fedrampui_installation1
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.order(6)
    def test06_check_log_icon_fedramp(self, resource, app_config, custom_logger):
        self.check_log_icon(resource, app_config, custom_logger)

    @pytest.mark.fedrampui_installation1
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.order(7)
    def test07_reconnect_device_hub_fedramp(self, app_config, resource, custom_logger):
        self.reconnect_device_hub(app_config, resource, custom_logger)

    @pytest.mark.fedrampui_installation1
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.order(7)
    def test_check_about_icon_after_reconnect_fedramp(self, resource, app_config, custom_logger, get_driver, get_product_name):
        self.verify_About_context_menu(resource, app_config, custom_logger, get_product_name)

    @pytest.mark.fedrampui_installation1
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.order(100)
    def test14_check_exit_device_hub_fedramp(self, app_config, resource, custom_logger):
        self.check_exit_device_hub(app_config, resource, custom_logger)

    @pytest.mark.fedrampui_installation1
    @pytest.mark.fedramp_sanityrun
    @pytest.mark.order(101)
    def test15_checkDHStatus_is_offline_fedramp(self, setup_dh, get_env, custom_logger):
        sys_name = common_utils.get_system_name(get_env)
        assert_that(setup_dh.check_fedramp_menu_item(), "Login Page is not Loaded")
        setup_dh.click_on_menu_item()
        assert_that(setup_dh.check_my_device_link_exists(), "My Device Link is not Present")
        my_device_page = setup_dh.click_on_my_device()
        custom_logger.info("My Device is clicked")
        assert_that(my_device_page.check_my_device_header_exists(), "Check My Devices page header is not present")
        my_device_page.refresh_manage_device_page()
        my_device_page.wait_for_first_device_after_refresh()
        custom_logger.info('Page is refreshed')
        dh_results = my_device_page.check_dh_name_in_table(sys_name)
        assert_that(dh_results['status'], "DH status is not present")
        assert_that(dh_results['dh_status'], equal_to("Offline"), 'DH status is not Offline')
        custom_logger.info("Device Hub status is Offline")

    @classmethod
    def teardown_class(cls):
        installer_path = os.getcwd() + "\\downloads\\" + common_config.dh_app_common_config_windows['Fedramp_installer_name']
        if os.path.exists(installer_path):
            os.remove(installer_path)
            print("DHUB installer deleted")
        else:
            print("No Installer is presents")
