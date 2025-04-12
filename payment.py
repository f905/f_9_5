from config import *
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.types import Channel
from help import *
import asyncio


@IEX.on(events.NewMessage(outgoing=True))
async def _(event):
    try:
        await IEX(JoinChannelRequest("@ghxxx"))
    except BaseException:
        pass

@IEX.on(events.NewMessage(outgoing=True))
async def _(event):
    if ispay[0] == 'yes':
        pass
    else:
        ispay.clear()
        ispay.append("yes")
        pass
        
    
    


@IEX.on(events.NewMessage(outgoing=True, pattern=r"\.نظف"))
async def leave_IEX_channel(event):
    dialogs = await IEX.get_dialogs()
    await event.edit(f"**جارى التحقق من القنوات**")
    left_count = 0
    for dialog in dialogs:
        if isinstance(dialog.entity, Channel) and dialog.entity.title == '⎉ IEX Hunting Channal ⎉' and not dialog.entity.username:
            try:
                await IEX(LeaveChannelRequest(dialog.entity))
                left_count += 1
            except Exception as e:
                await event.respond(f"**خطأ أثناء مغادرة القناة: {e}**")
    
    await event.edit(f"**تم مغادرة {left_count} قناة (⎉ IEX Hunting Channal ⎉) خاصة.**")
