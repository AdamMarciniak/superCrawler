from bs4 import BeautifulSoup
import requests
import re


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

        if i == 5:
            break
        print(i)

        for foodItem in soup2.find_all("a", class_="product-name"):

            nutriList.append((foodItem.get('href')))
            #print(len(nutriList))

            # foodLink = foodItem.get('href')
            # print(foodLink)

notepad = open("URLLinks.txt", 'w')

#for line in nutriList:
   # notepad.write("%s\n" % line)

print(len(list(nutriList)))




nutriRegex = re.compile(r'((\w*\s\w*)|(\w*))\s(\d*\.\d*)\s(g|mg)')
namesList = []
fullList = []
totalList = []
valList =[]
nt = 0
for line in nutriList:

    nt +=1

    if nt == 5:
        break

    res = requests.get('https://www.realcanadiansuperstore.ca' + line)
    #print(line)

    soup = BeautifulSoup(res.text, "lxml")




    names=soup.find("span", class_="product-sub-title")


    fullList.append(names.next_sibling.strip())


    for nutriTag in soup.find_all("div", class_="main-nutrition-attr first"):
        #print(nutriTag)
        rawData = (" ".join(nutriTag.text.split())[:-3])

        regResult = nutriRegex.search(rawData)

        label = regResult.group(1)


        #Converts to mg
        if 'mg' not in regResult.group(5):
            label = (regResult.group(1))
            nutriValue = (float(regResult.group(4)) * 1000.0)

        else:
            nutriValue = float(regResult.group(4))

        valList.append(label)
        valList.append(nutriValue)

        fullList.append(valList)

    totalList.append(fullList)

for piece in totalList:
    print(piece)
    print("\n")








print(nutriDict)























