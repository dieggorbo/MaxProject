import application_config
from pymongo import MongoClient

# Function that connects on mongodb cluster
def conn():
  host = application_config.db_host
  port = application_config.db_port
  database = application_config.db_database

  try:
    client = MongoClient(host,port)
    db = client[database]
  except Exception as e:
    print(e).enconde("UTF-8").strip()


# Function to insert data into mongo db
def insert(payload):
  print(str(payload))
  try:
    print("dentro do try")
    db = conn()
    db.insert_one(payload).inserted_id
  except Exception as e:
    print(str(e))

