#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [Countdown Timer Telegram bot by TeLe TiPs] (https://github.com/teletips/CountdownTimer-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/CountdownTimer-TeLeTiPs/blob/main/LICENSE
 
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import os
import asyncio
from plugins.teletips_t import *
from pyrogram.errors import FloodWait, MessageNotModified
from pyrogram.raw.functions.messages import UpdatePinnedMessage

bot=Client(
    "Countdown-TeLeTiPs",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

stoptimer = False

TELETIPS_MAIN_MENU_BUTTONS = [
            [
                InlineKeyboardButton('❓ HELP', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('👥 GROUP', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('📣 CHANNEL', url='https://t.me/education_bots_project_sl'),
                InlineKeyboardButton('👨‍💻 CREATOR', url='https://t.me/Video_chat_streamer')
            ],
            [
                InlineKeyboardButton('➕ CREATE YOUR BOT ➕', callback_data="TUTORIAL_CALLBACK")
            ]
        ]

@bot.on_message(filters.command(['start','help']) & filters.private)
async def start(client, message):
    text = START_TEXT
    reply_markup = InlineKeyboardMarkup(TELETIPS_MAIN_MENU_BUTTONS)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@bot.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery):
    if query.data=="HELP_CALLBACK":
        TELETIPS_HELP_BUTTONS = [
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_HELP_BUTTONS)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="GROUP_CALLBACK":
        TELETIPS_GROUP_BUTTONS = [
            [
                InlineKeyboardButton("🇱🇰 Anytime Any Qs", url="https://t.me/AnytimeAnyQs")
            ],
            [
                InlineKeyboardButton("🌎Edu_bot", url="https://t.me/education_bots_project_sl")
            ],
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_GROUP_BUTTONS)
        try:
            await query.edit_message_text(
                GROUP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass    

    elif query.data=="TUTORIAL_CALLBACK":
        TELETIPS_TUTORIAL_BUTTONS = [
            [
                InlineKeyboardButton("🎥 Video", url="https://t.me/TeLeTiPsOfficialChannel/462")
            ],
            [
                InlineKeyboardButton("⬅️ BACK", callback_data="START_CALLBACK"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_TUTORIAL_BUTTONS)
        try:
            await query.edit_message_text(
                TUTORIAL_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass      
          
    elif query.data=="START_CALLBACK":
        TELETIPS_START_BUTTONS = [
            [
                InlineKeyboardButton('❓ HELP', callback_data="HELP_CALLBACK")
            ],
            [
                InlineKeyboardButton('👥 GROUP', callback_data="GROUP_CALLBACK"),
                InlineKeyboardButton('📣 CHANNEL', url='https://t.me/education_bots_project_sl'),
                InlineKeyboardButton('👨‍💻 CREATOR', url='https://t.me/Video_chat_streamer')
            ],
            [
                InlineKeyboardButton('➕ CREATE YOUR BOT ➕', callback_data="TUTORIAL_CALLBACK")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(TELETIPS_START_BUTTONS)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass    



print("Countdown Timer is alive!")
bot.run()

#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
