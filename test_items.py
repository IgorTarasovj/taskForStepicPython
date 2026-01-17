import pytest
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_button(browser):
    browser.get(link)

    buttons = browser.find_elements(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")

    assert len(buttons) > 0, "Element does not exist"