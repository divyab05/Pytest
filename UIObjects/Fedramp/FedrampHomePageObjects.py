import time
from selenium.webdriver.common.by import By
from UIObjects.BaseObject import BasePage
from UIObjects.Fedramp.FedrampMyDevicesPageObjects import FedrampMyDevicesPageObjects
from UIObjects.SP360.SP360CreateShipRequestPageObjects import SP360CreateShipRequestObjectsClass
from UIObjects.SP360.SP360CreateShippingLabels import SP360CreateShippingLabelObjectsClass
from UIObjects.SP360.SP360PrintStampRollObjects import SP360PrintStampRollObjectsClass
from UIObjects.SP360.SP360StampEnvelope import SP360StampEnvelopeClass
from UIObjects.SP360.SP360StampSheets import SP360StampSheets


class FedrampHomePageObjectsClass(BasePage):
    fedramp_header = (By.XPATH, "//a[contains(text(),'SendPro')]")
    settings_icon = (By.XPATH, "//button[@aria-label='Settings']")
    my_device_link = (By.XPATH, "//a/span[contains(text(),'My Devices')]")
    roll_link = (By.XPATH, "//button[@id ='stamp_rolls']")
    stamps_link = (By.XPATH, "//a[contains(text(), 'Stamps')]")
    sp360_create_shipping_label_btn = (By.XPATH, "//button[@id='create_shipping_label']")
    ship_another_label = (By.XPATH, "(//a[contains(text(), 'Ship Another')])[1]")
    create_shipping_label_link = (By.XPATH, "//button[@id='create_shipping_label']")
    create_ship_request_btn = (By.XPATH, "//button[@id='create_ship_request']")
    pb_logo_link = (By.XPATH, "//a[contains(text(),'pitney bowes')]"),
    shipping_label = (By.XPATH, "//a[contains(text(),'Shipping Labels')]")
    shipping_label_print = (By.XPATH, "//button[@id='btnPrintShippingLabel']")
    shipping_request = (By.XPATH, "//a[@href='/sending/label/print/shipping_request']")
    close_btn = (By.XPATH, "//button[contains(text(),'Close')]")
    #continue_btn = (By.XPATH, "//button[@class='mat-ripple close']")
    shipping_and_label_link = (By.XPATH, "//span[contains(text(),'Shipping')]//parent::button")
    stamp_sheets_link = (By.XPATH, "//button[@id='stamp_sheets']")
    stamp_envelope_link = (By.XPATH, "//button[@id='stamp_envelope']")
    create_shipping_label_link_under_shipping_label = (By.XPATH, "//*[text()='Create Shipping Label']")
    err_ship_request = (By.XPATH, "//*[contains(text(),'Create ERR Ship Request')]")
    create_err_link = (By.XPATH, "//*[contains(text(),'Create an ERR')]")
    create_certified_mail_link = (By.XPATH, "//*[contains(text(),'Create a Certified Mail')]")

    def __init__(self, app_config, driver, custom_logger):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(FedrampHomePageObjectsClass, self).__init__(driver)

    def click_on_header(self):
        self.click_using_js(*self.fedramp_header)

    def check_header_exists(self):
        return self.wait_element(*self.fedramp_header)

    def check_setting_icon_in_homepage(self):
        flg = self.wait_element(*self.settings_icon)
        return flg

    def get_device_link_item(self):
        return self.find_element(*self.my_device_link)

    def check_fedramp_menu_item(self):
        flg = self.wait_element(*self.settings_icon)
        return flg

    def click_on_menu_item(self):
        self.custom_logger.info("Click on Settings icon")
        self.click_using_js(*self.settings_icon)

    def check_my_device_link_exists(self):
        flg = self.wait_element(*self.my_device_link)
        return flg

    def check_stamps_links(self):
        flg = self.wait_for_element_to_be_clickable(*self.stamps_link)
        return flg

    def click_on_stamps_link(self):
        self.custom_logger.info("Click on Stamps link")
        self.click_using_js(*self.stamps_link)

    def check_stamp_sheet_link_exists(self):
        flg = self.wait_element(*self.roll_link)
        return flg

    def click_on_stamp_sheet_link(self):
        self.click_using_js(*self.stamp_sheets_link)
        self.custom_logger.info("Stamps sheet link is clicked")
        return SP360StampSheets(self.app_config, self.driver, self.custom_logger)

    def click_on_my_device(self):
        self.custom_logger.info("Click on My Device link")
        self.wait_for_element_to_be_clickable(*self.my_device_link)
        self.click_using_js(*self.my_device_link)
        return FedrampMyDevicesPageObjects(self.app_config, self.driver, self.custom_logger)

    def click_on_shipping_and_mailing(self):
        self.wait_element(*self.shipping_and_label_link)
        self.click_using_js(*self.shipping_and_label_link)
        self.custom_logger.info("Clicked on shipping and mailing link")

    def check_create_ship_request_btn_exists(self):
        return self.wait_for_element_to_be_clickable(*self.shipping_request)

    def click_on_shipping_request(self):
        try:
            self.click_using_js(*self.shipping_request)
            self.custom_logger.info("Click on shipping request")
            return SP360CreateShipRequestObjectsClass(self.app_config, self.driver, self.custom_logger)
        except:
            self.click_using_js(*self.create_shipping_label_link_under_shipping_label)
            self.custom_logger.info("Shipping Request link is not present")
            return SP360CreateShipRequestObjectsClass(self.app_config, self.driver, self.custom_logger)

    def check_ship_another_label_btn_exists(self):
        return self.wait_element(*self.ship_another_label)

    def scroll_to_ship_another_label(self):
        self.wait_element(*self.ship_another_label)
        self.scroll_to_element(*self.ship_another_label)

    def click_on_shipping_label(self):
        self.click_using_js(*self.shipping_label)
        self.custom_logger.info("Clicked on shipping label")
        return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)

    def click_on_ship_another_label(self):
        self.click_using_js(*self.ship_another_label)
        return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)

    def check_stamp_envelope_link_exists(self):
        flg = self.wait_element_till_time_limit(30, *self.stamp_envelope_link)
        return flg

    def click_on_stamp_envelope_link(self):
        self.click_using_js(*self.stamp_envelope_link)
        self.custom_logger.info("Stamps envelope link is clicked")
        return SP360StampEnvelopeClass(self.app_config, self.custom_logger, self.driver)

    def check_roll_btn_exists(self):
        flg = self.wait_element(*self.roll_link)
        return flg

    def get_roll_link(self):
        return self.find_element(*self.roll_link)

    def click_on_roll_btn(self):
        self.custom_logger.info("Click on Roll Button")
        self.get_roll_link().click()
        return SP360PrintStampRollObjectsClass(self.app_config, self.driver, self.custom_logger)

    def click_shipping_label(self):
        try:
            self.wait_element(*self.create_shipping_label_link)
            self.click_on_shipping_and_mailing()
            self.click_using_js(*self.create_shipping_label_link_under_shipping_label)
            return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)
        except:
            return False

    def click_on_Err_ship_Request(self):
        self.wait_element(*self.err_ship_request)
        self.click_using_js(*self.err_ship_request)

    def click_on_create_err_link(self):
        self.wait_element(*self.create_err_link)
        self.click_using_js(*self.create_err_link)
        self.custom_logger.info("Clicked on Create ERR Link")
        return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)

    def click_on_certified_mail_link(self):
        self.wait_element(*self.create_certified_mail_link)
        self.click_using_js(*self.create_certified_mail_link)
        self.custom_logger.info("Clicked on Certified mail Link")
        return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)

    def check_err_or_certifiedmail_link(self, link):
        if link == "Certified Mail":
            self.wait_element(*self.create_certified_mail_link)
            return True
        elif link == "ERR link":
            self.wait_element(*self.create_err_link)
            return True
        else:
            return False
