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
            self.url = set()
            self.url.add("1234")
            self.extra = 0
        except Exception as e:
            raise Exception(e)

    def get_request(self, query: str):
        """
        This Configures the link by concatenating the reframed query with the source from where the images will get
        extracted and also put a request to the webdriver with the link
        :param query: Search parameter or image name
        """
        try:
            query = "+".join(query.split(" "))
            geturl = "https://www.google.com/search?q={}&tbm=isch".format(query)
            self.browser.get(geturl)
        except Exception as e:
            raise Exception(e)

    def fetch_image_url(self):
        try:
            thumbnail = self.fetch_thumbnail()
            for i in thumbnail:
                try:
                    i.click()
                    time.sleep(self.sleep)
                    image_url = self.browser.find_elements(By.CSS_SELECTOR,"img.n3VNCb")
                    for image_url in image_url:
                        if image_url.get_attribute('src') and 'http' in image_url.get_attribute('src'):
                            self.url.add(image_url.get_attribute('src'))
                    if len(self.url) == self.number_images:
                        break
                except Exception as e:
                    raise Exception(e)
            if len(self.url) < self.number_images:
                self.fetch_more()
            else:
                print(self.url)
                return self.url


        except Exception as e:
            raise Exception(e)

    def fetch_thumbnail(self):
        """
        The function will get maximum img elements to satisfy the required number of images (number_images).
        """
        try:
            thumbnail_results = self.browser.find_elements(By.CLASS_NAME,"Q4LuWd")
            prev = 0
            curr_len = len(thumbnail_results)
            while curr_len < self.number_images:
                self.__scroll_to_end();
                if (curr_len == prev and curr_len < self.number_images):
                    try:
                        show_more = self.browser.find_elements(By.CLASS_NAME, "mye4qd")
                        show_more[0].click()
                        time.sleep(self.sleep)
                    except Exception as e:
                        # logging
                        break
                thumbnail_results = self.browser.find_elements(By.CLASS_NAME, "Q4LuWd")
                prev = curr_len
                curr_len = len(thumbnail_results)
            return thumbnail_results

        except Exception as e:
            raise Exception(e)

    def fetch_more(self):
        try:
            getele = self.browser.find_elements(By.CLASS_NAME,"ZZ7G7b")
            getele[self.extra].click()
            self.extra += 1
            self.fetch_image_url()

        except Exception as e:
            raise Exception(e)

    def __scroll_to_end(self):
        """
        This is a helper function which scrolls to the bottom of the webpage.
        """
        try:
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            time.sleep(self.sleep)
        except Exception as e:
            raise Exception(e)




obj = ImageScapper(5,webdriver)
obj.get_request("wallpaper")
obj.fetch_more()