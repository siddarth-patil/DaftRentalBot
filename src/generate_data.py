import os
import time

from dotenv import load_dotenv

from available_filters import *
from exceptions import *

load_dotenv(".env")


def generate_end_time():
    try:
        max_hours = os.environ.get("maxHours")
        if not (isinstance(max_hours, int) and max_hours > 0 and max_hours <= 9):
            print(
                "Conditions for Maximum hours not satisfied, therefore, running the bot for 2 hours"
            )
            max_hours = 2
    except NameError:
        # Running it for 2 hours by default
        print("Running the bot for 2 hours as there were no hours specified.")
        max_hours = 2

    end_time = time.time() + 60 * 60 * max_hours
    print("Running it for: ", max_hours, " hours.")
    return end_time


class GenerateLink:
    def __init__(self) -> None:
        # Base link on which filters will be added
        self.link = "https://www.daft.ie/property-for-rent/ireland"

    def generate_filter_link(self):
        self.city_filter_link()
        self.price_filter_link()
        self.bed_filter_link()
        self.bath_filter_link()
        self.facilities_filter_link()

        print("Final link is: ", self.link)
        return self.link

    def city_filter_link(self):
        try:
            city_name = eval(os.environ.get("city_name"))
            if not isinstance(city_name, list):
                raise DaftRentalBotCityList
            if not all(isinstance(item, str) for item in city_name):
                raise DaftRentalBotCityStr
            if not all(item in available_cities for item in city_name):
                raise DaftRentalBotInvalidCity
            if len(city_name) == 1:
                self.link = f"https://www.daft.ie/property-for-rent/{city_name[0]}"
            elif not city_name:
                self.link += ""
            else:
                self.link += "?"
                for item in city_name:
                    self.link += f"location={item}&"
                self.link = self.link[:-1]
        except NameError:
            print("Searching rental places for Ireland as no specific city provided.")

    def price_filter_link(self):
        try:
            min_price = eval(os.environ.get("min_price"))
            if isinstance(min_price, str):
                min_price = int(min_price)
            min_price = min(available_price, key=lambda x: abs(x - min_price))
        except NameError:
            print("min_price is missing therefore using minimum price default value.")
            min_price = min(available_price)

        try:
            max_price = eval(os.environ.get("max_price"))
            if isinstance(max_price, str):
                max_price = int(max_price)
            max_price = min(available_price, key=lambda x: abs(x - max_price))
        except NameError:
            print("max_price is missing therefore using maximum price default value.")
            max_price = max(available_price)
        self.link += f"&rentalPrice_from={min_price}&rentalPrice_to={max_price}"

    def bath_filter_link(self):
        try:
            min_bed = eval(os.environ.get("min_bed"))
            if isinstance(min_bed, str):
                min_bed = int(min_bed)
            min_bed = min(available_beds, key=lambda x: abs(x - min_bed))
        except NameError:
            print("min_bed is missing therefore using minimum bed default value.")
            min_bed = min(available_beds)

        try:
            max_bed = eval(os.environ.get("max_bed"))
            if isinstance(max_bed, str):
                max_bed = int(max_bed)
            max_bed = min(available_beds, key=lambda x: abs(x - max_bed))
        except NameError:
            print("max_bed is missing therefore using maximum bed default value.")
            max_bed = max(available_beds)
        self.link += f"&numBeds_from={min_bed}&numBeds_to={max_bed}"

    def bed_filter_link(self):
        try:
            min_bath = eval(os.environ.get("min_bath"))
            if isinstance(min_bath, str):
                min_bath = int(min_bath)
            min_bath = min(available_beds, key=lambda x: abs(x - min_bath))
        except NameError:
            print("min_bath is missing therefore using minimum bath default value.")
            min_bath = min(available_bath)

        try:
            max_bath = eval(os.environ.get("max_bath"))
            if isinstance(max_bath, str):
                max_bath = int(max_bath)
            max_bath = min(available_beds, key=lambda x: abs(x - max_bath))
        except NameError:
            print("max_bath is missing therefore using maximum bath default value.")
            max_bath = max(available_bath)
        self.link += f"&numBaths_from={min_bath}&numBaths_to={max_bath}"

    def facilities_filter_link(self):
        available_facilities = ["pets-allowed", "parking"]
        try:
            facilities_name = eval(os.environ.get("facilities"))
            if not isinstance(facilities_name, list):
                raise DaftRentalBotFacilitiesList
            if not all(isinstance(item, str) for item in facilities_name):
                raise DaftRentalBotFacilitiesStr
            if not all(item in available_facilities for item in facilities_name):
                raise DaftRentalBotInvalidFacilities
            if not facilities_name:
                self.link += ""
            else:
                for item in facilities_name:
                    self.link += f"&facilities={item}"
        except NameError:
            print("No facilities provided.")
