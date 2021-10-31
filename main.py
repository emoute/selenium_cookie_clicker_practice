import time
from os import environ
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chromedriver_path = environ.get('CHROMEDRIVER_PATH')

service = Service(chromedriver_path)
browser = webdriver.Chrome(service=service)

cookie_clicker_url = 'https://orteil.dashnet.org/cookieclicker/'
browser.get(cookie_clicker_url)
time.sleep(1)
cookie = browser.find_element(By.ID, "bigCookie")
items = browser.find_elements(By.CSS_SELECTOR, "#store .product")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 2
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade prices
        all_prices = browser.find_elements(By.CSS_SELECTOR, "#store .price")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = browser.find_element(By.ID, "cookies").text.split()[0]
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        item_to_purchase = browser.find_element(By.ID, to_purchase_id)
        item_to_purchase.click()

        if highest_price_affordable_upgrade <= cookie_count:
            item_to_purchase.click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = browser.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
