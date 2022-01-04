from telethon.errors.rpcerrorlist import YouBlockedUserError
from EmikoRobot import telethn as tbot
from EmikoRobot.events import register
from EmikoRobot import ubot2 as ubot
from asyncio.exceptions import TimeoutError


@register(pattern="^/sg ?(.*)")
async def lastname(steal):
    steal.pattern_match.group(1)
    puki = await steal.reply("```Retrieving Such User Information..```")
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await puki.edit("```Please Reply To User Message.```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await puki.edit("```Reply To Real User's Message.```")
        return
    await puki.edit("```Please wait...```")
    try:
        async with ubot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply("```Error, report to @kenbotsupport```")
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await puki.edit(f"`{r.message}`")
                await ubot.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await puki.edit(
                    "```I Can't Find This User's Information, This User Has Never Changed His Name Before.```"
                )
                await ubot.delete_messages(conv.chat_id, [msg.id, r.id, response.id])
                return
            else:
                respond = await conv.get_response()
                await puki.edit(f"```{response.message}```")
            await ubot.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await puki.edit("`I'm Sick Sorry...`")


@register(pattern="^/quotly ?(.*)")
async def quotess(qotli):
    if qotli.fwd_from:
        return
    if not qotli.reply_to_msg_id:
        return await qotli.reply("```Mohon Balas Ke Pesan```")
    reply_message = await qotli.get_reply_message()
    if not reply_message.text:
        return await qotli.reply("```Mohon Balas Ke Pesan```")
    chat = "@QuotLyBot"
    if reply_message.sender.bot:
        return await qotli.reply("```Mohon Balas Ke Pesan```")
    await qotli.reply("```Sedang Memproses Sticker, Mohon Menunggu```")
    try:
        async with ubot.conversation(chat) as conv:
            try:
                response = await conv.get_response()
                msg = await ubot.forward_messages(chat, reply_message)
                response = await response
                """ - don't spam notif - """
                await ubot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                return await qotli.edit(
                    "```Harap Jangan Blockir @QuotLyBot Buka Blokir Lalu Coba Lagi```"
                )
            if response.text.startswith("Hi!"):
                await qotli.edit(
                    "```Mohon Menonaktifkan Pengaturan Privasi Forward Anda```"
                )
            else:
                await qotli.delete()
                await tbot.send_message(qotli.chat_id, response.message)
                await tbot.send_read_acknowledge(qotli.chat_id)
                """ - cleanup chat after completed - """
                await ubot.delete_messages(conv.chat_id, [msg.id, response.id])
    except TimeoutError:
        await qotli.edit()
