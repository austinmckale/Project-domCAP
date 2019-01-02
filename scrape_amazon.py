import random
import os
import datetime
import time
import requests
import names
from bs4 import BeautifulSoup
import sys
r = requests.Session()


get_pages = r.get("https://www.amazon.com/Best-Sellers/zgbs/amazon-devices/ref=zg_bs_nav_0")
soup = BeautifulSoup(get_pages.text,"lxml")
for product in soup.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')
    

get_pages1 = r.get("https://www.amazon.com/Best-Sellers/zgbs/amazon-devices/ref=zg_bs_nav_0")
soup1 = BeautifulSoup(get_pages1.text,"lxml")
for product in soup1.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')


get_pages2 = r.get("https://www.amazon.com/Best-Sellers-Amazon-Launchpad/zgbs/boost/ref=zg_bs_nav_0")
soup2 = BeautifulSoup(get_pages2.text,"lxml")
for product in soup2.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')

    
get_pages3 = r.get("https://www.amazon.com/Best-Sellers-Amazon-Launchpad/zgbs/boost/ref=zg_bs_nav_0")
soup3 = BeautifulSoup(get_pages3.text,"lxml")
for product in soup3.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')

get_pages4 = r.get("https://www.amazon.com/Best-Sellers-Appliances/zgbs/appliances/ref=zg_bs_nav_0")
soup4 = BeautifulSoup(get_pages4.text,"lxml")
for product in soup4.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')

get_pages5 = r.get("https://www.amazon.com/Best-Sellers-MP3-Downloads/zgbs/dmusic/ref=zg_bs_nav_0")
soup5 = BeautifulSoup(get_pages5.text,"lxml")
for product in soup5.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')

get_pages6 = r.get("https://www.amazon.com/Best-Sellers-Computers-Accessories/zgbs/pc/ref=zg_bs_nav_0")
soup6 = BeautifulSoup(get_pages6.text,"lxml")
for product in soup6.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')

get_pages7 = r.get("https://www.amazon.com/best-sellers-video-games/zgbs/videogames/ref=zg_bs_nav_0")
soup7 = BeautifulSoup(get_pages7.text,"lxml")
for product in soup7.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')

get_pages8 = r.get("https://www.amazon.com/Best-Sellers-Toys-Games/zgbs/toys-and-games/ref=zg_bs_nav_0")
soup8 = BeautifulSoup(get_pages8.text,"lxml")
for product in soup8.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')

get_pages9 = r.get("https://www.amazon.com/Best-Sellers-Sports-Outdoors/zgbs/sporting-goods/ref=zg_bs_nav_0")
soup9 = BeautifulSoup(get_pages9.text,"lxml")
for product in soup9.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')

get_pages10 = r.get("https://www.amazon.com/best-sellers-software/zgbs/software/ref=zg_bs_nav_0")
soup10 = BeautifulSoup(get_pages10.text,"lxml")
for product in soup10.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')

get_pages11 = r.get("https://www.amazon.com/best-sellers-movies-TV-DVD-Blu-ray/zgbs/movies-tv/ref=zg_bs_nav_0")
soup11 = BeautifulSoup(get_pages11.text,"lxml")
for product in soup11.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')

get_pages12 = r.get("https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0")
soup12 = BeautifulSoup(get_pages12.text,"lxml")
for product in soup12.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')

get_pages13 = r.get("https://www.amazon.com/Best-Sellers-Cell-Phones-Accessories/zgbs/wireless/ref=zg_bs_nav_0")
soup13 = BeautifulSoup(get_pages13.text,"lxml")
for product in soup13.select("ol#zg-ordered-list > li"):
    product_name = product.select_one("img[alt]")["alt"]
    with open("products.txt", "a") as myfile:
        myfile.write(product_name + '\n')










































