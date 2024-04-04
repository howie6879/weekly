"""
    Created by howie.hu at 2023-12-04.
    Description: 发送周刊到 TG，读取当前目录 tg_tmp.md 文件 文件格式和周刊格式一样
    export http_proxy=http://0.0.0.0:1090;export https_proxy=http://0.0.0.0:1090;
    PIPENV_DOTENV_LOCATION=./dev.env pipenv run python ./src/sender/tg_sender.py
    Changelog: all notable changes to this file will be documented
"""
import asyncio
import json
import os
import re
import time

from src.sender.tg_utils import append_to_json, parse_tg_tmp, send_to_tg, sender_config
from src.utils import md5_encode

with open(sender_config.SENDER_CACHE_PATH["tg_tmp"], "r", encoding="utf-8") as file:
    tg_cache_data = json.load(file)


for i in parse_tg_tmp():
    r_type = i["item_type"].replace(" ", "")
    r_title = i["item_content"].split("\n\n")[0].strip()
    r_content = i["item_content"].replace(r_title + "\n\n", "").strip()
    md_text = f"""
👉 名称：{r_title}
🤖 类型：{r_type}
👏 介绍：{r_content}
""".strip()
    try:
        image_link = re.findall(r"!\[.*?\]\((.*?)\)", md_text)[0]
    except IndexError:
        image_link = ""

    # 删除所有的图片链接
    pattern = r"!\[.*?\]\(.*?\)"
    # 使用正则表达式替换所有匹配项为空字符串
    md_text_without_images = (
        re.sub(pattern, "", md_text)
        .strip()
        .replace(":\n", "")
        .replace("：\n", "")
        .replace("\n\n", "")
        .strip()
    )

    if str(md_text_without_images).endswith(":"):
        md_text_without_images = md_text_without_images[:-1]

    msg_key = md5_encode(r_title)

    if msg_key in tg_cache_data:
        print(f"{r_title} 已经发送过了，跳过！")
    else:
        result = asyncio.run(
            send_to_tg(
                chat_id=os.getenv("TG_CHAT_ID"),
                text=md_text_without_images,
                image_link=image_link,
            )
        )
        if result["status"]:
            append_to_json(
                key=msg_key,
                value={
                    "text": md_text_without_images,
                    "image_link": image_link,
                },
                file_type="tg_tmp",
            )
            print(f"{r_title} 发送成功！")
        else:
            append_to_json(
                key=msg_key,
                value={
                    "text": md_text_without_images,
                    "image_link": image_link,
                },
                file_type="tg_tmp_error",
            )
            print(md_text_without_images)
            print(image_link)

            print(f"{r_title} 发送失败，原因：{result['info']}")
        time.sleep(5)
