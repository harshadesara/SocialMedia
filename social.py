from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from parsel import Selector
from time import sleep
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import urllib.request
from functools import partial
import pandas as pd

import csv
import re
from datetime import datetime

app = QtWidgets.QApplication([])
dlg = uic.loadUi("home.ui")
dlg2 = uic.loadUi("instagram.ui")
dlg3 = uic.loadUi("whatsapp.ui")
dlg2.data_tw.setColumnWidth(0, 150)
dlg2.data_tw.setColumnWidth(1, 320)
dlg2.data_tw.setColumnWidth(2, 100)


def search():
    try:
        dlg2.alert_lbl.clear()
        QApplication.processEvents()
        clearData()
        global skey
        skey = dlg2.search_le.text()
        count = 0
        if skey:
            print(skey)
        else:
            skey = "msu baroda"
        QApplication.processEvents()
        dlg2.search_le.clear()
        global chromedriver
        chromedriver = r'C:\Users\DELL\.PyCharm2019.2\config\scratches\SocialMedia\chromedriver'
        global driver
        QApplication.processEvents()
        driver = webdriver.Chrome(executable_path=chromedriver)
        QApplication.processEvents()
        driver.get("https://www.instagram.com/accounts/login/")
        QApplication.processEvents()
        id = "hagemaru_927"
        password = "hagemarusumit"
        QApplication.processEvents()
        sleep(3)
        id_field = driver.find_element_by_name('username')
        id_field.send_keys(id)
        password_field = driver.find_element_by_name('password')
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        QApplication.processEvents()
        sleep(5)
        driver.find_element_by_xpath('//*[@class="aOOlW   HoLwm "]').click()
        QApplication.processEvents()
        sleep(3)
        searchquery = driver.find_element_by_xpath('//*[@placeholder="Search"]')
        QApplication.processEvents()
        sleep(3)
        searchquery.send_keys(skey)
        QApplication.processEvents()
        sleep(3)
        # searchquery.send_keys(Keys.RETURN)
        # sleep(3)
        QApplication.processEvents()
        a = driver.find_elements_by_xpath(
            "//a[@class='yCE8d  ']/div[@class='z556c']/div[@role='button']/span[@class='_2dbep ']/img")
        QApplication.processEvents()
        name_lst = []
        row_number = 0
        edit = QPixmap('Images/go64.png')
        edit64 = QIcon(edit)
        global name_full_lst
        name_full_lst = []
        for i in a:
            QApplication.processEvents()
            name = i.get_attribute('alt').split('\'')[0]
            link = i.get_attribute('src')
            name_lst.append(name)
            name_full_lst.append(name)
            dlg2.data_tw.insertRow(row_number)
            QApplication.processEvents()

            for data in name_lst:
                QApplication.processEvents()
                lbl1 = QtWidgets.QLabel()
                image_url = link
                data1 = urllib.request.urlopen(image_url).read()
                image = QImage()
                image.loadFromData(data1)
                piximg = QPixmap(image)
                piximg_resized = piximg.scaled(150, 150, Qt.KeepAspectRatio)
                lbl1.setPixmap(piximg_resized)
                # lbl1.setFixedHeight(200)
                lbl1.setScaledContents(True)
                dlg2.data_tw.setCellWidget(row_number, 0, lbl1)

                cell = QtWidgets.QTableWidgetItem(str(data))
                dlg2.data_tw.setItem(row_number, 1, cell)

                btn1 = QtWidgets.QPushButton()
                btn1.setIcon(edit64)
                btn1.setIconSize(QSize(40, 40))
                # btn1.setMaximumHeight(80)
                # btn1.setMaximumWidth(80)
                dlg2.data_tw.setCellWidget(row_number, 2, btn1)
                btn1.clicked.connect(partial(instagram_to_user, action=row_number))
                QApplication.processEvents()
            row_number += 1
            name_lst = []
        dlg2.alert_lbl.setText("All results have been fetched")
    except Exception as e:
        print(e)


def send():
    try:
        global phone
        phone = dlg3.mobile_le.text()
        if phone:
            print(phone)
        else:
            phone = "9409213335"
        global msg
        msg = dlg3.msg_te.toPlainText()
        if msg:
            print(msg)
        else:
            msg = "hello"
        QApplication.processEvents()
        dlg3.mobile_le.clear()
        dlg3.msg_te.clear()
        global chromedriver2
        chromedriver2 = r'C:\Users\DELL\.PyCharm2019.2\config\scratches\SocialMedia\chromedriver'
        global driver2
        QApplication.processEvents()
        driver2 = webdriver.Chrome(executable_path=chromedriver2)
        driver2.get("https://web.whatsapp.com/")
        sleep(20)
        QApplication.processEvents()
        driver2.get("https://api.whatsapp.com/send?phone=91" + str(phone) + "&text=" + str(msg))
        sleep(7)
        QApplication.processEvents()
        driver2.find_element_by_xpath('//*[@class="_36or _2y_c _2z0c _2z07"]').click()
        sleep(7)
        QApplication.processEvents()
        driver2.find_element_by_xpath('//*[@class="_36or"]').click()
        # driver2.find_element_by_xpath('//*[@class="_3M-N-"]').click()

    except Exception as e:
        print(e)


def send2():
    try:
        dlg3.msg_sent_lbl.clear()
        global nme
        nme = dlg3.mobile_le.text()
        if nme:
            print(nme)
        else:
            nme = "Mom"
        global msg
        msg = dlg3.msg_te.toPlainText()
        if msg:
            print(msg)
        else:
            msg = "hello"
        QApplication.processEvents()
        dlg3.mobile_le.clear()
        dlg3.msg_te.clear()
        QApplication.processEvents()
        global chromedriver2
        chromedriver2 = r'C:\Users\DELL\.PyCharm2019.2\config\scratches\SocialMedia\chromedriver'
        global driver2
        QApplication.processEvents()
        driver2 = webdriver.Chrome(executable_path=chromedriver2)
        driver2.get("https://web.whatsapp.com/")
        sleep(20)
        QApplication.processEvents()
        driver2.find_element_by_xpath("//*[@title='New chat']").click()
        sleep(3)
        QApplication.processEvents()
        search = driver2.find_element_by_xpath("//*[@class='_3u328 copyable-text selectable-text']")
        search.send_keys(nme)
        sleep(3)
        QApplication.processEvents()
        #sel = Selector(text=driver2.page_source)
        #h = sel.xpath("//*[@class='_3NWy8']/span/text()").extract()
        #print(h)
        driver2.find_element_by_xpath("//*[@title='" + str(nme) + "']").click()
        sleep(3)
        QApplication.processEvents()
        write_msg = driver2.find_element_by_xpath("//*[@spellcheck='true']")
        write_msg.send_keys(msg)
        sleep(3)
        QApplication.processEvents()
        driver2.find_element_by_xpath('//*[@class="_3M-N-"]').click()
        dlg3.msg_sent_lbl.setText("Message Sent")

        # driver2.get("https://api.whatsapp.com/send?phone=91" + str(phone) + "&text=" + str(msg))
        # sleep(7)
        # driver2.find_element_by_xpath('//*[@class="_36or _2y_c _2z0c _2z07"]').click()
        # sleep(7)
        # driver2.find_element_by_xpath('//*[@class="_36or"]').click()

        # driver2.find_element_by_xpath('//*[@class="_3M-N-"]').click()
    except Exception as e:
        print(e)


def send2multiple():
    try:
        dlg3.msg_sent_lbl.clear()
        df = pd.read_csv(
            "C:\\Users\DELL\.PyCharm2019.2\config\scratches\WebScraping\plumbers in vadodara_20191219191352.csv")  # Change the filename from here
        global limit
        limit = dlg3.limit_le.text()
        if limit:
            print(limit)
        else:
            limit = 20
        global msg
        msg = dlg3.msg2_te.toPlainText()
        if msg:
            print(msg)
        else:
            msg = "hello"
        QApplication.processEvents()
        dlg3.limit_le.clear()
        dlg3.msg2_te.clear()
        QApplication.processEvents()
        global chromedriver2
        chromedriver2 = r'C:\Users\DELL\.PyCharm2019.2\config\scratches\SocialMedia\chromedriver'
        global driver2
        QApplication.processEvents()
        driver2 = webdriver.Chrome(executable_path=chromedriver2)
        driver2.get("https://web.whatsapp.com/")
        sleep(20)
        QApplication.processEvents()
        c = 0
        if int(limit) <= len(df):
            new_limit = int(limit)
        else:
            new_limit = len(df)
        while c < new_limit:
            try:
                QApplication.processEvents()
                n = df['Name'][c]
                driver2.find_element_by_xpath("//*[@title='New chat']").click()
                sleep(3)
                QApplication.processEvents()
                search = driver2.find_element_by_xpath("//*[@class='_3u328 copyable-text selectable-text']")
                search.send_keys(n)
                sleep(3)
                QApplication.processEvents()
                driver2.find_element_by_xpath("//*[@title='" + str(n) + "']").click()
                sleep(3)
                QApplication.processEvents()
                write_msg = driver2.find_element_by_xpath("//*[@spellcheck='true']")
                write_msg.send_keys(msg)
                sleep(3)
                QApplication.processEvents()
                driver2.find_element_by_xpath('//*[@class="_3M-N-"]').click()
                c += 1
            except Exception as e:
                print(e)
                QApplication.processEvents()
                driver2.find_element_by_xpath('//*[@class="qfKkX"]').click()
                c += 1
                continue
        dlg3.msg_sent_lbl.setText("Message Sent!")

    except Exception as e:
        print(e)


def instagram_to_user(action):
    try:
        dlg2.alert_lbl.clear()
        QApplication.processEvents()
        driver.get("https://www.instagram.com/" + str(name_full_lst[action]))
        sleep(3)
        sel = Selector(text=driver.page_source)
        h = sel.xpath("//*[@class='rkEop']/text()").extract()
        # h=driver.find_element_by_xpath("//*[@class='rkEop']/text()").extract()
        if not h:
            driver.find_element_by_xpath("//a[@class='-nal3 ']/span[@class='g47SY ']").click()
            QApplication.processEvents()
            a = driver.find_element_by_xpath("//a[@class='-nal3 ']/span")
            b = a.get_attribute('title')
            c = b.split(',')
            followers = int("".join(c))
            sleep(5)
            cnt = 0
            while cnt < followers:
                QApplication.processEvents()
                driver.find_element_by_xpath("//*[@class='sqdOP  L3NKy   y3zKF     ']").click()
                cnt += 1
                sleep(5)
        else:
            dlg2.alert_lbl.setText("Account you clicked is Private.")
    except Exception as e:
        print(e)


def insta_btn():
    dlg2.show()
    dlg.close()


def back():
    dlg2.search_le.clear()
    dlg2.alert_lbl.clear()
    dlg.show()
    clearData()
    dlg2.close()


def whatsapp_btn():
    dlg3.show()
    dlg.close()


def back2():
    dlg3.msg_sent_lbl.clear()
    dlg3.mobile_le.clear()
    dlg3.msg_te.clear()
    dlg3.limit_le.clear()
    dlg3.msg2_te.clear()
    dlg.show()
    dlg3.close()


def clearData():
    dlg2.data_tw.clearSelection()
    while dlg2.data_tw.rowCount() > 0:
        dlg2.data_tw.removeRow(0)
        dlg2.data_tw.clearSelection()


dlg.instagram_pb.pressed.connect(insta_btn)
dlg.whatsapp_pb.pressed.connect(whatsapp_btn)
dlg2.search_pb.pressed.connect(search)
dlg3.send_pb.pressed.connect(send2)
dlg3.send2_pb.pressed.connect(send2multiple)
dlg2.back_pb.pressed.connect(back)
dlg3.back_pb.pressed.connect(back2)
dlg.show()
app.exec()
# WebElement = driver.find_element_by_css_selector("span[class='Ap253']")
# print(WebElement)
# sel=Selector(text=driver.page_source)
# a=sel.xpath('//*[@class="Ap253"]/text()').extract()
# print(a)
# image_elements = driver.find_elements_by_xpath("//img")
# for image in image_elements:
#     img_src = image.get_attribute("src")
#     print(img_src)
#     alt = image.get_attribute("alt")
#     print(alt)
# sel = Selector(text=driver.page_source)
# a=sel.xpath('//*[@class="izU2O"]/text()').extract()
# print(a)
# a=driver.find_element_by_tag_name('a')
# for i in a:
#     print(i.get_attribute('href'))
# div = driver.find_element_by_class_name('izU2O')
# a=div.find_element_by_css_selector('a').get_attribute('href')
# print(a)
