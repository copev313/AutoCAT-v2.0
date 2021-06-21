'''
approval_constants.py
---------
  Storage for our xpaths required to target specific site elements.
'''
__COMING_SOON_ROOT = "/html/body/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/form"
__DESCRIPTION_IFRAME = "/html/body/div[2]/div[2]/div[2]/div[1]/div/div[2]/form/div/fieldset/div/ul/li[6]/div[2]/div/div/div[1]/div/div[3]/iframe"


company_details_tab = {
  "COMPANY_DESC_FIELD":
    "//*[@id='companyfield-32']",
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

  "DESC_FULLSCREEN_BUTTON":
    "//*[@id='fullscreen-1']",

  "FULLSCREEN_ALIGN_LEFT":
    "//*[@id='dropdown-menu-align-1']/div/div/ul/li[1]/a",

}

''' ***** DEFINE CONSTANTS ***** '''

# Company Details Tab:
COMPANY_DESC_FIELD      = company_details_tab["COMPANY_DESC_FIELD"]

# Coming Soon Page:
NEW_CATEGORY_BUTTON     = coming_soon_page["NEW_CATEGORY_BUTTON"]
NEW_CATEGORY_FIELD      = coming_soon_page["NEW_CATEGORY_FIELD"]
SAVE_CHANGES_BUTTON     = coming_soon_page["SAVE_CHANGES_BUTTON"]
FIRST_POS_NAME          = coming_soon_page["FIRST_POS_NAME"]
FIRST_POS_DIV           = coming_soon_page["FIRST_POS_DIV"]
FIRST_CAT_POS_INPUT     = coming_soon_page["FIRST_CAT_POS_INPUT"]

# Category Page:
HEADER_BRAND_NAME       = category_page["HEADER_BRAND_NAME"]
DESC_FULLSCREEN_BUTTON  = category_page["DESC_FULLSCREEN_BUTTON"]
FULLSCREEN_ALIGN_LEFT   = category_page[""] 