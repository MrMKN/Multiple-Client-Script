# Multiple-Client-Script


### Used Method 👇
``` python
"""
This sets up and starts all defined Clients one after another and keeps them idle,
waiting for input until stopped.
"""

from pyrogram import Client, Filters

app1 = Client("app1")
app2 = Client("app2")
# app_ = Client("app_")

filt = Filters.command("test")


# You can define individual handlers ...
@app1.on_message(filt)
def test1(a, m):
    m.reply("App 1 response")


# ... like these two.
@app2.on_message(filt)
def test2(a, m):
    m.reply("App 2 response")


# Or stack the decorator to have multiple Clients handle the same update
@app1.on_message(filt)
@app2.on_message(filt)
def test_all(a, m):
    m.reply("App response")


# Starting all individually, one after another
app1.start()
app2.start()
# app_.start()

Client.idle()

# Same for stopping, one after another
app1.stop()
app2.stop()
# app_.stop()
```

### THANKS TO

➪ [Mhdrzn ❣️](https://github.com/Mhdrzn)
➪ [ColinShark ❣️](https://gist.github.com/ColinShark)
