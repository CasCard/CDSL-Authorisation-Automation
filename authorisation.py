from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import config
import easyimap as e
import email.utils
import bs4 as bs
from bs4 import NavigableString, Tag
import re
from_address=""

KITE_URL="https://kite.zerodha.com/"
HOLDINGS_URL="https://kite.zerodha.com/holdings"

message=""
OTP=0
pattern='(\d{2}):(\d{2}):(\d{2})'

option=Options()

driver=webdriver.Chrome(executable_path=config.WEB_DRIVER_LOCATION)

option.add_experimental_option("prefs",
{"profile.default_content_setting_values.notifications": 2
 })
driver.get(KITE_URL)
driver.find_element_by_id('userid').send_keys(config.KITE_USERNAME)
driver.find_element_by_id('password').send_keys(config.KITE_PASSWORD)
driver.find_element_by_class_name("button-orange").click()
driver.implicitly_wait(60)
driver.find_element_by_id('pin').send_keys(config.KITE_PIN)
driver.find_element_by_class_name("button-orange").click()
driver.implicitly_wait(60)
time.sleep(2)
driver.get(HOLDINGS_URL)
driver.implicitly_wait(60)
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/section/div/div/div/span[2]/a[1]").click()
time.sleep(2)
driver.implicitly_wait(60)
windows_before=driver.window_handles[0]
try:
    WebDriverWait(driver,8).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div[3]/div/button[1]")))
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div[3]/div/button[1]").click()
except TimeoutException:
    print("Page not loaded")
time.sleep(2)
driver.implicitly_wait(60)
windows_after=driver.window_handles[1]
driver.switch_to.window(windows_after)
driver.implicitly_wait(60)
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/button").click()
time.sleep(3)
driver.find_element_by_id("txtPIN").send_keys(config.CDSL_PIN)
driver.find_element_by_id("btnCommit").click()
driver.implicitly_wait(60)

current_time=time.localtime()
current_minute=int(time.strftime("%M", current_time))
current_second=int(time.strftime("%S", current_time))
total_seconds=(current_minute*60)+current_second
print("Execution time")
print(current_time,total_seconds)
recieved=False
driver.switch_to.window(windows_before)
server=e.connect("imap.gmail.com", config.GMAIL_USERNAME, config.GMAIL_PASSWORD)
while from_address != "edis@cdslindia.co.in":
    message=server.listup(1)[0]
    print(message)
    time_of_new_email=message.date
    match = re.search(pattern, str(time_of_new_email))
    new_email_second=(int(match.group()[3:5])*60)+int(match.group()[6:9])
    print(new_email_second)
    if new_email_second>total_seconds:
        print(match.group())
        # message = server.mail(server.listids()[0])
        from_address=email.utils.parseaddr(message.from_addr)[1]
        print(from_address)
        break

print(message)

# MINUTE = time.strftime('%H:%M:%S')

soup=bs.BeautifulSoup(message.body,'lxml')
for br in soup.findAll('br'):
    next_s = br.nextSibling
    if not (next_s and isinstance(next_s,NavigableString)):
        continue
    next2_s = next_s.nextSibling
    if next2_s and isinstance(next2_s,Tag) and next2_s.name == 'br':
        text = str(next_s).strip()
        if len(text)==6:
            OTP=text
            break
print(OTP)
driver.implicitly_wait(60)
driver.switch_to.window(windows_after)
driver.implicitly_wait(60)
driver.find_element_by_id("OTP").send_keys(OTP)
driver.implicitly_wait(60)
driver.find_element_by_id("VerifyOTP").click()
driver.implicitly_wait(60)
time.sleep(5)
print("Success")
driver.quit()


