from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()

homeLink = 'https://www.realcanadiansuperstore.ca/Food/Fruits-%26-Vegetables/c/RCSS001001000000'

browser.get(homeLink)


# Click Region Button
BCButton = WebDriverWait(browser, 60).until(EC.element_to_be_clickable((By.XPATH, "//li/button[@data-store-id='1520']")))
BCButton.click()
print("BC button clicked")
time.sleep(5)
print('5 secs up')

def findSection(link):

    browser.get(link)

    print('sleeping 5 sec')
    time.sleep(5)
    print('awake')

    sectionElems = browser.find_elements_by_css_selector("li[data-level='1'] > a.sub-nav-link")


    sectionURLList = []

    print('printing  links')
    for link in sectionElems:
        attrib = link.get_attribute('href')
        print(attrib)
        sectionURLList.append(attrib)



    return(sectionURLList)



def findsubcategory(link):

    browser.get(link)

    print('sleeping 5 sec')
    time.sleep(5)
    print('awake')

    subCatElems = browser.find_elements_by_css_selector("div.subcategory-link > a")


    subCatURLList = []

    print('printing  links')
    for link in subCatElems:
        attrib = link.get_attribute('href')
        print(attrib)
        subCatURLList.append(attrib)



    return(subCatURLList)

def findItems(link):

    print('visitng page')
    print(link)
    browser.get(link)
    print('sleeping for items')
    time.sleep(5)
    print('item wake up')

    try:

        loadMore = browser.find_element_by_css_selector(".btn-show-more")
        print(loadMore)
        loadMore.click()
        time.sleep(2)

    except:
        pass




    itemElems = browser.find_elements_by_css_selector("a.product-name")
    print('found item elements')

    itemURLList = []

    print('printing item links')
    for link in itemElems:
        attrib = link.get_attribute('href')
        print(attrib)
        itemURLList.append(attrib)

    return(itemURLList)

fullList = set()


sectionLinks = findSection(homeLink)

for i in range(0,9):


    print('finding main subcats')

    subCatURLSetMain = findsubcategory(sectionLinks[i])

    print('found main subcats')
    fullnonSet = []
    for link in subCatURLSetMain:

        print('visitng mainsub link')
        print(link)

        print('going into subsubcat page')
        subCatURLSetSub = findsubcategory(link)
        print('found subsublinks')

        if len(subCatURLSetSub) < 1:
            fullList.update(findItems(link))

        for subLink in subCatURLSetSub:

            print('goin into subsublink')
            print(subLink)

            itemLinks = findItems(subLink)

            fullnonSet.append(itemLinks)

            fullList.update(itemLinks)


fullSetList = set(fullList)

print('length of List')
print(len(fullList))
print('length of set')
print(len(fullSetList))


fileObj = open('FullLinks.txt', 'w')

for line in fullSetList:

    fileObj.write(line)
    fileObj.write('\n')

fileObj.close()
