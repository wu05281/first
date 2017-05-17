from selenium import webdriver
import time
#登陆163 邮箱
browser = webdriver.Firefox()
browser.get('http://mail.163.com/')

#linkElem = browser.find_element_by_link_text('关于百度')
#linkElem.click()
browser.switch_to.frame('x-URS-iframe')
u = browser.find_element_by_name('email')
u.send_keys('18018605281')
p = browser.find_element_by_name('password')
p.send_keys('***********')
browser.find_element_by_id('dologin').click()
time.sleep(5)

browser.close()
browser.quit()
