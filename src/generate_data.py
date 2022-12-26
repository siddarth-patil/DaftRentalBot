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
        self.pets_filter_link()

        print("Final link is: ", self.link)
        return self.link

    def city_filter_link(self):
        try:
            city_name = os.environ.get("city_name")
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
            min_price = min(
                available_price, key=lambda x: abs(x - os.environ.get("min_price"))
            )
        except NameError:
            print("min_price is missing therefore using minimum price default value.")
            min_price = min(available_price)

        try:
            max_price = min(
                available_price, key=lambda x: abs(x - os.environ.get("max_price"))
            )
        except NameError:
            print("max_price is missing therefore using maximum price default value.")
            max_price = max(available_price)
        self.link += f"&rentalPrice_from={min_price}&rentalPrice_to={max_price}"

    def bath_filter_link(self):
        try:
            min_bed = min(
                available_beds, key=lambda x: abs(x - os.environ.get("min_bed"))
            )
        except NameError:
            print("min_bed is missing therefore using minimum bed default value.")
            min_bed = min(available_beds)

        try:
            max_bed = min(
                available_beds, key=lambda x: abs(x - os.environ.get("max_bed"))
            )
        except NameError:
            print("max_bed is missing therefore using maximum bed default value.")
            max_bed = max(available_beds)
        self.link += f"&numBeds_from={min_bed}&numBeds_to={max_bed}"

    def bed_filter_link(self):
        try:
            min_bath = min(
                available_beds, key=lambda x: abs(x - os.environ.get("min_bath"))
            )
        except NameError:
            print("min_bath is missing therefore using minimum bath default value.")
            min_bath = min(available_bath)

        try:
            max_bath = min(
                available_beds, key=lambda x: abs(x - os.environ.get("max_bath"))
            )
        except NameError:
            print("max_bath is missing therefore using maximum bath default value.")
            max_bath = max(available_bath)
        self.link += f"&numBaths_from={min_bath}&numBaths_to={max_bath}"

    def pets_filter_link(self):
        try:
            facilities_name = os.environ.get("facilities")
            if not isinstance(facilities_name, list):
                raise DaftRentalBotFacilitiesList
            if not all(isinstance(item, str) for item in facilities_name):
                raise DaftRentalBotFacilitiesStr
            if not all(item in available_cities for item in facilities_name):
                raise DaftRentalBotInvalidFacilities
            if not facilities_name:
                self.link += ""
            else:
                for item in facilities_name:
                    self.link += f"&facilities={item}"
        except NameError:
            print("No facilities provided.")
