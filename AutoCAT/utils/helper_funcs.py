'''
helper_funcs.py
------------
    A place for some quality of life functions.
'''
import os
import re
import time

from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located,
    element_to_be_clickable,
)
from selenium.webdriver.common.by import By


def timer(func):
    '''A decorator function to measure execute time of functions.'''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f"(Completed '{func.__name__}' in {round(finish - start, 2)} sec.)")
        return result
    return wrapper


def print_admin_info() -> None:
    '''Prints the account info for the admin user.'''
    load_dotenv()
    email = os.environ.get("ADMIN_EMAIL")
    pswd = "{}{}{}".format(os.environ.get('ADMIN_PASSWORD')[0],
                           '*' * len(os.environ.get('ADMIN_PASSWORD')),
                            os.environ.get('ADMIN_PASSWORD')[-1])

    print(f"ADMIN_EMAIL: {email} \nADMIN_PASSWORD: {pswd}")


def check_email(email_address: str) -> bool:
    '''Validates that the given string is an email address.'''
    regex = "^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
    return True if re.search(regex, email_address) else False


def _element_has_class(element_obj, class_name: str) -> bool:
    '''Returns a boolean of whether a web element contains a specific class name.'''
    classes = element_obj.get_attribute('class')
    for cls in classes.split(' '):
        if (cls == class_name):
            return True
    return False


def wait_for_save(driver, xpath: str, cls_name: str = 'disabled') -> None:
    '''Pauses program to wait for data to be saved successfully. Waits for
    the submit/update button to be disabled after inputting data and submitting.
    '''
    # Wait for the element to have the class 'classy':
    _d = driver
    elem = _d.find_element_by_xpath(xpath)
    classy = _element_has_class(elem, cls_name)
    # While the element doesn't have that class, pause then try again:
    while not classy:
        # Wait a sec:
        time.sleep(1)
        elem = _d.find_element_by_xpath(xpath)
        classy = _element_has_class(elem, cls_name)
    return None


def check_condition(driver, xpath: str, timeout: int = 5) -> None:
    '''Checks the visibility of a web element located at a given xpath. This
    function can be used to confirm the correct webpage has been loaded.'''
    _driver = driver
    try:
        WebDriverWait(_driver, timeout).until(
            visibility_of_element_located(
                (By.XPATH, xpath)
            )
        )
    except TimeoutError:
        print("\nTIMEOUT ERROR in check_condition!")
        _driver.quit()
        return
    except Exception as err:
        print(f"\nEXCEPTION OCCURED in check_condition: {err}")
        _driver.quit()
        return


def check_is_clickable(driver, xpath: str, timeout: int = 5) -> None:
    '''Checks if a web element is clickable at a given xpath.'''
    _driver = driver
    try:
        WebDriverWait(_driver, timeout).until(
            element_to_be_clickable(
                (By.XPATH, xpath)
            )
        )
    except TimeoutError:
        print("\nTIMEOUT ERROR in check_is_clickable!")
        _driver.quit()
        return
    except Exception as err:
        print(f"\nEXCEPTION OCCURED in check_is_clickable: {err}")
        _driver.quit()
        return


def _abbreviate_state(state: str) -> str:
    '''Given a state of the US, returns the appropriate abbreviation.

        * Used as a part of address_handler function. * 
    '''
    abbr_dict = {
        'ALABAMA': 'AL',
        'ALASKA': 'AK',
        'AMERICAN SAMOA': 'AS',
        'ARIZONA': 'AZ',
        'ARKANSAS':	'AR',
        'CALIFORNIA': 'CA',
        'COLORADO':	'CO',
        'CONNECTICUT': 'CT',
        'DELAWARE':	'DE',
        'DISTRICT OF COLUMBIA':	'DC',
        'FLORIDA': 'FL',
        'GEORGIA': 'GA',
        'GUAM':	'GU',
        'HAWAII': 'HI',
        'IDAHO': 'ID',
        'ILLINOIS': 'IL',
        'INDIANA': 'IN',
        'IOWA': 'IA',
        'KANSAS': 'KS',
        'KENTUCKY':	'KY',
        'LOUISIANA': 'LA',
        'MAINE': 'ME',
        'MARYLAND': 'MD',
        'MASSACHUSETTS': 'MA',
        'MICHIGAN':	'MI',
        'MINNESOTA': 'MN',
        'MISSISSIPPI': 'MS',
        'MISSOURI':	'MO',
        'MONTANA': 'MT',
        'NEBRASKA': 'NE',
        'NEVADA': 'NV',
        'NEW HAMPSHIRE': 'NH',
        'NEW JERSEY': 'NJ',
        'NEW MEXICO': 'NM',
        'NEW YORK':	'NY',
        'NORTH CAROLINA': 'NC',
        'NORTH DAKOTA':	'ND',
        'OHIO':	'OH',
        'OKLAHOMA':	'OK',
        'OREGON': 'OR',
        'PENNSYLVANIA':	'PA',
        'PUERTO RICO': 'PR',
        'RHODE ISLAND':	'RI',
        'SOUTH CAROLINA': 'SC',
        'SOUTH DAKOTA':	'SD',
        'TENNESSEE': 'TN',
        'TEXAS': 'TX',
        'UTAH':	'UT',
        'VERMONT': 'VT',
        'VIRGINIA':	'VA',
        'VIRGIN ISLANDS': 'VI',
        'WASHINGTON': 'WA',
        'WEST VIRGINIA': 'WV',
        'WISCONSIN': 'WI',
        'WYOMING': 'WY',
    }

    state = state.upper().strip()
    if state in abbr_dict.keys():
        return abbr_dict[state]
    else:
        return state.title()


def address_handler(country: str = '', state: str = '', city: str ='') -> str:
    '''Returns the appropriately formatted address based on the given
    country.'''
    # [CASE] Country is United States -> Return {city, state abbreviation}:
    if (country == 'United States'):
        state_abbr = _abbreviate_state(state)
        city = city.title()
        return f"{city}, {state_abbr}"

    # [CASE] Country other than US:
    else:
        if state:
            state = state.title()
            return f"{state}, {country}"
        elif city:
            return f"{city}, {country}"
        else:
            return country


def format_instagram_handle(handle: str):
    if handle:
        # [CASE] Contains '@' -> Remove @:
        if('@' in handle):
            handle = handle.replace('@', '')
        return handle.lower()

    return None


def minimum_order_amount_handler(inner_text: str) -> int:
    if inner_text:
        if (inner_text.contains('No minimum')):
            return None
        elif (inner_text.contains('$50')):
            return 50
        elif (inner_text.contains('$100')):
            return 100
        elif (inner_text.contains('$250')):
            return 250
    return None
