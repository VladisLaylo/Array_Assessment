"""
Scenario_1:
1. Validate that you are able to enroll properly with the test data
2. Validate the credit score page is loading properly
3. Validate that you are able to log out after finishing the test
"""
from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.MyCredit import MyCredit


class TestMyCreditManager(BaseTest):

    def test_login(self):
        self.myCredit = MyCredit(self.driver)

        self.myCredit.do_verify_your_identity_first_page()
        self.myCredit.do_verify_your_identity_second_page()
        self.myCredit.check_radio_buttons_15(TestData.USER_ANSW)
        self.myCredit.pass_last_pages()
        self.myCredit.get_user_title(MyCredit.USER_TITLE)
        self.myCredit.click_on_settings(MyCredit.SETTINGS)
        self.myCredit.click_on_logout(MyCredit.LOGOUT)
        self.myCredit.get_login_text(MyCredit.LOGIN_TITLE)
        # self.myCredit.expand_shadow_element(MyCredit.TAG_AAE, MyCredit.FIRST_NAME_FIELD)

# pytest Tests/test_MyCreditManagerPage.py
# pytest Tests/test_MyCreditManagerPage.py --count 5
# pytest Tests/test_MyCreditManagerPage.py -v --capture=tee-sys --html=reports/TestMyCreditScore.html
