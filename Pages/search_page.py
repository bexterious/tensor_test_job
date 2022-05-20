from Pages.base_page import BasePage
from Pages.locators import SearchPageLocators
import time
from selenium.webdriver.common.keys import Keys


class SearchPage(BasePage):

	def yandex_search(self):
		self.search_field()
		self.visibility_suggest_table()
		self.tensor_link_result()

	def search_field(self):
		assert self.is_element_present(*SearchPageLocators.SEARCH_WINDOW), \
			"No search field on the main page"

	def visibility_suggest_table(self):
		search_box = self.browser.find_element(*SearchPageLocators.SEARCH_WINDOW)
		search_box.send_keys('тензор')
		time.sleep(5)
		assert self.is_visibility_located(*SearchPageLocators.SUGGEST_TABLE), \
			"No table with tips on the main page"
		search_box.send_keys(Keys.ENTER)

	def tensor_link_result(self):
		links = self.browser.find_elements(*SearchPageLocators.LINKS_IN_SEARCH)
		item = [elem.text.strip() for elem in links[:1]]
		if "tensor.ru" not in item:
			raise Exception('The first link does not lead to tensor.ru')
		time.sleep(5)
