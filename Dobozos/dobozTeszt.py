from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5500/Dobozos/index.html')

def elementOne():
    elementOne = driver.find_element(By.ID, 'element-one')
    elementOne.click()
    assert 'blur' in elementOne.get_attribute('class')

def elementTwo(color):
    time.sleep(0.5)
    elementTwo = driver.find_element(By.ID, 'element-two')
    ActionChains(driver).move_to_element(elementTwo).perform()
    assert f'background-color: {color};' in elementTwo.get_attribute('style')

def elementThree():
    time.sleep(5)
    elementThree = driver.find_element(By.ID, 'element-three')
    ActionChains(driver).double_click(elementThree).perform()


elementOne()
driver.save_screenshot('element-one_teszt.png')

elementTwo('red')
driver.save_screenshot('element-two_teszt.png')

elementThree()
driver.save_screenshot('element-three-teszt.png')

print('sikeres teszt')
driver.close()