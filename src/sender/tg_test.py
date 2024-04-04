"""
    Created by howie.hu at 2023-12-04.
    Description: 有时候发送失败，单独测试
    export http_proxy=http://0.0.0.0:1090;export https_proxy=http://0.0.0.0:1090;
    PIPENV_DOTENV_LOCATION=./dev.env pipenv run python ./src/sender/tg_test.py
    Changelog: all notable changes to this file will be documented
"""
import asyncio
import os

from src.sender.tg_utils import send_to_tg

data = {
    "text": """👉 名称：[webdesk](https://webdesk.pigjs.com/)
🤖 类型：🕸网站
👏 介绍：一键将网站转化为桌面应用程序：""",
    "image_link": "https://cdn.jsdelivr.net/gh/howie6879/oss/uPic/EOn4M8.png",
}


result = asyncio.run(
    send_to_tg(
        chat_id=os.getenv("TG_CHAT_ID"),
        text=data["text"],
        image_link=data["image_link"],
    )
)

print(result)
