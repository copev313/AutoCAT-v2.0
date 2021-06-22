'''
approved_paths.py
---------
  Storage for our xpaths required to target specific site elements for the
  approval process.
'''
__BACKEND_LOGIN_ROOT = "//form[@id='login_form']/table"
__SEARCH_IN_ROOT = "//div[@id='header']/div[3]/div[1]/form/div"


login_portal = {
  "EMAIL_INPUT_FIELD":
    __BACKEND_LOGIN_ROOT + "/tbody[1]/tr[1]/td/input",

  "PASSWORD_INPUT_FIELD":
    __BACKEND_LOGIN_ROOT + "/tbody[1]/tr[2]/td/input",

  "LOGIN_BUTTON":
    __BACKEND_LOGIN_ROOT + "/tbody[2]/tr/td/button",

  "SEARCH_IN_BUTTON":
    __SEARCH_IN_ROOT + "/div[1]/button",
}

vendor_search = {
  "SEARCH_IN_USERS_DD":
    __SEARCH_IN_ROOT + "/div/ul/li[2]/a",

  "SEARCH_BAR_FIELD":
    __SEARCH_IN_ROOT + "/input",
}


''' ***** DEFINE CONSTANTS ***** '''

# Backend Admin Login:
EMAIL_INPUT_FIELD       = login_portal["EMAIL_INPUT_FIELD"]
PASSWORD_INPUT_FIELD    = login_portal["PASSWORD_INPUT_FIELD"]
LOGIN_BUTTON            = login_portal["LOGIN_BUTTON"]
SEARCH_IN_BUTTON        = login_portal["SEARCH_IN_BUTTON"]

# Vendor Email Search
SEARCH_IN_USERS_DD      = vendor_search["SEARCH_IN_USERS_DD"]
SEARCH_BAR_FIELD        = vendor_search["SEARCH_BAR_FIELD"]
