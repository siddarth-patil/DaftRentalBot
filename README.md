# DaftRentalBot

DaftRentalBot is an open source Python project that automates the process of applying for rental places on [daft.ie](https://www.daft.ie/).

## Features

- Search for rental properties on daft.ie based on location, price range, and number of bedrooms
- Filter search results by property type (e.g. apartment, house, studio)
- Apply to rental properties with a customizable application message
- Save and manage multiple application templates
- Specify search filters in the `.env` file, including "Maximum Price", "Minimum no. of beds", "Maximum no. of beds", "minimum no. of bathrooms", and "City Name"
- Keep a log of applied houses in the `logger.csv` file, including "Rent", "Address of the house", "Daft link to the house", and "Application status"

## Requirements

DaftRentalBot requires the following packages:

- Python 3.6 or higher
- [Selenium](https://pypi.org/project/selenium/)
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) (if using Chrome browser)

## Installation

To install DaftRentalBot, clone the repository and install the required packages:

```bash
git clone https://github.com/<username>/daftrentalbot.git
cd daftrentalbot
pip install -r requirements.txt
```

## Usage

To use DaftRentalBot, you will need to have a Daft account and provide your login credentials in the config.ini file. You will also need to specify your search filters in the .env file.

To start the bot, run the following command:

```bash
python main.py
```

The bot will search for rental properties on daft.ie based on the specified filters and display the results. You can filter the results by property type and select which properties to apply to. A log of applied houses will be kept in the logger.csv file.

## Contributing

We welcome contributions to DaftRentalBot. If you have a bug fix or new feature that you would like to contribute, please open a pull request.

## License

DaftRentalBot is licensed under the [Apache License 2.0](https://github.com/siddarth-patil/daft_automation/blob/6fc05f2908f719292cffc0017543f5c92bebb6db/LICENSE).