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


class SettingFactory(ABC):
    """
    Factory that represents a combination of currency 
    and language settings.
    The factory doesn't maintain any of the instances it creates.
    Once instances are created you are in charge of them.
    """

    def get_currency_setting(self) -> CurrencySetting:
        """Returns a new currency setting instance"""

    def get_language_setting(self) -> LanguageSetting:
        """Returns a new language setting instance"""


class EuropeSetting(SettingFactory):
    """Factory aimed at creating settings for Europe region"""

    def get_currency_setting(self) -> CurrencySetting:
        return EuroCurrencySetting()
    
    def get_language_setting(self) -> LanguageSetting:
        return GermanLanguageSetting()
    

class UnitedKingdomSetting(SettingFactory):
    """Factory aimed at creating settings for United Kingdom region"""

    def get_currency_setting(self) -> CurrencySetting:
        return PoundCurrencySetting()
    
    def get_language_setting(self) -> LanguageSetting:
        return EnglishLanguageSetting()


class UnitedStatesSetting(SettingFactory):
    """Factory aimed at creating settings for United States region"""

    def get_currency_setting(self) -> CurrencySetting:
        return DollarCurrencySetting()
    
    def get_language_setting(self) -> LanguageSetting:
        return EnglishLanguageSetting()


def read_setting() -> SettingFactory:
    """Constructs an setting factory based on the user's preference."""
    factories = {
        "eu": EuropeSetting(),
        "uk": UnitedKingdomSetting(),
        "us": UnitedStatesSetting(),
    }

    # read the desired region
    while True:
        region = input("Enter your region (eu, uk, us):")
        if region in factories:
            return factories[region]
        print(f"Unknown region option: {region}")


def main(fac: SettingFactory) -> None:
    """
    Main function
    Invokes factory methods
    """

    # create the currency and language setting
    currency_setting = fac.get_currency_setting()
    language_setting = fac.get_language_setting()

    # set a setting
    currency_setting.set_setting()
    language_setting.set_setting()

    # fetch data
    database = 'PostgreSQL'
    currency_setting.fetch_data(database)
    language_setting.fetch_data(database)


if __name__ == '__main__':
    # fetch factory from user input function
    setting_factory = read_setting()
    
    # provide SettingFactory to the main function
    main(setting_factory)

    """
    Factory Pattern should be used when there is a need to
    create a combination of classes with recurring methods.
    When objects customization is needed with many
    combinations one should use composition.
    """