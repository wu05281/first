from selenium import webdriver
import time
#登陆163 邮箱

# print('请输入你要发送的邮箱地址：')
# mail_to = input()
# #检查邮件格式
# print('mail to:%s' % mail_to)
browser = webdriver.Firefox()
browser.get('http://mail.163.com/')

#linkElem = browser.find_element_by_link_text('关于百度')
#linkElem.click()
browser.switch_to.frame('x-URS-iframe')
u = browser.find_element_by_name('email')
u.send_keys('18018605281')
p = browser.find_element_by_name('password')
p.send_keys('******')
browser.find_element_by_id('dologin').click()
# 切换至默认frame
browser.switch_to.default_content()
time.sleep(10)
send_mail = browser.find_element_by_class_name("mD0")
send_mail.click()
# browser.close()
# browser.quit()
