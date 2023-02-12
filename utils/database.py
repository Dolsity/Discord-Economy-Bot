from dotenv import load_dotenv
from pymongo import MongoClient
import os
from datetime import date

from .config import (
    Starting_Job,
    Starting_Bank,
    Starting_wallet,
    Starting_Hours
)

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
cluster = MongoClient(mongo_url)
db = cluster["Bot"]
profile = db["profile"]


async def create_user_profile(user_id, user_name, user_tags):
    find_profile = profile.find_one({"_id": user_id})

    if find_profile:
        return

    profile.insert_one({
        "_id": user_id,
        "name": user_name,
        "tags": user_tags,
        "job": Starting_Job,
        "bank": Starting_Bank,
        "wallet": Starting_wallet,
        "hours": Starting_Hours,    
        "since": f"{date.today()}"         
    })