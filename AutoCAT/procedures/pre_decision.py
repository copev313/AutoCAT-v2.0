'''
procedure.py
------------
    Class for our step-by-step processes required to create categories.
This module focuses on procedures necessary to completet the pre-decision
phase.
'''
import os

from constants.xpaths import (
    # Backend Admin Login:
    EMAIL_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    LOGIN_BUTTON,
    SEARCH_IN_BUTTON,

    # Vendor Email Search:
    SEARCH_IN_USERS_DD,
    SEARCH_BAR_FIELD,
    COMPANY_DETAILS_TAB,

)
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Procedure:
    '''Class used to trigger common procedures using the webdriver.

    Attributes:
    ----------
        driver : Selenium Chrome webdriver
            The web browser object used to pass in procedures.

    Methods:
    -------
        backend_login_portal():
            Executes the process required to log into the backend of the
            website.
    '''

    # Wait time (in seconds) for WebDriverWait events:
    TIMEOUT = 7

    def __init__(self, driver):
        self._driver = driver
        self._profile_id = ""
        self._vendor_email_address = ""


    @property
    def profile_id(self):
        return self._profile_id


    @property
    def vendor_email_address(self):
        return self._vendor_email_address


    @profile_id.setter
    def profile_id(self, id):
        '''Setter for overwritting a vendor's profile id.'''
        # [CASE] Id value is not an int or str  --> raise error.
        if ((type(id) is not str) or (type(id) is not int)):
            raise ValueError(
                "Property 'profile_id' must be of type int or str")
        else:
            self._profile_id = str(id)


    @vendor_email_address.setter
    def vendor_email_address(self, email):
        '''Setter for overwritting a vendor's email address.'''
        # [CASE] 'email' is a not a string --> raise error.
        if (type(email) is not str):
            raise ValueError(
                "Property 'vendor_email_address' must be of type str")
        else:
            self._vendor_email_address = email
    
    
    def backend_admin_login(self):
        '''Executes the process required to log into the backend of the website.'''
        print("\n⚙️  Backend Login Process starting . . .")
        _driver = self._driver
        load_dotenv()
        
        # Open browser to the login portal:
        _driver.get(os.environ.get("BACKEND_LOGIN_URL"))

        # Grab the necessary web elements via xpaths:
        _email_field = _driver.find_element_by_xpath(EMAIL_INPUT_FIELD)
        _pswd_field = _driver.find_element_by_xpath(PASSWORD_INPUT_FIELD)
        _login_btn = _driver.find_element_by_xpath(LOGIN_BUTTON)
        
        # [CHECK] For ADMIN_EMAIL environ var:
        if os.environ.get("ADMIN_EMAIL"):
            _email_field.send_keys(os.environ.get("ADMIN_EMAIL"))
        else:
            print("No environ variable 'ADMIN_EMAIL'! Exiting.")
            return

        # [CHECK] For ADMIN_PASSWORD enviro var:
        if os.environ.get("ADMIN_PASSWORD"):
            _pswd_field.send_keys(os.environ.get("ADMIN_PASSWORD"))
        else:
            print("No environ variable 'ADMIN_PASSWORD' Exiting.")
            return

        # Click Login Button:
        _login_btn.click()

        # Confirm we successfully logged in:
        try:
            # [CHECK] The 'Search in' dropdown button is visible:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.visibility_of_element_located((By.XPATH, SEARCH_IN_BUTTON))
            )
            current_url = _driver.current_url
            assert current_url == os.environ.get("BACKEND_LANDING_URL")
            print("\n🐱  AUTOCAT >>> Login Successfully!")
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm successfully login!")
            _driver.quit()
            return
        except AssertionError:
            print("\nASSERTION ERROR: We didn't make the right turn!")
            _driver.quit()
            return


    def vendor_email_search(self, email_address):
        '''
        Executes the process for looking up a vendor by email with the backend
        search engine.

        Parameters
        ----------
            email_address : str
                The vendor's email address for searching purposes.
        '''
        _driver = self._driver

        # Confirm we're successfully logged in:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.element_to_be_clickable((By.XPATH, SEARCH_IN_BUTTON))
            )
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm successfully login!")
            _driver.quit()
            return

        # Select search bar and enter vendor's email address:
        _search_bar = _driver.find_element_by_xpath(SEARCH_BAR_FIELD)
        _search_bar.send_keys(email_address)

        # Click 'Search in' button:
        _searchin_btn = _driver.find_element_by_xpath(SEARCH_IN_BUTTON)
        _searchin_btn.click()

        # Choose to search in 'Users' from the dropdown menu:
        _searchin_dd_opt = _driver.find_element_by_xpath(SEARCH_IN_USERS_DD)
        _searchin_dd_opt.click()

        # Selecting the Users option SHOULD automatically put the cursor back
        #   in the search bar.
        _search_bar.send_keys(Keys.RETURN)
