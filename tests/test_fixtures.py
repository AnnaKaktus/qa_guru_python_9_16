# Разные фикстуры


import pytest
from selene import browser, have


@pytest.mark.desktop
def test_desktop_different_fixture(desktop_browser):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.mobile
def test_mobile_different_fixture(mobile_browser):
    browser.open("https://github.com/")
    browser.element(".js-details-target.Button--link").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element("#login").should(have.text("Sign in to GitHub"))
