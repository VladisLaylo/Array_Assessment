from selenium.common.exceptions import JavascriptException
from selenium.webdriver.common.by import By
from Config.config import TestData
from Tests.BasePage import BasePage
import time


class MyCredit(BasePage):
    FIRST_PAGE_JS = "return document.querySelector('array-account-enroll').shadowRoot.querySelector"
    TAG_AAE = "array-account-enroll"
    TITLE1 = "('.description.svelte-iy0v6o')"
    TITLE2 = "('.description.svelte-15t0hrc')"
    TITLE3 = "('array-authentication-kba').shadowRoot.querySelector('.description.svelte-169z7uz')"
    TITLE4 = "('.description.svelte-1eb7gu4')"

    FIRST_NAME_FIELD = "('div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(" \
                       "1) > div:nth-child(1) > div:nth-child(3) > input:nth-child(1)') "
    LAST_NAME_FIELD = "('div:nth-child(" \
                      "2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > " \
                      "div:nth-child(1) > div:nth-child(3) > input:nth-child(1)') "
    STREET_FIELD = "('div:nth-child(2) " \
                   "> div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > div:nth-child(1) > " \
                   "div:nth-child(3) > input:nth-child(1)')"
    CITY_FIELD = "('div:nth-child(2) > " \
                 "div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(4) > div:nth-child(1) > " \
                 "div:nth-child(3) > input:nth-child(1)')"
    ZIP_FIELD = "('div:nth-child(2) > " \
                "div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(6) > div:nth-child(1) > " \
                "div:nth-child(3) > input:nth-child(1)')"
    STATE_MENU = "('.svelte-1qqj4dt.placeholder-visible')"
    ALABAMA_STATE = "(\"option[value='AL']\")"
    MONTH_MENU = "('div:nth-child(2) > " \
                 "div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > " \
                 "div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > select:nth-child(1)') "
    MONTH_BIRTH = "('div:nth-child(2) > " \
                  "div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > " \
                  "div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > select:nth-child(1) > " \
                  "option:nth-child(10)')"
    DAY_MENU = "('div:nth-child(2) > " \
               "div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > " \
               "div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > select:nth-child(1)') "
    DAY_BIRTH = "('div:nth-child(2) > " \
                "div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > " \
                "div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > select:nth-child(1) > " \
                "option:nth-child(7)')"
    YEAR_MENU = "('div:nth-child(2) > " \
                "div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > " \
                "div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > select:nth-child(1)')"
    YEAR_BIRTH = "(\"option[value='1957']\")"
    SSN_FIELD = "('div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > " \
                "div:nth-child(1) > div:nth-child(3) > input:nth-child(1)') "
    SUBMIT = "('button')"
    RADIO_LABEL = "('array-authentication-kba').shadowRoot.querySelectorAll('.label.svelte-2s0uww')"
    RADIO_BUTTON = "('array-authentication-kba').shadowRoot.querySelectorAll('.input.svelte-2s0uww')"

    SUBMIT2 = "('array-authentication-kba').shadowRoot.querySelector('button')"

    ARRAY_CREDIT_OVERVIEW = "return document.querySelector('array-credit-overview').shadowRoot.querySelector"
    USER_TITLE = "('.title.svelte-qjs7fl')"

    ARRAY_NAVBAR = "return document.querySelector('array-navbar').shadowRoot.querySelector"
    SETTINGS = "('div:nth-child(2) > div:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > div:nth-child(4) > " \
               "div:nth-child(1)').click() "
    LOGOUT = "('.submenu.logout.svelte-1ivnnxy').click()"

    ARRAY_LOGIN = "return document.querySelector('array-account-login').shadowRoot.querySelector"
    LOGIN_TITLE = "('div > div > div > .svelte-1gv5cw3')"
    LOCATOR = (By.XPATH, '//*[@id="__next"]/div/div/div')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def do_verify_your_identity_first_page(self):
        environment = self.driver.execute_script("return navigator.userAgent;")
        print(f"Performed on environment: {environment}")
        self.send_keys_into_field(self.FIRST_PAGE_JS, self.FIRST_NAME_FIELD, TestData.FIRSTNAME)
        self.send_keys_into_field(self.FIRST_PAGE_JS, self.LAST_NAME_FIELD, TestData.LASTNAME)
        self.send_keys_into_field(self.FIRST_PAGE_JS, self.STREET_FIELD, TestData.STREET)
        self.send_keys_into_field(self.FIRST_PAGE_JS, self.CITY_FIELD, TestData.CITY)
        self.send_keys_into_field(self.FIRST_PAGE_JS, self.ZIP_FIELD, TestData.ZIP)
        root = self.driver.find_element(by=By.TAG_NAME, value='array-account-enroll')
        self.expand_shadow_element(root)
        self.send_click(self.FIRST_PAGE_JS, self.STATE_MENU)
        self.send_click(self.FIRST_PAGE_JS, self.ALABAMA_STATE)
        self.send_submit(self.FIRST_PAGE_JS, self.SUBMIT)

    def do_verify_your_identity_second_page(self):
        self.send_click(self.FIRST_PAGE_JS, self.MONTH_MENU)
        self.send_click(self.FIRST_PAGE_JS, self.MONTH_BIRTH)
        self.send_click(self.FIRST_PAGE_JS, self.DAY_MENU)
        self.send_click(self.FIRST_PAGE_JS, self.DAY_BIRTH)
        self.send_click(self.FIRST_PAGE_JS, self.YEAR_BIRTH)
        self.send_keys_into_field(self.FIRST_PAGE_JS, self.SSN_FIELD, TestData.SSN)
        self.send_submit(self.FIRST_PAGE_JS, self.SUBMIT)

    def expand_shadow_element(self, element):
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def get_user_title(self, object_selector):
        time.sleep(30)
        js = MyCredit.ARRAY_CREDIT_OVERVIEW + object_selector
        element = self.driver.execute_script(js)
        print(f"USER NAME IS: {element.text}")

    def click_on_settings(self, object_selector):
        js = MyCredit.ARRAY_NAVBAR + object_selector
        self.driver.execute_script(js)

    def click_on_logout(self, object_selector):
        js = MyCredit.ARRAY_NAVBAR + object_selector
        self.driver.execute_script(js)
        print(f"USER HAVE BEEN LOGGED OUT >>>")

    def get_login_text(self, object_selector):
        time.sleep(5)
        js = MyCredit.ARRAY_LOGIN + object_selector
        element = self.driver.execute_script(js)
        print(f"RETURNED TO >>> {element.text}")

    def check_radio_button_value(self, num, list_n):
        b = list(range(0, 25))
        c0 = f"[{b[num]}]"
        c1 = f"[{b[num + 1]}]"
        c2 = f"[{b[num + 2]}]"
        c3 = f"[{b[num + 3]}]"
        c4 = f"[{b[num + 4]}]"
        rts = self.FIRST_PAGE_JS + self.RADIO_LABEL
        rbs = self.FIRST_PAGE_JS + self.RADIO_BUTTON

        try:
            element = self.driver.execute_script(rts + c0)
            radio0 = element.text
            print(radio0)
            pass
            if radio0 in list_n:
                print("Selected >>> " + radio0)
                self.driver.execute_script(rbs + c0).click()
                pass
            if radio0 not in list_n:
                pass
        finally:
            pass

        try:
            element = self.driver.execute_script(rts + c1)
            radio1 = element.text
            print(radio1)
            pass
            if radio1 in list_n:
                print("Selected >>> " + radio1)
                self.driver.execute_script(rbs + c1).click()
                pass
            if radio1 not in list_n:
                pass
        finally:
            pass

        try:
            element = self.driver.execute_script(rts + c2)
            radio2 = element.text
            print(radio2)
            pass
            if radio2 in list_n:
                print("Selected >>> " + radio2)
                self.driver.execute_script(rbs + c2).click()
                pass
            if radio2 not in list_n:
                pass
        finally:
            pass

        try:
            element = self.driver.execute_script(rts + c3)
            radio3 = element.text
            print(radio3)
            pass
            if radio3 in list_n:
                print("Selected >>> " + radio3)
                self.driver.execute_script(rbs + c3).click()
                pass
            if radio3 not in list_n:
                element = self.driver.execute_script(rts + c4)
                radio4 = element.text
                print("Selected >>> " + radio4)
                self.driver.execute_script(rbs + c4).click()
                pass
        finally:
            pass

    def check_radio_name_present(self, n):
        try:
            jsc = MyCredit.FIRST_PAGE_JS + MyCredit.RADIO_BUTTON + f"[{n}]"
            self.driver.execute_script(jsc)
        except JavascriptException:
            return False
        return True

    def check_radio_buttons_15(self, user_list):
        time.sleep(12)
        self.check_radio_button_value(0, user_list)
        self.check_radio_button_value(5, user_list)
        self.check_radio_button_value(10, user_list)
        self.send_submit(self.FIRST_PAGE_JS, self.SUBMIT2)

    def pass_last_pages(self):
        time.sleep(12)
        a = self.check_radio_name_present(1)
        b = self.check_radio_name_present(5)
        c = self.check_radio_name_present(20)

        try:
            if c is True:
                self.check_radio_button_value(0, TestData.USER_ANSW)
                self.check_radio_button_value(5, TestData.USER_ANSW)
                self.check_radio_button_value(10, TestData.USER_ANSW)
                self.check_radio_button_value(15, TestData.USER_ANSW)
                self.check_radio_button_value(25, TestData.USER_ANSW)
                self.send_submit(self.FIRST_PAGE_JS, self.SUBMIT2)
                time.sleep(10)
                self.send_submit(self.FIRST_PAGE_JS, self.SUBMIT)
                pass
            elif c is not True:
                pass

            if b is True:
                self.check_radio_button_value(0, TestData.USER_ANSW)
                self.check_radio_button_value(5, TestData.USER_ANSW)
                self.check_radio_button_value(10, TestData.USER_ANSW)
                self.send_submit(self.FIRST_PAGE_JS, self.SUBMIT2)
                time.sleep(10)
                self.send_submit(self.FIRST_PAGE_JS, self.SUBMIT)
            elif b is not True:
                pass

            if a is True:
                self.check_radio_button_value(0, TestData.USER_ANSW)
                self.send_submit(self.FIRST_PAGE_JS, self.SUBMIT2)
                time.sleep(10)
                self.send_submit(self.FIRST_PAGE_JS, self.SUBMIT)
                pass
            elif a is not True:
                time.sleep(10)
                self.send_submit(self.FIRST_PAGE_JS, self.SUBMIT)
                pass
        finally:
            print("ARRAY ACCOUNT ENROLL PASSED >>>")
            pass
