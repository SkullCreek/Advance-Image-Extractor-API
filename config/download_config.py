from dotenv import dotenv_values

config = dotenv_values("../.env")

cloud_name = config["CLOUDINARY_CLOUD_NAME"]
api_key = config["CLOUDINARY_API_KEY"]
api_secret = config["CLOUDINARY_API_SECRET"]
