#Finds all the URL links for every food item on the Superstore website.

from bs4 import BeautifulSoup
import requests
import re

nutriRegex = re.compile(r'((\w*\s\w*)|(\w*))\s(\d*\.\d*)\s(g|mg)')

from pprint import pprint

res = requests.get(r'https://www.realcanadiansuperstore.ca/food')

soup = BeautifulSoup(res.text, "lxml")
#print(soup)


nutriDict = {}
nutriList =[]
i = 0
mainLinkList = []


for nutriTag in soup.find_all("a", class_="sub-nav-link"):

    link = nutriTag.get('href')

    if link in mainLinkList:
        continue

    mainLinkList.append(link)


    if '/Food/' in link:

        res2 = requests.get('https://www.realcanadiansuperstore.ca'+ link)
        soup2 = BeautifulSoup(res2.text, "lxml")
        i+=1

        if i == 100:
            break
        print(i)


        for foodItem in soup2.find_all("a", class_="product-name"):

            nutriList.append((foodItem.get('href')))
            #print(len(nutriList))


            # foodLink = foodItem.get('href')
            # print(foodLink)

notepad = open("URLLinks.txt", 'w')

for line in nutriList:
    notepad.write("%s\n" % line)

print(len(list(nutriList)))













