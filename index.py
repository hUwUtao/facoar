from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import math

import pickle
import os

driver = webdriver.Chrome()

# cookie resume phase/login
driver.get("https://mbasic.facebook.com/home.php")
if not os.path.isfile("./cookies.pickle"):
  print("try login, you have 1 hour, or the script will out-of-bound")
  WebDriverWait(driver, 60 * 60).until(
    EC.url_matches("https://mbasic.facebook.com/home.php")
  )
  pickle.dump(driver.get_cookies(), open("cookies.pickle", "wb"))
  print("saved cookies.pickle, keep it safe")
else:
  print("found cookies.pickle, resume")
  cookies = pickle.load(open("cookies.pickle", "rb"))
  for cookie in cookies:
    driver.add_cookie(cookie)
  driver.get(
    # INNOCENT COW!
    "data:text/plain;charset=utf-8;base64,X19fX19fX19fX19fX19fX19fX19fX19fX18NCjwgSGV5LCBsb29rIGF0IHRoZSB0ZXJtaW5hbCEgPg0KICAtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQ0KICAgICAgICAgICAgXl9fXiANCiAgICAgICAgICAgIChvbylfX19fX19fDQogICAgICAgICAgICAgKF9fKSAgICAgICApLw0KICAgICAgICAgICAgICAgICB8fC0tLS13IHwNCiAgICAgICAgICAgICAgICAgfHwgICAgIHx8"
  )

driver.get(input("Enter the URL you want to save: "))
print("Started")
fs = 0


def ts():
  global fs
  fs = math.floor(time.time() * 1000)


ts()
P = fs
os.makedirs(f"pages/{P}", exist_ok=True)
with open(f"pages/{P}/index.html", "wb") as tio:
  while True:
    with open(f"pages/{P}/p{fs}.html", "wb") as fio:
      buf = b""
      ts()
      for e in driver.find_elements(
        By.CSS_SELECTOR,
        'div[id^="7"]:not([class*=" "]):has(div>div>span[id^=like])',
      ):
        buf += b"<fieldset>"
        buf += (
          e.get_attribute("outerHTML")
          .replace('href="/', 'href="https://mbasic.facebook.com/')
          .encode("utf8")
        )
        buf += b"</fieldset>\n"
      fio.write(buf)
      tio.write(buf)
      fio.write(f'<a href="./p{fs}.html"><h2>NEXT PAGE</h2></a>'.encode("utf8"))
    try:
      driver.find_element(
        By.CSS_SELECTOR, 'div[id*=more_2]>a[href^="/comment/replies/?ctoken"]'
      ).click()
    except:  # noqa: E722
      print(f"Finish, saved {P}/ and {P}.html")
      driver.quit()
      break
