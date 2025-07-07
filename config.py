from os import environ 

class Config:
    API_ID = environ.get("API_ID", "29245477")
    API_HASH = environ.get("API_HASH", "0abc83883262245c90ca337b7a0375c4")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7404600334:AAGpQv2DJb-s7yjXsgmH9_0pBOVFw7O1HXE") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = "mongodb+srv://Kafka:Au3OoWzCDYJKeuHU@cluster0.lz2m8iy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE_NAME = environ.get("DATABASE_NAME", "cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7654385403').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
