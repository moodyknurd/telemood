# Telemood  

![Build status](https://cloud.drone.io/api/badges/moodyknurd/telemood/status.svg?ref=refs/heads/main)

> A Telegram user automation script, written in Python


## Description

I wrote this to automate:

- Blocking on DMs (since Telegram doesn't have a native implementation for blocking private messages and I'm only on there
for groups anymore)

- Adding music notes to my name while I'm listening to a song (uses the `lastfm` telegram bot to check if I'm currently 
listening to something each time I come online)

I've used [Pyrogram](https://github.com/pyrogram/pyrogram) for this, with some additional digging into raw updates to 
block those pesky secret chats that Pyrogram doesn't have anything for yet.


## Usage  

NOTE: Get your `api_id` and `api_hash` from [here](https://my.telegram.org/auth?to=apps)

### Script:  
1. Create a virtual environment and install the required packages  
		cd telemood && python -m venv <whatevervenv> && source <whatevervenv>/bin/activate && pip install -r requirements.txt

2. Run the script  
		python telemood_app --id <your id> --hash <your hash>

### Docker:  
1. Start the container by passing your API id and hash  
		docker container run -it --name <container-name> -e API_ID=<your id> -e API_HASH=<your hash> moodyknurd/telemood
2. Enter the phone number you've registered with, and the confirmation code after, then `CTRL-P CTRL-Q` to exit the container without stopping it.
	
## TODO  

- Switch out the `debian:stable-slim` base image for an `alpine` one.
- Switch out the LastFM search for a ListenBrainz one instead.
