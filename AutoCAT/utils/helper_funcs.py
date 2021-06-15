'''
helper_funcs.py
------------
    A place for some quality of life functions.
'''
import os
import re

from dotenv import load_dotenv


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
    # [CASE] Country is United States -> Return {city, state abbreviation}:
    if (country == 'United States'):
        state_abbr = _abbreviate_state(state)
        city = city.title()
        return f"{city}, {state_abbr}"

    # [CASE] Country other than US:
    state = state.title()
    return f"{state}, {country}"
