import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1366, 768), (1600, 900)])
def desktop_browser(request):
    browser.config.base_url = "https://github.com"
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(800, 480), (480, 360), (896, 414)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(1920, 1080), (1366, 768), (1600, 900), (800, 480), (480, 360), (896, 414)])
def skip_browser(request):
    browser.config.base_url = "https://github.com"
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 896:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()
