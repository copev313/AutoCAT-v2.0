"""
approve_vendor.py
------------
    The class for running processes required to approve & create vendor
    categories. This module focuses on procedures necessary to complete the
    approval process.
"""
import os
from time import sleep

from xpaths.approved_paths import (
    # Backend Admin Login:
    EMAIL_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    LOGIN_BUTTON,
    SEARCH_IN_BUTTON,

    # Vendor Email Search:
    SEARCH_IN_USERS_DD,
    SEARCH_BAR_FIELD,

    # Approve Vendor:
    ACCOUNT_HEADER,
    COMPANY_NAME_FIELD,
    AD_UPDATE_BUTTON,
    APPROVE_VENDOR_BUTTON,
    
    # Complete Vendor Account:
    QUESTIONS_EMAIL_FIELD,
    COUNTRY_DD,
    STATE_AS_DD,
    STATE_AS_FIELD,
    CITY_FIELD,
    CA_SUBMIT_BUTTON,

    TRUSTED_DD,
    LOCATION_FIELD,
    WEBSITE_FIELD,
    INSTAGRAM_FIELD,
    CD_UPDATE_BUTTON,
)
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#import validators
from utils.helper_funcs import (
    timer,
    wait_for_save,
)


class ApproveVendorProcess:
    """Class used to trigger actions for the approval process using the
    selenium webdriver.

    Attributes:
    ----------
        driver : Selenium webdriver
            The web browser object used to pass in procedures.

    Methods:
    -------
        backend_admin_login():
            Logs into the backend of the website.

        vendor_email_search(email):
            Looks up a vendor using their email address.
        
        approve_vendor():
            [...]
    """

    # Wait time (in seconds) for WebDriverWait events:
    TIMEOUT = 5


    def __init__(self, driver):
        self._driver = driver
        self._profile_id: str = ""
        self._vendor_email_address: str = ""
        self._brand_name: str = ""
        self._company_country: str = ""
        self._company_state: str = ""
        self._company_city: str = ""
        self._website_url: str = ""
        self._instagram_handle: str = ""
        self._company_description: str = ""
        self._category_id: str = ""


    @timer
    def backend_admin_login(self) -> None:
        '''The process required to log into the backend of the website.'''
        print("\n⚙️  Backend Admin Login")
        _driver = self._driver

        # Load our environ. variables:
        load_dotenv()

        # Open browser to the login portal:
        _driver.get(os.environ.get("BACKEND_LOGIN_URL"))

        # Grab the necessary web elements via xpaths:
        _email_field = _driver.find_element_by_xpath(EMAIL_INPUT_FIELD)
        _pswd_field = _driver.find_element_by_xpath(PASSWORD_INPUT_FIELD)
        _login_btn = _driver.find_element_by_xpath(LOGIN_BUTTON)

        # [CHECK] ADMIN_EMAIL environ. variable was found:
        if os.environ.get("ADMIN_EMAIL"):
            _email_field.send_keys(os.environ.get("ADMIN_EMAIL"))
        else:
            print("No environ variable 'ADMIN_EMAIL'! Exiting.")
            return
        # [CHECK] ADMIN_PASSWORD environ. variable was found:
        if os.environ.get("ADMIN_PASSWORD"):
            _pswd_field.send_keys(os.environ.get("ADMIN_PASSWORD"))
        else:
            print("No environ variable 'ADMIN_PASSWORD' Exiting.")
            return

        # Click Login Button:
        _login_btn.click()

        # Confirm that we successfully logged in:
        try:
            # [CHECK] The 'Search in' dropdown button is visible:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.visibility_of_element_located((By.XPATH, SEARCH_IN_BUTTON))
            )
            # [CHECK] The current page is the backend landing page:
            assert _driver.current_url == os.environ.get("BACKEND_LANDING_URL")

        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm successfully login!")
            _driver.quit()
            return
        except AssertionError:
            print("\nASSERTION ERROR: We didn't make the right turn!")
            _driver.quit()
            return


    @timer
    def vendor_email_search(self, email: str) -> None:
        '''The process for looking up a vendor by email address with the
        backend search engine.

        Parameters
        ----------
            email : str
                The vendor's email address.
        '''
        _driver = self._driver
        print("\n🐱  Vendor Email Search")
        
        # [CHECK] Confirm the we're successfully logged in:
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
        _search_bar.send_keys(email)

        # Click 'Search in' button:
        _searchin_btn = _driver.find_element_by_xpath(SEARCH_IN_BUTTON)
        _searchin_btn.click()

        # Choose to search in 'Users' from the dropdown menu:
        _searchin_dd_opt = _driver.find_element_by_xpath(SEARCH_IN_USERS_DD)
        _searchin_dd_opt.click()

        # Selecting the Users option SHOULD automatically put the cursor back
        #   into the search bar.
        _search_bar.send_keys(Keys.RETURN)
        
        # [CHECK] Confirm that we successfully found the vendor's page:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.visibility_of_element_located((By.XPATH, ACCOUNT_HEADER))
            )
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm the vendor page loaded!")
            _driver.quit()
            return


    @timer
    def approve_vendor_button(self):
        '''Run the routine for pressing the 'Approve Vendor' button.'''
        print("\n✔️  Approved Vendor")
        _driver = self._driver
        
        # [CHECK] Confirm we successfully found the page:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, ACCOUNT_HEADER))
            )
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm the page was found!")
            _driver.quit()
            return
        
        # Grab email and brand name from header:
        _header = _driver.find_element_by_xpath(ACCOUNT_HEADER)
        header_parsed = _header.text.split('(')
        email_address = header_parsed[0].strip().lower()
        brand_name = header_parsed[1].replace(')',  '').strip()
        print(f"Brand Name: {brand_name}\nEmail Address: {email_address}")

        current_url = _driver.current_url
        self._profile_id = current_url.split('=')[-1]
        self._vendor_email_address = email_address
        self._brand_name = brand_name

        # Paste the brand name into the Company Name field:
        _company_name_field = _driver.find_element_by_xpath(COMPANY_NAME_FIELD)
        _company_name_field.clear()
        _company_name_field.send_keys(brand_name)

        # Submit:
        sleep(1)
        _company_name_field.send_keys(Keys.RETURN)
        sleep(1)

        # Wait for page to load after inputting data:
        wait_for_save(_driver, AD_UPDATE_BUTTON)

        # [CHECK] Confirm we successfully saved changes:
        try:
            # Grab element again to avoid 'staleness' error:
            _name_field2 = _driver.find_element_by_xpath(COMPANY_NAME_FIELD)
            # [CHECK] Does the value in the 'Company name' field match the brand name?
            assert brand_name == _name_field2.get_attribute('value')

        except AssertionError:
            print("\nASSERTION ERROR: Couldn't confirm field 'Company name'!")
            _driver.quit()
        except Exception as err:
            print(f"\nERROR: Exception in 'approve_vendor'!\n{err}")
            _driver.quit()

        _approve_btn = _driver.find_element_by_xpath(APPROVE_VENDOR_BUTTON)
        _approve_btn.click()
        sleep(1)


    @timer
    def complete_vendor_account(self):
        '''Run the routine for pressing the 'Approve Vendor' button.'''
        print("\n✔️  Complete Vendor Account")
        _driver = self._driver

        ''' * * * * * Complete 'Company Address' tab * * * * * '''

        # Form the URL for the Company Address tab:
        address_tab_url = "{root}?target=companyAddress&profile_id={id}".format(
                            root=os.environ.get("BACKEND_LANDING_URL"),
                            id=self._profile_id)

        # Got to our tab via URL:
        _driver.get(address_tab_url)
        
        # [CHECK] Confirm we successfully found our vendor page:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, QUESTIONS_EMAIL_FIELD))
            )
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm the company address tab \
                was opened!")
            _driver.quit()
            return

        # Paste email address into 'Product questions e-mail' field:
        _email_field =  _driver.find_element_by_xpath(QUESTIONS_EMAIL_FIELD)
        _email_field.clear()
        _email_field.send_keys(self._vendor_email_address)

        # Submit:
        sleep(1)
        _email_field.send_keys(Keys.RETURN)
        sleep(1)

        # Wait for page to indicate it successfully saved our input:
        wait_for_save(_driver, CA_SUBMIT_BUTTON)

        # Handle the 'Country' dropdown:
        _country_dd = _driver.find_element_by_xpath(COUNTRY_DD)
        _country_selected = _country_dd.find_element_by_xpath("//*[@selected='selected']")
        self._company_country = _country_selected.text

        # Handle the 'State' field:
        # [CASE] Country is United States --> Use the dropdown XPATH:
        if (self._company_country == 'United States'):
            _state_dd = _driver.find_element_by_xpath(STATE_AS_DD)
            data_val = _state_dd.get_attribute('data-value')
            _state_option = _state_dd.find_element_by_xpath(f"//*[@value='{data_val}']")
            self._company_state = _state_option.text
        # [CASE] Country is NOT the U.S. --> Use the field XPATH:
        else:
            _state_field = _driver.find_element_by_xpath(STATE_AS_FIELD)
            self._company_state = _state_field.get_attribute('value')

        # Handle the 'City' field:
        _city_field = _driver.find_element_by_xpath(CITY_FIELD)
        self._company_city = _city_field.get_attribute('value')
        print("City: " + self._company_city)
        print("State: " + self._company_state)
        print("Country: " + self._company_country)


        ''' * * * * * Complete 'Company Address' tab * * * * * '''

        # Form the URL for the Company Address tab:
        company_details_tab_url = "{root}?target=vendor&profile_id={id}".format(
                                    root=os.environ.get("BACKEND_LANDING_URL"),
                                    id=self._profile_id)

        # Go to our tab via URL:
        _driver.get(company_details_tab_url)
        
        # [CHECK] Next page successfully Loaded:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.presence_of_element_located((By.XPATH, LOCATION_FIELD))
            )
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm the company details tab \
                was opened!")
            _driver.quit()
            return

        # Handle the trusted dropdown:
        _trusted_dd = _driver.find_element_by_xpath(TRUSTED_DD)
        _trusted_opt = _trusted_dd.find_element_by_xpath("/option[1]")
        _trusted_dd.click()
        _trusted_opt.click()

        # Handle the location field:
        _location_field = _driver.find_element_by_xpath(LOCATION_FIELD)
        location = address_handler(country=self._company_country,
                                   state=self._company_state,
                                   city=self._company_city)
        print("Address:  " + location)  # debugs!
        # Replace location imformation:
        _location_field.clear()
        _location_field.send_keys(location)

        # Submit:
        sleep(1)
        _location_field.send_keys(Keys.RETURN)
        sleep(1)

        # Wait for the page to successfully save our location data:
        wait_for_save(_driver, CD_UPDATE_BUTTON)

        # Store website URL so we can launch it later:
        _website_field = _driver.find_element_by_xpath(WEBSITE_FIELD)
        self._website_url =  _website_field.get_attribute('value')
        print(f"Site URL:  {self._website_url}")

        # Handle formatting & storing Instagram handle (if applicable):
        _instagram_field = _driver.find_element_by_xpath(INSTAGRAM_FIELD)
        instagram = _instagram_field.get_attribute('value')
        if instagram:
            found_url = instagram.find('.com')
            # [CASE] Contains '@' -> Removed @:
            if '@' in instagram:
                instagram = instagram.replace('@', '')
            # [CASE] Is URL -> Strip to instagram handle only:
            if (found_url != -1):
                splitted = instagram.split('/')
                instagram = splitted[-2] or splitted[-1]
            print(f"Instagram:  {instagram}")
        else:
            print("Instagram:  None")

        # Store the Instagram handle:
        self._instagram_handle = instagram if instagram else None
