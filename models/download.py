import cloudinary
import cloudinary.uploader
import cloudinary.api
from config import download_config as dc
from utilities import utils

class DownloadImages:

    def __init__(self, urls):
        try:
            self.custom_logger = utils.CustomLogging("download")
            self.custom_logger.initialize_logger('../logs/database.log')
            self.storage = cloudinary.config(
                cloud_name=dc.cloud_name,
                api_key=dc.api_key,
                api_secret=dc.api_secret,
                secure=True
            )
            self.urls = urls
        except Exception as e:
            self.custom_logger.append_message("(download.py(__init__) - " + e.args[0], "exception")
            raise Exception(e)

    def download_image(self):
        pass

a = DownloadImages("abc")
