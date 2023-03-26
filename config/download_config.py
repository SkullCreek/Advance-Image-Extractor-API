from dotenv import dotenv_values

config = dotenv_values("../.env")

username = config["MEGA_EMAIL"]
password = config["MEGA_PASSWORD"]
