"""
Scenario_1:
1. Validate that you are able to enroll properly with the test data
2. Validate the credit score page is loading properly
3. Validate that you are able to log out after finishing the test

# noFramework approach
"""

import time
from selenium import webdriver
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/vanamali/PycharmProjects/Array_Assessment/Config/chromedriver')

"""s = Service('/Users/vanamali/PycharmProjects/Array_Assessment/Config/chromedriver')
driver = webdriver.Chrome(service=s)"""

#  TESTDATA

BASE_URL = "https://whitelabel.sandbox.array.io/signup?platform=v3"
FIRSTNAME = 'Thomas'
LASTNAME = 'Devos'
SSN = '3511'
# SSN = '666023511'
DOB = '1957-09-06'
STATE = 'AL'
STREET = '110 Beer Creek'
CITY = 'Tuscaloosa'
ZIP = '35405'

RANGE_1 = '$ 200 - $249'
RANGE_2 = '$ 385 - $484'

USER_ANSW = [
    "Thomas", "Devos", "Alabama", "Beer Creek", "Tuscaloosa", "35405", "110 Beer Creek", "$ 200 - $ 249",
    "$ 385 - $ 484", "Alabama", "ASI Medical", "Carroll County Bank &", "Great Financial SVC ", "IEC", "KIA Sorento",
    "Lynn Lee Const Co In", "New Hampshire", "Sallie Mae Servicing", "The Toronto-Dominion Bank", "Toyota Highlander",
    "Volkswagen Passat", "Wells Fargo & Company", "1957", "THOMAS", "DEVOS", "ALABAMA", "BEER CREEK", "TUSCALOOSA",
    "35405", "110 BEER CREEK", "$ 200 - $ 249", "$ 385 - $ 484", "ALABAMA", "ASI MEDICAL", "CARROLL COUNTY BANK &",
    "GREAT FINANCIAL SVC ", "IEC", "KIA SORENTO", "LYNN LEE CONST CO IN", "NEW HAMPSHIRE", "SALLIE MAE SERVICING",
    "THE TORONTO-DOMINION BANK", "TOYOTA HIGHLANDER", "VOLKSWAGEN PASSAT", "WELLS FARGO & COMPANY", "1957"
]

# OBJECTS
FIRST_PAGE_JS = "return document.querySelector('array-account-enroll').shadowRoot.querySelector"
TITLE1 = "('.description.svelte-iy0v6o')"
TITLE2 = "('.description.svelte-15t0hrc')"
TITLE3 = "('array-authentication-kba').shadowRoot.querySelector('.description.svelte-169z7uz')"
TITLE4 = "('.description.svelte-1eb7gu4')"

FIRST_NAME_FIELD = "('div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > " \
                   "div:nth-child(1) > div:nth-child(3) > input:nth-child(1)') "
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
NEXT = "('button').click()"
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
SUBMIT2 = "('button').click()"

RADIO_BUTTON = "('array-authentication-kba').shadowRoot.querySelectorAll('.input.svelte-2s0uww')"
RADIO_OPTION = "('array-authentication-kba').shadowRoot.querySelectorAll('.label.svelte-2s0uww')"

SUBMIT4 = "('array-authentication-kba').shadowRoot.querySelector('button').click()"

ARRAY_CREDIT_OVERVIEW = "return document.querySelector('array-credit-overview').shadowRoot.querySelector"
USER_TITLE = "('.title.svelte-qjs7fl')"

ARRAY_NAVBAR = "return document.querySelector('array-navbar').shadowRoot.querySelector"
SETTINGS = "('div:nth-child(2) > div:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > div:nth-child(4) > " \
           "div:nth-child(1)').click() "
LOGOUT = "('.submenu.logout.svelte-1ivnnxy').click()"

ARRAY_LOGIN = "return document.querySelector('array-account-login').shadowRoot.querySelector"
LOGIN_TITLE = "('div > div > div > .svelte-1gv5cw3')"


def click_on_element(object_selector):
    js = FIRST_PAGE_JS + object_selector
    driver.execute_script(js).click()


def click_on_next(object_selector):
    js = FIRST_PAGE_JS + object_selector
    driver.execute_script(js)


def send_keys_into_field(object_selector, key):
    js = FIRST_PAGE_JS + object_selector
    driver.execute_script(js).send_keys(key)


def get_element_text(object_selector):
    js = FIRST_PAGE_JS + object_selector
    element = driver.execute_script(js)
    print(element.text)


def get_user_title(object_selector):
    js = ARRAY_CREDIT_OVERVIEW + object_selector
    element = driver.execute_script(js)
    print(f"USER NAME IS: {element.text}")


def click_on_settings(object_selector):
    js = ARRAY_NAVBAR + object_selector
    driver.execute_script(js)


def click_on_logout(object_selector):
    js = ARRAY_NAVBAR + object_selector
    driver.execute_script(js)


def get_login_text(object_selector):
    js = ARRAY_LOGIN + object_selector
    element = driver.execute_script(js)
    print(element.text)


def check_radio_button_value(page_js, radio_text_selector, radio_button_selector, num, list_n):
    b = list(range(0, 25))
    c0 = f"[{b[num]}]"
    c1 = f"[{b[num + 1]}]"
    c2 = f"[{b[num + 2]}]"
    c3 = f"[{b[num + 3]}]"
    c4 = f"[{b[num + 4]}]"
    rts = page_js + radio_text_selector
    rbs = page_js + radio_button_selector

    try:
        element = driver.execute_script(rts + c0)
        radio0 = element.text
        print(element.text)
        if radio0 in list_n:
            driver.execute_script(rbs + c0).click()
            pass
    finally:
        pass

    try:
        element = driver.execute_script(rts + c1)
        radio1 = element.text
        print(element.text)
        if radio1 in list_n:
            driver.execute_script(rbs + c1).click()
            pass
    finally:
        pass

    try:
        element = driver.execute_script(rts + c2)
        radio2 = element.text
        print(element.text)
        if radio2 in list_n:
            driver.execute_script(rbs + c2).click()
            pass
    finally:
        pass

    try:
        element = driver.execute_script(rts + c3)
        radio3 = element.text
        print(element.text)
        if radio3 in list_n:
            driver.execute_script(rbs + c3).click()
            pass
        if radio3 not in list_n:
            driver.execute_script(rbs + c4).click()
    finally:
        pass


def check_radio_name_present(n):
    try:
        jsc = FIRST_PAGE_JS + RADIO_BUTTON + f"[{n}]"
        driver.execute_script(jsc)
    except JavascriptException:
        return False
    return True


def pass_last_pages():
    a = check_radio_name_present(1)
    b = check_radio_name_present(11)
    c = check_radio_name_present(21)

    try:
        if c is True:
            check_radio_button_value(0, USER_ANSW)
            check_radio_button_value(5, USER_ANSW)
            check_radio_button_value(10, USER_ANSW)
            check_radio_button_value(15, USER_ANSW)
            check_radio_button_value(25, USER_ANSW)
            click_on_next(SUBMIT4)
            time.sleep(10)
            click_on_next(SUBMIT2)
            pass
        elif c is not True:
            pass

        if b is True:
            check_radio_button_value(0, USER_ANSW)
            check_radio_button_value(5, USER_ANSW)
            check_radio_button_value(10, USER_ANSW)
            click_on_next(SUBMIT4)
            time.sleep(10)
            click_on_next(SUBMIT2)
        elif b is not True:
            pass

        if a is True:
            check_radio_button_value(0, USER_ANSW)
            click_on_element(SUBMIT4)
            time.sleep(10)
            click_on_next(SUBMIT2)
            pass
        elif a is not True:
            time.sleep(5)
            click_on_next(SUBMIT2)
            pass
    finally:
        print("Done")


# FIRST PAGE

driver.maximize_window()
driver.delete_all_cookies()
driver.get("chrome://settings/clearBrowserData")
driver.get(BASE_URL)
time.sleep(2)


def expand_shadow_element(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root


root = driver.find_element(by=By.TAG_NAME, value='array-account-enroll')

expand_shadow_element(root)



"""def expand_shadow_element(self, tag, element):
    shadow_root = self.driver.execute_script(
        f"return arguments[0].shadowRoot.querySelector('{tag}').shadowRoot.querySelector" + element)
    return shadow_root"""


get_element_text(TITLE1)

send_keys_into_field(FIRST_NAME_FIELD, FIRSTNAME)
send_keys_into_field(LAST_NAME_FIELD, LASTNAME)
send_keys_into_field(STREET_FIELD, STREET)
send_keys_into_field(CITY_FIELD, CITY)
send_keys_into_field(ZIP_FIELD, ZIP)

click_on_element(STATE_MENU)
click_on_element(ALABAMA_STATE)

click_on_next(NEXT)

# SECOND PAGE

get_element_text(TITLE2)

click_on_element(MONTH_MENU)
click_on_element(MONTH_BIRTH)
click_on_element(DAY_MENU)
click_on_element(DAY_BIRTH)
click_on_element(YEAR_MENU)
click_on_element(YEAR_BIRTH)
send_keys_into_field(SSN_FIELD, SSN)

click_on_next(SUBMIT2)

# THIRD PAGE

time.sleep(10)

# check_radio_button_value(0, USER_ANSW)
# check_radio_button_value(5, USER_ANSW)
# check_radio_button_value(10, USER_ANSW)

check_radio_button_value(FIRST_PAGE_JS, RADIO_OPTION, RADIO_BUTTON, 0, USER_ANSW)

click_on_next(SUBMIT4)
time.sleep(10)

# FINAL PAGE

pass_last_pages()
time.sleep(40)

get_user_title(USER_TITLE)
click_on_settings(SETTINGS)
click_on_logout(LOGOUT)

time.sleep(5)

get_login_text(LOGIN_TITLE)

driver.close()

# pytest Tests/draft.py
# pytest Tests/draft.py -v --capture=tee-sys --html=reports/TestMyCreditScore.html
