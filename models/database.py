from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from config import database_config
from utilities import utils


class Cassandra:
    """
    This makes connection with the Cassandra database to store user data such as email and url with the help of UUID
    """

    def __init__(self):
        """
        Establish connection with DATASTAX cassandra database and create a session to execute query
        """
        try:
            self.custom_logger = utils.CustomLogging("database")
            self.custom_logger.initialize_logger('../logs/database.log')

            cloud_config = {
                'secure_connect_bundle': database_config.cloud_config_path
            }
            auth_provider = PlainTextAuthProvider(database_config.cassandra_ClientId,
                                                  database_config.cassandra_ClientSecret)
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            self.session = cluster.connect()
            self.session.set_keyspace(database_config.keyspace_name)
            self.custom_logger.append_message("(database.py(create_table)) - Database Connected", "info")

        except Exception as e:
            self.custom_logger.append_message("(database.py(__init__)) - " + str(e.args[0]), "exception")
            raise Exception(e)

    def create_table(self):
        """
        Creates table if not exists in the database
        """
        try:
            self.session.execute('CREATE TABLE IF NOT EXISTS {}'
                                 '(id UUID, email text, url text, PRIMARY KEY (id,email));'
                                 .format(database_config.table_name))
            self.custom_logger.append_message("(database.py(create_table)) - Table Created", "info")

        except Exception as e:
            self.custom_logger.append_message("(database.py(create_table)) - " + str(e.args[0]), "exception")
            raise Exception(e)

    def select_query(self, req_id):
        """
        Select the user data with UUID
        :param req_id: UUID to search in database
        :return: id, email, url
        """
        try:
            prepared = self.session.prepare(
                "SELECT * FROM {} WHERE id=? ALLOW FILTERING".format(database_config.table_name))
            return self.session.execute(prepared, [req_id]).one()

        except Exception as e:
            self.custom_logger.append_message("(database.py(select_query)) - " + str(e.args[0]), "exception")
            raise Exception(e)

    def insert_user_data(self, uuid, email, url):
        """
        Insert uuid, email and url into the database
        :param uuid: unique UUID
        :param email: email of the user
        :param url: url from where user can download zip file
        """
        try:
            prepared = self.session.prepare("INSERT INTO " + database_config.table_name + "(id, email, url) VALUES ("
                                                                                          "?, ? , ?)")
            self.session.execute(prepared, [uuid, email, url])
            self.custom_logger.append_message("(database.py(create_table)) - Data Inserted", "info")

        except Exception as e:
            self.custom_logger.append_message("(database.py(insert_user_data)) - " + str(e.args[0]), "exception")
            raise Exception(e)

    def delete_url(self, req_id):
        """
        Delete id, email, url
        :param req_id: unique UUID registered with the user
        """
        try:
            prepared = self.session.prepare('DELETE FROM {} WHERE id=?'.format(database_config.table_name))
            self.session.execute(prepared, [req_id])
            self.custom_logger.append_message("(database.py(create_table)) - URL Deleted", "info")

        except Exception as e:
            self.custom_logger.append_message("(database.py(delete_url)) - " + str(e.args[0]), "exception")
            raise Exception(e)

    def close_session(self):
        """
        Shutdown the session
        """
        try:
            self.session.shutdown()
        except Exception as e:
            self.custom_logger.append_message("(database.py(close_session)) - " + str(e.args[0]), "exception")
            raise Exception(e)

    def delete_table(self):
        """
        Drop table id exists
        """
        try:
            self.session.execute("DROP TABLE IF EXISTS {}".format(database_config.table_name))

        except Exception as e:
            self.custom_logger.append_message("(database.py(delete_table)) - " + str(e.args[0]), "exception")
            raise Exception(e)
