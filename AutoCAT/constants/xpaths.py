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

  # may not need this xpath/element
  "COMPANY_DETAILS_TAB":
    "//div[@id='main']/div[1]/div/div[1]/ul/li[3]/a",
}

account_details_tab = {
  "VENDOR_HEADER":
    "//*[@id='breadcrumb']/ul/li/span",

  "COMPANY_NAME_FIELD":
    "//input[@id='taxid']",
}

company_address_tab = {
  "QUESTIONS_EMAIL_FIELD":
    "//input[@id='product-questions-admin-email']",

  "COUNTRY_DD":
    "//select[@id='location-country']",

  "STATE_AS_DD":
    "//select[@id='location-state']",

  "STATE_AS_FIELD":
    "//input[@id='location-custom-state']",

  "CITY_FIELD":
    "//*[@id='location-city']",
}

company_details_tab = {
  "LOCATION_FIELD":
    "//*[@id='vendorlocation']",

  "WEBSITE_FIELD":
    "//*[@id='companyfield-18']",

  "COMPANY_DESC_FIELD":
    "//*[@id='companyfield-32']",

  "INSTAGRAM_FIELD":
    "//*[@id='companyfield-33']",
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

# Account Details Tab:
VENDOR_HEADER           = account_details_tab["VENDOR_HEADER"]
COMPANY_NAME_FIELD      = account_details_tab["COMPANY_NAME_FIELD"]

# Company Address Tab:
QUESTIONS_EMAIL_FIELD   = company_address_tab["QUESTIONS_EMAIL_FIELD"]
COUNTRY_DD              = company_address_tab["COUNTRY_DD"]
STATE_AS_DD             = company_address_tab["STATE_AS_DD"]
STATE_AS_FIELD          = company_address_tab["STATE_AS_FIELD"]
CITY_FIELD              = company_address_tab["CITY_FIELD"]

# Company Details Tab:
LOCATION_FIELD          = company_details_tab["LOCATION_FIELD"]
WEBSITE_FIELD           = company_details_tab["WEBSITE_FIELD"]
COMPANY_DESC_FIELD      = company_details_tab["COMPANY_DESC_FIELD"]
INSTAGRAM_FIELD         = company_details_tab["INSTAGRAM_FIELD"]
