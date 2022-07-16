import os
import html
import nekos
import requests
from PIL import Image
from telegram import ParseMode
from EmikoRobot import dispatcher, updater
import EmikoRobot.modules.sql.nsfw_sql as sql
from EmikoRobot.modules.log_channel import gloggable
from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CommandHandler, run_async, CallbackContext
from EmikoRobot.modules.helper_funcs.filters import CustomFilters
from EmikoRobot.modules.helper_funcs.chat_status import user_admin
from telegram.utils.helpers import mention_html, mention_markdown, escape_markdown


@user_admin
@gloggable
def add_nsfw(update: Update, context: CallbackContext):
    chat = update.effective_chat
    msg = update.effective_message
    user = update.effective_user  # Remodified by @EverythingSuckz
    is_nsfw = sql.is_nsfw(chat.id)
    if not is_nsfw:
        sql.set_nsfw(chat.id)
        msg.reply_text("Activated NSFW Mode!")
        message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"ACTIVATED_NSFW\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        )
        return message
    else:
        msg.reply_text("NSFW Mode is already Activated for this chat!")
        return ""


@user_admin
@gloggable
def rem_nsfw(update: Update, context: CallbackContext):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    is_nsfw = sql.is_nsfw(chat.id)
    if not is_nsfw:
        msg.reply_text("NSFW Mode is already Deactivated")
        return ""
    else:
        sql.rem_nsfw(chat.id)
        msg.reply_text("Rolled Back to SFW Mode!")
        message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"DEACTIVATED_NSFW\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        )
        return message


def list_nsfw_chats(update: Update, context: CallbackContext):
    chats = sql.get_all_nsfw_chats()
    text = "<b>NSFW Activated Chats</b>\n"
    for chat in chats:
        try:
            x = context.bot.get_chat(int(*chat))
            name = x.title if x.title else x.first_name
            text += f"• <code>{name}</code>\n"
        except BadRequest:
            sql.rem_nsfw(*chat)
        except Unauthorized:
            sql.rem_nsfw(*chat)
        except RetryAfter as e:
            sleep(e.retry_after)
    update.effective_message.reply_text(text, parse_mode="HTML")


def neko(update, context):
    msg = update.effective_message
    target = "neko"
    msg.reply_photo(nekos.img(target))


def feet(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "feet"
    msg.reply_photo(nekos.img(target))


def yuri(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "yuri"
    msg.reply_photo(nekos.img(target))


def trap(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "trap"
    msg.reply_photo(nekos.img(target))


def futanari(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "futanari"
    msg.reply_photo(nekos.img(target))


def hololewd(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "hololewd"
    msg.reply_photo(nekos.img(target))


def lewdkemo(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "lewdkemo"
    msg.reply_photo(nekos.img(target))


def sologif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "solog"
    msg.reply_video(nekos.img(target))


def feetgif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "feetg"
    msg.reply_video(nekos.img(target))


def cumgif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "cum"
    msg.reply_video(nekos.img(target))


def erokemo(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "erokemo"
    msg.reply_photo(nekos.img(target))


def lesbian(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "les"
    msg.reply_video(nekos.img(target))


def wallpaper(update, context):
    msg = update.effective_message
    target = "wallpaper"
    msg.reply_photo(nekos.img(target))


def lewdk(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "lewdk"
    msg.reply_photo(nekos.img(target))


def ngif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "ngif"
    msg.reply_video(nekos.img(target))


def tickle(update, context):
    msg = update.effective_message
    target = "tickle"
    msg.reply_video(nekos.img(target))


def lewd(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "lewd"
    msg.reply_photo(nekos.img(target))


def feed(update, context):
    msg = update.effective_message
    target = "feed"
    msg.reply_video(nekos.img(target))


def eroyuri(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "eroyuri"
    msg.reply_photo(nekos.img(target))


def eron(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "eron"
    msg.reply_photo(nekos.img(target))


def cum(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "cum_jpg"
    msg.reply_photo(nekos.img(target))


def bjgif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "bj"
    msg.reply_video(nekos.img(target))


def bj(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "blowjob"
    msg.reply_photo(nekos.img(target))


def nekonsfw(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "nsfw_neko_gif"
    msg.reply_video(nekos.img(target))


def solo(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "solo"
    msg.reply_photo(nekos.img(target))


def kemonomimi(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "kemonomimi"
    msg.reply_photo(nekos.img(target))


def avatarlewd(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "nsfw_avatar"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


def gasm(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "gasm"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


def poke(update, context):
    msg = update.effective_message
    target = "poke"
    msg.reply_video(nekos.img(target))


def anal(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "anal"
    msg.reply_video(nekos.img(target))


def hentai(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "hentai"
    msg.reply_photo(nekos.img(target))


def avatar(update, context):
    msg = update.effective_message
    target = "nsfw_avatar"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


def erofeet(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "erofeet"
    msg.reply_photo(nekos.img(target))


def holo(update, context):
    msg = update.effective_message
    target = "holo"
    msg.reply_photo(nekos.img(target))


def keta(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "keta"
    if not target:
        msg.reply_text("No URL was received from the API!")
        return
    msg.reply_photo(nekos.img(target))


def pussygif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "pussy"
    msg.reply_video(nekos.img(target))


def tits(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "tits"
    msg.reply_photo(nekos.img(target))


def holoero(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "holoero"
    msg.reply_photo(nekos.img(target))


def pussy(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "pussy_jpg"
    msg.reply_photo(nekos.img(target))


def hentaigif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "random_hentai_gif"
    msg.reply_video(nekos.img(target))


def classic(update, context):
    msg = update.effective_message
    target = "classic"
    msg.reply_video(nekos.img(target))


def kuni(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "kuni"
    msg.reply_video(nekos.img(target))


def waifu(update, context):
    msg = update.effective_message
    target = "waifu"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


def kiss(update, context):
    msg = update.effective_message
    target = "kiss"
    msg.reply_video(nekos.img(target))


def femdom(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "femdom"
    msg.reply_photo(nekos.img(target))


def hug(update, context):
    msg = update.effective_message
    target = "cuddle"
    msg.reply_video(nekos.img(target))


def erok(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "erok"
    msg.reply_photo(nekos.img(target))


def foxgirl(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "fox_girl"
    msg.reply_photo(nekos.img(target))


def titsgif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "boobs"
    msg.reply_video(nekos.img(target))


def ero(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "ero"
    msg.reply_photo(nekos.img(target))


def smug(update, context):
    msg = update.effective_message
    target = "smug"
    msg.reply_video(nekos.img(target))


def baka(update, context):
    msg = update.effective_message
    target = "baka"
    msg.reply_video(nekos.img(target))


def dva(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    nsfw = requests.get("https://api.computerfreaker.cf/v1/dva").json()
    url = nsfw.get("url")
    # do shit with url if you want to
    if not url:
        msg.reply_text("No URL was received from the API!")
        return
    msg.reply_photo(url)


ADD_NSFW_HANDLER = CommandHandler("addnsfw", add_nsfw, run_async=True)
REMOVE_NSFW_HANDLER = CommandHandler("rmnsfw", rem_nsfw, run_async=True)
LIST_NSFW_CHATS_HANDLER = CommandHandler(
    "nsfwchats", list_nsfw_chats, filters=CustomFilters.dev_filter, run_async=True
)
LEWDKEMO_HANDLER = CommandHandler("lewdkemo", lewdkemo, run_async=True)
NEKO_HANDLER = CommandHandler("neko", neko, run_async=True)
FEET_HANDLER = CommandHandler("feet", feet, run_async=True)
YURI_HANDLER = CommandHandler("yuri", yuri, run_async=True)
TRAP_HANDLER = CommandHandler("trap", trap, run_async=True)
FUTANARI_HANDLER = CommandHandler("futanari", futanari, run_async=True)
HOLOLEWD_HANDLER = CommandHandler("hololewd", hololewd, run_async=True)
SOLOGIF_HANDLER = CommandHandler("sologif", sologif, run_async=True)
CUMGIF_HANDLER = CommandHandler("cumgif", cumgif, run_async=True)
EROKEMO_HANDLER = CommandHandler("erokemo", erokemo, run_async=True)
LESBIAN_HANDLER = CommandHandler("lesbian", lesbian, run_async=True)
WALLPAPER_HANDLER = CommandHandler("wallpaper", wallpaper, run_async=True)
LEWDK_HANDLER = CommandHandler("lewdk", lewdk, run_async=True)
NGIF_HANDLER = CommandHandler("ngif", ngif, run_async=True)
TICKLE_HANDLER = CommandHandler("tickle", tickle, run_async=True)
LEWD_HANDLER = CommandHandler("lewd", lewd, run_async=True)
FEED_HANDLER = CommandHandler("feed", feed, run_async=True)
EROYURI_HANDLER = CommandHandler("eroyuri", eroyuri, run_async=True)
ERON_HANDLER = CommandHandler("eron", eron, run_async=True)
CUM_HANDLER = CommandHandler("cum", cum, run_async=True)
BJGIF_HANDLER = CommandHandler("bjgif", bjgif, run_async=True)
BJ_HANDLER = CommandHandler("bj", bj, run_async=True)
NEKONSFW_HANDLER = CommandHandler("nekonsfw", nekonsfw, run_async=True)
SOLO_HANDLER = CommandHandler("solo", solo, run_async=True)
KEMONOMIMI_HANDLER = CommandHandler("kemonomimi", kemonomimi, run_async=True)
AVATARLEWD_HANDLER = CommandHandler("avatarlewd", avatarlewd, run_async=True)
GASM_HANDLER = CommandHandler("gasm", gasm, run_async=True)
POKE_HANDLER = CommandHandler("poke", poke, run_async=True)
ANAL_HANDLER = CommandHandler("anal", anal, run_async=True)
HENTAI_HANDLER = CommandHandler("hentai", hentai, run_async=True)
AVATAR_HANDLER = CommandHandler("avatar", avatar, run_async=True)
EROFEET_HANDLER = CommandHandler("erofeet", erofeet, run_async=True)
HOLO_HANDLER = CommandHandler("holo", holo)
TITS_HANDLER = CommandHandler("tits", tits, run_async=True)
PUSSYGIF_HANDLER = CommandHandler("pussygif", pussygif, run_async=True)
HOLOERO_HANDLER = CommandHandler("holoero", holoero, run_async=True)
PUSSY_HANDLER = CommandHandler("pussy", pussy, run_async=True)
HENTAIGIF_HANDLER = CommandHandler("hentaigif", hentaigif, run_async=True)
CLASSIC_HANDLER = CommandHandler("classic", classic, run_async=True)
KUNI_HANDLER = CommandHandler("kuni", kuni, run_async=True)
WAIFU_HANDLER = CommandHandler("waifu", waifu, run_async=True)
LEWD_HANDLER = CommandHandler("lewd", lewd, run_async=True)
KISS_HANDLER = CommandHandler("kiss", kiss, run_async=True)
FEMDOM_HANDLER = CommandHandler("femdom", femdom, run_async=True)
CUDDLE_HANDLER = CommandHandler("hug", hug, run_async=True)
EROK_HANDLER = CommandHandler("erok", erok, run_async=True)
FOXGIRL_HANDLER = CommandHandler("foxgirl", foxgirl, run_async=True)
TITSGIF_HANDLER = CommandHandler("titsgif", titsgif, run_async=True)
ERO_HANDLER = CommandHandler("ero", ero, run_async=True)
SMUG_HANDLER = CommandHandler("smug", smug, run_async=True)
BAKA_HANDLER = CommandHandler("baka", baka, run_async=True)
DVA_HANDLER = CommandHandler("dva", dva, run_async=True)


dispatcher.add_handler(ADD_NSFW_HANDLER)
dispatcher.add_handler(REMOVE_NSFW_HANDLER)
dispatcher.add_handler(LIST_NSFW_CHATS_HANDLER)
dispatcher.add_handler(LEWDKEMO_HANDLER)
dispatcher.add_handler(NEKO_HANDLER)
dispatcher.add_handler(FEET_HANDLER)
dispatcher.add_handler(YURI_HANDLER)
dispatcher.add_handler(TRAP_HANDLER)
dispatcher.add_handler(FUTANARI_HANDLER)
dispatcher.add_handler(HOLOLEWD_HANDLER)
dispatcher.add_handler(SOLOGIF_HANDLER)
dispatcher.add_handler(CUMGIF_HANDLER)
dispatcher.add_handler(EROKEMO_HANDLER)
dispatcher.add_handler(LESBIAN_HANDLER)
dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(LEWDK_HANDLER)
dispatcher.add_handler(NGIF_HANDLER)
dispatcher.add_handler(TICKLE_HANDLER)
dispatcher.add_handler(LEWD_HANDLER)
dispatcher.add_handler(FEED_HANDLER)
dispatcher.add_handler(EROYURI_HANDLER)
dispatcher.add_handler(ERON_HANDLER)
dispatcher.add_handler(CUM_HANDLER)
dispatcher.add_handler(BJGIF_HANDLER)
dispatcher.add_handler(BJ_HANDLER)
dispatcher.add_handler(NEKONSFW_HANDLER)
dispatcher.add_handler(SOLO_HANDLER)
dispatcher.add_handler(KEMONOMIMI_HANDLER)
dispatcher.add_handler(AVATARLEWD_HANDLER)
dispatcher.add_handler(GASM_HANDLER)
dispatcher.add_handler(POKE_HANDLER)
dispatcher.add_handler(ANAL_HANDLER)
dispatcher.add_handler(HENTAI_HANDLER)
dispatcher.add_handler(AVATAR_HANDLER)
dispatcher.add_handler(EROFEET_HANDLER)
dispatcher.add_handler(HOLO_HANDLER)
dispatcher.add_handler(TITS_HANDLER)
dispatcher.add_handler(PUSSYGIF_HANDLER)
dispatcher.add_handler(HOLOERO_HANDLER)
dispatcher.add_handler(PUSSY_HANDLER)
dispatcher.add_handler(HENTAIGIF_HANDLER)
dispatcher.add_handler(CLASSIC_HANDLER)
dispatcher.add_handler(KUNI_HANDLER)
dispatcher.add_handler(WAIFU_HANDLER)
dispatcher.add_handler(LEWD_HANDLER)
dispatcher.add_handler(KISS_HANDLER)
dispatcher.add_handler(FEMDOM_HANDLER)
dispatcher.add_handler(CUDDLE_HANDLER)
dispatcher.add_handler(EROK_HANDLER)
dispatcher.add_handler(FOXGIRL_HANDLER)
dispatcher.add_handler(TITSGIF_HANDLER)
dispatcher.add_handler(ERO_HANDLER)
dispatcher.add_handler(SMUG_HANDLER)
dispatcher.add_handler(BAKA_HANDLER)
dispatcher.add_handler(DVA_HANDLER)

__handlers__ = [
    ADD_NSFW_HANDLER,
    REMOVE_NSFW_HANDLER,
    LIST_NSFW_CHATS_HANDLER,
    NEKO_HANDLER,
    FEET_HANDLER,
    YURI_HANDLER,
    TRAP_HANDLER,
    FUTANARI_HANDLER,
    HOLOLEWD_HANDLER,
    SOLOGIF_HANDLER,
    CUMGIF_HANDLER,
    EROKEMO_HANDLER,
    LESBIAN_HANDLER,
    WALLPAPER_HANDLER,
    LEWDK_HANDLER,
    NGIF_HANDLER,
    TICKLE_HANDLER,
    LEWD_HANDLER,
    FEED_HANDLER,
    EROYURI_HANDLER,
    ERON_HANDLER,
    CUM_HANDLER,
    BJGIF_HANDLER,
    BJ_HANDLER,
    NEKONSFW_HANDLER,
    SOLO_HANDLER,
    KEMONOMIMI_HANDLER,
    AVATARLEWD_HANDLER,
    GASM_HANDLER,
    POKE_HANDLER,
    ANAL_HANDLER,
    HENTAI_HANDLER,
    AVATAR_HANDLER,
    EROFEET_HANDLER,
    HOLO_HANDLER,
    TITS_HANDLER,
    PUSSYGIF_HANDLER,
    HOLOERO_HANDLER,
    PUSSY_HANDLER,
    HENTAIGIF_HANDLER,
    CLASSIC_HANDLER,
    KUNI_HANDLER,
    WAIFU_HANDLER,
    LEWD_HANDLER,
    KISS_HANDLER,
    FEMDOM_HANDLER,
    LEWDKEMO_HANDLER,
    CUDDLE_HANDLER,
    EROK_HANDLER,
    FOXGIRL_HANDLER,
    TITSGIF_HANDLER,
    ERO_HANDLER,
    SMUG_HANDLER,
    BAKA_HANDLER,
    DVA_HANDLER,
]

"""
__help__ = 
*NSFW:*
❂ /addnsfw : Enable NSFW mode
❂ /rmnsfw : Disable NSFW mode
 
*Available commands:*  
❂ /neko: Sends Random SFW Neko source Images.
❂ /feet: Sends Random Anime Feet Images.
❂ /yuri: Sends Random Yuri source Images.
❂ /trap: Sends Random Trap source Images.
❂ /futanari: Sends Random Futanari source Images.
❂ /hololewd: Sends Random Holo Lewds.
❂ /lewdkemo: Sends Random Kemo Lewds.
❂ /sologif: Sends Random Solo GIFs.
❂ /cumgif: Sends Random Cum GIFs.
❂ /erokemo: Sends Random Ero-Kemo Images.
❂ /lesbian: Sends Random Les Source Images.
❂ /lewdk: Sends Random Kitsune Lewds.
❂ /ngif: Sends Random Neko GIFs.
❂ /tickle: Sends Random Tickle GIFs.
❂ /lewd: Sends Random Lewds.
❂ /feed: Sends Random Feeding GIFs.
❂ /eroyuri: Sends Random Ero-Yuri source Images.
❂ /eron: Sends Random Ero-Neko source Images.
❂ /cum: Sends Random Cum Images.
❂ /bjgif: Sends Random Blow Job GIFs.
❂ /bj: Sends Random Blow Job source Images.
❂ /nekonsfw: Sends Random NSFW Neko source Images.
❂ /solo: Sends Random NSFW Neko GIFs.
❂ /kemonomimi: Sends Random KemonoMimi source Images.
❂ /avatarlewd: Sends Random Avater Lewd Stickers.
❂ /gasm: Sends Random Orgasm Stickers.
❂ /poke: Sends Random Poke GIFs.
❂ /anal: Sends Random Anal GIFs.
❂ /hentai: Sends Random Hentai source Images.
❂ /avatar: Sends Random Avatar Stickers.
❂ /erofeet: Sends Random Ero-Feet source Images.
❂ /holo: Sends Random Holo source Images.
❂ /tits: Sends Random Tits source Images.
❂ /pussygif: Sends Random Pussy GIFs.
❂ /holoero: Sends Random Ero-Holo source Images.
❂ /pussy: Sends Random Pussy source Images.
❂ /hentaigif: Sends Random Hentai GIFs.
❂ /classic: Sends Random Classic Hentai GIFs.
❂ /kuni: Sends Random Pussy Lick GIFs.
❂ /waifu: Sends Random Waifu Stickers.
❂ /kiss: Sends Random Kissing GIFs.
❂ /femdom: Sends Random Femdom source Images.
❂ /cuddle: Sends Random Cuddle GIFs.
❂ /erok: Sends Random Ero-Kitsune source Images.
❂ /foxgirl: Sends Random FoxGirl source Images.
❂ /titsgif: Sends Random Tits GIFs.
❂ /ero: Sends Random Ero source Images.
❂ /smug: Sends Random Smug GIFs.
❂ /baka: Sends Random Baka Shout GIFs.
❂ /dva: Sends Random D.VA source Images.
"""


__mod_name__ = "Nsfw​"
