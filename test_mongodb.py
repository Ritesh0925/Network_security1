from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv
load_dotenv()

uri = os.getenv("MONGO_DB_URL") or os.getenv("MONGODB_URL_KEY") or "mongodb+srv://guptariteshkumar249_db_user:Admin123@cluster0.9ozooto.mongodb.net/?appName=Cluster0"
ca = certifi.where()

client = MongoClient(uri, tlsCAFile=ca)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)