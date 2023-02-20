from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from config import database_config

cloud_config= {
  'secure_connect_bundle': database_config.cloud_config_path
}
auth_provider = PlainTextAuthProvider(database_config.cassandra_ClientId, database_config.cassandra_ClientSecret)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()
session.set_keyspace(database_config.keyspace_name)

row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")