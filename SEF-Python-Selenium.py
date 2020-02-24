from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime
import ctypes  # An included library with Python install.   


browser = webdriver.Firefox()
browser.get('https://www.sef.pt')

link = browser.find_element_by_class_name('login-launcher')
link.click()

userName = browser.find_element_by_id('txtUsername')
userName.send_keys('yourEmail@domain.com')

password = browser.find_element_by_id('txtPassword')
password.send_keys('yourSecurePassword')

loginBtn = browser.find_element_by_id('btnLogin')
loginBtn.click()

appointments = browser.find_element_by_id('agendamentosLink')
appointments.click()

newAppointmentBtn = browser.find_element_by_id('btnNovoAgendamento')
newAppointmentBtn.click()

phone = browser.find_element_by_id('txtTelephone')
phone.send_keys('123456789') # insert your phone here

serviceDropdown = Select(browser.find_element_by_id('Services_List'))
serviceDropdown.select_by_value('7') # renew of residence type

# here you can add more office depending on your needs
leiriaOffice = {'name': 'Leiria', 'code': '260'}
coimbraOffice = {'name': 'Coimbra', 'code': '20L'}

sefOfficesINearby= [leiriaOffice,coimbraOffice]
found = False

for office in sefOfficesINearby: 
    placesDropdown = Select(browser.find_element_by_id('Places_List'))
    placesDropdown.select_by_value(office['code'])

    try:
        resultOkLeiria = browser.find_element_by_xpath('//*[@id="ctl00_ctl53_g_948e31d8_a34a_4c4d_aa9f_c457786c05b7_ctl00_lblVagasLivres"]')
        print(resultOkLeiria.text)
        assert 'VAGAS LIVRES' in resultOkLeiria.text
        print('Yeah!!! Found in ' + office['name'] +'!')
        found = True
        break
    except:
        print('No appointments in ' + office['name'])

print('Checked at: ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

if found:
    print('There is an appointment! We made it!')
    ctypes.windll.user32.MessageBoxW(0, "Open Firefox window to proceed!", "There is an appointment", 1)
else:
    print('No luck this time')
    browser.close()
