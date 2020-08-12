import time
import unittest
from selenium.webdriver.common.keys import Keys
from first import BrowserRunner
import publish


class Login(BrowserRunner):
    def test_login(self):
        login_button = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div/main/div/div/div/div[1]/button/span[1]/span')
        login_button.click()
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        self.driver.get(
            'https://accounts.google.com/signin/oauth?response_type=code&client_id=27021292206-1iedinbvgo79q4elvue11dn15jaah7ja.apps.googleusercontent.com&redirect_uri=https://hamropatro-android-test.firebaseapp.com/__/auth/handler&state=AMbdmDn9kfsvfUYkVMtXHHIDpGNQ3nLWNTHRgbqBo5isMdfLlWK-nUpTGwsNHGP3s_K8byXzWwRSQI0EpNgvgFJBTQePruxFIQKZl1udyoW-GYeevMpLJCNp_d6nBxS9DCg5r2JO6S05akyx3lW6KJ2Ym4hxDMveBV8vCywOgkbgQzPd8wiqFanurDhW_0bBj-V_ZWz7L_jDTBkLRkXIIoujtEQu71vzqjOSMgLlp3QKgIU-mVcfNfAHixmm49xhORCxG4N0jkj6aDpunvuj0J1BOYdaz_ElnqT6cHaOFsNUAytcu2N-jTZ2MsPMaBcIBACV6QAHc_gLzuVrxd9SDnAi&scope=openid+https://www.googleapis.com/auth/userinfo.email+profile&context_uri=https://dev-dot-lightspeed-cms.lax-hamrostack.com&o2v=1&as=g9rNGOnK_cr1_6_P71ajAA')
        time.sleep(5)
        google_email = self.driver.find_element_by_id("identifierId")
        google_email.send_keys("something@gmail.com")
        google_email.send_keys(Keys.RETURN)
        time.sleep(3)
        google_password = self.driver.find_element_by_name('password')
        google_password.send_keys("something")
        google_password.send_keys(Keys.RETURN)
        time.sleep(2)
        self.driver.switch_to.window(window_before)
        time.sleep(10)
        login_button.click()
        self.assertIn("Light Speed", self.driver.title)
        publish.add(self.driver)


if __name__ == '__main__':
    unittest.main()
