from dotenv import load_dotenv
import os 
import time

load_dotenv(".env")

def generateEndTime():
    MAX_HOURS = os.environ.get('maxHours')
    MAX_MINUTES = os.environ.get('maxMinutes')

    # end_time = time.time() + 60 * MAX_MINUTES * MAX_HOURS
    end_time = time.time() + 60 * 3
    print("Running it for: ", MAX_HOURS, " hours.")
    return end_time

def generateFilterLink():
    MAX_PRICE = os.environ.get('maxPrice')
    MIN_BED = os.environ.get('minBed')
    MAX_BED = os.environ.get('maxBed')
    MIN_BATH = os.environ.get('minBath')
    CITY_NAME = os.environ.get('cityName')

    link = f"https://www.daft.ie/property-for-rent/ireland?rentalPrice_to={MAX_PRICE}&numBeds_from={MIN_BED}&numBeds_to={MAX_BED}&numBaths_from={MIN_BATH}&sort=publishDateDesc&location={CITY_NAME}&location={CITY_NAME}-city"
    print("Generated Link is: ", link)
    return link
        