import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from UIObjects.BaseObject import BasePage
from UIObjects.Canada.CanadaHomePageObjects import CanadaHomePageObjectsClass
from UIObjects.Fedramp.FedrampHomePageObjects import FedrampHomePageObjectsClass
from UIObjects.Germany.GermanyHomePageObjects import GermanyHomePageObjectsClass
from UIObjects.SP360.SP360HomePageObjects import SP360HomePageObjectsClass
from selenium.webdriver.support import expected_conditions as EC

from UIObjects.UK.UKHomePageObjects import UKHomePageObjectsClass


class LogInObjectsClass(BasePage):
    username = (By.XPATH, "//input[contains(@id,'username')]")
    password = (By.XPATH, "//input[contains(@id,'password')]")
    sso_password = (By.NAME, "password")
    signInBtn = (By.ID, 'signinButton')
    nextbtn = (By.ID, 'nextButton')
    nextbtn_sso = (By.ID, "okta-signin-submit")
    sso_username = (By.XPATH, "//input[@id='okta-signin-username']")
    btn_verify = (By.XPATH, "//input[@value='Verify']")
    btn_next_fedramp = (By.ID, "idp-discovery-submit")
    btn_siginin_fedaramp = (By.XPATH, "//div[@class='o-form-button-bar']/input")
    btn_Agree_fedramp =(By.XPATH,"//button[text()='Agree']")

    def __init__(self, app_config, driver, custom_logger):
        self.app_config = app_config
        self.custom_logger = custom_logger
        super(LogInObjectsClass, self).__init__(driver)

    def get_user_name(self):
        return self.find_element(*self.username)

    def get_password(self):
        return self.find_element(*self.password)

    def get_sign_in_btn(self):
        return self.find_element(*self.signInBtn)

    def get_next_btn(self):
        return self.find_element(*self.nextbtn)

    def check_log_in_page_loaded(self):
        flg = self.wait_element_till_time_limit(50,*self.username)
        return flg

    def check_sso_username(self):
        flg = self.find_element(*self.sso_username).is_displayed()
        return flg

    def check_password_input_exists(self):
        try:
            flg = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.password))
            return flg
        except:
            return False

    def get_sso_user_name(self):
        return self.find_element(*self.sso_username)

    def get_next_btn_fedramp(self):
        return self.find_element(*self.btn_next_fedramp)

    def enterLogInDetails(self,user_name, pass_word,get_product_name):
        print(get_product_name)

        if get_product_name == "fedramp":
            print('inside Fedramp')
            self.custom_logger.info("Enter username")
            self.get_user_name().send_keys(user_name)
            self.wait_element(*self.btn_next_fedramp)
            self.get_next_btn_fedramp().click()
            self.wait_element(*self.password)
            self.custom_logger.info("Enter Password")
            self.get_password().send_keys(pass_word)
        else :
            self.custom_logger.info("Enter username")
            self.get_user_name().send_keys(user_name)
            self.wait_element(*self.nextbtn)
            self.get_next_btn().click()
            password_flg = self.check_password_input_exists()
            if password_flg:
                self.wait_element(*self.password)
                self.custom_logger.info("Enter Password")
                self.get_password().send_keys(pass_word)
            else:
                self.login_with_sso_user(user_name, pass_word)
        # elif get_product_name == "sp360canada":
        #     self.custom_logger.info("Enter username")
        #     self.get_user_name().send_keys(user_name)
        #     self.wait_element(*self.nextbtn)
        #     self.get_next_btn().click()
        #     password_flg = self.check_password_input_exists()
        #     if password_flg:
        #         self.wait_element(*self.password)
        #         self.custom_logger.info("Enter Password")
        #         self.get_password().send_keys(pass_word)
        #     else:
        #         self.login_with_sso_user(user_name, pass_word)
        # elif get_product_name == "sp360uk":
        #     self.custom_logger.info("Enter username")
        #     self.get_user_name().send_keys(user_name)
        #     self.wait_element(*self.nextbtn)
        #     self.get_next_btn().click()
        #     password_flg = self.check_password_input_exists()
        #     if password_flg:
        #         self.wait_element(*self.password)
        #         self.custom_logger.info("Enter Password")
        #         self.get_password().send_keys(pass_word)
        #     else:
        #         self.login_with_sso_user(user_name, pass_word)


    def login_with_sso_user(self, user_name, pass_word):
        self.custom_logger.info("Enter username")
        self.wait_element(*self.sso_username)
        self.get_sso_user_name().send_keys(user_name)
        self.wait_element(*self.nextbtn_sso)
        self.find_element(*self.nextbtn_sso).click()
        self.wait_element(*self.sso_password)
        self.find_element(*self.sso_password).click()
        self.find_element(*self.sso_password).send_keys(pass_word)
        self.custom_logger.info("Enter Password")

    def get_verify_btn_sso_user(self):
        return self.find_element(*self.btn_verify)


    def check_sigIn_btn_visible(self):
        try:
            flg = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(self.signInBtn))
            return flg
        except:
            return False

    def click_sign_in_button_sp360(self):
        print('inside click')
        flg = self.check_sigIn_btn_visible()
        print(flg)
        if flg:
            self.custom_logger.info("Clicked on sign in button for SP360")
            self.get_sign_in_btn().click()
        elif self.verify_if_element_is_visible(*self.btn_verify):
            self.custom_logger.info("Clicked on verify button")
            self.get_verify_btn_sso_user().click()

    def click_sign_in_button_fedramp(self):
        time.sleep(2)
        self.wait_element(*self.btn_siginin_fedaramp)
        self.custom_logger.info("Clicked on sign in button for Fedramp")
        self.click_using_js(*self.btn_siginin_fedaramp)


    def click_sigIn_btn(self,get_product_name):
        print(get_product_name)
        if get_product_name == "sp360commercial":
            self.click_sign_in_button_sp360()
            return SP360HomePageObjectsClass(self.app_config, self.driver, self.custom_logger)
        elif get_product_name == "fedramp":
            print('Fedramp setting icon')
            self.click_sign_in_button_fedramp()
           # self.wait_element(*self.btn_Agree_fedramp)
            #self.click_using_js(*self.btn_Agree_fedramp)
            return FedrampHomePageObjectsClass(self.app_config, self.driver, self.custom_logger)
        elif get_product_name == "sp360canada":
            self.click_sign_in_button_sp360()
            return CanadaHomePageObjectsClass(self.app_config, self.driver, self.custom_logger)
        elif get_product_name == "sp360uk":
            self.click_sign_in_button_sp360()
            return UKHomePageObjectsClass(self.app_config, self.driver, self.custom_logger)
        elif get_product_name == "sp360germany":
            self.click_sign_in_button_sp360()
            return GermanyHomePageObjectsClass(self.app_config, self.driver, self.custom_logger)

    def click_Agree_btn(self,get_product_name):
        if get_product_name == "fedramp":
            self.click_using_js(*self.btn_Agree_fedramp)

