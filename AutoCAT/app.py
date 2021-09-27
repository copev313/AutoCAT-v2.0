"""
app.py
------
    Our entry point for getting our Gooey GUI initialized and running.
"""
import sys
from time import time

import validators
from gooey import Gooey, GooeyParser

from procedures.approve_vendor import ApproveVendorProcess
from utils.webdriver import MyWebDriver


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
    # Start timer:
    start = time()

    parser = GooeyParser(prog="AutoCAT", description=f"\n{PROG_DESC}")

    # Accept argument for the vendor's email address:
    parser.add_argument(
        "Vendor", action="store", type=str, help="Vendor's email address:"
    )

    # Grab user's input:
    args = parser.parse_args()
    email_input = args.Vendor

    # [CHECK] Validation for Vendor Emails:
    if (not validators.email(email_input)):
        print("Vendor field may only contain email addresses!")
        raise ValueError

    print("\nLaunching Approval Process . . .")

    # Initialize our WebDriver + Procedures classes:
    driver = MyWebDriver().initialize_driver()
    approve = ApproveVendorProcess(driver)

    # Run all procedures:
    approve.run_all(email_input)
    delta = round(time() - start, 3)
    print(f"\n ---- Completed in {delta} seconds total. ----")


# Run Gooey Program:
if __name__ == "__main__":

    try:
        goopy()

    except KeyboardInterrupt:
        print("CANCELLED!")
        sys.exit(1)

    except ValueError as err:
        print(f"\nVALUE ERROR: {str(err)}")
        sys.exit(1)

    except Exception as err:
        print(f"\nERROR ENCOUNTERED! CLOSING ...\n{err}")
        sys.exit(1)
