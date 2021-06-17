'''
approval.py
------------
    A class for our step-by-step processes required to create vendor
    categories. This module focuses on procedures necessary to complete the
    approval process.
'''
import os
from time import sleep


from xpaths.approval_constants import (
    # TODO
)
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
#import validators
from utils.helper_funcs import ( timer, wait_for_save )


class ApprovalProcess:

    def __init__(self):
        pass

