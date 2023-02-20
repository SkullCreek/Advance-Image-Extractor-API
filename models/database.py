from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from config import database_config


class Cassandra:
    def __init__(self):
        try:
            cloud_config = {
                'secure_connect_bundle': database_config.cloud_config_path
            }
            auth_provider = PlainTextAuthProvider(database_config.cassandra_ClientId,
                                                  database_config.cassandra_ClientSecret)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.session = cluster.connect()
            self.session.set_keyspace(database_config.keyspace_name)

        except Exception as e:
            raise Exception(e)

    def create_table(self):
        try:
            self.session.execute('CREATE TABLE IF NOT EXISTS {}'
                                 '(id UUID, email text, url text, PRIMARY KEY (id));'
                                 .format(database_config.table_name))

        except Exception as e:
            raise Exception(e)

    def select_query(self):
        try:
            result = self.session.execute('SELECT * FROM {}'.format(database_config.table_name))
            print(result)
        except Exception as e:
            raise Exception(e)


c = Cassandra()
c.create_table()
c.select_query()
# a.create_table()
