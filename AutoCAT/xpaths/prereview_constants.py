'''
prereview_constants.py
---------
  Storage for our xpaths required to target specific site elements.
'''

account_details_tab = {
  "VENDOR_HEADER":
    "//*[@id='breadcrumb']/ul/li/span",

  "COMPANY_NAME_FIELD":
    "//input[@id='taxid']",
  
  "AD_UPDATE_BUTTON":
    "//button[@type='submit']",
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
    
  "CA_SUBMIT_BUTTON":
    "//button[@type='submit']"
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
  
  "CD_UPDATE_BUTTON":
    "//button[@type='submit']",
}

''' ***** DEFINE CONSTANTS ***** '''

# Account Details Tab:
VENDOR_HEADER           = account_details_tab["VENDOR_HEADER"]
COMPANY_NAME_FIELD      = account_details_tab["COMPANY_NAME_FIELD"]
AD_UPDATE_BUTTON        = account_details_tab["AD_UPDATE_BUTTON"]

# Company Address Tab:
QUESTIONS_EMAIL_FIELD   = company_address_tab["QUESTIONS_EMAIL_FIELD"]
COUNTRY_DD              = company_address_tab["COUNTRY_DD"]
STATE_AS_DD             = company_address_tab["STATE_AS_DD"]
STATE_AS_FIELD          = company_address_tab["STATE_AS_FIELD"]
CITY_FIELD              = company_address_tab["CITY_FIELD"]
CA_SUBMIT_BUTTON        = company_address_tab["CA_SUBMIT_BUTTON"]

# Company Details Tab:
LOCATION_FIELD          = company_details_tab["LOCATION_FIELD"]
WEBSITE_FIELD           = company_details_tab["WEBSITE_FIELD"]
COMPANY_DESC_FIELD      = company_details_tab["COMPANY_DESC_FIELD"]
INSTAGRAM_FIELD         = company_details_tab["INSTAGRAM_FIELD"]
CD_UPDATE_BUTTON        = company_details_tab["CD_UPDATE_BUTTON"]
