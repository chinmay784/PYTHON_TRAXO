# from pymongo import MongoClient
# from app.core.config import MONGO_URI, DB_NAME

# client = MongoClient(MONGO_URI)
# db = client[DB_NAME]

# users_collection = db["adminusers"]


# from pymongo import MongoClient
# from app.core.config import MONGO_URI, DB_NAME

# client = MongoClient(MONGO_URI)
# db = client[DB_NAME]

# # users_collection = db["users"]
# # ✅ NEW COLLECTION
# users_collection = db["adminUsers"]

# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017")

# database = client["admin_db"]

# # Collections
# users_collection = database["users"]
# company_collection = database["companies"]


from pymongo import MongoClient
from app.core.config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
print("Connected to MongoDB")

# users_collection = db["users"]
# ✅ NEW COLLECTION
users_collection = db["adminUsers"]
company_collection = db["companies"]