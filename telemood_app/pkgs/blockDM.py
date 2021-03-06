from pyrogram.raw.types.update_encryption import UpdateEncryption # type: ignore
from pyrogram.raw.types import EncryptedChatRequested # type: ignore
from pyrogram.types import User # type: ignore

from typing import List

async def block_regular_dm(telemood, unsolicited_message):
    if not (unsolicited_message.from_user.is_contact or unsolicited_message.from_user.is_self or unsolicited_message.from_user.is_bot):
        await unsolicited_message.delete()
        await telemood.block_user(unsolicited_message.from_user.id)

async def block_secret_dm(telemood, update, users):
    if isinstance(update, UpdateEncryption) and isinstance(update["chat"], EncryptedChatRequested):
        offender_id: List = list(users.keys())[0]
        offender: User = await telemood.get_users(offender_id)
        if not offender.is_contact:
            await telemood.block_user(offender_id)
    pass
