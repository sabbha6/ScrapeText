from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_driver(url):
  # Set the browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get(url)

  return driver


def main():
  driver = get_driver("https://automated.pythonanywhere.com/")
  time.sleep(2)
  # click_login = driver.find_element(By.XPATH,
  #                                   '//*[@id="basicExampleNav"]/div/a')
  # click_login.click()
  driver = get_driver("https://automated.pythonanywhere.com/login/")
  username = driver.find_element(By.ID, 'id_username')
  username.send_keys('automated')
  password = driver.find_element(By.ID, 'id_password')
  password.send_keys('automatedautomated' + Keys.RETURN)
  time.sleep(2)
  temperature = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/h1[2]')))
  print(float(temperature.text.split(': ')[1]))
  # print(driver.current_url)


# txt = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
# print(txt.text)

main()
