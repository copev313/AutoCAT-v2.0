'''
app.py
------
    Our entry point for getting our Gooey GUI initialized and running.
'''
import sys
import time

from gooey import Gooey, GooeyParser

from procedures.pre_decision import Procedure
from utils.helper_funcs import check_email
from utils.webdriver import WebDriver


@Gooey(program_name="AutoCAT: The Automation You Need For the Jobs You Don't!",
       description="\nThis program is intended for pre-decision Boutsy" \
        " category builds.",
       default_size=(550, 450),
       required_cols=1)
def goopy():
    '''
    The main function responsible for parsing our arguments and building our
    Gooey GUI.
    '''
    parser = GooeyParser(prog="AutoCAT",
                         description="\nThis program is intended for pre-decision Boutsy" \
                            " category builds.")

    parser.add_argument("Vendor",
                        action="store",
                        type=str,
                        help="Vendor's email address:")

    parser.add_argument("--Headless",
                        action="store_true",
                        help=" Run process in headless mode?")

    args = parser.parse_args()

    print("\n🐱  AUTOCAT >>> Launching . . .")
     # Validation for Vendor's Email:
    if (not check_email(args.Vendor)):
        print("Vendor field requires an email address!")
        raise ValueError
    
    # Initialize our WebDriver + Procedures classes:
    driver = WebDriver().initialize_driver()
    procedure = Procedure(driver)

    

    # Headless Handler:
    if (bool(args.Headless)):
        print("\nRunning in headless mode!")
        # TODO: Implement this option later . . .


    ''' ***** BEGIN CAT BUILD PROCESS ***** '''
    # Log into backend as admin:
    procedure.backend_admin_login()

    # Search for the Vendor's vendor page by email:
    procedure.vendor_email_search(args.Vendor)

    # ACCOUNT DETAILS TAB -->
    procedure.complete_account_details_tab()

    # COMPANY ADDRESS TAB -->
    procedure.complete_company_address_tab()

    # COMPANY DETAILS TAB -->
    procedure.complete_company_details_tab()

    ''' ***** END CAT BUILD PROCESS ***** '''


# Run Gooey Program:
if __name__ == '__main__':

    try:
        start_time = time.time()
        goopy()
        interval = time.time() - start_time
        print(f"\n ---------- Completed in { round(interval, 3) } seconds total. ---------- ")

    except KeyboardInterrupt:
        print("TEST CANCELLED!")
        driver.close()
        sys.exit(1)

    except ValueError as err:
        print(str(err))
        driver.close()
        sys.exit(1)

    except Exception as err:
        print(f"\nERROR ENCOUNTERED! CLOSING ...\n{err}")
        sys.exit(1)
