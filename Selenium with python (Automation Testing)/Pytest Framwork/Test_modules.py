# test_calculator.py

# import pytest
# from selenium.webdriver.chrome import webdriver


# import pytest
# @pytest.fixture
# def firefox_options(firefox_options):
#     firefox_options.binary = '/path/to/firefox-bin'
#     firefox_options.add_argument('-foreground')
#     firefox_options.set_preference('browser.anchor_color', '#FF0000')
#     return firefox_options

import pytest
@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = '/path/to/chrome'
    chrome_options.add_extension('/path/to/extension.crx')
    chrome_options.add_argument('--kiosk')
    return chrome_options

