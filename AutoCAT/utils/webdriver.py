'''
webdriver.py
------------
    Class for building our Selenium Chrome webdriver.

'''
from selenium import webdriver


# Our default & experimental option flags for configuring our Chrome webdriver:
DEFAULT_FLAGS = ["--start-maximized",
                 "--incognito",
                 "--disable-notifcations",
                 "--disable-extensions"]

EXP_OPTS = ["enable-automation",
            "enable-logging"]


class WebDriver:
    '''A class for the Selenium Chrome webdriver.

    This object encapsulates methods for building a Chrome options object and
    initializing a Selenium automated browser/driver object.

    Attributes
    ----------
        flags : list [str], optional
            A list of flags that enable special options and functionality in
            the Selenium Chrome browser. (default DEFAULT_FLAGS)

        exp_opts: list [str], optional
            A list of experimental options that can be accepted by the Chrome
            Selenium webdriver. (default EXP_OPTS)

    Properties
    ----------
        flags : list [str]
            Returns the current flags of the given instance of WebBrowser.

        exp_opts : list [str]
            Returns the experimental flags of the given instance of WebBrowser.

        headless : bool
            Returns whether headless mode is enabled for the given instance of
            WebBrowser.

    Methods
    -------
        initialize_driver(headless=False):
            Initializes the Selenium webdriver object.
    '''
    
    def __init__(self, flags=None, exp_opts=None):
        self._flags = flags if flags else DEFAULT_FLAGS
        self._exp_opts = exp_opts if exp_opts else EXP_OPTS
        
    @property
    def flags(self):
        return self._flags

    @property
    def exp_opts(self):
        return self._exp_opts

    @property
    def headless(self):
        return self._headless
    
    def _build_options(self):
        '''Builds a ChromeOptions object for specifying special config settings
        for our Chrome webdriver.

        * Used as a helper within `initialize_driver` function.

        Returns
        -------
            _opts : webdriver.ChromeOptions object
        '''
        _opts = webdriver.ChromeOptions()
        for flag in self._flags:
            _opts.add_argument(flag)
        _opts.add_experimental_option("excludeSwitches", self._exp_opts)
        return _opts
    
    def initialize_driver(self, headless=False):
        '''
        Initializes and returns a Google Chrome webdriver used to perform
        automated tasks in the browser.

        Parameters
        ----------
            headless: bool, optional
                Whether the webdriver will be ran in headless mode when
                initialized. (Default False)

        Returns
        -------
            _driver : webdriver.Chrome object
                A Selenium Chrome webdriver.

        '''
        _driver = webdriver.Chrome(options=self._build_options())
        if headless:
            _driver.headless = True
        return _driver
