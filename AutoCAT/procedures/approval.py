"""
approval.py
------------
    A class for our step-by-step processes required to create vendor
    categories. This module focuses on procedures necessary to complete the
    approval process.
"""
import os
from time import sleep


# from xpaths.approval_constants import ()
from xpaths.prereview_constants import (
    # Backend Admin Login:
    EMAIL_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    LOGIN_BUTTON,
    SEARCH_IN_BUTTON,
    # Vendor Email Search:
    SEARCH_IN_USERS_DD,
    SEARCH_BAR_FIELD,
    # Company Details Tab:
    CD_UPDATE_BUTTON,
)
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helper_funcs import timer, wait_for_save


class ApprovalProcess:
    """Class used to trigger actions for the approval process using the
    selenium webdriver.

    Attributes:
    ----------
        driver : Selenium webdriver
            The web browser object used to pass in procedures.

        email_address: str
            The vendor's email address.

    Methods:
    -------
    """

    # Wait time (in seconds) for WebDriverWait events:
    TIMEOUT = 5

    def __init__(self, driver, email_address):
        self._driver = driver
        self._profile_id: str = ""
        self._vendor_email_address: str = str(email_address).lower()
        self._company_description: str = ""
