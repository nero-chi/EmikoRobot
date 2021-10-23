from pyrogram import filters
from pyrogram.types import (
    Message, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton, 
    Chat, 
    CallbackQuery,
)
from NaoRobot import pbot


@pbot.on_callback_query(filters.regex("cbhlp"))
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
                    InlineKeyboardButton("Chatbot", callback_data="cbchatbot"),
                    InlineKeyboardButton("Fun", callback_data="cbfun"),
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
        f"""Here is the help for the Admin module:

Admins Play Major Roles To Manage A Group, We Have Created Some Hack Command In Our Bot So It Will Help To Manage Group Easily Via Bot.
You Just Need To Give Commands To Bot And But Will Work for You. Click On Bellow Buttons & Get Detailed Information.
 `• /admins`: list of admins in the chat""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Ban", callback_data="cbban"),
                    InlineKeyboardButton("Approval", callback_data="cbapproval"),
                    InlineKeyboardButton("Set Group", callback_data="cbgroup")
                ],
                [
                    InlineKeyboardButton("Muting", callback_data="cbmute"),
                    InlineKeyboardButton("Disabling", callback_data="cbdisabl"),
                    InlineKeyboardButton("Purge", callback_data="cbpurge")
                ],
                [
                    InlineKeyboardButton("Warns", callback_data="cbwarn"),
                    InlineKeyboardButton("Welcome", callback_data="cbwelcome"),
                    InlineKeyboardButton("Promote", callback_data="cbpromote")
                ],
                [
                    InlineKeyboardButton("🔙 Back", callback_data="cbhlp"
                    )
                ]
            ]
        ),
    )


@pbot.on_callback_query(filters.regex("cbban"))
async def cbban(_, query: CallbackQuery):
    await query.edit_message_text(
        """Here is the help for the Bans module:

👮 Admins only:

  `• /ban` (userhandle): bans a user. (via handle, or reply)
  `• /banme`: banned yourself, don't try it.
  `• /sban` (userhandle): Silently ban a user. Deletes command, Replied message and doesn't reply. (via handle, or reply)
  `• /tban` (userhandle) x(m/h/d): bans a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
  `• /unban` (userhandle): unbans a user. (via handle, or reply)
  `• /kick` (userhandle): kicks a user out of the group, (via handle, or reply)""",
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

@pbot.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    await query.edit_message_text(
        """👮 Admins only:

  `• /mute` (userhandle): silences a user. Can also be used as a reply, muting the replied to user.
  `• /tmute` (userhandle) x(m/h/d): mutes a user for x time. (via handle, or reply). m = minutes, h = hours, d = days.
  `• /unmute` (userhandle): unmutes a user. Can also be used as a reply, muting the replied to user.""",
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
async def cbapproval(_, query: CallbackQuery):
    await query.edit_message_text(
        """Here is the help for the Approvals module:

Sometimes, you might trust a user not to send unwanted content.
Maybe not enough to make them admin, but you might be ok with locks, blacklists, and antiflood not applying to them.

That's what approvals are for - approve of trustworthy users to allow them to send

👮Admin commands:

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


@pbot.on_callback_query(filters.regex("cbgroup"))
async def cbgroup(_, query: CallbackQuery):
    await query.edit_message_text(
        """👮Admins only:

  `• /pin`: silently pins the message replied to - add 'loud' or 'notify' to give notifs to users
  `• /unpin`: unpins the currently pinned message
  `• /invitelink`: gets invitelink
  •` /setgtitle` (newtitle): Sets new chat title in your group.
  `• /setgpic`: As a reply to file or photo to set group profile pic!
  `• /delgpic`: Same as above but to remove group profile pic.
  `• /setsticker`: As a reply to some sticker to set it as group sticker set!
  `• /setdescription` (description): Sets new chat description in group.
  `• /antispam` (on/off/yes/no): Will toggle our antispam tech or return your current settings.
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


@pbot.on_callback_query(filters.regex("cbpurge"))
async def cbpurge(_, query: CallbackQuery):
    await query.edit_message_text(
        """👮 Admins only:

  `• /del`: deletes the message you replied to
  `• /purge`: deletes all messages between this and the replied to message.
  `• /purge` (integer X): deletes the replied message, and X messages following it if replied to a message.""",
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


@pbot.on_callback_query(filters.regex("cbwelcome"))
async def cbwelcome(_, query: CallbackQuery):
    await query.edit_message_text(
        """Here is the help for the Greetings module:

👮 Admins only:

  `• /welcome` (on/off): enable/disable welcome messages.
  `• /welcome`: shows current welcome settings.
  `• /welcome noformat`: shows current welcome settings, without the formatting - useful to recycle your welcome messages!
  `• /goodbye`: same usage and args as /welcome.
  `• /setwelcome` (sometext): set a custom welcome message. If used replying to media, uses that media.
  `• /setgoodbye` (sometext): set a custom goodbye message. If used replying to media, uses that media.
  `• /resetwelcome`: reset to the default welcome message.
  `• /resetgoodbye`: reset to the default goodbye message.
  `• /cleanwelcome` (on/off): On new member, try to delete the previous welcome message to avoid spamming the chat.
  `• /welcomemutehelp`: gives information about welcome mutes.
  `• /cleanservice` (on/off): deletes telegrams welcome/left service messages.
 Example:
user joined chat, user left chat.
Welcome markdown:
  `• /welcomehelp`: view more formatting information for custom welcome/goodbye messages.""",
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


@pbot.on_callback_query(filters.regex("cbdisabl"))
async def cbdisable(_, query: CallbackQuery):
    await query.edit_message_text(
        """Here is the help for the Disabling module:

• `/cmds`: check the current status of disabled commands

👮 Admins only:

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


@pbot.on_callback_query(filters.regex("cbwarn"))
async def cbwarn(_, query: CallbackQuery):
    await query.edit_message_text(
        """👮 Admins only:

  `• /warns` <userhandle>: get a user's number, and reason, of warns.
  `• /warnlist`: list of all current warning filters
  `• /warn` (userhandle): warn a user. After 3 warns, the user will be banned from the group. Can also be used as a reply.
  `• /dwarn` (userhandle): warn a user and delete the message. After 3 warns, the user will be banned from the group. Can also be used as a reply.
  `• /resetwarn` (userhandle): reset the warns for a user. Can also be used as a reply.
  `• /addwarn` (keyword) (reply message): set a warning filter on a certain keyword. If you want your keyword to   be a sentence, encompass it with quotes, as such: /addwarn "very angry" This is an angry user.
  `• /nowarn` (keyword): stop a warning filter
  `• /warnlimit` (number): set the warning limit
  `• /strongwarn` (on/yes/off/no): If set to on, exceeding the warn limit will result in a ban. Else, will just punch.""",
