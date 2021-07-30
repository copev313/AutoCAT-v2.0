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
    default_size=(525, 375),
    required_cols=1,
)
def goopy():
    """The main function responsible for parsing our arguments and building our
    Gooey GUI.
    """
    parser = GooeyParser(prog="AutoCAT", description=f"\n{PROG_DESC}")

    # Vendor Email field:
    parser.add_argument(
        "Vendor", action="store", type=str, help="Vendor's email address:"
    )

    # Grab user's input:
    args = parser.parse_args()
    email_input = args.Vendor

    # Validation for Vendor Emails:
    if (not validators.email(email_input)):
        print("Vendor field may only contain email addresses!")
        raise ValueError

    print("\nLaunching Approval Process . . .")

    # Initialize our WebDriver + Procedures classes:
    driver = WebDriver().initialize_driver()
    approve = ApproveVendorProcess(driver)

    # Log into backend as admin:
    approve.backend_admin_login()
    # Search for the vendor page by email:
    approve.vendor_email_search(email_input)
    # Copy/Paste account info:
    approve.complete_vendor_account()
    # Complete Coming Soon Page:
    approve.complete_coming_soon_page()
    # Complete the Category Page:
    approve.complete_category_page()
    # Clean up:
    approve.clean_up()
    # Add Vendor Stats to MongoDB:
    approve.save_stats_to_db()


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
