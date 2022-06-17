
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def send_keys_into_field(self, js, object_selector, key):
        jsc = js + object_selector
        self.driver.execute_script(jsc).send_keys(key)

    def send_click(self, js, object_selector):
        jsc = js + object_selector
        self.driver.execute_script(jsc).click()

    def send_submit(self, js, object_selector):
        jsc = js + object_selector
        self.driver.execute_script(jsc).click()

    def get_shadow_ele_text(self, jsc):
        element = self.driver.execute_script(jsc)
        ele = element.text
        print(ele)
