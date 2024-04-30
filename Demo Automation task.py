from selenium import webdriver

# Provide the correct path to the Chrome WebDriver executable
driver = webdriver.Chrome(":\Users\ideofuzion\PycharmProjects\pythonProject3\venv\Lib\site-packages\selenium\webdriver\__init__.py")
driver.get('https://takaturn.io/')
element=driver.find_element_by_xapth("/html/body/div[3]/div[2]/button[2]").click()
element2=driver.find_element_by_xapth("/html/body/div[6]/div/div/div[2]/div[3]/button[2]").click()
login=driver.find_element_by_xapth("/html/body/div[2]/header/nav/div/div[2]/div/a").click()
Email=driver.find_element_by_xapth("//*[@id='email'']").send_keys("abdulbasitcomsats@gmail.com")
password=driver.find_element_by_xapth("//*[@id='password']").send_keys("Pass@123")
buttonlogin=driver.find_element_by_xapth('//*[@id="login-btn"]').click()
driver.quit()
