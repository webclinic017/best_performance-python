import sys
sys.path.append("/home/sp/codes/personal/best_performance-python")
from utils.logger.logger import Logger
from sele import get_chrome_driver


class Crawler(Logger):
    def __init__(self, *args, **kwargs):
        self.init_logger("./", "test")
        self.driver = get_chrome_driver()


if __name__ == '__main__':
    c = Crawler()
    d = c.driver

    d.get("https://www.amazon.com/s?k=camping&ref=nb_sb_noss")
    element = d.find_elements_by_xpath('//*[@id="anonCarousel2"]/ol/li')
    element.find_elements_by_tag_name("img").get_attribute('src')
