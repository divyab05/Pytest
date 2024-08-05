import datetime
import inspect
import json
import logging
import os

import webdriver_manager
from hamcrest import assert_that
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from ConfigFiles.config import Config
from FrameWorkUtilities import crypt
from FrameWorkUtilities.zephyr_utils import zephyr_utils
from UIObjects.LogInPageObjects import LogInObjectsClass


def pytest_addoption(parser):
    try:

        # Adding Addoption for DeviceHub
        parser.addoption('--app_env', action='store', default="QA",
                         help='Environment to run the Test Suite on')
        parser.addoption('--product_name', action='store', default="sp360commercial",
                         help='Project name to run test suite')
        parser.addoption('--username', action='store', default="default",
                         help='username pass from command prompt')
        parser.addoption('--password', action='store', default="default"
                         , help='password pass from command prompt')
        parser.addoption('--browser', action='store', default="chrome", help="browser to run the suite")
        parser.addoption('--language', action='store', default="english",
                         help="Language selection for DH App Installation")
        parser.addoption('--run_mode', action='store', default="headed", help="browser to run in headless mode")

    except Exception as e:
        print("Exception when trying to run test: %s" % __file__)
        print("Python says:%s" % str(e))


@pytest.fixture(scope='session', autouse=True)
def context():
    yield {}


@pytest.fixture(scope='session', autouse=True)
def get_language(request, custom_logger):
    custom_logger.info("Executing test Suite for project {arg1} ".format(arg1=
                                                                         request.config.getoption('--language')))
    print(request.config.getoption('--language'))
    return request.config.getoption('--language')


@pytest.fixture(scope='session', autouse=True)
def get_env(request, custom_logger):
    custom_logger.info("Initializing {arg1} environment".format(arg1=request.config.getoption('--app_env')))
    print(request.config.getoption('--app_env'))
    return request.config.getoption('--app_env')


@pytest.fixture(scope='session', autouse=True)
def get_product_name(request, custom_logger):
    custom_logger.info("Executing test Suite for project {arg1} ".format(arg1=
                                                                         request.config.getoption('--product_name')))
    print(request.config.getoption('--product_name'))
    return request.config.getoption('--product_name')


def pytest_terminal_summary(terminalreporter, exitstatus):
    """add additional section in terminal summary reporting."""
    env = ["qa", "ppd", "prod"]
    if terminalreporter.config.getoption("--app_env") in env:
        product_name = terminalreporter.config.getoption("--product_name")
        #project_name = terminalreporter.config.getoption("-m")
        # service_name = str(project_name).split("{arg1}{arg2}".format(arg1="_", arg2=product_name))[0]
        # print(service_name)
        obj_zephyr = zephyr_utils()
        token = obj_zephyr.jwt_token_generation()
        response_data = obj_zephyr.create_automation_job(token, product_name)
        print(response_data.text)
        job_id = (str(json.loads(response_data.text)['message']).split(":"))[1].strip()
        print("Automation Job id is {arg1}".format(arg1=job_id))
        obj_zephyr.execute_automation_task(job_id, token)


@pytest.fixture(scope='session', autouse=True)
def get_username(request, custom_logger):
    custom_logger.info("Executing test Suite for username {arg1} ".format(arg1=
                                                                          request.config.getoption('--username')))
    print(request.config.getoption('--username'))
    return request.config.getoption('--username')


@pytest.fixture(scope='session', autouse=True)
def get_password(request, custom_logger):
    custom_logger.info("Executing test Suite for password {arg1} ".format(arg1=
                                                                          request.config.getoption('--password')))
    print(request.config.getoption('--password'))
    return request.config.getoption('--password')


@pytest.fixture(scope='session', autouse=True)
def get_browser(request, custom_logger):
    custom_logger.info("Test suite starts running on {arg1} browser".format(arg1=request.config.getoption('--browser')))
    return request.config.getoption('--browser')


@pytest.fixture(scope='session', autouse=True)
def get_run_mode(request, custom_logger):
    custom_logger.info("Test suite is executing in {arg1} mode".format(arg1=request.config.getoption('--run_mode')))
    return request.config.getoption('--run_mode')


@pytest.fixture(scope='session', autouse=True)
def app_config(request, get_env, get_product_name, get_language, custom_logger):
    cfg = Config(get_env, get_product_name, get_language)
    custom_logger.info("Initializing config.py file for product {arg1} based on environment "
                       "{arg2}".format(arg1=get_product_name, arg2=get_env, arg3=get_language))
    yield cfg


@pytest.fixture(scope='session', autouse=True)
def custom_logger(logLevel=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    log_path = os.path.join(os.getcwd(), 'logs')
    if os.path.exists(log_path) is False:
        try:
            os.makedirs(log_path, exist_ok=True)
        except OSError as error:
            print("Directory can not be created with error message {arg1}".format(arg1=error))

    log_file_name = 'logfile_' + str(datetime.datetime.now()).replace(":", "_") + '.log'
    file_handler = logging.FileHandler(log_path + '/' + log_file_name, mode='a')
    file_handler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    yield logger


@pytest.fixture(scope="session")
def get_driver(get_browser, get_run_mode):
    global options, driver
    if get_browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        down_dir_path = os.getcwd() + "\downloads"
        options.add_experimental_option("prefs", {
            "download.default_directory": down_dir_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        if get_run_mode == "headless":
            options.add_argument("--headless=new")
        # for windows 11
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # for windows 10
        # driver = webdriver.Chrome(service=Service(webdriver_manager.ChromeDriverManager().install()), options=options)
        # driver = webdriver.Chrome(service=Service(webdriver_manager.ChromeDriverManager().install()), options=options)
        # driver = webdriver.Chrome(options=options)

    elif get_browser == "firefox":
        options = webdriver.FirefoxOptions()
        down_dir_path = os.getcwd() + "\downloads"
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.dir", down_dir_path)
        if get_run_mode == "headless":
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif get_browser == "safari":
        options = webdriver.SafariOptions()
        driver = webdriver.Safari(options=options)
    elif get_browser == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def setup_dh(get_driver, app_config, custom_logger, get_username, get_password, get_product_name):
    custom_logger.info("Launching the application with url {arg1}".format(arg1=app_config.env_cfg['url']))
    get_driver.get(app_config.env_cfg['url'])
    login_obj = LogInObjectsClass(app_config, get_driver, custom_logger)
    assert_that(login_obj.check_log_in_page_loaded(), "Login Page is not loaded")
    if get_username == "default" and get_username == "default":

        decrypted_pwd = crypt.decode(app_config.env_cfg['pwd_encrypted_key'], app_config.env_cfg['enc_pwd'])
        login_obj.enterLogInDetails(app_config.env_cfg['username'], decrypted_pwd, get_product_name)
    else:
        login_obj.enterLogInDetails(get_username, get_password, get_product_name)
    print('get_product_name  ' + get_product_name)
    homePage = login_obj.click_sigIn_btn(get_product_name)
    homePage.check_setting_icon_in_homepage()
    login_obj.click_Agree_btn(get_product_name)
    yield homePage
