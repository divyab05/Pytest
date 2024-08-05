import time
from selenium.webdriver.common.by import By
from UIObjects.BaseObject import BasePage
from UIObjects.Germany.GermanyMyDevicesPageObjects import GermanyMyDevicesObjectsClass
from UIObjects.SP360.SP360CreateShipRequestPageObjects import SP360CreateShipRequestObjectsClass
from UIObjects.SP360.SP360CreateShippingLabels import SP360CreateShippingLabelObjectsClass
from UIObjects.SP360.SP360PrintStampRollObjects import SP360PrintStampRollObjectsClass
from UIObjects.SP360.SP360StampSheets import SP360StampSheets


class GermanyHomePageObjectsClass(BasePage):
    germany_header = (By.XPATH, "//a[contains(text(),'Pitney') or contains(text(),'pitney')]")
    germany_menu_item = (By.XPATH, "//button[@aria-label='Settings']")
    my_device_link = (By.XPATH, "//a/span[contains(text(),'My Devices')]")
    roll_link = (By.XPATH, "//button[@id ='stamp_rolls']")
    stamps_link = (By.XPATH, "//a[contains(text(), 'Stamps')]")
    germany_create_shipping_label_btn = (By.XPATH, "//button[@id='create_shipping_label']")
    ship_another_label = (By.XPATH, "(//a[contains(text(), 'Ship Another')])[1]")
    create_shipping_label_link = (By.XPATH, "//button[@id='create_shipping_label']")
    create_ship_request_btn = (By.XPATH, "//button[@id='create_ship_request']")
    pb_logo_link = (By.XPATH, "//a[contains(text(),'pitney bowes')]"),
    send_a_parcel = (By.XPATH, "//a[contains(text(),'Send a Parcel')]")
    shipping_label_print = (By.XPATH, "//button[@id='btnPrintShippingLabel']")
    shipping_request = (By.XPATH, "//a[@href='/sending/label/print/shipping_request']")
    close_btn = (By.XPATH, "//button[contains(text(),'Close')]")
    #continue_btn = (By.XPATH, "//button[@class='mat-ripple close']")
    shipping_and_label_link = (By.XPATH, "//span[contains(text(),'Shipping')]//parent::button")
    stamp_sheets_link = (By.XPATH, "//button[@id='stamp_sheets']")
    stamp_envelope_link = (By.XPATH, "//button[@id='stamp_envelope']")
    create_shipping_label_link_under_shipping_label = (By.XPATH, "//*[text()='Create Shipping Label']")
    general_preferences = (By.XPATH,"//a[@href='/general-preference/preferences']")
    shipping_label = (By.XPATH, "//*[contains(text(),'Shipping Labels')]")


    def __init__(self, app_config, driver, custom_logger):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(GermanyHomePageObjectsClass, self).__init__(driver)

    def check_setting_icon_in_homepage(self):
        flg = self.wait_element(*self.germany_menu_item)
        return flg

    def get_germany_header(self):
        return self.find_element(*self.germany_header)

    def get_germany_menu_item(self):
        return self.find_element(*self.germany_menu_item)

    def get_stamps_link(self):
        return self.find_element(*self.stamps_link)

    def get_roll_link(self):
        return self.find_element(*self.roll_link)

    def check_header_exists(self):
        flg = self.wait_element(*self.germany_header)
        return flg

    def click_on_header(self):
        self.custom_logger.info("Click on germany header link")
        self.get_germany_header().click()
        time.sleep(4)

    def get_device_link_item(self):
        return self.find_element(*self.my_device_link)

    def check_germany_menu_item(self):
        flg = self.wait_element(*self.germany_menu_item)
        return flg

    def click_on_menu_item(self):
        self.custom_logger.info("Click on Settings icon")
        self.click_using_js(*self.germany_menu_item)

    def check_my_device_link_exists(self):
        flg = self.wait_element(*self.my_device_link)
        return flg

    def click_on_my_device(self):
        self.custom_logger.info("Click on My Device link")
        self.wait_for_element_to_be_clickable(*self.my_device_link)
        self.click_using_js(*self.my_device_link)
        return GermanyMyDevicesObjectsClass(self.app_config, self.driver, self.custom_logger)

    def check_postage_sheet_btn(self):
        flg = self.wait_element(*self.roll_link)
        return flg

    def check_stamps_links(self):
        flg = self.wait_for_element_to_be_clickable(*self.stamps_link)
        return flg

    def click_on_stamps_link(self):
        self.custom_logger.info("Click on Stamps link")
        self.click_using_js(*self.stamps_link)

    def check_roll_btn_exists(self):
        flg = self.wait_element(*self.roll_link)
        return flg

    def click_on_roll_btn(self):
        self.custom_logger.info("Click on Roll Button")
        self.get_roll_link().click()
        return SP360PrintStampRollObjectsClass(self.app_config, self.driver, self.custom_logger)

    def get_create_shipping_label_btn(self):
        return self.find_element(*self.germany_create_shipping_label_btn)

    def check_create_shipping_label_btn(self):
        return self.wait_element(*self.germany_create_shipping_label_btn)

    def click_on_create_label_btn(self):
        self.custom_logger.info("Click on Create Shipping Labels")
        self.get_create_shipping_label_btn().click()
        return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)

    def check_ship_another_label_btn_exists(self):
        return self.wait_element(*self.ship_another_label)

    def scroll_to_ship_another_label(self):
        self.wait_element(*self.ship_another_label)
        self.scroll_to_element(*self.ship_another_label)

    def click_on_ship_another_label(self):
        self.click_using_js(*self.ship_another_label)
        return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)

    def check_create_ship_request_btn_exists(self):
        return self.wait_for_element_to_be_clickable(*self.shipping_request)


    def click_on_create_ship_request_btn(self):
        self.click_using_js(*self.create_ship_request_btn)
        return SP360CreateShipRequestObjectsClass(self.app_config, self.driver, self.custom_logger)

    def verify_PB_logo_in_homePage(self):
        self.verify_if_element_is_visible(*self.pb_logo_link)

    def click_on_shipping_label(self):
        self.wait_element(*self.shipping_label)
        self.click_using_js(*self.shipping_label)
        self.custom_logger.info("Clicked on Send a Parcel")
        return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)

    def click_on_close_btn(self):
        if (self.find_element(*self.close_btn).is_displayed() == True):
            self.click_using_js(*self.close_btn)

    def check_create_shipping_label_link(self):
        return self.wait_element(*self.create_shipping_label_link)

    def click_create_shipping_label_link(self):
        self.click_using_js(*self.create_shipping_label_link)
        return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)

    def click_on_shipping_and_mailing(self):
        self.wait_element(*self.shipping_and_label_link)
        self.click_using_js(*self.shipping_and_label_link)
        self.custom_logger.info("Clicked on shipping and mailing link")

    def click_on_shipping_request(self):
        try:
            self.click_using_js(*self.shipping_request)
            self.custom_logger.info("Click on shipping request")
            return SP360CreateShipRequestObjectsClass(self.app_config, self.driver, self.custom_logger)
        except:
            self.click_using_js(*self.create_shipping_label_link_under_shipping_label)
            self.custom_logger.info("Shipping Request link is not present")
            return SP360CreateShipRequestObjectsClass(self.app_config, self.driver, self.custom_logger)

    def check_stamp_sheet_link_exists(self):
        flg = self.wait_element(*self.roll_link)
        return flg

    def click_on_stamp_sheet_link(self):
        self.click_using_js(*self.stamp_sheets_link)
        self.custom_logger.info("Stamps sheet link is clicked")
        return SP360StampSheets(self.app_config, self.driver, self.custom_logger)

    def check_stamp_envelope_link_exists(self):
        flg = self.wait_element_till_time_limit(30,*self.stamp_envelope_link)
        return flg


    def click_shipping_label(self):
        try:
            self.wait_element(*self.create_shipping_label_link)
            self.click_on_shipping_and_mailing()
            self.click_using_js(*self.create_shipping_label_link_under_shipping_label)
            return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)
        except:
            return False

    def click_general_prefereces(self):
        self.wait_element(*self.general_preferences)
        self.click_using_js(*self.general_preferences)

