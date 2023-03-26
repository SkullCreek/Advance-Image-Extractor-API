import os.path
import urllib.request
from mega import Mega
import zipfile
from config import download_config as dc
from utilities import utils


class DownloadImages:
    """
    Create a downloadable link to download all the extracted images
    """

    def __init__(self, urls):
        """
        Initialize the cloud storage and custom logger
        :param urls: set of url of image
        """
        try:
            self.custom_logger = utils.CustomLogging("download")
            self.custom_logger.initialize_logger('../logs/database.log')
            self.mega = Mega()
            self.login = self.mega.login(dc.username, dc.password)
            self.urls = urls
        except Exception as e:
            self.custom_logger.append_message("(download.py(__init__) - " + e.args[0], "exception")
            raise Exception(e)

    def generate_link(self, uuid):
        """
        Downloads all the images with the help of urls inside a zip file, uploads it to cloud storage and creates
        downloadable link :param uuid: Unique id of every job assigned :return:
        """
        try:
            filename = uuid + ".zip"
            with zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED) as zipf:
                for url in self.urls:
                    image_path = os.path.basename(url)
                    urllib.request.urlretrieve(url, image_path)
                    zipf.write(image_path)
                    os.remove(image_path)

            self.login.upload(filename)
            link = self.login.export(filename)
            os.remove(filename)
            return link
        except Exception as e:
            self.custom_logger.append_message("(download.py(generate_link) - " + e.args[0], "exception")
            raise Exception(e)

# url = [
#     "https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg",
#     "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Shaqi_jrvej.jpg/1200px-Shaqi_jrvej.jpg"]
# a = DownloadImages(url)
# print(a.generate_link("1234"))
