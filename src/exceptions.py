class DaftRentalBotCityList(Exception):
    """city_name should be of type List."""


class DaftRentalBotCityStr(Exception):
    """Each item inside city_name should be of type String."""


class DaftRentalBotInvalidCity(Exception):
    """Each item inside city_name shold be a part of available_cities"""


class DaftRentalBotFacilitiesList(Exception):
    """facilities should be of type List."""


class DaftRentalBotFacilitiesStr(Exception):
    """Each item inside facilities should be of type String."""


class DaftRentalBotInvalidFacilities(Exception):
    """Each item inside facilities shold be a part of available_facilities"""
