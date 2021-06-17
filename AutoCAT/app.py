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

import procedures.prereview as prereview
import procedures.approval as approval
from utils.helper_funcs import check_email
from utils.webdriver import WebDriver


PROG_NAME = "AutoCAT: The Automation You Need For the Jobs You Don't!"
PROG_DESC = "This program is intended to perform Boutsy category builds."
BG_COLOR_1 = "#828A9E"
BG_COLOR_2 = "#D3D5DB"


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
        choices=["Pre-Review", "Approval"],
        gooey_options={
            "readonly": True,
            "validator": {
                "test": "user_input == 'Pre-Review' or user_input == 'Approval'",
                "message": "Choose a process from the options",
            },
        },
    )

    # Grab user's input:
    args = parser.parse_args()

    """ ***** WINDOW LOGIC *****"""
    print("\nLaunching . . .")
    vendor_email = args.Vendor
    selected_process = args.Process

    # Validation for Vendor Emails:
    if (not validators.email(vendor_email)):
        print("Vendor field may only contain email addresses!")
        raise ValueError

    # [CASE] Run 'Pre-Review' Process:
    if (selected_process == "Pre-Review"):

        # Initialize our WebDriver + Procedures classes:
        driver = WebDriver().initialize_driver()
        pr_procedure = prereview.PreReviewProcess(driver)

        # Log into backend as admin:
        pr_procedure.backend_admin_login()
        # Search for the Vendor's vendor page by email:
        pr_procedure.vendor_email_search(vendor_email)

        # "ACCOUNT DETAILS" TAB -->
        pr_procedure.complete_account_details_tab()
        # "COMPANY ADDRESS" TAB -->
        pr_procedure.complete_company_address_tab()
        # "COMPANY DETAILS" TAB -->
        pr_procedure.complete_company_details_tab()

        # Open Vendor's Site in New Tab:
        pr_procedure.launch_vendor_website()

    # [CASE] Run 'Approval' Process:
    elif (selected_process == "Approval"):
        pass
        # Initialize our WebDriver + Procedures classes:
        # driver = WebDriver().initialize_driver()
        # appr_procedure = approval.ApprovalProcess(driver, vendor_email)

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
