import pywinauto
import time
import sys
from datetime import date
import pyautogui
from pywinauto import Application

from FrameWorkUtilities.common_utils import common_utils


class DeviceHubObjectsClass(common_utils):

    def __init__(self, app_config):
        self.app_config = app_config

    def click_ok_btn_installer_lang_popup(self):
        installer_land_window = pywinauto.Desktop(backend="uia").window(title_re="Installer Language",
                                                                        class_name='#32770')
        installer_land_window.child_window(title="OK", class_name="Button").click_input(
            button='left')

    def select_language_from_combo_box(self):
        installer_lang_window = pywinauto.Desktop(backend="uia").window(title_re="Installer Language",
                                                                        class_name='#32770')
        installer_lang_window.type_keys("%{DOWN}")

    def get_system_tray_icon(self):
        if sys.getwindowsversion().build > 22000:
            sys_tray = pywinauto.Desktop(backend="uia").window(title="Taskbar", control_type="Pane")
            icon = sys_tray.child_window(title_re="Show Hidden Icons", auto_id="SystemTrayIcon", control_type="Button")
        else:
            sys_tray = pywinauto.Desktop(backend="uia").window(class_name="Shell_TrayWnd")
            tray = sys_tray.child_window(auto_id="303", control_type="Pane")
            icon = tray.child_window(title="Notification Chevron", auto_id="1502", control_type="Button")
        return icon

    def get_notification_icon_over_flow_window(self):
        if sys.getwindowsversion().build > 22000:
            notification_tray = pywinauto.Desktop(backend="uia").window(title="System tray overflow window.",
                                                                        control_type="Pane")
        else:
            notification_tray = pywinauto.Desktop(backend="uia").window(title="Notification Overflow").child_window(
                title="Overflow Notification Area")
        return notification_tray

    def get_device_hub_online_notification_window(self, tray_obj):
        if sys.getwindowsversion().build > 22000:
            return tray_obj.child_window(title_re='.*' + self.app_config.dh_config["DH_object_dh_online_txt"],
                                         auto_id="NotifyItemIcon",
                                         control_type="Button")
        else:
            return tray_obj.child_window(title_re=self.app_config.dh_config["DH_object_dh_online_txt"],
                                         control_type="Button", found_index=0)

    def get_new_device_hub_version_available_notification_window(self, tray_obj):
        if sys.getwindowsversion().build > 22000:
            return tray_obj.child_window(title_re='.*' + self.app_config.dh_config["Dh_new_DH_version_available_obj"],
                                         auto_id="NotifyItemIcon",
                                         control_type="Button")
        else:
            return tray_obj.child_window(title_re=self.app_config.dh_config["Dh_new_DH_version_available_obj"] + "!",
                                         control_type="Button", found_index=0)

    def get_connection_failed_notification_window(self, tray_obj):
        if sys.getwindowsversion().build > 22000:
            return tray_obj.child_window(title_re='.*Connection failed', auto_id="NotifyItemIcon",
                                         control_type="Button")
        else:
            return tray_obj.child_window(title_re="Connection failed",
                                         control_type="Button", found_index=0)

    def verify_if_new_version_dh_update_available(self, tray_obj):
        try:
            if sys.getwindowsversion().build > 22000:
                return tray_obj.child_window(
                    title_re='.*' + self.app_config.dh_config["Dh_new_DH_version_available_obj"],
                    auto_id="NotifyItemIcon",
                    control_type="Button").exists()
            else:
                return tray_obj.child_window(
                    title_re=self.app_config.dh_config["Dh_new_DH_version_available_obj"] + "!",
                    control_type="Button", found_index=0).exists()
        except:
            return False

    def get_device_hub_context_menu_obj(self):
        return pywinauto.Desktop(backend="uia").window(class_name="QMenu")

    def get_context_menu_options(self, menu_optn_title, context_menu_obj):
        return context_menu_obj.child_window(title_re=menu_optn_title, control_type="MenuItem")

    def get_device_hub_activation_window(self):
        return pywinauto.Desktop(backend="uia").window(title="DeviceHub Activation")

    def get_username_object(self, db_activation_window_obj):
        return db_activation_window_obj.child_window(title="Pitney Bowes", control_type="Pane"). \
            child_window(title="Email", auto_id="username", control_type="Edit")

    def get_passowrd_object(self, db_activation_window_obj):
        return db_activation_window_obj.child_window(title="Pitney Bowes", control_type="Pane").child_window(
            title="Password", auto_id="password", control_type="Edit")

    def get_sign_in_button_object(self, db_activation_window_obj):
        return db_activation_window_obj.child_window(title="Pitney Bowes", control_type="Pane").child_window(
            title="Sign In", auto_id="signinButton", control_type="Button")

    def get_dh_already_running_window(self):
        return pywinauto.Desktop(backend="uia").window(class_name="#32770", title='Info')

    def get_dh_installation_progress_window(self, dh_obj):
        return dh_obj.child_window(title="Please wait while DeviceHub is being installed.")

    def get_dh_installation_finish_window(self, dh_obj):
        return dh_obj.child_window(title="Setup was completed successfully.")

    def get_system_notification_obj(self):
        win_notification = pywinauto.Desktop(backend="uia").window(class_name='Windows.UI.Core.CoreWindow',
                                                                   title='New notification')
        return win_notification

    def get_starting_dh_notification(self, win_not):
        return win_not.child_window(title="Starting DeviceHub...", control_type="Text")

    def get_dh_online_norification(self, win_not):
        return win_not.child_window(title="DeviceHub is Online!", control_type="Text")

    def get_hidden_tray(self):
        hidden_tray = pywinauto.Desktop(backend="uia").window(title="Taskbar", control_type="Pane")
        icon = hidden_tray.child_window(title="Show Hidden Icons Hide", auto_id="SystemTrayIcon", control_type="Button")
        return icon

    def click_on_hidden_tray(self):
        if sys.getwindowsversion().build > 22000:
            hidden_tray = pywinauto.Desktop(backend="uia").window(title="Taskbar", control_type="Pane")
            icon = hidden_tray.child_window(title="Show Hidden Icons Hide", auto_id="SystemTrayIcon",
                                            control_type="Button").click()
        else:
            self.get_system_tray_icon().click()

    def right_click_notification_tray(self):
        self.move_cursor()
        sys_tray_icon = self.get_system_tray_icon()
        if sys_tray_icon.exists():
            sys_tray_icon.click()
            time.sleep(1)
            notification_tray = self.get_notification_icon_over_flow_window()
            tray_area = self.get_device_hub_online_notification_window(notification_tray)
            time.sleep(4)
            tray_area.click_input(button='right')

    def click_notification_tray_update(self, app_config):
        tray_area = ""
        sys_tray_icon = self.get_system_tray_icon()
        if sys_tray_icon.exists():
            sys_tray_icon.click()
            time.sleep(1)
            notification_tray = self.get_notification_icon_over_flow_window()
            if self.verify_if_new_version_dh_update_available(notification_tray):
                tray_area = self.get_new_device_hub_version_available_notification_window(notification_tray)
                time.sleep(4)
                tray_area.click_input(button='right')
            else:
                tray_area = self.get_connection_failed_notification_window(notification_tray)
                tray_area.click_input(button='right')
                context_menu = self.get_device_hub_context_menu_obj()
                self.get_context_menu_options(app_config.dh_config["DH_object_Reconnect"],
                                              context_menu).click_input(button='left')
                self.click_on_hidden_tray()
                time.sleep(3)
                self.wait_for_DH_to_be_online()
                tray_area = self.get_new_device_hub_version_available_notification_window(notification_tray)

                time.sleep(4)
                tray_area.click_input(button='right')

    def wait_for_DH_to_be_online(self):
        pyautogui.moveTo(100, 150)
        pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
        pyautogui.dragTo(100, 150)
        pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down
        sys_tray_icon = self.get_system_tray_icon()
        time.sleep(2)
        if sys_tray_icon.exists():
            time.sleep(3)
            sys_tray_icon.click()
            time.sleep(2)
            notification_tray = self.get_notification_icon_over_flow_window()
            self.wait_for_window_to_appear(
                self.get_device_hub_online_notification_window(notification_tray), 120)

    def get_about_menu_window(self):
        return pywinauto.Desktop(backend='uia').window(title=self.app_config.dh_config["DH_object_About"],
                                                       control_type="Window")

    def get_about_menu_Ok_button(self):
        about_window = pywinauto.Desktop(backend='uia').window(title=self.app_config.dh_config["DH_object_About"],
                                                               control_type="Window")
        ok_button = about_window.child_window(title="OK", control_type="Button")
        return ok_button

    def get_logs_explorer_window(self):
        logs_explorer_window = pywinauto.Desktop(backend="uia").window(class_name="CabinetWClass", title='logs')
        inside_exp = logs_explorer_window.child_window(auto_id="41477", control_type="Pane")
        return logs_explorer_window

    def get_close_button(self):
        close_button = self.get_logs_explorer_window().child_window(title="Close", control_type="Button")
        return close_button

    def get_date_in_yyyy_dd_mm(self):
        curr_date = date.today()
        return curr_date

    def get_device_hub_offline_notification(self):
        app_notification = self.get_system_notification_obj()
        offline_notification = app_notification.child_window(auto_id="NormalToastView", control_type="Window")
        return offline_notification.child_window(
            title_re='.*' + self.app_config.dh_config["DH_object_dh_offline_txt"],
            control_type="Text")

    def get_check_for_update_dialog(self):
        self.wait_for_window_to_appear(pywinauto.Desktop(backend="uia").window(class_name="#32770", title='DeviceHub'),
                                       20)
        check_for_update_window = pywinauto.Desktop(backend="uia").window(class_name="#32770", title='DeviceHub')
        check_for_update_dialog = check_for_update_window.child_window(
            auto_id="65535", control_type="Text")
        return check_for_update_dialog

    def click_check_for_update_ok_btn(self):
        about_window = pywinauto.Desktop(backend="uia").window(class_name="#32770", title='DeviceHub')
        about_window.child_window(title="OK", control_type="Button").click_input(
            button='left')

    def get_dh_update_in_progress_norification(self, win_not):
        return win_not.child_window(title=self.app_config.dh_config["DH_updates_in_progress_obj"], control_type="Text")

    def get_successful_update_dialog(self):
        self.wait_for_window_to_appear(pywinauto.Desktop(backend="uia").window(class_name="#32770"), 120)
        check_for_update_window = pywinauto.Desktop(backend="uia").window(class_name="#32770")
        check_for_update_dialog = check_for_update_window.child_window(
            title=self.app_config.dh_config["successful_updation_msg"], control_type="Text")
        return check_for_update_dialog

    def click_ok_btn_after_update(self):
        about_window = pywinauto.Desktop(backend="uia").window(class_name="#32770")
        about_window.child_window(title="OK", auto_id="2", control_type="Button").click_input(
            button='left')

    def click_cancel_update_dialog(self):
        about_window = pywinauto.Desktop(backend="uia").window(class_name="#32770", title='DeviceHub')
        about_window.child_window(title="Cancel", control_type="Button").click_input(
            button='left')

    def get_dh_uninstallation_progress_window(self, dh_obj):
        return dh_obj.child_window(title="Please wait while DeviceHub is being uninstalled.")

    def wait_for_DH_explorer_window(self):
        time.sleep(10)
        self.wait_for_window_to_appear(
            pywinauto.Desktop(backend="uia").window(class_name="CabinetWClass", title='DeviceHub_v1'), 50)

    def move_cursor(self):
        pyautogui.moveTo(100, 150)
        pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
        pyautogui.dragTo(100, 150)
        pyautogui.dragRel(0, 10)

    def check_installer_window_exists(self):
        try:
            app = Application().connect(title_re="Installer Language", class_name='#32770')
            self.wait_for_window_to_appear(app.DeviceHub.child_window(title="OK", class_name="Button"), 10)
            return True
        except:
            return False

    def get_about_popup_text(self, custom_logger):
        self.right_click_notification_tray()
        custom_logger.info("Context menu is displayed")
        context_menu = self.get_device_hub_context_menu_obj()
        self.get_context_menu_options(self.app_config.dh_config["DH_object_About"], context_menu).click_input(
            button='left')
        about_icon_window_popup = self.get_about_menu_window()
        custom_logger.info("About menu is clicked and pop up is displayed")
        get_pop_up_text = about_icon_window_popup.child_window(title_re=".*DeviceHub v1",
                                                               control_type="Text").window_text()
        return get_pop_up_text


    def click_on_logs_return_current_date(self, custom_logger):
        self.right_click_notification_tray()
        custom_logger.info("Context menu is displayed")
        context_menu = self.get_device_hub_context_menu_obj()
        self.get_context_menu_options(self.app_config.dh_config["DH_object_Logs"], context_menu).click_input(
            button='left')
        custom_logger.info("Logs menu is Clicked")
        time.sleep(2)
        date = self.get_date_in_yyyy_dd_mm()
        curr_date = str(date).replace("-", ".")
        return curr_date

    def click_exit_from_context_menu(self, custom_logger):
        self.right_click_notification_tray()
        custom_logger.info("Context menu is displayed")
        context_menu = self.get_device_hub_context_menu_obj()
        self.get_context_menu_options(self.app_config.dh_config["DH_object_exit"], context_menu).click_input(
            button='left')
        custom_logger.info("Exit Button is Clicked")

    def get_check_for_update_popup(self, custom_logger):
        self.right_click_notification_tray()
        custom_logger.info("Context menu is not displayed")
        context_menu = self.get_device_hub_context_menu_obj()
        self.get_context_menu_options(self.app_config.dh_config["DH_object_check_for_update"],
                                      context_menu).click_input(button='left')
        check_for_update_dialog = self.get_check_for_update_dialog()
        return check_for_update_dialog

    def click_ok_btn_proxy_setting_page(self):
        installer_land_window = pywinauto.Desktop(backend="uia").window(title_re="Proxy Settings")
        installer_land_window.child_window(title="OK").click_input(
            button='left')


