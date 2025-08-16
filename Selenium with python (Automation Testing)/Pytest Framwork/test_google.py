import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_bing_title(driver):
    driver.get("https://www.bing.com")
    assert "Bing" in driver.title

