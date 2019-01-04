import operator
import math
import time
from selenium.webdriver.common.by import By
import random
import subprocess
import os
from Naked.toolshed.shell import execute_js
import datetime
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait  
from selenium.webdriver.common.action_chains import ActionChains 
from pyfiglet import figlet_format
from threading import Thread
import _thread
from colorama import Fore, Back, Style
from colorama import init
import pandas



print("Welcome to Dominus Inc Random Activity for Gmails")
time.sleep(1)
print("This module uses Gmails you input to act human on. This is then used to recieve easier captchas")
time.sleep(1)
print("Any questions, feel free to DM me @dominus_labs on Twitter")
time.sleep(1)
print("Fuck EVE Captcha and all those other solutions.")
time.sleep(3)
print(Fore.GREEN + "Starting random activity!!")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("start-maximized")
options.add_argument('--log-level=3')
# add headless by doing options.add_argument('--headless')
#untested might not work :shrug:
options.add_argument('disable-infobars')
browser=webdriver.Chrome(chrome_options=options)
browser.get("https://accounts.google.com/ServiceLogin/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=AddSession")
def login():

    user = input("Enter gmail username")
    password = input("Enter gmail password")
    time.sleep(5)
    login = browser.find_element_by_name('identifier')
    login.send_keys(user)
    next0 = browser.find_element_by_xpath('//*[@id="identifierNext"]/content/span')
    next0.click()
    time.sleep(3)
    try:
        passw = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    except:
        passw = browser.find_element_by_id('password')
    time.sleep(2)
    
    passw.send_keys(password)
    time.sleep(2)
    final = browser.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
    final.click()

def search():
    random_searches = "cool"
    
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search.send_keys(random_searches)
    search.send_keys(Keys.RETURN)
    time.sleep(random.randint(1,500))
    browser.get('http://www.google.com')

def docs():
    lines = open("doc_tittles.txt").read().splitlines()
    random_tittle = random.choice(lines)

        #makes a new google docs
    time.sleep(2)
    browser.get("http://google.com")
    search = browser.find_element_by_name('q')
    text = "google docs"
    for character in text:
        search.send_keys(character)
        time.sleep(0.2)
    search.send_keys(Keys.RETURN)
    time.sleep(4.2)
    browser.get("https://docs.google.com/docs")
    time.sleep(.5)
    browser.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div[1]").click()
    time.sleep(2.31234)
    tittlee = browser.find_element_by_css_selector(".docs-title-input")
    tittlee.send_keys(random_tittle)
    time.sleep(1.321)
    docstext = browser.find_element_by_id("docs-editor-container").click()
    time.sleep(2.32523)
    docsbody = browser.find_element_by_id("docs-editor-container").click()                                 #import time here as well


def random_email():
    lines = open('random_text.txt').read().splitlines()
    randombodytext =random.choice(lines)
    browser.execute_script("window.open('');")
    time.sleep(3)
    browser.switch_to.window(browser.window_handles[5])
    browser.get("https://mail.google.com/mail/u/0/")

    time.sleep(.548394)
    browser.find_element_by_css_selector(".T-I.J-J5-Ji.T-I-KE.L3").click()
    time.sleep(.92892372)
    sendto =  str(random.randint(1, 9999999999999999999)) + "@dominusinc.club"

    recieve = browser.find_element_by_name("to")
    recieve.send_keys(sendto)
    time.sleep(6.289356798273)
    subject = browser.find_element_by_name("subjectbox")
    subject.send_keys("An interesting passage for you Dom!!!")

    time.sleep(4.1827348912)
    bodytext = browser.find_element_by_css_selector(".Am.Al.editable.LW-avf")
    bodytext.send_keys(randombodytext)

    time.sleep(4.12341278)
    browser.find_element_by_css_selector(".T-I.J-J5-Ji.aoO.T-I-atl.L3").click()


        #does random math
def math_sums():
    vari1 = (random.randint(-99999999,999999))
    vari2 = (random.randint(-99999999,999999))
    ops = {'+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv}
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(vari1,vari2)
    equation = '{} {} {} = \n'.format(vari1, op, vari2) 
    browser.get("https://www.google.com/")
    search = browser.find_element_by_name('q')
    search.send_keys(equation)
    search.send_keys(Keys.RETURN)

def youtube():
    lines = open("youtube_links.txt").read().splitlines()
    random_links = random.choice(lines)
    browser.get(random_links)
    time.sleep(4)        
    if random.randint(0,3) == 3:
        browser.find_element_by_css_selector("#subscribe-button paper-button").click()   
        time.sleep(tim)
    

def shopping():

    browser.get("https://www.google.com/shopping?hl=en")
    search = browser.find_element_by_name('q')
    lines = open('products.txt*').read().splitlines()
    random_item_search =random.choice(lines)
    text = random_item_search
    for character in text:
        search.send_keys(character)
        time.sleep(0.2)
    search.send_keys(Keys.RETURN)
    time.sleep(4.2)
    browser.find_element(By.XPATH, '(//h3)[1]/a').click()
    
    
def googlenews():
    browser.get("https://plus.google.com/discover")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    
    
def googlenews():
    browser.get("https://news.google.com/?hl=en-US&gl=US&ceid=US:en")
    for x in range (0,5):
        ran_num = str(random.randint(6,14))
        randon_type = browser.find_element_by_xpath("/html/body/div[8]/div[2]/header/div[4]/div[2]/div/c-wiz/div/div[" + ran_num + "]/a/div[2]/span").click()
        random_int = str(random.randint(0,80))
        browser.execute_script("window.scrollTo(0," + random_int)
        time.sleep(random_int)


if __name__ == '__main__':
    login()
    search()
    docs()
    random_email()
    math_sums()
    youtube()
    shopping()
    googlenews()
    googlenews()