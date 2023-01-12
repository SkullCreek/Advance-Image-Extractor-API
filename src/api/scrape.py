from selenium import webdriver

class ImageScapper:
    """
    ImageScapper class scrapes images from website

    Attributes:

    """

    def __int__(self, query: str, number_images: int, wd: webdriver, sleep: int = 1):
        """
        The constructor to initiate the object with
        :param query: Category of images want to extract
        :param number_images: Number of images want to extract
        :param wd: selenium webdriver
        :param sleep: sleeping time between clicks
        """
        try:
            self.query = query
            self.number_images = number_images
            self.wd = wd
            self.sleep = sleep
        except Exception as e:
            raise Exception(e)

    def get_request(self):
        pass