from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import Timer
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

checking_products_sleep = 5  # Every this many seconds it will check for new products to buy
checking_upgrades_sleep = 15  # Every this many seconds it will check for new upgrades to buy


def check_products():
    Timer(checking_products_sleep, check_products).start()
    products_available = driver.find_elements(By.CSS_SELECTOR, "#products .enabled")
    if len(products_available) > 0:
        highest = len(products_available) - 1
        products_available[highest].click()


def check_upgrades():
    Timer(checking_upgrades_sleep, check_upgrades).start()
    upgrades_available = driver.find_elements(By.CSS_SELECTOR, "#upgrades .enabled")
    if len(upgrades_available) > 0:
        highest = len(upgrades_available) - 1
        upgrades_available[highest].click()


def main():
    driver.get("https://orteil.dashnet.org/cookieclicker/")

    time.sleep(3)
    lang = driver.find_element(By.XPATH, '//*[@id="langSelect-PL"]')
    lang.click()
    time.sleep(3)

    got_it = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]')
    got_it.click()
    end = time.time() + 60*5
    check_products()
    check_upgrades()
    cookie = driver.find_element(By.ID, "bigCookie")

    while time.time() < end:
        cookie.click()

    final = driver.find_element(By.ID, "cookiesPerSecond").text.split()[2]

    with open("scores.txt", mode="a") as scores:
        scores.write(f"SCORE: {final} \nchecking products: {checking_products_sleep}s \nchecking upgrades: "
                     f"{checking_upgrades_sleep}s\n\n")

    driver.close()


if __name__ == "__main__":
    main()
