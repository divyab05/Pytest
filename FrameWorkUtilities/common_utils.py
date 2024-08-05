import configparser
import os
import platform
import time
import polling
from pywinauto.timings import wait_until
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException, \
    ElementNotVisibleException, ElementNotSelectableException, StaleElementReferenceException
from FrameWorkUtilities import excel_utils


class common_utils:

    @staticmethod
    def check_wait_until_element_present(expression):
        try:
            # wait a maximum of 10.5 seconds for the
            # the objects expression method to return 10
            # in increments of .5 of a second
            flg = wait_until(10.5, .5, expression, True)
            return flg
        except TimeoutError as e:
            flg = False
            return flg

    @staticmethod
    def read_config_return_value(config_section_header, config_key):
        path = os.getcwd() + "/ConfigFiles/"
        config = configparser.RawConfigParser()
        config.read(os.path.join(path, "config.txt"))
        return config.get(config_section_header, config_key)

    @staticmethod
    def wait_for_window_to_appear(expression, timeunit):
        try:
            result = polling.poll(
                lambda: expression.exists(),
                step=3,
                timeout=timeunit)
            print("Inside Polling")
        except Exception as err:
            print("Element does not exists and timeout after {arg1} seconds".format(arg1=timeunit))
            return False
        return True

    @staticmethod
    def close_browser(driver):
        driver.close()

    @staticmethod
    def timeout_handler(func):
        def exception_decorator(*args, **kwargs):
            try:
                func(*args, **kwargs)
                return True
            except TimeoutException:
                print("ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {arg1}".format(arg1=args))
                return False
            except Exception:
                print("EXCEPTION OCCURRED FOR FUNCTION {arg1} AND LOCATOR {arg2}".format(arg1=func.__name__, arg2=args))
                return False

        return exception_decorator

    @staticmethod
    def exception_handler(func):
        def exception_decorator(*args, **kwargs):
            try:
                results = func(*args, **kwargs)
                return results
            except TimeoutException:
                print("ELEMENT NOT FOUND WITHIN GIVEN TIME! --> {arg1}".format(arg1=func.__name__))
                raise
            except NoSuchElementException:
                print("LOCATOR NOT FOUND {arg1} FOR FUNCTION {arg2}".format(arg1=args, arg2=func.__name__))
                raise
            except NoSuchWindowException:
                print("WINDOW NOT FOUND FOR FUNCTION {arg1} AND LOCATOR {arg2}".format(arg1=func.__name__, arg2=args))
                raise
            except ElementNotVisibleException:
                print("ELEMENT NOT VISIBLE FOR FUNCTION {arg1} AND LOCATOR {arg2}".format(arg1=func.__name__,
                                                                                          arg2=args))
                raise
            except ElementNotSelectableException:
                print("ELEMENT NOT SELECTABLE FOR FUNCTION {arg1} AND LOCATOR {arg2}".format(arg1=func.__name__,
                                                                                             arg2=args))
                raise
            except StaleElementReferenceException:
                print("STALE ELEMENT REFERENCE FOR FUNCTION {arg1} AND LOCATOR {arg2}".format(arg1=func.__name__,
                                                                                              arg2=args))
            except Exception:
                print("EXCEPTION OCCURRED FOR FUNCTION {arg1} AND LOCATOR {arg2}".format(arg1=func.__name__, arg2=args))
                raise

        return exception_decorator

    @staticmethod
    def get_system_name(env):
        if env == "prod":
            sys_name = platform.uname().node
            return sys_name
        else:
            sys_name = platform.uname().node + "-{arg1}".format(arg1=str(env).lower())
            return sys_name

    @staticmethod
    def read_excel_data_store(file_name, sheet_name):
        file_path = os.getcwd() + "/TestData/{arg1}".format(arg1=file_name)
        results = excel_utils.read_from_excel(file_path, sheet_name)
        return results['Records']

    """
    This function is used to check the download status of Devicehub installer
    file_name: Name of the file which is downloading
    """

    @staticmethod
    def check_download_complete(file_name):
        time.sleep(10)
        wait = True
        file_path = os.getcwd() + "\downloads"
        while wait:
            for file_name in os.listdir(file_path):
                if file_name.split(".")[1] == "crdownload" or len(os.listdir(file_path)) > 1:
                    print("Downloading in progress")
                    time.sleep(5)
                else:
                    wait = False
        print("Finished Downloading all files")

    def replace_txt_in_a_file(self, filepath, txt_to_replace, txt_replaced):
        with open(filepath, 'r') as file:
            filedata = file.read()
            print(filedata)
            filedata = filedata.replace(txt_to_replace, txt_replaced)
        with open(filepath, 'w') as file:
            file.write(filedata)


