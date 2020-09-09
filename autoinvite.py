import requests
from selenium import webdriver
import time
import json

with open('C:\\path_to_json_file\\example.json') as f:
    data = json.load(f)
driver = webdriver.Chrome(executable_path=data['path'])
driver.get('https://www.chess.com/login')
time.sleep(3)
driver.find_element_by_id('username').send_keys(data['username'])
driver.find_element_by_id('password').send_keys(data['password'])
driver.find_element_by_id('login').click()
r = requests.get(data['apilink'])
members = r.json()[data['timeframe']]
for i in data['invitelist']:
    driver.get(i['invitelink'])
    time.sleep(3)
    try:
        x = int(driver.find_element_by_class_name('clubs-manage-members-text').text[:2])
        invites = members[data['number']:data['number']+x]
        invitelist = [j['username'] for j in invites]
        for n in invitelist:
            driver.find_element_by_class_name('form-input-input').send_keys(n+' ')
            time.sleep(1)
        print(invitelist)
        print(i['clubname'],x)
        driver.find_element_by_id('members_invite_invite').click()
        time.sleep(2)
    except:
        continue
data['number'] += 30
a_file = open('C:\\path_to_json_file\\example.json', 'w')
json.dump(data, a_file)
a_file.close()
