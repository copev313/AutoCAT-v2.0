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

    # Complete Vendor Account:
    ACCOUNT_HEADER,
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
    COMPANY_DESC_FIELD,
    CD_UPDATE_BUTTON,

    # Complete Coming Soon Page:
    NEW_CATEGORY_BUTTON,
    NEW_CATEGORY_FIELD,
    SAVE_CHANGES_BUTTON,
    FIRST_POS_NAME,
    FIRST_POS_DIV,
    FIRST_CAT_POS_INPUT,

    # Complete Category Page:
    #HEADER_BRAND_NAME,
    #CATEGORY_NAME_FIELD,
    #DESCRIPTION_BOLD_BUTTON,
    CLEAN_URL_FIELD,
    SHOW_SEARCH_BOX_SWITCH,
    #CATEGORY_UPDATE_BUTTON,
)
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.helper_funcs import (
    address_handler,
    check_condition,
    check_is_clickable,
    format_instagram_handle,
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
        
        complete_vendor_account():
            Executes the steps required to finish setting up a vendor's
            account.

        complete_coming_soon_page():
            Completes the Coming Soon page portion of a category build.

        complete_category_page():
            Completes the category page.
    """

    # Wait time (in seconds) for WebDriverWait events:
    TIMEOUT = 5
    # Time (in seconds) for the delay between submission events:
    SUBMISSION_DELAY = 0.5

    # References to the new tabs we will open:
    ComingSoonWindow = None
    CategoryWindow = None


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

        # [CHECK] Confirm that we successfully logged in:
        check_condition(_driver, SEARCH_IN_BUTTON)

        # [CHECK] The current page is the backend landing page:
        assert _driver.current_url == os.environ.get("BACKEND_LANDING_URL")


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
        check_is_clickable(_driver, SEARCH_IN_BUTTON)

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


    @timer
    def complete_vendor_account(self) -> None:
        '''Executes the steps required to finish setting up a vendor's account
        by completing / editting fields found in the different tabs.'''
        print("\n🐱  Complete Vendor Account")
        _driver = self._driver
        
        ''' * * * * * Grab Info from 'Account Details' tab * * * * * '''
        
        # [CHECK] Confirm we successfully loaded the page:
        check_condition(_driver, ACCOUNT_HEADER)
        
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

        ''' * * * * * Complete 'Company Address' tab * * * * * '''

        # Form the URL for the Company Address tab:
        address_tab_url = "{root}?target=companyAddress&profile_id={id}".format(
                            root=os.environ.get("BACKEND_LANDING_URL"),
                            id=self._profile_id)

        # Got to our tab via URL:
        _driver.get(address_tab_url)
        
        # [CHECK] Confirm we successfully found our vendor page:
        check_condition(_driver, QUESTIONS_EMAIL_FIELD)

        # PASTE email address into 'Product questions e-mail' field:
        _email_field =  _driver.find_element_by_xpath(QUESTIONS_EMAIL_FIELD)
        _email_field.clear()
        _email_field.send_keys(self._vendor_email_address)

        # Submit:
        sleep(self.SUBMISSION_DELAY)
        _email_field.send_keys(Keys.RETURN)
        sleep(self.SUBMISSION_DELAY)

        # Wait for page to indicate it successfully saved our input:
        wait_for_save(_driver, CA_SUBMIT_BUTTON)

        # Copy value in the 'Country' dropdown:
        _country_dd = _driver.find_element_by_xpath(COUNTRY_DD)
        _country_selected = _country_dd.find_element_by_xpath("//*[@selected='selected']")
        self._company_country = _country_selected.text

        # Copy value the 'State' field:
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

        # Copy value in the 'City' field:
        _city_field = _driver.find_element_by_xpath(CITY_FIELD)
        self._company_city = _city_field.get_attribute('value')
        print("City: " + self._company_city)
        print("State: " + self._company_state)
        print("Country: " + self._company_country)


        ''' * * * * * Complete 'Company Details' tab * * * * * '''

        # Form the URL for the Company Details tab:
        company_details_tab_url = "{root}?target=vendor&profile_id={id}".format(
                                    root=os.environ.get("BACKEND_LANDING_URL"),
                                    id=self._profile_id)

        # Go to our tab via URL:
        _driver.get(company_details_tab_url)
        
        # [CHECK] Next page successfully Loaded:
        check_condition(_driver, LOCATION_FIELD)

        # Handle the trusted dropdown:
        _trusted_dd = _driver.find_element_by_xpath(TRUSTED_DD)
        _trusted_dd.click()
        _trusted_option = _trusted_dd.find_element_by_xpath("option[@value='1']")
        _trusted_option.click()

        # Handle the location field:
        _location_field = _driver.find_element_by_xpath(LOCATION_FIELD)
        location = address_handler(
            country=self._company_country,
            state=self._company_state,
            city=self._company_city
        )
        print("Address:  " + location)  # debugs!
        # Replace location imformation:
        _location_field.clear()
        _location_field.send_keys(location)

        # Store website URL so we can launch it later:
        _website_field = _driver.find_element_by_xpath(WEBSITE_FIELD)
        self._website_url =  _website_field.get_attribute('value')
        print(f"Site URL:  {self._website_url}")

        # Copy description from 'Company Description':
        _descr_field = _driver.find_element_by_xpath(COMPANY_DESC_FIELD)
        self._company_description = _descr_field.text

        # Handle formatting & storing Instagram handle (if applicable):
        _instagram_field = _driver.find_element_by_xpath(INSTAGRAM_FIELD)
        gram_val = _instagram_field.get_attribute('value')
        instagram = format_instagram_handle(gram_val)
        print(f"Instagram:  {instagram}")

        # Store the Instagram handle:
        self._instagram_handle = instagram

        # Submit:
        sleep(self.SUBMISSION_DELAY)
        _instagram_field.send_keys(Keys.RETURN)
        sleep(self.SUBMISSION_DELAY)

        # Wait for the page to successfully save our location data:
        wait_for_save(_driver, CD_UPDATE_BUTTON)


    @timer
    def complete_coming_soon_page(self) -> None:
        '''Completes the Coming Soon page portion of a category build.'''
        print("\n🐱  Completing Coming Soon Page")
        _driver = self._driver

        coming_soon_url = "{root}?target=categories&id=1845".format(
                            root=os.environ.get("BACKEND_LANDING_URL"))

        # Open a new tab to the 'Coming Soon' page:
        _driver.execute_script("window.open('');")
        ComingSoonWindow = _driver.window_handles[1]
        _driver.switch_to.window(ComingSoonWindow)
        _driver.get(coming_soon_url)

        # [CHECK] Make sure new category button is loaded:
        check_is_clickable(_driver, NEW_CATEGORY_BUTTON)

        # Click 'New category' button:
        _new_cat_btn = _driver.find_element_by_xpath(NEW_CATEGORY_BUTTON)
        _new_cat_btn.click()

        # [CHECK] Make sure new category field is present:
        check_condition(_driver, NEW_CATEGORY_FIELD)

        # Enter brand name into new category field:
        _new_cat_field = _driver.find_element_by_xpath(NEW_CATEGORY_FIELD)
        _new_cat_field.send_keys(self._brand_name)

        # Hit 'Save changes' button:
        _save_btn = _driver.find_element_by_xpath(SAVE_CHANGES_BUTTON)
        sleep(self.SUBMISSION_DELAY)
        _save_btn.click()
        sleep(self.SUBMISSION_DELAY)

        # Wait for page to load after adding category:
        wait_for_save(_driver, SAVE_CHANGES_BUTTON)

        # [CHECK] Confirm element exists:
        check_condition(_driver, FIRST_POS_NAME)
        el = _driver.find_element_by_xpath(FIRST_POS_NAME)
        assert el.get_attribute('title') == self._brand_name

        _first_pos_bname = _driver.find_element_by_xpath(FIRST_POS_NAME)

        # Store the category_id:
        link_href = _first_pos_bname.get_attribute('href')
        splitted = link_href.split('=')
        self._category_id = splitted[-1]

        # Change category position to 10,000.
        _pos_div = _driver.find_element_by_xpath(FIRST_POS_DIV)
        _pos_div.click()
        _pos_input = _driver.find_element_by_xpath(FIRST_CAT_POS_INPUT)
        _pos_input.send_keys('10000')

        # Save changes:
        _save_btn = _driver.find_element_by_xpath(SAVE_CHANGES_BUTTON)
        sleep(self.SUBMISSION_DELAY)
        _save_btn.click()
        sleep(self.SUBMISSION_DELAY)

        # Wait for page to load after entering new position:
        wait_for_save(_driver, SAVE_CHANGES_BUTTON)


    @timer
    def complete_category_page(self):
        '''Completes the category page.'''
        print("\n🐱  Completing Category Page")
        _driver = self._driver

        # Form the URL to the category page:
        category_page_url = "{root}?target=category&id={cat_id}".format(
                            root=os.environ.get("BACKEND_LANDING_URL"),
                            cat_id=self._category_id)

        # Open a new tab to the newly created category page:
        _driver.execute_script("window.open('');")
        CategoryWindow = _driver.window_handles[2]
        _driver.switch_to.window(CategoryWindow)
        _driver.get(category_page_url)

        # [CHECK] Category Page Successfully Loaded:
        check_condition(_driver, CLEAN_URL_FIELD)

        '''
        # (1) Fill in description:
        print(f"\nDescription: {self._company_description}") "body > p"
        desc_js = "let desc = document.querySelector('body').querySelector('p'); \
                    desc.innerText = \'{}\';".format(self._company_description)
        _driver.execute_script(desc_js)
        '''
        # (2) Complete the Clean URL field:
        _clean_url_field = _driver.find_element_by_xpath(CLEAN_URL_FIELD)
        clean_value = _clean_url_field.get_attribute('value')

        # [CASE] Current slug ends in '-' already:
        if (clean_value[-1] == '-'):
            clean_value = clean_value[ :-1]
        new_val = f"{clean_value}-wholesale"
        print(f"NEW URL SLUG: {new_val}")   # debugs!

        _clean_url_field.clear()
        _clean_url_field.send_keys(new_val)

        # (3) Click 'Show search box' switch -> change to 'YES':
        _show_search_switch = _driver.find_element_by_xpath(SHOW_SEARCH_BOX_SWITCH)
        checked = _show_search_switch.get_attribute('checked')
        # [CASE] 'Show search box' switch is not set to 'YES':
        if not checked:
            js_script = ("const switchElement = document.getElementById('showsearchbox'); " 
                         "let checkedAttr = document.createAttribute('checked'); "
                         "checkedAttr.value = 'checked'; "
                         "switchElement.setAttributeNode(checkedAttr); ")
            _driver.execute_script(js_script)
            print("Checked 'Show search box' successfully! :)")
        
        _clean_url_field = _driver.find_element_by_xpath(CLEAN_URL_FIELD)
        _clean_url_field.send_keys(Keys.RETURN)
        sleep(1)
