import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 9000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", None))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/IstkharXrobot/Mc",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/THUNDERDEVS")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+PaEtaAu9DI9mYzc9")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = [
    "https://telegra.ph/file/8fb11f38033d3195c9c8c.jpg",
    "https://telegra.ph/file/106167c80a3fc3ab9f1e8.jpg",
    "https://telegra.ph/file/89070543c0f7f2e51118d.jpg",
    "https://telegra.ph/file/3a0afc7a07f35747684eb.jpg",
    "https://telegra.ph/file/0db46c5fca2c69829a7d4.jpg",
    "https://telegra.ph/file/f7e5522656c24abf1bd90.jpg",
    "https://telegra.ph/file/621f76810deb42513f345.jpg",
    "https://telegra.ph/file/095d4d1a638bd42e54189.jpg",
    "https://telegra.ph/file/0a6cf2af7eead7fcb0745.jpg",
]

PING_VID_URL = getenv(
    "PING_VID_URL", "https://graph.org/file/babb71b593f36549218ce.jpg"
    )

PLAYLIST_IMG_URL = "https://graph.org/file/4a254d425fb4bf09b7470.jpg"
STATS_VID_URL = "https://graph.org/file/51f37e3c2d4aaff5cf80e.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/df01978f91c14b16292f1.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/a6e3e9d54c8b2e01787b6.jpg"
STREAM_IMG_URL = "https://graph.org/file/49bcbc23be713fbe06bac.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/809651f9be99ee2bf76ab.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/134c9f52f4ba0f7691cd1.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/4b5c2174d7f38b4b4abd7.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/80feff5bb4a03cf331945.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/0379defeb51910065beac.jpg"
FAILED = "https://graph.org/file/323b07bccd5e5e1f81f61.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
