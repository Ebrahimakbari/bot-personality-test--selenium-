from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait , Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time ,random

driver = webdriver.Chrome()
driver.get('https://www.google.com')
actions = ActionChains(driver)
Wait = WebDriverWait(driver, 20)
driver.maximize_window()

def scroll(step):
    actions.scroll_to_element(step).perform()
    step.click()

search_result = Wait.until(ec.element_to_be_clickable((By.NAME,'q'))).send_keys('تست روانشناسی'+Keys.ENTER)
target_webpage = Wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a'))).click()
step_1 = Wait.until(ec.element_to_be_clickable((By.XPATH,'/html/body/main/div[3]/div/div[4]/div/a[1]')))
scroll(step_1)
step_2 = Wait.until(ec.element_to_be_clickable((By.LINK_TEXT,'تست شخصیت شناسی MBTI')))
scroll(step_2)
step_3 = Wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'a[href="javascript:void(0);"]')))
scroll(step_3)
step_4 = Wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR,'div[class="col-6 pl-1"]')))
scroll(step_4)
year = Wait.until(ec.element_to_be_clickable((By.XPATH, '//select[@id="age"]')))
Select(year).select_by_value('1375')
sex = Wait.until(ec.element_to_be_clickable((By.XPATH, '//select[@id="gender"]')))
Select(sex).select_by_value('زن')
step_5 = Wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="start-exam-form"]/div[2]/button'))).click()

for _ in range(10):
    time.sleep(3)
    num = str(random.randint(1,2))
    final = Wait.until(ec.element_to_be_clickable((By.XPATH, f'//label[@for="answer-{num}"]'))).click()
