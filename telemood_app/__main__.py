import argparse
import asyncio
import aiohttp
import sys
from pyrogram import Client, filters, idle
''' for the tetris thing '''
from pyrogram.raw.functions.users import GetFullUser
''' '''
import pkgs.getLastFMSong 
import pkgs.blockDM

parser = argparse.ArgumentParser(description='Run Telemood.',)
parser.add_argument('--id', required=True, type=int, help='Provide the app id', dest='api_id')
parser.add_argument('--hash', required=True, type=str, help='Provide the app hash', dest='api_hash')
args = parser.parse_args()

telemood = Client(":memory:", args.api_id, args.api_hash)

try:
    telemood.start()

    is_online_filter = filters.create(lambda _, __, is_me = telemood.get_me(): is_me["status"] == "online")

    @telemood.on_user_status(is_online_filter)
    async def startup_tasks(_, __):
        teletasks = list()
        teletasks.append(asyncio.ensure_future(pkgs.getLastFMSong.get_last_song(telemood)))
        await asyncio.gather(*teletasks)
        teletasks.clear()
    
    @telemood.on_message(filters.private)
    async def block_dm(_, unsolicited_message):
        await pkgs.blockDM.block_regular_dm(telemood, unsolicited_message)

    @telemood.on_raw_update()
    async def check_dm(_, update, users, __):
        await pkgs.blockDM.block_secret_dm(telemood, update, users)

    idle()

except KeyboardInterrupt:
    telemood.stop()
