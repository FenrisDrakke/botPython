from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def applyStarRating(self, *starValues):
        starFiltrationBox = self.driver.find_element(By.ID, 'filter_class')
        starChildElements = starFiltrationBox.find_elements(By.CSS_SELECTOR, '*')

        for starValue in starValues:
            for starElement in starChildElements:
                if str(starElement.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    starElement.click()


    def sortPriceLowestFirst(self):
        element = self.driver.find_element(By.CSS_SELECTOR,'li[data-id="price"]')
        element.click()