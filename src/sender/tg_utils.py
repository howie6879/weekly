"""
    Created by howie.hu at 2023-11-29.
    Description: TG 发送脚本工具
        PIPENV_DOTENV_LOCATION=./dev.env pipenv run python ./src/tg.py
    Changelog: all notable changes to this file will be documented
"""


import asyncio
import json
import os
import re

import telegram

import src.sender.config as sender_config

from src.utils import md5_encode


def append_to_json(key, value, file_type: str = "tg"):
    """
    读取 JSON 文件内容
    """
    file_path = sender_config.SENDER_CACHE_PATH[file_type]
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # 追加新的键值对
    data[key] = value

    # 写入 JSON 文件
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)


def parse_tg_tmp():
    """
    解析 MD 文件
    """
    tg_tmp_path = sender_config.TG_TMP_PATH
    md_str = ""
    with open(tg_tmp_path, "r", encoding="utf-8") as file:
        md_str = file.read()
    # 读取 🎯 项目 部分内容
    repo_str = re.compile(r"## 🎯 项目(.*?)## 🤖 软件", flags=re.S).search(md_str)[1].strip()
    # 读取 🤖 软件 部分内容
    soft_str = re.compile(r"## 🤖 软件(.*?)## 👀 资料", flags=re.S).search(md_str)[1].strip()
    # 读取 👀 资料 部分内容
    data_str = re.compile(r"## 👀 资料(.*?)## 🕸 网站", flags=re.S).search(md_str)[1].strip()
    # 读取 🕸 网站 部分内容
    web_str = re.compile(r"## 🕸 网站(.*?)## ✍️ 说明", flags=re.S).search(md_str)[1].strip()

    cat_dict = {
        "🎯 项目": repo_str,
        "🤖 软件": soft_str,
        "👀 资料": data_str,
        "🕸 网站": web_str,
    }

    return_data = []
    for cat, content in cat_dict.items():
        for each in content.split("###")[1:]:
            item_content = each.strip()
            if item_content:
                return_data.append(
                    {
                        "item_type": cat,
                        "item_content": item_content,
                    }
                )
    return return_data


async def send_to_tg(chat_id, text, image_link):
    """
    发送到 Telegram
    """
    bot = telegram.Bot(token=os.getenv("TG_BOT_TOKEN"))
    msg_key = md5_encode(text)
    if image_link:
        func = bot.send_photo(
            chat_id=chat_id,
            photo=image_link,
            caption=text,
            parse_mode="Markdown",
        )
    else:
        func = bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
    try:
        await asyncio.wait_for(func, timeout=10)
        return {"status": True, "info": "ok"}
    except Exception as e:
        return {"status": False, "info": str(e)}
