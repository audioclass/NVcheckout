import time

from selenium import webdriver
import requests

delayInSeconds = 0.5
productIdentifier = "5438481700"
apiUrl = (
    "https://api.digitalriver.com/v1/shoppers/me/products/{pID}/inventory-status?apiKey=9485fa7b159e42edb08a83bde0d83dia".format(
        pID=str(productIdentifier)))
cartUrl = (
    "https://store.nvidia.com/store/nvidia/en_US/buy/productID.{pID}/clearCart.yes/nextPage.QuickBuyCartPage".format(
        pID=str(productIdentifier)))
pollFrequency = 0


# async def buy():
# await chrome.get(cartUrl)
def openbrowser():
    chrome = webdriver.Chrome()
    return chrome


def closebrowser(browser):
    browser.quit()


def fetch(url):
    response = requests.get(url)
    return response


chrome = openbrowser()

while True:
    stock = fetch(apiUrl)

    if "OUT_OF_STOCK" in stock.text:
        print(str(stock) + ": No stock available, waiting {time} seconds...".format(time=delayInSeconds))
    else:
        print(str(stock) + ": Product might be in stock, opening webpage!")
        chrome.get(cartUrl)
        break

    time.sleep(delayInSeconds)
