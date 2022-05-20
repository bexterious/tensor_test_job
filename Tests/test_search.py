from Pages.search_page import SearchPage
from Config.config import TestData


def test_yandex_main_page(browser):
	link = TestData.BASE_URL
	page = SearchPage(browser, link)
	page.open()
	page.yandex_search()
