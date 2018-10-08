import application_config
from pymongo import MongoClient

host = application_config.db_host
port = application_config.db_port
database = application_config.db_database

client = MongoClient(host,port)
db_client = client[database]

