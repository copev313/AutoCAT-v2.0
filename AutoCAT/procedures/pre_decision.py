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
    COMPANY_DETAILS_TAB,  # may not need this xpath/element

    # Account Details Tab:
    VENDOR_HEADER,
    COMPANY_NAME_FIELD,
    
    # Company Address Tab:
    QUESTIONS_EMAIL_FIELD,
    COUNTRY_DD,
    STATE_AS_DD,
    STATE_AS_FIELD,
    CITY_FIELD,
)
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helper_funcs import abbreviate_state


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

        vendor_email_search(email_address):
            Executes the process for looking up a vendor by email address 
            with the backend search engine.

        complete_account_details_tab():
            Copy and pastes the brand name into the 'Company name' field
            on the Company Details tab.
    '''

    # Wait time (in seconds) for WebDriverWait events:
    TIMEOUT = 5

    def __init__(self, driver):
        self._driver = driver
        self._profile_id: str = ""
        self._vendor_email_address: str = ""
        self._company_country: str = ""
        self._company_state: str = ""
        self._company_city: str = ""


    @property
    def profile_id(self):
        return self._profile_id


    @property
    def vendor_email_address(self):
        return self._vendor_email_address


    @profile_id.setter
    def profile_id(self, id: str):
        '''Setter for overwritting a vendor's profile id.'''
        # [CASE] Id value is not an int or str  --> raise error.
        if ((type(id) is not str) or (type(id) is not int)):
            raise ValueError(
                "Property 'profile_id' must be of type int or str")
        else:
            self._profile_id = str(id)


    @vendor_email_address.setter
    def vendor_email_address(self, email: str):
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
                EC.visibility_of_element_located(
                    (By.XPATH, SEARCH_IN_BUTTON)
                )
            )
            current_url = _driver.current_url
            assert current_url == os.environ.get("BACKEND_LANDING_URL")

            # Set the vendor's profile_id from the URL:
            self._profile_id = current_url.split('=')[-1]
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
        '''Executes the process for looking up a vendor by email address with the
        backend search engine.

        Parameters
        ----------
            email_address : str
                The vendor's email address for searching purposes.
        '''
        _driver = self._driver

        # Confirm the we re successfully logged in:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, SEARCH_IN_BUTTON)
                )
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


    def complete_account_details_tab(self):
        '''Copy and pastes the brand name into the 'Company name' field on the
        Company Details tab.'''
        print("\n🐱  AUTOCAT >>> Beginning Task: 'Account Details Tab'")
        _driver = self._driver

        # [CHECK] Confirm we successfully found out vendor page:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.presence_of_element_located(
                    (By.XPATH, VENDOR_HEADER)
                )
            )
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm the vendor page was found!")
            _driver.quit()
            return

        # COPY the Brand Name:
        _vendor_header = _driver.find_element_by_xpath(VENDOR_HEADER)
        header_txt = _vendor_header.text
        print(header_txt)
        parsed_header = header_txt.split('(')
        email_address = parsed_header[0].strip()
        brand_name = parsed_header[1].replace(')', '').strip()
        print(f"Brand Name: {brand_name}\nEmail Address: {email_address}")  # debugging!

        # PASTE the Brand Name:
        _company_name_field = _driver.find_element_by_xpath(COMPANY_NAME_FIELD)
        _company_name_field.clear()
        _company_name_field.send_keys(brand_name)
        _company_name_field.send_keys(Keys.RETURN)
        

        # [CHECK] Confirm we successfully saved changes:
        try:
            # Verify vendor's company name is in company_name_field:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.presence_of_element_located(
                    (By.XPATH, COMPANY_NAME_FIELD)
                )
            )
            # Grab element again to avoid 'staleness' error:
            _company_name_field2 = _driver.find_element_by_xpath(COMPANY_NAME_FIELD)
            # Does the value in the 'Company name' field match the brand name?
            assert brand_name == _company_name_field2.get_attribute('value')
        
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm successful page save!")
            _driver.quit()
        except AssertionError:
            print("\nASSERTION ERROR: Couldn't confirm field 'Company name'!")
            _driver.quit()
        except Exception as err:
            print(f"\nERROR: Exception in 'copy_paste_brand_name'!\n{err}")
            _driver.quit()

        # Store the vendor's email address from the Vendor's page (lowercase):
        self._vendor_email_address = email_address.lower()
        print("\n✔️  AUTOCAT >>> 'Account Details Tab' - TASK COMPLETE!")

"""
    def complete_company_address_tab(self):
        '''Pastes the vendor's email address into the appropriate field and
        copies/stores the city and state information (if applicable).'''
        print("\n🐱  AUTOCAT >>> Beginning Task: 'Company Address Tab'")
        _driver = self._driver

        # Form the URL for the Company Address tab:
        next_tab_url = "{root}?target=companyAddress&profile_id={id}".format(
                        root=os.environ.get("BACKEND_LANDING_URL"),
                        id=self._profile_id)
        # Got to our tab via URL:
        _driver.get(next_tab_url)

        # [CHECK] Confirm we successfully found out vendor page:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.presence_of_element_located(
                    (By.XPATH, QUESTIONS_EMAIL_FIELD)
                )
            )
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm the company address tab \
                was opened!")
            _driver.quit()
            return
"""
