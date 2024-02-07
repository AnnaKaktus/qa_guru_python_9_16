# Пропуск мобилки, если размеры десктопные; пропуск десктопа, если размеры мобилки

import pytest
from selene import browser, have


@pytest.mark.desktop
def test_desktop_skip(skip_browser):
    if skip_browser == "mobile":
        pytest.skip("Это мобилка")
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.mobil
def test_mobile_skip(skip_browser):
    if skip_browser == "desktop":
        pytest.skip("Это десктоп")
    browser.open("https://github.com/")
    browser.element(".js-details-target.Button--link").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element("#login").should(have.text("Sign in to GitHub"))
