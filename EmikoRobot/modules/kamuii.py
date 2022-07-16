import os
from telethon.errors.rpcerrorlist import YouBlockedUserError

from EmikoRobot import ubot2
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot, TEMP_DOWNLOAD_DIRECTORY, SUPPORT_CHAT


@register(pattern="^/kamuii ?(.*)")
async def _(fry):
    level = fry.pattern_match.group(1)
    kntl = await fry.reply("`Deepfrying this image...`")
    if fry.fwd_from:
        return
    if not fry.reply_to_msg_id:
        await kntl.edit("`Reply to a stickers`")
        return
    reply_message = await fry.get_reply_message()
    if not reply_message.media:
        await fry.edit("`this file not supported`")
        return
    if reply_message.sender.bot:
        await fry.edit("`Reply to a asticker to destroy`")
        return
    chat = "@image_deepfrybot"
    message_id_to_reply = fry.message.reply_to_msg_id
    async with ubot2.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/deepfry {level}"
                msg_level = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
                response = await conv.get_response()
            else:
                response = await conv.get_response()
            """ - don't spam notif - """
            await ubot2.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await fry.reply(f"`Error, tell the problem on @{SUPPORT_CHAT}`")
            return
        if response.text.startswith("Forward"):
            await fry.edit(f"`Error, tell the problem on @{SUPPORT_CHAT}`")
        else:
            downloaded_file_name = await ubot2.download_media(
                response.media, TEMP_DOWNLOAD_DIRECTORY
            )
            await tbot.send_file(
                fry.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply,
            )
            """ - cleanup chat after completed - """
            try:
                msg_level
            except NameError:
                await ubot2.delete_messages(conv.chat_id, [msg.id, response.id])
            else:
                await ubot2.delete_messages(
                    conv.chat_id, [msg.id, response.id, r.id, msg_level.id]
                )
    await kntl.delete()
    return os.remove(downloaded_file_name)
