"""
app.py
------
    Our entry point for getting our Gooey GUI initialized and running.
"""
import os
import sys
from time import time

import validators
from gooey import Gooey, GooeyParser

from procedures.approve_vendor import ApproveVendorProcess
#import procedures.decline_vendor as DeclineVendorProcess
from utils.helper_funcs import check_email
from utils.webdriver import WebDriver


PROG_NAME = "AutoCAT: The Automation You Need For the Jobs You Don't!"
PROG_DESC = "This program is intended to perform Boutsy category builds."
BG_COLOR_1 = "#B5BBC9"
BG_COLOR_2 = "#E3E4E6"


@Gooey(
    program_name=PROG_NAME,
    image_dir=".\images",
    header_bg_color=BG_COLOR_1,
    body_bg_color=BG_COLOR_2,
    footer_bg_color=BG_COLOR_1,
    richtext_controls=True,
    default_size=(550, 450),
    required_cols=1,
)
def goopy():
    """
    The main function responsible for parsing our arguments and building our
    Gooey GUI.
    """
    parser = GooeyParser(prog="AutoCAT", description="\n" + PROG_DESC)

    # Vendor Email field:
    parser.add_argument(
        "Vendor", action="store", type=str, help="Vendor's email address:"
    )

    parser.add_argument(
        "Process",
        metavar="Choose Process",
        widget="Dropdown",
        choices=["Approved", "Declined"],
        gooey_options={
            "readonly": True,
            "validator": {
                "test": "user_input == 'Approved' or user_input == 'Declined'",
                "message": "Choose a process from the options",
            },
        },
    )

    # Grab user's input:
    args = parser.parse_args()

    """ ***** WINDOW LOGIC *****"""
    '''copev313@gmail.com'''
    email_input = args.Vendor
    process_input = args.Process

    # Validation for Vendor Emails:
    if (not validators.email(email_input)):
        print("Vendor field may only contain email addresses!")
        raise ValueError

    if (process_input == "Approved"):
        print("\nLaunching Approval Process . . .")

        # Initialize our WebDriver + Procedures classes:
        driver = WebDriver().initialize_driver()
        approve = ApproveVendorProcess(driver)

        # Log into backend as admin:
        approve.backend_admin_login()
        # Search for the vendor page by email:
        approve.vendor_email_search(email_input)
        # Save company name field + hit 'Approve vendor' button:
        approve.approve_vendor_button()
        # Fill out the rest of the account info (copy/paste):
        approve.complete_vendor_account()


    elif (process_input == "Denied"):
        print("\nLaunching Decline Process . . .")
        print("\nCOMING SOON!")

    else:
        raise ValueError("Somehow an invalid process option was selected!")


# Run Gooey Program:
if __name__ == "__main__":

    try:
        start = time()
        goopy()
        print(
            f"\n ----- Completed in { round(time() - start, 3) } seconds total. -----"
        )

    except KeyboardInterrupt:
        print("CANCELLED!")
        sys.exit(1)
    except ValueError as err:
        print(f"\nVALUE ERROR: {str(err)}")
        sys.exit(1)
    except Exception as err:
        print(f"\nERROR ENCOUNTERED! CLOSING ...\n{err}")
        sys.exit(1)
