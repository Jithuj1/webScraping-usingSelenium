
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UrlList import UrlLists


def collectData(url):
    finalCollection = []
    driver = webdriver.Chrome()

    for url in UrlLists:
        driver.get(url)

        # Find the element to hover over
        try:
            element = driver.find_element(By.XPATH, "//div[@id='pc-drawer-id-1']")
        except:
            continue

        # Use ActionChains to hover over the element
        hover = ActionChains(driver).move_to_element(element)
        hover.perform()

        # Wait for the data to appear
        wait = WebDriverWait(driver, 10)
        data = wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@id="pc-drawer-id-1"]')))
        # data = wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@class="icon-arrow-down"]')))

        # Extract the data

        text_data = data.text

        line = text_data.split("\n")
        singleCollection = []
        for i in line:
            if i.startswith('Standard'):
                singleCollection.append(i)
        finalCollection.append(singleCollection)
        print(singleCollection)
    driver.quit()
    return finalCollection
    
meaningfulData = collectData(UrlLists)

print(meaningfulData)
