from pyrogram import Client, filters

api_id = 34571372
api_hash = "5f04e0a394bd1105244896f2e99fcb1c"
bot_token = "8576766768:AAGK4KR0m60j6vOj2rEEEHRTteqjjKOBUvU"

app = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.video)
async def receber_video(client, message):
    file_id = message.video.file_id
    
    link = f"https://t.me/{(await client.get_me()).username}?start={file_id}"
    
    await message.reply_text(f"🎬 Link do vídeo:\n{link}")

@app.on_message(filters.command("start"))
async def start(client, message):
    if len(message.command) > 1:
        file_id = message.command[1]
        await message.reply_video(file_id)
    else:
        await message.reply_text("Envie um vídeo!")

app.run()