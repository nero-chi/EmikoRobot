from pyrogram import filters
from pyrogram.types import (
    Message, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton, 
    Chat, 
    CallbackQuery,
)
from NaoRobot import pbot


@pbot.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Here is help menu, in this menu you can several the command
click the button to get the description of the command""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Admins", callback_data="cbadmins"),
                    InlineKeyboardButton("Anime", callback_data="cbanime"),
                    InlineKeyboardButton("Anti-Spam", callback_data="cbantispam")
                ],
                [
                    InlineKeyboardButton("Connect", callback_data="cbconnect"),
                    InlineKeyboardButton("Extra", callback_data="cbextra"),
                    InlineKeyboardButton("F-Subs", callback_data="cbfsub")
                ],
                [
                    InlineKeyboardButton("Federation", callback_data="cbfed"),
                    InlineKeyboardButton("Fun", callback_data="cbfun"),
                    InlineKeyboardButton("Greetings", callback_data="cbgreetings")
                ],
                [
                    InlineKeyboardButton("User", callback_data="cbuser"),
                    InlineKeyboardButton("Locks", callback_data="cblocks"),
                    InlineKeyboardButton("Music", callback_data="cbmusic")
                ],
                [
                    InlineKeyboardButton("Upload", callback_data="cbupload"),
                    InlineKeyboardButton("Stickers", callback_data="cbsticker"),
                    InlineKeyboardButton("Report", callback_data="cbreport")
                ],
                [
                    InlineKeyboardButton("Nsfw", callback_data="cbnsfw"),
                    InlineKeyboardButton("Google", callback_data="cbgoogle"),
                    InlineKeyboardButton("Tools", callback_data="cbtools")
                ],
                [
                    InlineKeyboardButton("Logomaker", callback_data="cblogo"),
                    InlineKeyboardButton("Chatbot", callback_data="cbchatbot"),
                    InlineKeyboardButton("Filters", callback_data="cbfilters"),
                ],
                [
                    InlineKeyboardButton("🔙 Back home", callback_data="cbhome"
                    )
                ]
            ]
        ),
    )
 

@pbot.on_callback_query(filters.regex("cbadmins"))
async def cbadmins(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Here is the admin permission""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Ban/Mute", callback_data="cbban"),
                    InlineKeyboardButton("Approval", callback_data="cbapproval"),
                    InlineKeyboardButton("Backup", callback_data="cbbackup")
                ],
                [
                    InlineKeyboardButton("Disabling", callback_data="cbdisabling")
                ],
                [
                    InlineKeyboardButton("🔙 Back", callback_data="cbhelp"
                    )
                ]
            ]
        ),
    )


@pbot.on_callback_query(filters.regex("cbban"))
async def cbban(_, query: CallbackQuery):
    await query.edit_message_text(
        """Here is the help for the Bans/Mutes module:

User Commands:
  `• /kickme:` kicks the user who issued the command
  
Admins only:
  `• /ban` (userhandle): bans a user. (via handle, or reply)
  banme
  `• /sban` (userhandle): Silently ban a user. Deletes command, Replied message and doesn't reply. (via handle, or reply)
  `• /tban (userhandle) x(m/h/d): bans a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
  `• /unban` (userhandle): unbans a user. (via handle, or reply)
  `• /kick` (userhandle): kicks a user out of the group, (via handle, or reply)
  `• /mute` (userhandle): silences a user. Can also be used as a reply, muting the replied to user.
  `• /tmute` (userhandle) x(m/h/d): mutes a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
  `• /unmute` (userhandle): unmutes a user. Can also be used as a reply, muting the replied to user.
  `• /zombies`: searches deleted accounts
  `• /zombies clean`: removes deleted accounts from the group.
  `• /snipe` (chatid) (string): Make me send a message to a specific chat.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Back", callback_data="cbadmins"
                    )
                ]
            ]
        ),
    )


@pbot.on_callback_query(filters.regex("cbapproval"))
async def cbapprov(_, query: CallbackQuery):
    await query.edit_message_text(
        """Here is the help for the Approvals module:

Sometimes, you might trust a user not to send unwanted content.
Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.

That's what approvals are for - approve of trustworthy users to allow them to send

Admin commands:
- `/approval`: Check a user's approval status in this chat.
- `/approve`: Approve of a user. Locks, blacklists, and antiflood won't apply to them anymore.
- `/unapprove`: Unapprove of a user. They will now be subject to locks, blacklists, and antiflood again.
- `/approved`: List all approved users.
- `/unapproveall`: Unapprove ALL users in a chat. This cannot be undone.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Back", callback_data="cbadmins"
                    )
                ]
            ]
        ),
    )


@pbot.on_callback_query(filters.regex("cbbackup"))
async def cbbackup(_, query: CallbackQuery):
    await query.edit_message_text(
        """Here is the help for the Backups module:

Only for group owner:

 `• /import`: Reply to the backup file for the butler / emilia group to import as much as possible, making transfers very easy!  Note that files / photos cannot be imported due to telegram restrictions.

 `• /export`: Export group data, which will be exported are: rules, notes (documents, images, music, video, audio, voice, text, text buttons)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Back", callback_data="cbadmins"
                    )
                ]
            ]
        ),
    )


@pbot.on_callback_query(filters.regex("cbdisabling"))
async def cbdisable(_, query: CallbackQuery):
    await query.edit_message_text(
        """Here is the help for the Disabling module:

• `/cmds`: check the current status of disabled commands

Admins only:
• `/enable` (cmd name): enable that command
• `/disable` (cmd name): disable that command
• `/enablemodule` (module name): enable all commands in that module
• `/disablemodule` (module name): disable all commands in that module
• `/listcmds`: list all possible toggleable commands""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔙 Back", callback_data="cbadmins"
                    )
                ]
            ]
        ),
    )

