import time

from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    search_bar_id = "adsearch-input"
    search_bar_drop_down_xpath = ".//span[@class='non-query-string']"
    creatives_xpath = "//span[@class='header-text']"
    creative_verify_xpath = "//img[@class='fade-in']"
    random_brand_link_text = "Random Brand"
    random_brand_text_xpath = "//span[@class='page-type']"
    ads_mouseover_xpath = "//div[@class='er-creative  ']"
    ads_share_link_text = "Share"
    share_window_xpath = "//div[@class='popup-body']"
    share_window_close_class = "close-popup-icon"
    load_more_link_text = "Load More"
    rand_list = []

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(50)
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 200)
        # self.wait = WebDriverWait(driver, 200, poll_frequency=1)
        # self.wait = WebDriverWait(driver, 300, poll_frequency=1,
        #                           ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

    def searchBrand(self, search_text):
        search = self.wait.until(
            expected_conditions.visibility_of_element_located((By.ID, self.search_bar_id)))
        search.click()
        search.send_keys(search_text)

    def selectBrand(self, search_text):
        search_list = self.wait.until(
            expected_conditions.visibility_of_all_elements_located((By.XPATH, self.search_bar_drop_down_xpath)))
        for each_brand in search_list:
            try:
                if each_brand.text == search_text:
                    time.sleep(100)
                    each_brand.click()
                    break
            except TimeoutException:
                pass

    def creativecount(self):
        cc = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.creatives_xpath)))
        time.sleep(5)
        if cc.text:
            cc_split = cc.text
            creatives_count = cc_split.split(" ")
            while True:
                try:
                    load_more_button = self.wait.until(
                        expected_conditions.visibility_of_element_located((By.LINK_TEXT, self.load_more_link_text)))
                    time.sleep(2)
                    load_more_button.click()
                    time.sleep(5)
                except Exception as e:
                    print(e)
                    break
            creative_actual_count = self.wait.until(
                expected_conditions.visibility_of_any_elements_located((By.XPATH, self.creative_verify_xpath)))
            return creatives_count, creative_actual_count

    def randomBrand(self):
        self.wait.until(
            expected_conditions.visibility_of_element_located((By.LINK_TEXT, self.random_brand_link_text))).click()
        random = self.wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.random_brand_text_xpath)))
        return random.text

    def adsCheck(self):
        ads = self.wait.until(
            expected_conditions.visibility_of_all_elements_located((By.XPATH, self.ads_mouseover_xpath)))
        for each_ad in ads:
            hover = ActionChains(self.driver).move_to_element(each_ad)
            hover.perform()
            time.sleep(40)
            self.wait.until(
                expected_conditions.visibility_of_element_located((By.LINK_TEXT, self.ads_share_link_text))).click()
            break

    def verifyShare(self):
        self.driver.find_element_by_xpath(self.share_window_xpath).click()
        self.driver.find_element_by_class_name(self.share_window_close_class).click()
