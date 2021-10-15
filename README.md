# AutoCAT v2.0 (Selenium Category Build Automation)
 The automation you need for the jobs your don't! This is an automated workflow project for a simple task that I'm tired of doing manually.

## Initial Setup:

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
    ADMIN_EMAIL=(your email)
    ADMIN_PASSWORD=(your password)

    BACKEND_LOGIN_URL=(URL of the backend login page)
    BACKEND_LANDING_URL=(URL of the backend landing page - after log in)

    MONGO_HOST=(MongoDB URI)
    ```

## Usage:
 - To run the program, simply run the following command from the 'AutoCAT' folder:

    ```python app.py```

 - Enter the email address for the vendor you wish to build a category for. Upon submission, the program will automatically run through the process of creating the category for you.
 (It currently needs little to no intervention, but a human eye is recommended to ensure that the category is created properly.)

 - NOTE: The company description will still need copy/pasted into the category description field.

-----

## Convenience Commands:

   *Once initial setup is complete*, and any changes saved, the following command can be ran via the terminal from the repo folder to activate the virtual environment and launch the program:

   ```setup```


   **IMPORTANT:**

   *After the `setup` command is ran*, subsequent launches of the program can be accomplished by using the following command from the 'AutoCAT' directory:

   ```run```

-----

## Additional Notes:

   - Nothing yet...