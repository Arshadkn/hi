#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '๐๏ธ'join ๐๏ธ, url="https://t.me/movievillagegroup"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('๐๏ธ' Group ๐๏ธ, url='https://t.me/movievillagegroup'),
        InlineKeyboardButton('๐ท๐๐๐ ๐ค', callback_data="help")
    ],[
        InlineKeyboardButton('๐ฃ๏ธcreate your own', url='https://youtu.be/uAHl5jvnrhk')
    ],[
        InlineKeyboardButton('๐๏ธour group๐๏ธ', url='https://t.me/movievillagegroup'),
        InlineKeyboardButton('๐๏ธsupport๐๏ธ', url='https://t.me/movievillagegroup:')
    ],[
        InlineKeyboardButton('๐ฅ ๐คjoin๐ค ๐ฅ', url='https://t.me/fanik77')
   ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('๐๏ธHome๐๏ธ', callback_data='start'),
        InlineKeyboardButton('๐ฐ๐๐๐๐ ๐ฉ', callback_data='about')
    ],[
        InlineKeyboardButton('๐ ๐ฒ๐๐๐๐ ๐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('๐ค @๐ผ๐๐_๐๐ ๐ค', url='https://t.me/fanik77')
    ],[
        InlineKeyboardButton('๐ค @arshad6153 ๐ค', url='https://t.me/fanik77')
    ],[
        InlineKeyboardButton('๐? ๐ท๐๐๐', callback_data='start'),
        InlineKeyboardButton('๐ฒ๐๐๐๐ ๐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
