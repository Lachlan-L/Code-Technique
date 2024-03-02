import Harris_farm_markets
import requests
from bs4 import BeautifulSoup

def colesScrape(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "lmxl.parser")

    returnArray = []
    pageNum = 1
    while (len(soup.findAll(attrs={'class': 'sc-6fb8ea3a-3 kzXkbX coles-targeting-ProductTileProductTileWrapper'})) != 0):
        objs = soup.findAll(attrs={'class': 'sc-6fb8ea3a-3 kzXkbX coles-targeting-ProductTileProductTileWrapper'})
        for obj in objs:
            soup = BeautifulSoup(str(obj), "lmxl.parser")
            NAMETAG = soup.find(class_="product__title")
            COSTTAG = soup.find(class_="price__value")
            SAVEDTAG = soup.find(class_="badge-label")
            LINKTAG = soup.find(class_="sc-51f151be-0 irGhqP")

            imageLink = LINKTAG.find('img')['src']
            name = NAMETAG.text.split('|')[0]
            name = name.replace("Coles ", "")

            if SAVEDTAG:
                saved = SAVEDTAG.text

            newObj = {}
            newObj['name'] = name
            newObj['cost'] = float(COSTTAG.text[1:])
            newObj['image'] = imageLink
            # newObj['saved'] = float(saved.split(" ")[1][1:])

            returnArray.append(newObj)

        pageNum = pageNum + 1
        URL = URL[:-1] + str(pageNum)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "lmxl.parser")
    return returnArray

def aldiScrape(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "lmxl.parser")
    objs = soup.find_all(class_="box--wrapper ym-gl ym-g25")

    returnArray = []
    for obj in objs:
        soup = BeautifulSoup(str(obj), "lmxl.parser")
        NAMETAG = soup.find(class_="box--description--header")
        COSTTAG = soup.find(class_="box--value")
        CENTTAG = soup.find(class_="box--decimal")

        imageLink = obj.find('img')['src']
        newObj = {}
        newObj['name'] = NAMETAG.text.strip()
        newObj['cost'] = float(COSTTAG.text[1:] + CENTTAG.text)
        newObj['image'] = imageLink

        returnArray.append(newObj)
    return returnArray

TEST = "https://www.coles.com.au/on-special/meat-seafood?page=1"
print(colesScrape(TEST))


def meatScrape():
    returnObj = colesScrape("https://www.coles.com.au/on-special/meat-seafood/bbq-sausages-burgers?page=1")
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/beef-veal?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/game?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/hams-bacon?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/lamb?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/mince?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/organic-meat?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/pork?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/poultry?page=1"):
        returnObj.append(obj)
    for obj in colesScrape("https://www.coles.com.au/on-special/meat-seafood/meat-free-range?page=1"):
        returnObj.append(obj)
    return returnObj

def vegetableScrape():
    return colesScrape("https://www.coles.com.au/on-special/fruit-vegetables/vegetables?page=1")

def fruitScrape():
    return colesScrape("https://www.coles.com.au/on-special/fruit-vegetables/fruit?page=1")

def seafoodScrape():
    return colesScrape("https://www.coles.com.au/on-special/meat-seafood/seafood?page=1")

# FRUIT "https://www.coles.com.au/on-special/fruit-vegetables/fruit?page=1"
# VEGETABLE "https://www.coles.com.au/on-special/fruit-vegetables/vegetables"
# SEAFOOD "https://www.coles.com.au/on-special/meat-seafood/seafood"

# MEAT
# https://www.coles.com.au/on-special/meat-seafood/bbq-sausages-burgers
# https://www.coles.com.au/on-special/meat-seafood/beef-veal
# https://www.coles.com.au/on-special/meat-seafood/game
# https://www.coles.com.au/on-special/meat-seafood/hams-bacon
# https://www.coles.com.au/on-special/meat-seafood/lamb
# https://www.coles.com.au/on-special/meat-seafood/mince
# https://www.coles.com.au/on-special/meat-seafood/organic-meat
# https://www.coles.com.au/on-special/meat-seafood/pork
# https://www.coles.com.au/on-special/meat-seafood/poultry


# VEGAN MEAT https://www.coles.com.au/on-special/meat-seafood/meat-free-range

# TEST = "https://www.iga.com.au/low-prices-every-day/"
# wooliesScrape(TEST)

TEST = "https://www.aldi.com.au/groceries/super-savers/"
print(aldiScrape(TEST))