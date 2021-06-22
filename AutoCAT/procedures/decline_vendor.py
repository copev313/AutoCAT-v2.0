"""
decline_vendor.py
------------
    The class for running processes required to decline vendor accounts.
"""
import os
from time import sleep

'''
from xpaths.declined_paths import (
    
)
'''
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import validators
from utils.helper_funcs import (
    timer,
    wait_for_save,
)


class DeclineVendorProcess:
    """Class used to trigger actions for the decline process using the
    selenium webdriver.

    Attributes:
    ----------
        driver : Selenium webdriver
            The web browser object used to pass in procedures.

    Methods:
    -------
    """

    # Wait time (in seconds) for WebDriverWait events:
    TIMEOUT = 5


    def __init__(self, driver):
        self._driver = driver
        self._profile_id: str = ""
        self._vendor_email_address: str = str(email_address).lower()
        self._brand_name: str = ""

