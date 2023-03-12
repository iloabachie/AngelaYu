from selenium import webdriver
import os, dotenv  # py -m pip install python-dotenv

dotenv.load_dotenv('day48-selenium\\.env')
token = os.getenv('TOKEN')
username = os.getenv('USERZNAME')


print(token, username)
print(os.environ.get('TOKEN'))
print(os.getenv('TEMP'))

chrome_driver_path = 'D:\\Documents\\Python lessons\\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.amazon.com')
driver.find_element()

driver.close() # closes active tab
driver.quit() # closes the window


