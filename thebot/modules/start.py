from thebot import dankbot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from thebot.utils.errors import capture_err


@dankbot.on_message(~filters.me & filters.command('start', prefixes='/'), group=8)
@capture_err
async def start(_, message):
   if message.chat.type == "private":
     if len(message.text.split()) >= 2:
       suckz = message.text.split()[1]
       if suckz == "help":
          buttons = [
                     [
                        InlineKeyboardButton('Anime', switch_inline_query_current_chat='anime '),
                        InlineKeyboardButton('Manga', switch_inline_query_current_chat='manga ')
                     ],
                     [
                        InlineKeyboardButton('Airing', switch_inline_query_current_chat='airing '),
                        InlineKeyboardButton('Character', switch_inline_query_current_chat='char ')
                     ]
                  ]
          await message.reply_text('Available cmds for now :\n /animeinfo - search anime on AniList\n /mangainfo - search manga on Anilist\n /charinfo - search character on Anilist\n /airinfo - check airing status of an anime\n /wa by replying to a media - find what anime a media is from\n.', reply_markup=InlineKeyboardMarkup(buttons))
     else:
       photo = "https://telegra.ph/file/f154371daaca23b7268e9.jpg"
       buttons = [
            [
            InlineKeyboardButton('Anime', switch_inline_query_current_chat='anime '),
            InlineKeyboardButton('Manga', switch_inline_query_current_chat='manga ')
            ],
            [
            InlineKeyboardButton('Airing', switch_inline_query_current_chat='airing '),
            InlineKeyboardButton('Character', switch_inline_query_current_chat='char ')
            ],
            [
            InlineKeyboardButton('Help', 'help'),
            ]
                  ]
       await message.reply_photo(photo,
         caption='Hi,\nCheck Help to know what I can do ;)\nSeach in Inline by Clicking these buttons below!',
         reply_markup=InlineKeyboardMarkup(buttons))
   else:
       await message.reply_text("Hey!. Iam Souya!")
