"""
    Created by howie.hu at 2023-12-04.
    Description: 发送配置
    Changelog: all notable changes to this file will be documented
"""
import os

BASE_DIR = os.path.dirname(__file__)
SENDER_CACHE_PATH = {
    "tg": os.path.join(BASE_DIR, "json/tg_sender.json"),
    "tg_tmp": os.path.join(BASE_DIR, "json/tg_tmp.json"),
    "tg_tmp_error": os.path.join(BASE_DIR, "json/tg_tmp_error.json"),
}
TG_TMP_PATH = os.path.join(os.path.dirname(__file__), "md/tg_tmp.md")
