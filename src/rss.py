"""
    Created by howie.hu at 2022-06-04.
    Description: 生成周刊RSS
        pipenv run python src/rss.py
    Changelog: all notable changes to this file will be documented
"""

import datetime
import os
import re
import time

import markdown
import pytz

from feedgen.feed import FeedGenerator

BASE_URL = "https://weekly.howie6879.com/"
DOCS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")
RSS_FILE = os.path.join(DOCS_PATH, "rss/rss.xml")


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
                if "老胡的周刊" in file:
                    full_file_path = year_path + "/" + file
                    # 目标文件
                    match_obj = re.compile(r"第(.*?)期").search(full_file_path)[1]
                    with open(full_file_path, "r", encoding="utf-8") as fp:
                        article_name = file.replace(".md", "")
                        content = str(fp.read()).replace(f"# {article_name}\n", "")
                        content = f"> 如果样式查看有问题，可以通过网页浏览：[{article_name}](https://weekly.howie6879.com/{each}/{article_name}.html)\n{content}"
                        file_html = markdown.markdown(content)

                        res_dict[match_obj] = {
                            "weekly_year": weekly_year,
                            "file_name": weekly_year + "/" + file,
                            "file_title": file,
                            "file_path": full_file_path,
                            "file_html": file_html,
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
        "老胡的信息周刊，每周记录我看到的有价值的信息，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个留存以及共享。"
    )
    fg.author({"name": "howie6879"})
    fg.link(href="https://weekly.howie6879.com/", rel="self")
    fg.logo("https://weekly.howie6879.com/statics/images/howie.jpeg")
    fg.generator(
        generator="howie6879/weekly",
        uri="https://weekly.howie6879.com/",
    )
    for i in sorted(res_dict)[:]:
        cur_data = res_dict[i]

        fe = fg.add_entry()
        weekly_year = cur_data["weekly_year"]
        file_name: str = cur_data["file_name"]
        file_title: str = cur_data["file_title"]
        file_date = (
            str(weekly_year + "/" + file_name.split("~")[1].split(".老胡")[0]).replace(
                "/", "-"
            )
            + " 00:00:00"
        )
        fe.id(file_title)
        fe.title(cur_data["file_title"])
        fe.link(href=f"{BASE_URL}{file_name.replace('md','html')}")
        fe.description(f"<![CDATA[ {cur_data['file_html']} ]]>")
        fe.author(name="老胡的储物柜")
        dt = datetime.datetime.strptime(file_date, "%Y-%m-%d %H:%M:%S")
        beijing_tz = pytz.timezone("Asia/Shanghai")
        dt_with_tz = dt.replace(tzinfo=beijing_tz)
        fe.pubDate(dt_with_tz)
    # rss_data = str(fg.atom_str(pretty=True), "utf-8")
    fg.rss_file(RSS_FILE, pretty=True, encoding="utf-8")
    fg.rss_file(
        RSS_FILE.replace("rss/rss.xml", "index.xml"), pretty=True, encoding="utf-8"
    )
    print("周刊RSS生成成功!")


if __name__ == "__main__":
    gen_rss()
