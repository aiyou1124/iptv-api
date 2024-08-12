from selenium import webdriver


def setup_driver(proxy=None):
    """
    Setup the driver for selenium
    """
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument("--log-level=3")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("blink-settings=imagesEnabled=false")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    if proxy:
        options.add_argument("--proxy-server=%s" % proxy)
    driver = webdriver.Chrome(options=options)
    return driver
