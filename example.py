"""An example for selenium with docker-compose."""
import time
import logging
from selenium import webdriver

from settings import logging

logger = logging.getLogger(__name__)


class ExampleSelenium(object):

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Remote(
            "http://hub:4444/wd/hub", options=options)

    def close(self):
        self.driver.quit()

    def start_visit(self):
        logger.debug('Start visit web page!')
        self.driver.get('https://heho.com.tw/')
        if self.driver.find_elements_by_css_selector('.box-text-inner h5'):
            all_repo = self.driver.find_elements_by_css_selector(
                '.box-text-inner h5')
            for i in all_repo:
                logger.debug(f'news: {i.text}')
        else:
            logger.debug(f'There is something wrong QQ...')


if __name__ == "__main__":
    imp = ExampleSelenium()
    imp.start_visit()
