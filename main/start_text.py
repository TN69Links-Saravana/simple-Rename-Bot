from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="<b>Tʜɪs Is Pᴇʀsᴏɴᴀʟ Usᴇ Bᴏᴛ 🙏. Dᴏ Yᴏᴜ Wᴀɴᴛ Yᴏᴜʀ Oᴡɴ Bᴏᴛ? 👇 Cʟɪᴄᴋ Tʜᴇ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ Tᴏ Dᴇᴘʟᴏʏ</b>"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ 🤖", url="https://github.com/TN69Links-Saravana/Simple-Rename-Bot")
        ],[
        InlineKeyboardButton("🖥️ Hᴏᴡ Tᴏ Dᴇᴘʟᴏʏ 🖥️", url="https://youtube.com/@TN69Links")
    ]])
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"<b>Hᴇʟʟᴏ {msg.from_user.mention} I Aᴍ Sɪᴍᴘʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ Wɪᴛʜ Pᴇʀsᴏɴᴀʟ Usᴀɢᴇ.\nTʜɪs Bᴏᴛ Is Mᴀᴅᴇ Bʏ :</b> <b><a href=https://t.me/Cute_Boy_Saravana>Ƭɴ69 ×͜× Sᴀʀᴀᴠᴀɴᴀ࿐</a></b>"                                     
    button= [[
        InlineKeyboardButton("🦋 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ 🦋", url="https://t.me/TN69Links")
        ],[
        InlineKeyboardButton("𖣘 Hᴇʟᴘ", callback_data="help"),
        InlineKeyboardButton("✪⁠ Aʙᴏᴜᴛ", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "<b>Jᴜsᴛ Sᴇɴᴅ A Fɪʟᴇ Aɴᴅ /rename <new name> Wɪᴛʜ Rᴇᴘʟᴀʏᴇᴅ Yᴏᴜʀ Fɪʟᴇ\n\n"
    txt += "Sᴇɴᴅ Pʜᴏᴛᴏ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ Aᴜᴛᴏᴍᴀᴛɪᴄ \n"
    txt += "/view Tᴏ Sᴇᴇ Yᴏᴜʀ Tʜᴜᴍʙɴᴀɪʟ  \n"
    txt += "/del Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Tʜᴜᴍʙɴᴀɪʟ</b>"
    button= [[        
        InlineKeyboardButton("🚫 Cʟᴏsᴇ", callback_data="del"),
        InlineKeyboardButton("⬅️ Bᴀᴄᴋ", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/Cute_Boy_Saravana>Ƭɴ69 ×͜× Sᴀʀᴀᴠᴀɴᴀ࿐</a>"  
    Source="<a href=https://github.com/TN69Links-Saravana/Simple-Rename-Bot>Click Here</a>"
    txt=f"<b>Mʏ Nᴀᴍᴇ : {me.mention}\nSᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ : <a href=https://t.me/RoyalxMovies>Jᴏɪɴ Hᴇʀᴇ</a>\n🌸 YᴏᴜTᴜʙᴇ Cʜᴀɴɴᴇʟ : <a href=https://youtube.com/@TN69Links>Sᴜʙsᴄʀɪʙᴇ Nᴏᴡ</a>\n😈 Mʏ Mᴀsᴛᴇʀ : {Master}\nSᴏᴜʀᴄᴇ Cᴏᴅᴇ : {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Cʟᴏsᴇ", callback_data="del"),
        InlineKeyboardButton("⬅️ Bᴀᴄᴋ", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


