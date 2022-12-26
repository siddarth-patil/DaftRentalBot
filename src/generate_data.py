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
        max_price = os.environ.get("max_price")
        min_bed = os.environ.get("min_bed")
        max_bed = os.environ.get("max_bed")
        min_bath = os.environ.get("min_bath")

        self.city_filter_link()
        self.price_filter_link()

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
            else:
                self.link += "?"
                for item in city_name:
                    self.link += f"location={item}&"
        except NameError:
            print("Searching rental places for Ireland as no specific city provided.")
            self.link = "https://www.daft.ie/property-for-rent/ireland"

    def price_filter_link(self):
        try:
            pass
        except:
            pass
