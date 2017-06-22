from bs4 import BeautifulSoup
import requests
import re





nutriRegex = re.compile(r'((\w*\s\w*)|(\w*))\s(\d*\.\d*)\s(g|mg)')


res = requests.get(r'https://www.realcanadiansuperstore.ca/Food/Fruits-%26-Vegetables/Fruit/Apples-%26-Pears/Anjou-Pears/p/20174514001_KG?isPDPFlow=Y')

soup = BeautifulSoup(res.text, "lxml")
#print(soup)

elems = soup.select("span.nutrition-label")

parsedList = soup.find_all("div", class_="main-nutrition-attr first")

nutriDict = {}
nutriList =[]

for nutriTag in soup.find_all("div", class_="main-nutrition-attr first"):

    rawData = (" ".join(nutriTag.text.split())[:-3])

    regResult = nutriRegex.search(rawData)

    label = regResult.group(1)

    #Converts to mg
    if 'mg' not in regResult.group(5):
        label = (regResult.group(1))
        nutriValue = (float(regResult.group(4)) * 1000.0)

    else:
        nutriValue = float(regResult.group(4))

    nutriDict[label] = nutriValue




print(nutriDict)









