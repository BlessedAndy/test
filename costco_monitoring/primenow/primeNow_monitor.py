'''
Created on Apr 4, 2020

@author: Administrator
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from com.tools.notify import send_SMS_message

'''
Configuration block
'''
#Change to False when the script works
Debug = False

#------------------------------------------------------------
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')

if(Debug == False):
    options.headless = True # set to headless without opening browser

#Your account and password for Costco
userEmail = 'blessedandy@hotmail.com'
userPassword = 'Zsmfxy@516'
zipcode = 19087


def monitor():
    driver = webdriver.Chrome(options=options, executable_path=r'C:/stock/chromedriver.exe')
    
    #Change the checkout URL as yours
    URL = 'https://primenow.amazon.com/'
    driver.get(URL)
    
    #input userEmail and password
    input_zipcode = driver.find_element_by_id('lsPostalCode')
    input_zipcode.clear()
    input_zipcode.send_keys(zipcode)
    input_zipcode.send_keys(Keys.ENTER)
    
    sleep(1)
    #input userEmail and password
    driver.get('https://primenow.amazon.com/account/address')
#     login_page = driver.find_element_by_css_selector('div.show-for-large page_header_drop_menu_trigger__triggerText__3dDUD')
#     login_page.click()
    sleep(1)
    input_userEmail = driver.find_element_by_id('ap_email')
    input_userEmail.clear()
    input_userEmail.send_keys(userEmail)
     
    input_userPassword = driver.find_element_by_id('ap_password')
    input_userPassword.clear()
    input_userPassword.send_keys(userPassword)
    input_userPassword.send_keys(Keys.ENTER)
    
#     sleep(7)
    #go to cart
    driver.get('https://primenow.amazon.com/checkout/enter-checkout?merchantId=A1DIH8I0L20LO5&ref=pn_sc_ptc_bwr')
#     sleep(7)
    
    while True:
        driver.refresh()
        sleep(7)
        
        try:
#             Delivery_options = driver.find_element_by_name('deliveryslotForm').text
            Delivery_options = driver.find_element_by_xpath('//*[@id="delivery-slot-form"]/div/span').text
#             Delivery_options = driver.find_element_by_css_selector('div.a-section a-spacing-none a-padding-small').text
            print(Delivery_options)
        except Exception:
            print('Exception Prime now ... There is time slot available now ...')
#             send_SMS_message('Prime now ... There is time slot available now ...')
        #NO 1-HOUR DELIVERY WINDOWS ARE AVAILABLE
        if(Delivery_options != 'No delivery windows available. New windows are released throughout the day.'):
            print('There is time available now ...')
            send_SMS_message('Prime now ... There is time available now ...')
            
    driver.close()
    
monitor()

#TODO:
#auto purchase
'''
click continue:

<button type="submit" data-radium="true" style="touch-action: manipulation; cursor: pointer; border: 1px solid transparent; border-radius: 4px; font-weight: 600; white-space: nowrap; user-select: none; -webkit-font-smoothing: antialiased; background-image: none; display: inline-flex; align-items: center; padding-left: 16px; padding-right: 16px; font-size: 16px; height: 40px; background-color: rgb(48, 113, 169); color: rgb(238, 238, 238);">Continue</button>


place order:
<button type="button" data-radium="true" style="touch-action: manipulation; cursor: pointer; border: 1px solid transparent; border-radius: 4px; font-weight: 600; white-space: nowrap; user-select: none; -webkit-font-smoothing: antialiased; background-image: none; display: block; align-items: center; padding-left: 24px; padding-right: 24px; font-size: 18px; height: 48px; background-color: rgb(48, 113, 169); color: rgb(238, 238, 238); width: 100%;">Place order</button>
'''