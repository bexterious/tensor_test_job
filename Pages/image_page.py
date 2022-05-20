from Pages.base_page import BasePage
from Pages.locators import ImagePageLocators
from urllib.parse import unquote
import time


class ImagePage(BasePage):

	def yandex_images(self):
		self.link_images()
		self.category_check()
		self.picture_actions()

	def link_images(self):
		assert self.is_element_present(*ImagePageLocators.LINK_IMAGES), \
			"No 'Pictures' link on the page"
		images = self.browser.find_element(*ImagePageLocators.LINK_IMAGES)
		images.click()
		window_after = self.browser.window_handles[1]
		self.browser.switch_to.window(window_after)
		time.sleep(2)
		assert 'https://yandex.ru/images/' in self.browser.current_url, \
			"You didn't go to the image page"

	def category_check(self):
		category1 = self.browser.find_element(*ImagePageLocators.FIRST_CATEGORY) 
		category1_text = self.browser.find_element(*ImagePageLocators.FIRST_CATEGORY_TEXT).text
		self.browser.execute_script("arguments[0].click();", category1)
		time.sleep(5)
		search_text = unquote(self.browser.current_url).\
			replace('https://yandex.ru/images/search?utm_source=main_stripe_big&text=', '')
		search_text_corrected = search_text.strip('&nl=1&source=morda')
		assert category1_text == search_text_corrected, "Search doesn't match the selected image"

	def picture_actions(self):
		pic1 = self.browser.find_element(*ImagePageLocators.FIRST_IMAGE_IN_SEARCH).click()
		assert self.is_element_present(*ImagePageLocators.WINDOW_WITH_IMG),\
			"The window with the image doesn't open"
		time.sleep(5)
		id_img1 = self.browser.find_element(*ImagePageLocators.OPENED_IMAGE).get_attribute('src')
		button_next = self.browser.find_element(*ImagePageLocators.FORWARD_BUTTON).click()
		id_img2 = self.browser.find_element(*ImagePageLocators.OPENED_IMAGE).get_attribute('src')
		assert id_img1 != id_img2, "The image didn't change after pressing the 'forward' button!"
		time.sleep(5)
		button_back = self.browser.find_element(*ImagePageLocators.BACK_BUTTON).click()
		id_img3 = self.browser.find_element(*ImagePageLocators.OPENED_IMAGE).get_attribute('src')
		assert id_img1 == id_img3, "The 'back' button doesn't return to the previous image"
		time.sleep(5)


	