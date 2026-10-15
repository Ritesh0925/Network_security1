from pymongo import MongoClient
uri = "mongodb+srv://guptariteshkumar249_db_user:Admin123@cluster0.9ozooto.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)