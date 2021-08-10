# Telemood 

__A Telegram user automation script, written in Python__


## Description

I wrote this to automate:

* Blocking on DMs (since Telegram doesn't have a native implementation for blocking private messages and I'm only on there
for groups anymore)

* Adding music notes to my name while I'm listening to a song (uses the `lastfm` telegram bot to check if I'm currently 
listening to something each time I come online) (plan to migrate this to listenbrainz if and when I can)

I've used [Pyrogram](https://github.com/pyrogram/pyrogram) for this, with some additional digging into raw updates to 
block those pesky secret chats that Pyrogram doesn't have anything for yet.


## Installation

    cd telemood && python -m venv <whatevervenv> && source <whatevervenv>/bin/activate && pip install -r requirements.txt
    python telemood_app


## Usage

1. Get your `api_id` and `api_hash` from [here](https://my.telegram.org/auth?to=apps)
2. Run the script: `python telemood_app --id <your id> --hash <your hash>`
	
