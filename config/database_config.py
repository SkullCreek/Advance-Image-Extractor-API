from dotenv import dotenv_values

config = dotenv_values("../.env")

cloud_config_path = config["CLOUD_CONFIG_PATH"]
cassandra_ClientId = config["CASSANDRA_CLIENT_ID"]
cassandra_ClientSecret = config["CASSANDRA_CLIENT_SECRET"]
keyspace_name = config["KEYSPACE_NAME"]
table_name = config["TABLE_NAME"]