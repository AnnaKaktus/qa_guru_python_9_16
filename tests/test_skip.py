# Пропуск мобилки, если размеры десктопные; пропуск десктопа, если размеры мобилки

import pytest
from selene import browser, have


@pytest.mark.desktop
def test_mobile_skip(detect_browser):
    if detect_browser == "mobile":
        pytest.skip("Это мобилка")
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.mobile
def test_desktop_skip(detect_browser):
    if detect_browser == "desktop":
        pytest.skip("Это десктоп")
    browser.open("https://github.com/")
    browser.element(".js-details-target.Button--link").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element("#login").should(have.text("Sign in to GitHub"))