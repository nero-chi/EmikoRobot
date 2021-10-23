

import asyncio
import traceback
import os
from pathlib import Path
from datetime import datetime
from NaoRobot import telethn as tbot
from NaoRobot import OWNER_ID
from NaoRobot.events import register as pbot


DELETE_TIMEOUT = 5


# Send_Module

@pbot(pattern="^/send ?(.*)")
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./NaoRobot/modules/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
     message_id = event.message.id
     await event.client.send_file(
             event.chat_id,
             the_plugin_file,
        force_document=True,
        allow_cache=False,
        reply_to=message_id
    )
    end = datetime.now()
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()

# Install_Module

@pbot(pattern="^/install")
async def install(event):
    if event.fwd_from:
        return
    if event.sender_id == OWNER_ID:
        pass
    else:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "NaoRobot/modules/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                (shortname.replace(".py", ""))
                await event.reply("Your File Installed Successfully! \n `{}`".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                k = await event.reply("Errors! Cannot install this module.")
                await asyncio.sleep(2)
                await k.delete()
        except Exception as e:  # pylint:disable=C0103,W0703
            j = await event.reply(str(e))
            await asyncio.sleep(3)
            await j.delete()
            os.remove(downloaded_file_name)
    await asyncio.sleep(3)
    await event.delete()
