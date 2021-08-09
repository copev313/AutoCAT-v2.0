# AutoCAT v2.0 (Selenium Category Build Automation)
 The automation you need for the jobs your don't! This is an automated workflow project for a simple task that I got tired of doing manually.

## Setup:

 - Inside the repo folder create your virtual environment:

    ```python -m venv env```

 - Activate the virtual environment:

    ```cd env\scripts```

    ```activate```

 - Download the required dependencies:

    ```pip install -r requirements.txt```

 - Copy 'chromedriver.exe' into the 'env\Scripts' folder. Please see the [current releases](https://chromedriver.chromium.org/downloads) for the latest stable version of the Google Chrome webdriver. Remember that in some cases you may need to download the latest version of the driver for the program to run properly.

 - A .env file is required in the repo folder for the program to log into the website. The necessary variables are included in the block below, simply copy/paste, inserting the corresponding values for your account.

    ```
    ADMIN_EMAIL=
    ADMIN_PASSWORD=

    BACKEND_LOGIN_URL=
    BACKEND_LANDING_URL=
    ```

## Usage:
 - To run the program, simply run the following command from the 'AutoCAT' folder:

    ```python app.py```

 - Enter the email address for the vendor you wish to build a category for. Upon submission, the program will automatically run through the process of creating the category for you.
 (It currently needs little to no intervention, but a human eye is recommended to ensure that the category is created properly.)

 - NOTE: The company description will still need copy/pasted into the category description field.

## Videos:

Given that this program is very task specific and requires admin credentials to run through the process, checkout the videos below to see it in action!

https://user-images.githubusercontent.com/59665246/128732593-367dc9b8-65a9-4866-886e-791e21b57278.mp4

https://user-images.githubusercontent.com/59665246/128732573-abfbc293-645d-4c12-95a6-518473157905.mp4


