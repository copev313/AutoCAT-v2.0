# AutoCAT v2.0 (Selenium Category Build Automation)
 The automation you need for the jobs your don't! This is an automated workflow project for a simple task that I'm tired of doing manually.

### Setup:

 - Inside the repo folder create your virtual environment:

    ```python -m venv env```

 - Download the required dependencies:

    ```pip install -r requirements.txt```

 - Copy 'chromedriver.exe' into the 'env\Scripts' folder. Please see the [current releases](https://chromedriver.chromium.org/downloads) for the latest stable version of the Google Chrome webdriver.

 - A .env file is required in the repo folder for the program to run properly. The necessary variables are included in the block below, simply copy/paste.

    ```
    ADMIN_EMAIL=
    ADMIN_PASSWORD=

    BACKEND_LOGIN_URL=
    BACKEND_LANDING_URL=
    ```

### Notes:

 - TODO: Handle a comma seperated list of email addresses so that the process can be repeated for multiple accounts at once.
