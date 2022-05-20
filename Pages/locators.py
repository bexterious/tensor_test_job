from selenium.webdriver.common.by import By


class SearchPageLocators:
	SEARCH_WINDOW = (By.ID, "text")
	SUGGEST_TABLE = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile')
	LINKS_IN_SEARCH = (By.CSS_SELECTOR, ".Path.Organic-Path.Organic-Path_verified.path.organic__path")


class ImagePageLocators:
	LINK_IMAGES = (By.CSS_SELECTOR, '[data-id="images"]')
	FIRST_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > img')
	FIRST_CATEGORY_TEXT = (By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > div.PopularRequestList-SearchText')
	FIRST_IMAGE_IN_SEARCH = (By.XPATH, '//body/div[3]/div[2]/div[1]/div[1]/div/div[1]')
	WINDOW_WITH_IMG = (By.CSS_SELECTOR, '.MediaViewer-LayoutScene.MediaViewer_theme_fiji-LayoutScene')
	BACK_BUTTON = (By.CSS_SELECTOR, '.MediaViewer-ButtonPrev.MediaViewer_theme_fiji-ButtonPrev')
	FORWARD_BUTTON = (By.CSS_SELECTOR, '.MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext')
	OPENED_IMAGE = (By.CSS_SELECTOR, '.MediaViewer-View.MediaViewer_theme_fiji-View > div > img')
