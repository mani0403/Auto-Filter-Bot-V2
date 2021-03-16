#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_text(
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Group", url="https://t.me/books_tamil"),
                        InlineKeyboardButton("Channel", url="https://t.me/bookss_tamil"),
                    ],
                    [
                        InlineKeyboardButton(
                            "⭕️ whatsapp status channnel ⭕️", url="https://t.me/whatsapp_tamil")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

