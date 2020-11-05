"""Selenium for app store expansion."""
import logging
import random
import re
import time
from abc import ABCMeta

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


class CrawlerBase(metaclass=ABCMeta):
    """Crawler Base."""

    def _random_latancy(self):
        return random.randint(0, 1)+random.random()


class AppStoreCrawler(CrawlerBase):
    """App Store crawler with selenium."""

    def __init__(self):
        """__init__."""
        self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(
            ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(), chrome_options=self.chrome_options)

    def close(self):
        """Close driver."""
        self.driver.close()

    def crawler_category(self):
        """Crawler Category."""

        url = 'https://apps.apple.com/tw/genre/ios/id36'
        self.driver.get(url)
        time.sleep(self._random_latancy())
        all_categories = self.driver.find_elements_by_css_selector(
            '#genre-nav a')

        all_cats_url = []
        for cat in all_categories:
            cat_link = cat.get_attribute('href')
            all_cats_url.append(cat_link)
        for cat_link in all_cats_url:
            self.crawler_app(cat_link)

    def crawler_app(self, cat_link):
        """Crawler app."""
        alphabet_list = []
        for i in range(ord('a'), ord('z') + 1):
            alphabet_list.append(chr(i).upper())
        alphabet_list.append('*')

        for alphabet in alphabet_list:
            for page in range(1, 200):
                url = f'{cat_link}?letter={alphabet}&page={page}#page'
                self.driver.get(url)
                time.sleep(self._random_latancy())

                if self.driver.find_elements_by_css_selector('#selectedcontent a'):
                    all_app = self.driver.find_elements_by_css_selector(
                        '#selectedcontent a')

                    all_app_list = []
                    for app in all_app:
                        link = app.get_attribute('href')
                        all_app_list.append(link)

                    for link in all_app_list:
                        fid = re.search(
                            r'\/id(\d*)', link).group(1)
                        self.judgment_comments(link)
                else:
                    break

    def judgment_comments(self, url):
        """Judgement comments."""
        self.driver.get(url)
        time.sleep(self._random_latancy())
        if self.driver.find_elements_by_css_selector(
                '.we-rating-count'):
            comments_count = re.search(
                '•(.*?)則評分', self.driver.find_element_by_css_selector(
                    '.we-rating-count').text).group(1)
            # comment count >= 1000,
            try:
                comments_count = int(comments_count.replace(',', ''))
                if comments_count >= 1000:
                    logging.info(f'Comment count over 1000 : {url}.')
            except ValueError:
                if '万' in comments_count:
                    logging.info(f'Comment count over 1000 : {url}.')


if __name__ == "__main__":
    try:
        ascrawler = AppStoreCrawler()
        ascrawler.crawler_category()

    except Exception as e:
        logging.error(e)
        ascrawler.close()
    finally:
        ascrawler.close()
