<p align="center">
    <a href="http://hits.dwyl.com/siddarth-patil/repo/DaftRentalBot"><img src="https://hits.dwyl.com/siddarth-patil/repo/DaftRentalBot.svg?style=flat-square" alt="HitCount"></a>
    <a href="https://ko-fi.com/P5P5HAOTL"><img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="ko-fi"></a>
    <a href='https://github.com/MShawon/github-clone-count-badge'><img alt='GitHub Clones' src='https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.githubusercontent.com/siddarth-patil/51a993d18f4c3d624dd5c11473ef64c2/raw/clone.json&logo=github'></a>
</p>

# DaftRentalBot

DaftRentalBot is an open source Python project that automates the process of applying for rental places on [daft.ie](https://www.daft.ie/).

## Features

-   Search for rental properties on daft.ie based on location, price range, number of bathrooms, and number of bedrooms. All the properties should be stored in `.env` file in root directory.
-   Apply to rental properties with a customizable application message
-   Keep a log of applied houses in the `logger.csv` file, including "Rent", "Address of the house", "Daft link to the house", and "Application status"

## Requirements

DaftRentalBot requires the following packages:

-   [Python 3.7 or higher](https://www.python.org/downloads/)
-   [Selenium](https://pypi.org/project/selenium/)
-   [Chrome Browser](https://www.google.com/intl/en_ie/chrome/)

## Installation

To install DaftRentalBot, clone the repository and install the required packages:

```bash
git clone https://github.com/siddarth-patil/DaftRentalBot
cd DaftRentalBot
pip install -r requirements.txt
```

## Usage

To use DaftRentalBot, you will need to have a Daft account and provide your login credentials in the `.env` file. You will also need to specify your search filters in the `.env` file.

To start the bot, run the following command:

```bash
python src/main.py
```

The bot will search for rental properties on daft.ie based on the specified filters and apply for the places automatically. A log of applied houses will be kept in the `logger.csv` file. Logs of the running script will also be printed on the terminal.

## Contributing

We welcome contributions to DaftRentalBot. If you have a bug fix or new feature that you would like to contribute, please open a pull request.

## Upcoming Features/Bug Fixes

-   Add a filter to support Pet Friendly, Smoking friendly, etc. houses.
-   Write tests to check for the valid inputs from the user.

## License

DaftRentalBot is licensed under the [Apache License 2.0](https://github.com/siddarth-patil/daft_automation/blob/6fc05f2908f719292cffc0017543f5c92bebb6db/LICENSE).
