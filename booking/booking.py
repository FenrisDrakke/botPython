from selenium import webdriver
import booking.constant as const
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

from booking.booking_filtration import BookingFiltration



class Booking(webdriver.Chrome):
    def __init__(self, drive_path=r"C:\selenium drivers", teardown=False):
        self.driver_path = drive_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(13)

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.teardown:
                self.quit()

    def land_fist_page(self):
        self.get(const.baseUrl)

    def changeCurrency(self, currency=None):
        currencyElement = self.find_element(By.CSS_SELECTOR, 'button[data-testid = "header-currency-picker-trigger"]')
        currencyElement.click()
        selectedCurrencyElement = self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def selectPlaceToGo(self,placeToGo):
        searchField = self.find_element(By.ID, ":Ra9:")
        searchField.clear()
        searchField.send_keys(placeToGo)
        #searchField.send_keys(Keys.ENTER)

        #firstResult = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        #firstResult.click()
    def selectDates(self, checkInDate, checkOutDate):
        checkInElement = self.find_element(By.CSS_SELECTOR, f'td[data-date=""{checkInDate}]')
        checkInElement.click()

        checkOutElement = self.find_element(By.CSS_SELECTOR, f'td[data-date=""{checkOutDate}]')
        checkOutElement.click()

    def selectAdults(self, count=1):
        selectionElement = self.find_element(By.ID, 'xp__guests__toggle')
        selectionElement.click()

        while True:
            decreaseAdultsElement = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
            decreaseAdultsElement.click()
            adultsValueElement = self.find_element(By.ID, 'group_adults')
            adultsValue = adultsValueElement.get_attribute('value')

            if int(adultsValue) == 1:
                break

        increaseButtonElement = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')

        for _ in range(count - 1):
            increaseButtonElement.click()

    def clickSearch(self):
        searchButton = self.find_element(By.CSS_SELECTOR,'button[type="submit"]')
        searchButton.click()

    def applyFiltrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.applyStarRating(4, 5)

        filtration.sortPriceLowestFirst()