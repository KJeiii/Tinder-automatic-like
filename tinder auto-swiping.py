from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Chromewebdriver_path = '輸入自己Chromedriver的路徑'
tinder_URL = 'https://tinder.com/app/recs'
EMAIL = '目前是用FB帳號登入，請填入FB帳號'
PASSWORD = '請填入FB密碼'

driver = webdriver.Chrome(executable_path=Chromewebdriver_path)
driver.get(url=tinder_URL)
wait = WebDriverWait(driver,10)

accept_cookie = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c964396036"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')))
accept_cookie = driver.find_element(By.XPATH,'//*[@id="c964396036"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept_cookie.click()

login = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c964396036"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/div[2]/div[2]')))
login = driver.find_element(By.XPATH,'//*[@id="c964396036"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/div[2]/div[2]')
login.click()

login_by_FB = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c-763985040"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')))
login_by_FB = driver.find_element(By.XPATH,'//*[@id="c-763985040"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]/div/div')
login_by_FB.click()
time.sleep(5)

print(driver.window_handles)
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]

driver.switch_to.window(window_after)
print(driver.title)
FB_username = wait.until(EC.element_to_be_clickable((By.ID,'email')))
FB_username = driver.find_element(By.ID,'email')
FB_username.send_keys(EMAIL)
FB_password = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="pass"]')))
FB_password = driver.find_element(By.XPATH,'//*[@id="pass"]')
FB_password.send_keys(PASSWORD)
FB_login = driver.find_element(By.NAME,'login')
FB_login.click()
# continue_as_username = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="mount_0_0_E8"]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div')))
# continue_as_username = driver.find_element(By.XPATH,'//*[@id="mount_0_0_E8"]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div')
# continue_as_username.click()
print(driver.window_handles)
driver.switch_to.window(window_before)
print(driver.title)
time.sleep(5)

## Environtment setting
share_location = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c-763985040"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')))
share_location = driver.find_element(By.XPATH,'//*[@id="c-763985040"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
share_location.click()

no_interest = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c-763985040"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')))
no_interest = driver.find_element(By.XPATH,'//*[@id="c-763985040"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
no_interest.click()

# cross_on_darkmode = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="q-2130158254"]/main/div/div[2]/button')))
# no_interest = driver.find_element(By.XPATH,'//*[@id="q-2130158254"]/main/div/div[2]/button')
# no_interest.click()

## Like
for n in range(100):
    try:
        try:
            # 20230413memo：XPATH換了
            like = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c964396036"]/div/div[1]/div/div/main/div/div/div/div/div[4]/div/div[4]/button')))
            like = driver.find_element(By.XPATH,'//*[@id="c964396036"]/div/div[1]/div/div/main/div/div/div/div/div[4]/div/div[4]/button')
            like.click()
        except:
            like = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c964396036"]/div/div[1]/div/div/main/div/div/div/div/div[3]/div/div[4]/button')))
            like = driver.find_element(By.XPATH,'//*[@id="c964396036"]/div/div[1]/div/div/main/div/div/div/div/div[3]/div/div[4]/button')
            like.click()
    except:
        try:
            return_to_tinder = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="c-763985040"]/main/div/div/div/div[4]/button')))
            return_to_tinder = driver.find_element(By.XPATH,'//*[@id="c-763985040"]/main/div/div/div/div[4]/button')
            return_to_tinder.click()
        except:
            no_interest_set_web = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="q-2130158254"]/main/div/div[2]/button[2]')))
            no_interest_set_web = driver.find_element(By.XPATH,'//*[@id="q-2130158254"]/main/div/div[2]/button[2]')
            no_interest_set_web.click()
