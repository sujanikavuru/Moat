import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

input_text = ["Saturn", "Saturday’s Market", "Krux"]
rand_list = []
count = 0
driver = webdriver.Chrome(executable_path="drivers/chromedriver")
driver.get("https://moat.com/")
driver.maximize_window()

for i in input_text:
    # driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    # driver.get("https://moat.com/")
    # driver.maximize_window()
    if count > 0:
        driver.back()
        driver.back()

    wait = WebDriverWait(driver, 200)
    search = wait.until(
        expected_conditions.visibility_of_element_located((By.ID, "adsearch-input")))
    search.click()
    search.send_keys(i)
    search_list = wait.until(
        expected_conditions.visibility_of_all_elements_located((By.XPATH, ".//span[@class='non-query-string']")))
    for k in search_list:
        if k.text == i:
            k.click()
            break

    wait = WebDriverWait(driver, 200)
    var = wait.until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//span[@class='header-text']")))
    time.sleep(20)
    # driver.implicitly_wait(100)
    # wait = WebDriverWait(driver, 200)
    print("creatives_count", var.text)

    rb = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Random Brand")))
    rb.click()
    random = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[@class='page-type']")))
    rand_list.append(random.text)
    element_to_hover_over = wait.until(
        expected_conditions.visibility_of_all_elements_located((By.XPATH, "//div[@class='er-creative  ']")))
    for each in element_to_hover_over:
        hover = ActionChains(driver).move_to_element(each)
        hover.perform()
        share = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Share")))
        share.click()
        driver.find_element_by_xpath("//div[@class='popup-body']").click()
        driver.find_element_by_class_name("close-popup-icon").click()
        break
    # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    count = count + 1
print(rand_list)


