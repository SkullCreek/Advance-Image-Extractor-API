from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class ImageScapper:
    """
    ImageScapper class scrapes images from website

    Attributes:

    """
    def __init__(self, number_images: int, wd: webdriver, sleep: int = 1):
        """
        The constructor to initiate the object with
        :param number_images: Number of images want to extract
        :param wd: selenium webdriver
        :param sleep: sleeping time between clicks
        """
        try:
            self.number_images = number_images
            self.browser = wd.Chrome(ChromeDriverManager().install())
            self.sleep = sleep
        except Exception as e:
            raise Exception(e)

    def get_request(self, query: str):
        try:
            query = "+".join(query.split(" "))
            url = "https://www.google.com/search?q={}&tbm=isch".format(query)
            self.browser.get(url)
        except Exception as e:
            raise Exception(e)

    def fetch_thumbnail(self):
        try:
            thumbnail_results = self.browser.find_elements(By.CLASS_NAME,"Q4LuWd")
            prev = 0
            curr_len = len(thumbnail_results)
            while curr_len < self.number_images:
                self.scroll_to_end()
                if (curr_len == prev and curr_len < self.number_images):
                    try:
                        show_more = self.browser.find_elements(By.CLASS_NAME, "mye4qd")
                        if len(show_more) == 0:
                            break
                        else:
                            show_more[0].click()
                            time.sleep(self.sleep)
                    except Exception as e:
                        # logging
                        break
                thumbnail_results = self.browser.find_elements(By.CLASS_NAME, "Q4LuWd")
                prev = curr_len
                curr_len = len(thumbnail_results)


            print(curr_len)
        except Exception as e:
            raise Exception(e)

    def scroll_to_end(self):
        try:
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            time.sleep(self.sleep)
        except Exception as e:
            raise Exception(e)




obj = ImageScapper(1000,webdriver)
obj.get_request("nature")
obj.fetch_thumbnail()