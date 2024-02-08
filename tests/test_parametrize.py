# Параметризация с помощью  indirect


import pytest
from selene import browser, have


@pytest.mark.desktop
@pytest.mark.parametrize("desktop_browser", [(1280, 720), (1480, 720), (2200, 1080)], indirect=True)
def test_desktop_indirect(desktop_browser):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.mobile
@pytest.mark.parametrize("mobile_browser", [(640, 360), (400, 240), (760, 410)], indirect=True)
def test_mobile_indirect(mobile_browser):
    browser.open("https://github.com/")
    browser.element(".js-details-target.Button--link").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element("#login").should(have.text("Sign in to GitHub"))