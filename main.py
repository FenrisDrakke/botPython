from time import sleep

from booking.booking import Booking

with Booking() as bot:
    bot.land_fist_page()
    bot.changeCurrency(currency='EUR')
    bot.selectPlaceToGo('Paris')
    bot.selectDates(checkInDate='2023-04-24', checkOutDate='2023-04-30')
    bot.selectAdults(1)
    bot.clickSearch()
    bot.applyFiltrations()
    #sleep(1000)