'''
webdriver.py
------------
    Class for building our Selenium Chrome webdriver.
'''
from selenium import webdriver


# Default & Experimental option flags for configuring our Chrome webdriver:
DEFAULT_FLAGS = ["--start-maximized",
                 "--incognito",
                 "--disable-notifications",
                 "--disable-extensions",
                ]

EXP_OPTS = ["enable-automation", "enable-logging"]


class MyWebDriver:
    '''A class for building the Selenium Chrome webdriver.

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

    Parameters
    ----------
        flags : list [str]
            The current flags of the given instance of WebBrowser.

        exp_opts : list [str]
            The experimental flags of the given instance of WebBrowser.

    Methods
    -------
        initialize_driver():
            Returns an initialized Selenium Chrome webdriver.
    '''

    def __init__(self, flags: list = None, exp_opts: list = None):
        self._flags = flags if flags else DEFAULT_FLAGS
        self._exp_opts = exp_opts if exp_opts else EXP_OPTS

    @property
    def flags(self) -> list:
        return self._flags

    @property
    def exp_opts(self) -> list:
        return self._exp_opts


    def _build_options(self) -> webdriver.ChromeOptions:
        '''Builds a ChromeOptions object for specifying special config settings
        for our Chrome webdriver.

        Returns
        -------
            selenium.webdriver.ChromeOptions
        '''
        _opts = webdriver.ChromeOptions()

        # Add default flags:
        for flag in self._flags:
            _opts.add_argument(flag)

        # Add experimental flags:
        _opts.add_experimental_option("excludeSwitches", self._exp_opts)

        # Option to keep the web browser open after program is finished:
        _opts.add_experimental_option("detach", True)
        return _opts


    def initialize_driver(self) -> webdriver.Chrome:
        '''Initializes and returns a Google Chrome webdriver used to perform
        automated tasks in the browser.

        Returns
        -------
            selenium.webdriver.Chrome
        '''
        return webdriver.Chrome(options=self._build_options())
