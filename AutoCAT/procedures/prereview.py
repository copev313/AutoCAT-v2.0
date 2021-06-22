'''
prereview.py
------------
    A class for our step-by-step processes required to create vendor
    categories. This module focuses on procedures necessary to complete the
    pre-decision (tedious copy/paste) phase.
'''
import os
from time import sleep

from xpaths.prereview_constants import (
    # Account Details Tab:
    VENDOR_HEADER,
    COMPANY_NAME_FIELD,
    AD_UPDATE_BUTTON,

    # Company Address Tab:
    QUESTIONS_EMAIL_FIELD,
    COUNTRY_DD,
    STATE_AS_DD,
    STATE_AS_FIELD,
    CITY_FIELD,
    CA_SUBMIT_BUTTON,

    # Company Details Tab:
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
import validators
from utils.helper_funcs import (
    address_handler,
    print_admin_info,
    timer,
    wait_for_save,
)


class PreReviewProcess:
    '''Class used to trigger common procedures for the prereview process
    using the selenium webdriver.

    Attributes:
    ----------
        driver : Selenium webdriver
            The web browser object used to pass in procedures.

    Methods:
    -------
        complete_company_address_tab():
            Completes the tasks required on the Company Address tab of the
            vendor's page.

        complete_company_details_tab():
            Performs the steps required on the Company Details tab of the
            vendor's page.

        launch_vendor_website():
            Launches the vendor's website in a new tab in the current window 
            (if a proper URL was given).
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


    @timer
    def complete_company_address_tab(self):
        '''Pastes the vendor's email address into the appropriate field and
        stores the city and state information for use in the next tab.'''
        print("\n🐱  Company Address Tab")
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


    @timer
    def complete_company_details_tab(self):
        '''Overwrites the information in the 'Location' field with the
        appropriately formatted location.

        Prints the 'Instagram Handle' field.

        Stores the website URL from the 'Website or Link to...' field to
        launch the site upon the completion of the current tab.
        '''
        print("\n🐱  Company Details Tab")
        _driver = self._driver

        # Form the URL for the Company Address tab:
        company_details_tab_url = "{root}?target=vendor&profile_id={id}".format(
                                    root=os.environ.get("BACKEND_LANDING_URL"),
                                    id=self._profile_id)

        # Go to our tab via URL:
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
        print("Site URL:  " + self._website_url)

        # Handle formatting & storing Instagram handle (if applicable):
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
            print("Instagram:  " + instagram)
        else:
            print("Instagram:  None")

        # Store the Instagram handle:
        self._instagram_handle = instagram if instagram else None


    @timer
    def launch_vendor_website(self):
        '''Opens the vendor's website from their given URL in a new tab in the
        current window.'''
        _driver = self._driver

        # [CHECK] Make sure the Account Details tab is finished:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.presence_of_element_located(
                    (By.XPATH, LOCATION_FIELD)
                )
            )
            # [CHECK] The location field is not empty:
            _location_field = _driver.find_element_by_xpath(LOCATION_FIELD)
            assert _location_field.get_attribute('value') != ''

        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't confirm the company details tab \
                location field is present!")
            _driver.quit()
            return
        except AssertionError:
            print("\ASSERTION ERROR: Couldn't verify the location field saved \
                correctly!")
            _driver.quit()
            return

        # [CHECK] Did the website field actually contain a URL?
        if validators.url(self._website_url):
            # Open new tab:
            _driver.execute_script("window.open('');")
            # Switch to new tab:
            _driver.switch_to.window(_driver.window_handles[1])
            # Go to website:
            _driver.get(self._website_url)
