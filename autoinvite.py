import requests
import time
from helium import *
def invite(link,username,password,x):
    r = requests.get('https://api.chess.com/pub/club/chess-university/members')
    members = r.json()['weekly'][x:x+30]        
    invitelist = []
    for i in members:
        invitelist.append(i['username'])
    print(invitelist)
    driver = start_chrome('https://www.chess.com/login')
    time.sleep(3)
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login').click()
    time.sleep(3)
    driver.get(link)
    time.sleep(3)
    for i in invitelist:
        driver.find_element_by_class_name('form-input-input').send_keys(i+' ')
        time.sleep(1)
    time.sleep(1)
    driver.find_element_by_id('members_invite_invite').click()