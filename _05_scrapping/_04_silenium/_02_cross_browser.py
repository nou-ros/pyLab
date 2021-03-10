'''
1. web driver manager: helps to work with various web browsers. pip install webdriver-manager. With this new updated driver will be checked automatically.
2. cross browsing. 
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

#chrome
from webdriver_manager.chrome import ChromeDriverManager
# firefox
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName = 'opera'

if browserName == "chrome":
    # this will automatically download chrome driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari()
else:
    print("Please pass the correct browser name: " + browserName)
    # with exception the implicit, get and other methods will not be called. 
    raise Exception('driver is not found.')

driver.implicitly_wait(10)
driver.get('https://www.facebook.com/')
driver.find_element(By.ID, 'email').send_keys('test@gmail.com')
driver.find_element(By.ID, 'pass').send_keys('test@12345')
driver.find_element(By.NAME, 'login').click()

print(driver.title)
time.sleep(5)
driver.quit()