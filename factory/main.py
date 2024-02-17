"""
User country setting example
"""

import pathlib
from abc import ABC, abstractmethod


class CurrencySetting(ABC):
    """Representation of country settings."""

    @abstractmethod
    def set_setting(self):
        """Sets currency setting for a user"""

    @abstractmethod
    def fetch_data(self, db):
        """Fetches data linked to currency"""


class EuroCurrencySetting(CurrencySetting):
    """User Euro currency setting"""

    def set_setting(self):
        print('Setting Euro as currency.')

    def fetch_data(self, db):
        print(f'Fetch Euro prices from the {db} database.')


class PoundCurrencySetting(CurrencySetting):
    """User Pound currency setting"""

    def set_setting(self):
        print('Setting Pound as currency.')

    def fetch_data(self, db):
        print(f'Fetch Pound prices from the {db} database.')


class DollarCurrencySetting(CurrencySetting):
    """User Dollar currency setting"""

    def set_setting(self):
        print('Setting Dollar as currency.')

    def fetch_data(self, db):
        print(f'Fetch Dollar prices from the {db} database.')


class LanguageSetting(ABC):
    """Representation of language setting."""

    def set_setting(self, cart):
        """Sets language setting for a user"""

    @abstractmethod
    def fetch_data(self, db):
        """Fetches data linked to language"""


class GermanLanguageSetting(LanguageSetting):
    """User German Language setting"""

    def set_setting(self):
        print('Setting German as Language.')

    def fetch_data(self, db):
        print(f'Fetch German text from the {db} database.')


class EnglishLanguageSetting(LanguageSetting):
    """User English Language setting"""

    def set_setting(self):
        print('Setting English as Language.')

    def fetch_data(self, db):
        print(f'Fetch English text from the {db} database.')


def main() -> None:
    """Main function"""

    # read the desired region
    region: str
    while True:
        region = input("Enter your region (eu, uk, us):")
        if region in {"eu", "uk", "us"}:
            break
        print(f"Unknown region option: {region}")

    # create the currency and language setting
    currency_setting: CurrencySetting
    language_setting: LanguageSetting
    if region == "eu":
        currency_setting = EuroCurrencySetting()
        language_setting = GermanLanguageSetting()
    elif region == "uk":
        currency_setting = PoundCurrencySetting()
        language_setting = EnglishLanguageSetting()     
    else:
        # Default: us region
        currency_setting = DollarCurrencySetting()
        language_setting = EnglishLanguageSetting()

    # set a setting
    currency_setting.set_setting()
    language_setting.set_setting()

    # fetch data
    database = 'PostgreSQL'
    currency_setting.fetch_data(database)
    language_setting.fetch_data(database)


if __name__ == '__main__':
    main()