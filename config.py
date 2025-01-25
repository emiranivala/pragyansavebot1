# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25121213"))
API_HASH = getenv("API_HASH", "b734dcc45da130a8156e2be836594706")
BOT_TOKEN = getenv("BOT_TOKEN", "7842255168:AAEiEtOdBj4SugCNih1_CIigHO3x6NRV6qM")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5464921200").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://PihuMusic:PihuMusic@cluster0.w3eiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002380299642")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001573605549"))
#CHANNEL_USERNAME="@VRindavanNeeko16008"
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "1000000000000000000000000000000000000000000000000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5001000000000000000000000000000000000000000000000000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)


