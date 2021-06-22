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

approve_vendor = {
  "ACCOUNT_HEADER":
    "//*[@id='breadcrumb']/ul/li/span",
  
  "COMPANY_NAME_FIELD":
    "//input[@id='taxid']",
  
  "AD_UPDATE_BUTTON":
    "//button[@type='submit']",
    
  "APPROVE_VENDOR_BUTTON":
    "/html/body/div[2]/div[2]/div[2]/div[1]/div/div[2]/form/div/div/div/div[2]/button",
}

complete_vendor_account = {
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
    
  "CA_SUBMIT_BUTTON":
    "//button[@type='submit']",


  "TRUSTED_DD":
    "//*[@id='istrustedvendor']",
  
  "LOCATION_FIELD":
    "//*[@id='vendorlocation']",

  "WEBSITE_FIELD":
    "//*[@id='companyfield-18']",

  "COMPANY_DESC_FIELD":
    "//*[@id='companyfield-32']",

  "INSTAGRAM_FIELD":
    "//*[@id='companyfield-33']",

  "CD_UPDATE_BUTTON":
    "//button[@type='submit']",
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

# Approval Confirmation:
ACCOUNT_HEADER          = approve_vendor["ACCOUNT_HEADER"]
COMPANY_NAME_FIELD      = approve_vendor["COMPANY_NAME_FIELD"]
AD_UPDATE_BUTTON        = approve_vendor["AD_UPDATE_BUTTON"]
APPROVE_VENDOR_BUTTON   = approve_vendor["APPROVE_VENDOR_BUTTON"]

# Complete Vendor Account:
QUESTIONS_EMAIL_FIELD   = complete_vendor_account["QUESTIONS_EMAIL_FIELD"]
COUNTRY_DD              = complete_vendor_account["COUNTRY_DD"]
STATE_AS_DD             = complete_vendor_account["STATE_AS_DD"]
STATE_AS_FIELD          = complete_vendor_account["STATE_AS_FIELD"]
CITY_FIELD              = complete_vendor_account["CITY_FIELD"]
CA_SUBMIT_BUTTON        = complete_vendor_account["CA_SUBMIT_BUTTON"]

TRUSTED_DD              = complete_vendor_account["TRUSTED_DD"]
LOCATION_FIELD          = complete_vendor_account["LOCATION_FIELD"]
WEBSITE_FIELD           = complete_vendor_account["WEBSITE_FIELD"]
INSTAGRAM_FIELD         = complete_vendor_account["INSTAGRAM_FIELD"]
CD_UPDATE_BUTTON        = complete_vendor_account["CD_UPDATE_BUTTON"]
