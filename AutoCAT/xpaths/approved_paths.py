'''
approved_paths.py
---------
  Storage for our xpaths required to target specific site elements for the
  approval process.
'''
__BACKEND_LOGIN_ROOT = "//form[@id='login_form']/table"
__SEARCH_IN_ROOT = "//div[@id='header']/div[3]/div[1]/form/div"
__COMING_SOON_ROOT = "/html/body/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/form"
__DESCRIPTION_IFRAME = "/html/body/div[2]/div[2]/div[2]/div[1]/div/div[2]/form/div/fieldset/div/ul/li[6]/div[2]/div/div/div[1]/div/div[3]/iframe"


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

complete_vendor_account = {
  "ACCOUNT_HEADER":
    "//*[@id='breadcrumb']/ul/li/span",

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

coming_soon_page = {
  "NEW_CATEGORY_BUTTON":
    __COMING_SOON_ROOT + "/div[1]/div[2]/div/button",

  "NEW_CATEGORY_FIELD":
    "//*[@id='new-n1-name']",

  "SAVE_CHANGES_BUTTON":
    __COMING_SOON_ROOT + "/div[2]/div/div/button",

  "FIRST_POS_NAME":
    __COMING_SOON_ROOT + "/div[1]/div[3]/table/tbody[2]/tr[1]/td[3]/div/div[1]/span/a",

  "FIRST_POS_DIV":
    __COMING_SOON_ROOT + "/div[1]/div[3]/table/tbody[2]/tr[1]/td[1]/div/div[1]/div/div[1]",

  "FIRST_CAT_POS_INPUT":
    __COMING_SOON_ROOT + "/div[1]/div[3]/table/tbody[2]/tr[1]/td[1]/div/div[1]/div/div[2]/div/div/div/span/input",
}

category_page = {
  "HEADER_BRAND_NAME":
    "/html/body/div[2]/div[2]/div[2]/h1/div/ul/li[3]/span",

  "CLEAN_URL_FIELD":
    "//*[@id='cleanurl']",

  "DESC_FULLSCREEN_BUTTON":
    "//*[@id='fullscreen-1']",

  "FULLSCREEN_ALIGN_LEFT":
    "//*[@id='dropdown-menu-align-1']/div/div/ul/li[1]/a",

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

# Complete Vendor Account:
ACCOUNT_HEADER          = complete_vendor_account["ACCOUNT_HEADER"]
QUESTIONS_EMAIL_FIELD   = complete_vendor_account["QUESTIONS_EMAIL_FIELD"]
COUNTRY_DD              = complete_vendor_account["COUNTRY_DD"]
STATE_AS_DD             = complete_vendor_account["STATE_AS_DD"]
STATE_AS_FIELD          = complete_vendor_account["STATE_AS_FIELD"]
CITY_FIELD              = complete_vendor_account["CITY_FIELD"]
CA_SUBMIT_BUTTON        = complete_vendor_account["CA_SUBMIT_BUTTON"]

TRUSTED_DD              = complete_vendor_account["TRUSTED_DD"]
LOCATION_FIELD          = complete_vendor_account["LOCATION_FIELD"]
WEBSITE_FIELD           = complete_vendor_account["WEBSITE_FIELD"]
COMPANY_DESC_FIELD      = complete_vendor_account["COMPANY_DESC_FIELD"]
INSTAGRAM_FIELD         = complete_vendor_account["INSTAGRAM_FIELD"]
CD_UPDATE_BUTTON        = complete_vendor_account["CD_UPDATE_BUTTON"]

# Coming Soon Page:
NEW_CATEGORY_BUTTON     = coming_soon_page["NEW_CATEGORY_BUTTON"]
NEW_CATEGORY_FIELD      = coming_soon_page["NEW_CATEGORY_FIELD"]
SAVE_CHANGES_BUTTON     = coming_soon_page["SAVE_CHANGES_BUTTON"]
FIRST_POS_NAME          = coming_soon_page["FIRST_POS_NAME"]
FIRST_POS_DIV           = coming_soon_page["FIRST_POS_DIV"]
FIRST_CAT_POS_INPUT     = coming_soon_page["FIRST_CAT_POS_INPUT"]

# Category Page:
HEADER_BRAND_NAME       = category_page["HEADER_BRAND_NAME"]
CLEAN_URL_FIELD         = category_page["CLEAN_URL_FIELD"]
