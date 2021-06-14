'''
xpaths.py
---------
  Storage for our xpaths required to target specific site elements.
'''

__BACKEND_LOGIN_ROOT = "//form[@id='login_form']/table"
__SEARCH_IN_ROOT = "//div[@id='header']/div[3]/div[1]/form/div"


backend_login_portal = {
  "EMAIL_INPUT_FIELD":
    __BACKEND_LOGIN_ROOT + "/tbody[1]/tr[1]/td/input",

  "PASSWORD_INPUT_FIELD":
    __BACKEND_LOGIN_ROOT + "/tbody[1]/tr[2]/td/input",

  "LOGIN_BUTTON":
    __BACKEND_LOGIN_ROOT + "/tbody[2]/tr/td/button",

  "SEARCH_IN_BUTTON":
    __SEARCH_IN_ROOT + "/div[1]/button",
}

backend_vendor_search = {
  "SEARCH_IN_USERS_DD":
    __SEARCH_IN_ROOT + "/div/ul/li[2]/a",

  "SEARCH_BAR_FIELD":
    __SEARCH_IN_ROOT + "/input",

  "COMPANY_DETAILS_TAB":
    "//div[@id='main']/div[1]/div/div[1]/ul/li[3]/a",
}

account_details_tab = {
  "VENDOR_HEADER":
    "//div[@id='breadcrumb']/ul/li/span",

  "COMPANY_NAME_FIELD":
    "//input[@id='taxid']",
}

''' ***** DEFINE CONSTANTS ***** '''

# Backend Admin Login:
EMAIL_INPUT_FIELD       = backend_login_portal["EMAIL_INPUT_FIELD"]
PASSWORD_INPUT_FIELD    = backend_login_portal["PASSWORD_INPUT_FIELD"]
LOGIN_BUTTON            = backend_login_portal["LOGIN_BUTTON"]
SEARCH_IN_BUTTON        = backend_login_portal["SEARCH_IN_BUTTON"]

# Vendor Email Search
SEARCH_IN_USERS_DD      = backend_vendor_search["SEARCH_IN_USERS_DD"]
SEARCH_BAR_FIELD        = backend_vendor_search["SEARCH_BAR_FIELD"]
COMPANY_DETAILS_TAB     = backend_vendor_search["COMPANY_DETAILS_TAB"]

# Copy/Paste Brand Name:
VENDOR_HEADER           = account_details_tab["VENDOR_HEADER"]
COMPANY_NAME_FIELD      = account_details_tab["COMPANY_NAME_FIELD"]
