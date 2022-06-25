"""
    Created by howie.hu at 2022-06-04.
    Description: 生成周刊RSS
    Changelog: all notable changes to this file will be documented
"""

import os
import re
import time

from feedgen.feed import FeedGenerator

BASE_URL = "https://weekly.howie6879.cn/"
DOCS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")
RSS_FILE = os.path.join(os.path.join(DOCS_PATH, "rss"), "rss.xml")


def gen_rss():
    """生成周刊RSS文件"""
    res_dict = {}

    for each in os.listdir(DOCS_PATH):
        if each.startswith("20"):
            # 年份
            weekly_year = each
            # 周刊文件在对应年份下面
            year_path = DOCS_PATH + "/" + weekly_year

            for file in os.listdir(year_path):
                if "我的周刊" in file:
                    full_file_path = year_path + "/" + file
                    # 目标文件
                    match_obj = re.compile(r"第(.*?)期").search(full_file_path)[1]
                    res_dict[match_obj] = {
                        "file_name": weekly_year + "/" + file,
                        "file_title": file,
                        "file_path": full_file_path,
                        "file_updated_at": os.path.getmtime(full_file_path),
                        "file_updated_at_date": time.strftime(
                            "%Y-%m-%d %H:%M:%S",
                            time.localtime(os.path.getmtime(full_file_path)),
                        ),
                    }
    # RSS Header
    # Header
    fg = FeedGenerator()
    fg.id("老胡的周刊")
    fg.title("老胡的周刊")
    fg.description(
        "我的信息周刊，每周记录我看到的有价值的信息，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个留存以及共享。"
    )
    fg.author({"name": "howie6879"})
    fg.link(href="https://github.com/howie6879/weekly", rel="self")
    fg.logo("https://images-1252557999.file.myqcloud.com/uPic/howie.jpg")
    fg.generator(
        generator="howie6879/weekly",
        uri="https://github.com/howie6879/weekly",
    )
    for i in sorted(res_dict)[-30:]:
        cur_data = res_dict[i]

        fe = fg.add_entry()
        file_name: str = cur_data["file_name"]
        fe.id(file_name)
        fe.title(cur_data["file_title"])
        fe.link(href=f"{BASE_URL}/{file_name.replace('md','html')}")
        fe.description("")
        fe.author(name="老胡的储物柜")
    # rss_data = str(fg.atom_str(pretty=True), "utf-8")
    fg.rss_file(RSS_FILE, pretty=True, encoding="utf-8")
    print("周刊RSS生成成功!")


if __name__ == "__main__":
    gen_rss()
