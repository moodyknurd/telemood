import argparse
import requests
import schedule
from pyrogram import Client, filters, idle
from pyrogram.raw.functions.users import GetFullUser
from pyrogram.raw.functions.messages import GetAllChats
from pyrogram.raw.types import InputUserSelf, UserFull
from pyrogram.raw.base import UserFull as UserFullBase
from pyrogram.raw.base import InputUser
from pyrogram.raw.base.messages import Chats
from pyrogram.raw.types.messages import Chats
from pyrogram.raw.base import Chat
from pyrogram.raw.functions.messages import DeleteChat
from pyrogram.raw.types.update_encryption import UpdateEncryption
from pyrogram.raw.types import EncryptedChatRequested
from pyrogram.raw.functions.contacts import GetContactIDs
from pyrogram.types import User
from datetime import datetime

parser = argparse.ArgumentParser(description='Run Telemood.',)
parser.add_argument('--id', required=True, type=int, help='Provide the app id', dest='api_id')
parser.add_argument('--hash', required=True, type=str, help='Provide the app hash', dest='api_hash')
args = parser.parse_args()

telemood = Client(":memory:", args.api_id, args.api_hash)

afk = False

telemood.start()

try: 
    is_online_filter = filters.create(lambda _, __, is_me = telemood.get_me(): is_me["status"] == "online")

    def get_40l_pb():
        current_status = telemood.send(
            GetFullUser(id = InputUserSelf())
        )["about"]
        #print(something)
        user_data = requests.get("https://ch.tetr.io/api/users/moodyknurd/records")
        pb = user_data.json()['data']['records']['40l']['record']['endcontext']['finalTime']/1000
        tetris_status = f"40L PB: {int(pb/60)}m{int(pb%60)}s"
        status_parts = current_status.split("|")
        if (len(status_parts) == 2):
            status_parts[1] = tetris_status
        else:
            status_parts.append(tetris_status)
        current_status = " | ".join(status_parts)
        telemood.update_profile(bio = current_status)
        #telemood.send(
        #        UpdateStatus(offline=True)
        #)

    def get_lastfm_results():
        last_song = telemood.get_inline_bot_results("lastfmrobot")["results"][0]["send_message"]["message"]
        return last_song

    def get_currently_playing():
        last_song = get_lastfm_results()
        name_tokens = telemood.get_me()["first_name"].split()
        #print(last_song)
        if "is now listening to" in last_song:
            if not "🎵" in name_tokens:
                name_tokens.insert(0, "🎵")
                name_tokens.append( "🎵")
        else:
            if "🎵" in name_tokens:
                name_tokens = list(name_tokens[1:-1])
        new_name = " ".join(name_tokens)
        #print(new_name)
        telemood.update_profile(first_name = new_name)

        
    @telemood.on_message(filters.private)
    def block_dm(moi, unsolicited_message):
        if not (unsolicited_message.from_user.is_contact or unsolicited_message.from_user.is_self or unsolicited_message.from_user.is_bot):
            unsolicited_message.delete()
            telemood.block_user(unsolicited_message.from_user.id)

    @telemood.on_user_status(is_online_filter)
    def update_status(moi, is_me):
        #get_40l_pb()
        get_currently_playing()

    @telemood.on_raw_update()
    def check_dm(moi, update, users, _):
        if isinstance(update, UpdateEncryption) and isinstance(update["chat"], EncryptedChatRequested):
            offender_id = list(users.keys())[0]
            #print(f"This is the update: {update}, and this is the user:{offender}")
            offender = telemood.get_users(offender_id)
            if not offender.is_contact:
                telemood.block_user(offender_id)
        pass
        
    # telemood.run()
    idle()
except KeyboardInterrupt:
    telemood.stop()
    sys.exit(0)
