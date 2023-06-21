"""
BSD 2-Clause License
Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2023-2024, Eren-YeagerO, [ https://github.com/Eren-YeagerO]
Copyright (c) 2023-2024, Programmer Network, [ https://github.com/Eren-YeagerO/Hori ]
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import asyncio
import datetime
from datetime import datetime

from telegram import __version__ as ptb
from telethon import Button

from Hori import BOT_NAME, BOT_USERNAME, SUPPORT_CHAT
from Hori import tbot as Horix
from Hori.events import register

edit_time = 5
""" =======================Horix====================== """
file1 = "https://graph.org/file/8af7c21f6b5c5dfb55241.jpg"
file2 = "https://graph.org/file/2808aba74d5f1667f71ee.jpg"
file3 = "https://graph.org/file/488755b1ed61dffb45dca.jpg"
file4 = "https://graph.org/file/354a3c1adb16121b89848.jpg"
""" =======================Horix====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount} {unit}{"" if amount == 1 else "s"}')
    return ", ".join(parts)


@register(pattern=("/alive"))
async def hmm(yes):
    await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    HoriX = f"**☘️I'm {BOT_NAME}\n👄I'm Working Perfectly **\n\n"
    HoriX += f"**✨My Uptime :** `{uptime}`\n\n"
    HoriX += f"**👺My Creator:** [TOAA](https://t.me/Itz_Shion_II)"
    BUTTON = [
        [
            Button.url("♻️Help", f"https://t.me/{BOT_USERNAME}?start=help"),
            Button.url("🌱Support", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    await Horix.send_file(yes.chat_id, file="https://graph.org/file/7d58c0096a704c8a93e21.mp4",caption=HoriX, buttons=BUTTON)
