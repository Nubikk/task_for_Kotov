import pyautogui
import PyQt6
import selenium
from selenium import webdriver
from PyQt6 import QtWidgets, uic
import time

link = None
mess = None



def attack(link, mess, lgn, pas):
    browser = webdriver.Chrome()
    browser.get(link)
    lgn_input = browser.find_element_by_xpath('//*[@id="email"]')
    lgn_input.send_keys(lgn)
    pas_input = browser.find_element_by_xpath('//*[@id="pass"]')
    pas_input.send_keys(pas)
    lgn_btn = browser.find_element_by_xpath('//*[@id="login_button"]')
    lgn_btn.click()
    for i in range(5):
        input = browser.find_element_by_xpath('//*[@id="im_editable242631542"]')
        input.send_keys(mess)
        btn = browser.find_element_by_xpath('//*[@id="content"]/div/div/div[3]/div[2]/div[4]/div[2]/div[4]/div[1]/button')
        btn.click()
        time.sleep(7)




def start():
    global link
    global mess

    link = win.Link.text()
    mess = win.Message.text()

    #bots = dict()
    #bot = True
    #with open('bot_inf') as f:
    #    if not f.read(1):
    #        bot = False
    #    else:
    #        for line in f:
    #            tmp = line.split()
    #            bots[tmp[0]] = tmp[1]

    attack(link, mess, "lgn", "pass")


app = QtWidgets.QApplication([])

win = uic.loadUi("spamer.ui")
win.Start_btn.clicked.connect(start)

win.show()
app.exec()