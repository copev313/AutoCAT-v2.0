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

    # Company Details Tab:
    LOCATION_FIELD,
    WEBSITE_FIELD,
    COMPANY_DESC_FIELD,
    INSTAGRAM_FIELD,
)
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helper_funcs import address_handler, print_admin_info, timer


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
        self._website_url: str = ""
        self._instagram_handle: str = ""
        self._company_description: str = ""


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


    @timer
    def backend_admin_login(self):
        '''Executes the process required to log into the backend of the website.'''
        print("\n⚙️  ## Backend Admin Login ##")
        _driver = self._driver
        load_dotenv()

        # Print Admin Login Info to Console (password censored):
        print_admin_info()

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
    def vendor_email_search(self, email_address):
        '''Executes the process for looking up a vendor by email address with the
        backend search engine.

        Parameters
        ----------
            email_address : str
                The vendor's email address for searching purposes.
        '''
        _driver = self._driver
        print("\n🐱  ## Vendor Email Search ##")
        
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


    @timer
    def complete_account_details_tab(self):
        '''Copy and pastes the brand name into the 'Company name' field on the
        Company Details tab.'''
        print("\n🐱  ## Account Details Tab ##")
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
        parsed_header = header_txt.split('(')
        email_address = parsed_header[0].strip()
        brand_name = parsed_header[1].replace(')', '').strip()
        print(f"Brand Name: {brand_name}\nEmail Address: {email_address}")

        # Set the vendor's profile_id from the URL:
        current_url = _driver.current_url
        self._profile_id = current_url.split('=')[-1]

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


    @timer
    def complete_company_address_tab(self):
        '''Pastes the vendor's email address into the appropriate field and
        stores the city and state information for use in the next tab.'''
        print("\n🐱  ## Company Address Tab ##")
        _driver = self._driver

        # Form the URL for the Company Address tab:
        address_tab_url = "{root}?target=companyAddress&profile_id={id}".format(
                        root=os.environ.get("BACKEND_LANDING_URL"),
                        id=self._profile_id)

        # Got to our tab via URL:
        _driver.get(address_tab_url)

        # [CHECK] Confirm we successfully found our vendor page:
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

        # Paste email address into 'Product questions e-mail' field:
        _email_field =  _driver.find_element_by_xpath(QUESTIONS_EMAIL_FIELD)
        _email_field.clear()
        _email_field.send_keys(self._vendor_email_address)
        _email_field.send_keys(Keys.RETURN)

        # [CHECK] The page has reloaded after submit:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.presence_of_element_located(
                    (By.XPATH, COUNTRY_DD)
                )
            )
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm the company address tab \
                submitted successfully!")
            _driver.quit()
            return

        # Handle Country Dropdown:
        _country_dd = _driver.find_element_by_xpath(COUNTRY_DD)
        _country_selected = _country_dd.find_element_by_xpath("//*[@selected='selected']")
        print("Country: " + _country_selected.text)
        self._company_country = _country_selected.text

        # Handle State:
        # [CASE] Country is United States --> Use the dropdown XPATH:
        if (self._company_country == 'United States'):
            _state_dd = _driver.find_element_by_xpath(STATE_AS_DD)
            data_val = _state_dd.get_attribute('data-value')
            _state_option = _state_dd.find_element_by_xpath(f"//*[@value='{data_val}']")
            self._company_state = _state_option.text
        # [CASE] Country is NOT U.S. --> Use the field XPATH:
        else:
            _state_field = _driver.find_element_by_xpath(STATE_AS_FIELD)
            self._company_state = _state_field.get_attribute('value')
        print("State: " + self._company_state)

        # Handle City Field:
        _city_field = _driver.find_element_by_xpath(CITY_FIELD)
        self._company_city = _city_field.get_attribute('value')
        print("City: " + self._company_city)


    @timer
    def complete_company_details_tab(self):
        '''Overwrites the inforamtion in the 'Location' field with the
        appropriately formatted location.
        
        Stores the 'Company Description' field ofr later use.

        Formats the 'Instagram Handle' field (if applicable).

        Stores the website URL from the 'Website or Link to...' field to
        launch the site upon the completion of the current tab.
        '''
        print("\n🐱  ## Company Details Tab ##")
        _driver = self._driver

        # Form the URL for the Company Address tab:
        company_details_tab_url = "{root}?target=vendor&profile_id={id}".format(
                                    root=os.environ.get("BACKEND_LANDING_URL"),
                                    id=self._profile_id)

        # Got to our tab via URL:
        _driver.get(company_details_tab_url)

        # [CHECK] Page Successfully Loaded:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.presence_of_element_located(
                    (By.XPATH, LOCATION_FIELD)
                )
            )
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm the company details tab \
                was opened!")
            _driver.quit()
            return

        _location_field = _driver.find_element_by_xpath(LOCATION_FIELD)
        address = address_handler(country=self._company_country,
                                  state=self._company_state,
                                  city=self._company_city)
        print("ADDRESS:  " + address)  # debugs!
        # Replace location imformation:
        _location_field.clear()
        _location_field.send_keys(address)

        # Store website URL so we can launch it later:
        _website_field = _driver.find_element_by_xpath(WEBSITE_FIELD)
        self._website_url =  _website_field.get_attribute('value')
        print("SITE URL:  " + self._website_url)

        # Store the company description:
        _company_desc_field = _driver.find_element_by_xpath(COMPANY_DESC_FIELD)
        self._company_description = _company_desc_field.text

        # Handle formatting & storing instagram handle (if applicable):
        _instagram_field = _driver.find_element_by_xpath(INSTAGRAM_FIELD)
        instagram = _instagram_field.get_attribute('value')
        if instagram:
            found_url = instagram.find('.com')
            # [CASE] Contains '@' -> Removed @:
            if '@' in instagram:
                instagram = instagram.replace('@', '')
            # [CASE] Is URL -> Strip to instragram handle only:
            if (found_url != -1):
                splitted = instagram.split('/')
                instagram = splitted[-2] or splitted[-1]
            print("INSTAGRAM:  " + instagram)
