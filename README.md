    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ 」─
</h3>

<p align="center"><a href="https://dashboard.heroku.com/new?template=https://github.com/Yuuichiexe/waitoo"> <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

<p align="center"><a href="https://heroku-deployer.herokuapp.com"> <img src="https://img.shields.io/badge/Redirect%20To%20Heroku-black?style=for-the-badge&logo=heroku" width="200" height="35.45"/></a></p>


# Horix Example Plugin Format

## Advanced: Decorators
```python3

from Hori.modules.helper_funcs.decorators import Horicmd
from telegram import Update
from telegram.ext import CallbackContext

@Horicmd(command='hi', pass_args=True)
def hello(update: Update, context: CallbackContext):
    message = update.effective_message
    message.reply_text("hello")

    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There
"""
```



## Advanced: Pyrogram
```python3
from Hori import pgram

Hori_PYRO_Hello = filters.command("hi")

@pgram.on_message(Hori_PYRO_Hello) & ~filters.edited & ~filters.bot)
async def hmm(client, message):
    j = "Hello there"
    await message.reply(j)
    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There
"""
```

## Advanced: Telethon
```python3

from Hori import tbot
from Hori.events import register

@register(pattern="^/hi$")
async def hmm(event):
    j = "Hello there"
    await event.reply(j)
    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There
"""
```

## Advanced: PTB
```python3

from Hori import dispatcher
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

def hi(update: Update, context: CallbackContext):
    j = "hello"
    update.effective_message.reply_text(j)

HANDLER = CommandHandler("hi", hi, run_async=True)
dispatcher.add_handler(HANDLER)

__handlers__ = [ HANDLER, ]
    
__mod_name__ = "Hi"
__help__ = """
<b>Hi</b>
- /hi: Say Hello There
"""
```
