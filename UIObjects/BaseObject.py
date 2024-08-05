import os

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait
from FrameWorkUtilities.common_utils import common_utils


class BasePage(object):

    def __init__(self, driver):
        self.window_handles = None
        self.driver = driver
        self.timeout = 30

    @common_utils.exception_handler
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    @common_utils.exception_handler
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    # def open(self, url):
    #     url = self.base_url + url
    #     self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    @common_utils.exception_handler
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # def press_down_arrow_key(self):
    #     down_key = ActionChains(self.driver).key_down(Keys.DOWN).

    @common_utils.timeout_handler
    def wait_element(self, *locator):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))

    @common_utils.timeout_handler
    def wait_for_window(self, num):
        WebDriverWait(self.driver, 30).until((EC.number_of_windows_to_be(num)))

    def wait_for_element_not_present(self, *locator):
        flg = WebDriverWait(self.driver, 40).until(EC.invisibility_of_element_located(locator))
        return flg

    @common_utils.timeout_handler
    @common_utils.exception_handler
    def wait_element_till_time_limit(self, time_limit, *locator):
        WebDriverWait(self.driver, time_limit).until(EC.presence_of_element_located(locator))

    @common_utils.timeout_handler
    @common_utils.exception_handler
    def wait_for_element_to_be_clickable(self, *locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))

    @common_utils.exception_handler
    def scroll_to_element(self, *locator):
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def pop_up_exists(self):

        try:
            WebDriverWait(self.driver, 30).until(EC.alert_is_present())
            alert = Alert(self.driver)
            print(alert.text)
            alert.accept()
            print("Alert accepted")
        except:
            print("no Alert found")

    @common_utils.exception_handler
    def press_tab(self):
        tab = ActionChains(self.driver).send_keys(Keys.TAB * 1)
        tab.perform()

    def click_using_js(self, *locator):
        element = self.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_new_window(self):
        WebDriverWait(self.driver, 120).until(EC.new_window_is_opened(self.driver.window_handles))

    def switch_to_first_child_window(self, *locator):
        window = self.driver.switch_to.window(self.driver.window_handles[1])
        print("Inside Child window {arg1}".format(arg1=self.driver.title))
        WebDriverWait(self.driver, 90).until(EC.presence_of_element_located(locator))
        return window

    def switch_to_parent_window(self):
        parent_window = self.driver.switch_to.window(self.driver.window_handles[0])
        return parent_window

    def close_current_window(self):
        self.driver.close()

    def verify_if_element_is_visible(self, *locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
            return True
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False

    def delete_installer(self, installer_path):
        try:
            if os.path.exists(installer_path):
                os.remove(installer_path)
                print("DHUB installer deleted")
            else:
                print("No Installer is presents")
        except:
            print("")
