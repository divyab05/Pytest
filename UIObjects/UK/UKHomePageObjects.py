import time
from selenium.webdriver.common.by import By
from UIObjects.BaseObject import BasePage
from UIObjects.SP360.SP360CreateShippingLabels import SP360CreateShippingLabelObjectsClass
from UIObjects.SP360.SP360MyDevicesPageObjects import SP360MyDevicesObjectsClass
from UIObjects.UK.UKPostageEnvelope import UKPostageEnvelope
from UIObjects.UK.UKPostageRoll import UKPostageRoll
from UIObjects.UK.UKStampSheets import UKStampSheets


class UKHomePageObjectsClass(BasePage):
    uk_header = (By.XPATH, "//a[contains(text(),'Pitney') or contains(text(),'pitney')]")
    settings_btn = (By.XPATH, "//button[@aria-label='Settings']")
    my_device_link = (By.XPATH, "//a[@href = '/device-hub/devices' and contains(text(), 'My Devices')]")
    send_a_letter_link = (By.XPATH, "//a[(@href='/mailing') and contains(text(), 'Send a Letter')]")
    sp360_create_shipping_label_btn = (By.XPATH, "//button[@id='create_shipping_label']")
    ship_another_label = (By.XPATH, "(//a[contains(text(), 'Ship Another')])[1]")
    create_shipping_label_link = (By.XPATH, "//button[@id='create_shipping_label']")
    pb_logo_link = (By.XPATH, "//a[contains(text(),'pitney bowes')]"),

    shipping_label_print = (By.XPATH, "//button[@id='btnPrintShippingLabel']")
    close_btn = (By.XPATH, "//button[contains(text(),'Close')]")
    continue_btn = (By.XPATH, "//button[@class='mat-ripple close']")
    shipping_and_label_link = (By.XPATH, "//span[contains(text(),'Shipping & Mailing')]")
    create_shipping_label_link_under_shipping_label = (By.XPATH, "//a[text()='Create Shipping Label']")
    postage_sheets_link = (By.XPATH, "//button/div[text()='Postage Sheets']")
    send_parcel_link = (By.XPATH, "//a[contains(text(),'Send a Parcel')]")
    postage_roll_link = (By.XPATH, "//button/div[text()='Postage Roll']")
    postage_envelope_link = (By.XPATH, "//div[text()='Envelope']//parent::button")

    def __init__(self, app_config, driver, custom_logger):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(UKHomePageObjectsClass, self).__init__(driver)

    def check_setting_icon_in_homepage(self):
        flg = self.wait_element(*self.settings_btn)
        return flg

    def check_sp360_menu_item(self):
        flg = self.wait_element(*self.settings_btn)
        return flg

    def get_uk_header(self):
        return self.find_element(*self.uk_header)

    def get_sp360_menu_item(self):
        return self.find_element(*self.settings_btn)

    def get_stamps_link(self):
        return self.find_element(*self.send_a_letter_link)

    def get_postage_roll_link(self):
        return self.find_element(*self.postage_roll_link)

    def check_header_exists(self):
        flg = self.wait_element(*self.uk_header)
        return flg

    def click_on_header(self):
        self.custom_logger.info("Click on UK header link")
        self.click_using_js(*self.uk_header)

    def get_device_link_item(self):
        return self.find_element(*self.my_device_link)

    def click_on_menu_item(self):
        self.custom_logger.info("Click on Settings icon")
        self.click_using_js(*self.settings_btn)

    def check_my_device_link_exists(self):
        flg = self.wait_element(*self.my_device_link)
        return flg

    def click_on_my_device(self):
        self.custom_logger.info("Click on My Device link")
        self.wait_for_element_to_be_clickable(*self.my_device_link)
        self.click_using_js(*self.my_device_link)
        return SP360MyDevicesObjectsClass(self.app_config, self.driver, self.custom_logger)

    def check_postage_sheet_btn(self):
        flg = self.wait_element(*self.postage_sheets_link)
        return flg

    def check_send_a_letter_link(self):
        flg = self.wait_for_element_to_be_clickable(*self.send_a_letter_link)
        return flg

    def click_send_a_letter_link(self):
        self.custom_logger.info("Click on Send letter link")
        self.click_using_js(*self.send_a_letter_link)

    def check_postage_roll_btn_exists(self):
        flg = self.wait_element(*self.postage_roll_link)
        return flg

    def click_on_postage_roll_btn(self):
        self.custom_logger.info("Click on Postage Roll Button")
        self.click_using_js(*self.postage_roll_link)
        return UKPostageRoll(self.app_config, self.driver, self.custom_logger)

    def get_create_shipping_label_btn(self):
        return self.find_element(*self.sp360_create_shipping_label_btn)

    def check_create_shipping_label_btn(self):
        return self.wait_element(*self.sp360_create_shipping_label_btn)

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

    def verify_PB_logo_in_homePage(self):
        self.verify_if_element_is_visible(*self.pb_logo_link)

    def click_on_shipping_label(self):
        self.wait_element(*self.send_parcel_link)
        self.click_using_js(*self.send_parcel_link)
        self.custom_logger.info("Clicked on send Parcel ")
        return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)

    def click_on_close_btn(self):
        if self.find_element(*self.close_btn).is_displayed() == True:
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

    def check_postage_sheet_link_exists(self):
        flg = self.wait_element(*self.postage_sheets_link)
        return flg

    def click_on_postage_sheet_link(self):
        self.click_using_js(*self.postage_sheets_link)
        self.custom_logger.info("Postage sheet link is clicked")
        return UKStampSheets(self.app_config, self.driver, self.custom_logger)

    def check_postage_envelope_link_exists(self):
        flg = self.wait_element_till_time_limit(30, *self.postage_envelope_link)
        return flg

    def click_on_postage_envelope_link(self):
        self.wait_element(*self.postage_envelope_link)
        self.click_using_js(*self.postage_envelope_link)
        self.custom_logger.info("Stamps envelope link is clicked")
        return UKPostageEnvelope(self.app_config, self.driver, self.custom_logger)

    def click_shipping_label(self):
        try:
            self.wait_element(*self.create_shipping_label_link)
            self.click_on_shipping_and_mailing()
            self.click_using_js(*self.create_shipping_label_link_under_shipping_label)
            return SP360CreateShippingLabelObjectsClass(self.app_config, self.driver, self.custom_logger)
        except:
            return False
