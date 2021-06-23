"""
approval.py
------------
    A class for our step-by-step processes required to create vendor
    categories. This module focuses on procedures necessary to complete the
    approval process.
"""
import os
from time import sleep

from xpaths.prereview_constants import (
    # Backend Admin Login:
    EMAIL_INPUT_FIELD,
    PASSWORD_INPUT_FIELD,
    LOGIN_BUTTON,
    SEARCH_IN_BUTTON,

    # Vendor Email Search:
    SEARCH_IN_USERS_DD,
    SEARCH_BAR_FIELD,

    # Account Details Tab:
    VENDOR_HEADER,

    # Company Details Tab:
    COMPANY_DESC_FIELD,
    CD_UPDATE_BUTTON,
)
from xpaths.approval_constants import (
    # Company Details Tab:
    COMPANY_DESC_FIELD,

    # Coming Soon Page:
    NEW_CATEGORY_BUTTON,
    NEW_CATEGORY_FIELD,
    SAVE_CHANGES_BUTTON,
    FIRST_POS_NAME,
    FIRST_POS_DIV,
    FIRST_CAT_POS_INPUT,

    # Category Page:
    HEADER_BRAND_NAME,
    DESC_FULLSCREEN_BUTTON,
    FULLSCREEN_ALIGN_LEFT,
)
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
    
    # References to the new tabs we will open:
    ComingSoonWindow = None
    CategoryWindow = None


    def __init__(self, driver, email_address):
        self._driver = driver
        self._profile_id: str = ""
        self._vendor_email_address: str = str(email_address).lower()
        self._brand_name: str = ""
        self._company_description: str = ""
        self._category_id: str = ""


    @timer
    def complete_coming_soon_page(self) -> None:
        '''Executes the steps required to complete the Coming Soon page
        portion of a category build.
        '''
        print("\n🐱  Coming Soon Page")
        _driver = self._driver

        coming_soon_url = "{root}?target=categories&id=1845".format(
                            root=os.environ.get("BACKEND_LANDING_URL"))

        # Open a new tab to the 'Coming Soon' page:
        _driver.execute_script("window.open('');")
        ComingSoonWindow = _driver.window_handles[1]
        _driver.switch_to.window(ComingSoonWindow)
        _driver.get(coming_soon_url)

        # [CHECK] Make sure new category button is loaded:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.element_to_be_clickable(
                    (By.XPATH, NEW_CATEGORY_BUTTON)
                )
            )
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't find the NEW_CATEGORY_BUTTON element!")
            _driver.quit()
            return

        # Click 'New category' button:
        _new_cat_btn = _driver.find_element_by_xpath(NEW_CATEGORY_BUTTON)
        _new_cat_btn.click()

        # [CHECK] Make sure new category field is present:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(
                    (By.XPATH, NEW_CATEGORY_FIELD)
                )
            )
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't find the NEW_CATEGORY_FIELD element!")
            _driver.quit()
            return

        # Enter brand name into new category field:
        _new_cat_field = _driver.find_element_by_xpath(NEW_CATEGORY_FIELD)
        _new_cat_field.send_keys(self._brand_name)

        # Hit 'Save changes' button:
        _save_btn = _driver.find_element_by_xpath(SAVE_CHANGES_BUTTON)

        sleep(1)
        _save_btn.click()
        sleep(1)

        # Wait for page to load after adding category:
        wait_for_save(_driver, SAVE_CHANGES_BUTTON)

        # [CHECK] Confirm element exists:
        try:
            WebDriverWait(_driver, self.TIMEOUT).until(
                EC.visibility_of_element_located(
                    (By.XPATH, FIRST_POS_NAME)
                )
            )
            el = _driver.find_element_by_xpath(FIRST_POS_NAME)
            assert el.get_attribute('title') == self._brand_name
        except AssertionError:
            print("\ASSERTION ERROR: Couldn't verify FIRST_POS_NAME was equal to brand_name!")
            _driver.quit()
            return
        except TimeoutError:
            print("\nTIMEOUT ERROR: Couldn't find the FIRST_POS_NAME element!")
            _driver.quit()
            return

        _first_pos_name = _driver.find_element_by_xpath(FIRST_POS_NAME)

        # Form the URL to the category page:
        link_href = _first_pos_name.get_attribute('href')
        splitted = link_href.split('=')
        category_id = splitted[-1]
        self._category_id = "{root}?target=category&id={cat_id}".format(
                            root=os.environ.get("BACKEND_LANDING_URL"),
                            cat_id=category_id)

        # Change category position to 10,000.
        _pos_div = _driver.find_element_by_xpath(FIRST_POS_DIV)
        _pos_div.click()
        sleep(1)
        _pos_input = _driver.find_element_by_xpath(FIRST_CAT_POS_INPUT)
        _pos_input.send_keys('10000')


        # Save changes:
        _save_btn = _driver.find_element_by_xpath(SAVE_CHANGES_BUTTON)
        sleep(1)
        _save_btn.click()
        sleep(1)

        # Wait for page to load after entering new position:
        wait_for_save(_driver, SAVE_CHANGES_BUTTON)


    @timer
    def complete_category_page(self):
        '''Fills in the appropriate fields on the newly created
        category page.
        '''
        print("\n🐱  Complete Category Page")
        _driver = self._driver

        # Open current page to category URL:
        # Open a new tab to the 'Coming Soon' page:
        _driver.execute_script("window.open('');")
        CategoryWindow = _driver.window_handles[2]
        _driver.switch_to.window(CategoryWindow)
        _driver.get(self._category_id)
        
        VendorWindow = _driver.window_handles[0]
        

        # PASTE in description:
        _fullscreen_btn = _driver.find_element_by_xpath(DESC_FULLSCREEN_BUTTON)
        _fullscreen_btn.click()
        sleep(1)
        _align_left_btn = _driver.find_element_by_xpath(FULLSCREEN_ALIGN_LEFT)
        _align_left_btn.click()
        sleep(1)
        _desc_field = _driver.find_elements_by_css_selector("body > p")
        _desc_field.send_keys(self._company_description)

        try:
            assert _desc_field.text == self._company_description
        except AssertionError:
            print("\ASSERTION ERROR: DESCRIPTION_FIELD not equal to _company_description!")
            _driver.quit()
            return

        # Append '-wholesale' to 'Clean URL':
        
        # Click 'Show search box'
        
        # Hit 'Update' button:

        # Close category and coming soon pages:
        

    @timer
    def finish_vendor_page(self):
        '''Finishes the vendor page by pasting in the vendor's brand category
        and changing them to a trusted vendor.
        '''
        pass
