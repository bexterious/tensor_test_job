from Pages.image_page import ImagePage
from Config.config import TestData


def test_images(browser):
    link = TestData.BASE_URL
    page = ImagePage(browser, link)
    page.open()
    page.yandex_images()
