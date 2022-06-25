"""
    Created by howie.hu at 2022-05-10.
    Description: 持久化周刊数据到数据库
    Changelog: all notable changes to this file will be documented
"""
import os
import re
import sqlite3

DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "weekly.db")


def init_db():
    """
    数据库初始化，每次更新重新建立数据库
    """
    if os.path.isfile(DB_FILE):
        os.remove(DB_FILE)

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        """
        create table items
        (
            id            integer primary key autoincrement,
            weekly_year   integer     NOT NULL,
            weekly_number integer     NOT NULL,
            item_type     varchar(10) NOT NULL,
            item_content  text
        )
        """
    )
    conn.commit()
    cursor.close()
    conn.close()


def parse_md() -> list:
    """
    获取所有周刊md文件地址
    """
    # 数据库初始化
    init_db()
    base_path = "./docs"
    for each in os.listdir(base_path):
        if each.startswith("20"):
            # 年份
            weekly_year = each
            # 周刊文件在对应年份下面
            year_path = base_path + "/" + weekly_year
            for file in os.listdir(year_path):
                if "我的周刊" in file and "md" in file:
                    full_file_path = year_path + "/" + file
                    # 基础数据
                    weekly_number: int = 0
                    md_str = ""
                    with open(full_file_path, "r", encoding="utf-8") as fp:
                        md_str = fp.read()
                    # 解析周刊号
                    weekly_number = int(re.compile(r"第(.*?)期").search(md_str)[1])
                    # 读取 🎯 项目 部分内容
                    repo_str = (
                        re.compile(r"## 🎯 项目(.*?)## 🤖 软件", flags=re.S)
                        .search(md_str)[1]
                        .strip()
                    )
                    # 读取 🤖 软件 部分内容
                    soft_str = (
                        re.compile(r"## 🤖 软件(.*?)## 👀 资料", flags=re.S)
                        .search(md_str)[1]
                        .strip()
                    )
                    # 读取 👀 资料 部分内容
                    data_str = (
                        re.compile(r"## 👀 资料(.*?)## 🕸 网站", flags=re.S)
                        .search(md_str)[1]
                        .strip()
                    )
                    # 读取 🕸 网站 部分内容
                    web_str = (
                        re.compile(r"## 🕸 网站(.*?)## ✍️ 说明", flags=re.S)
                        .search(md_str)[1]
                        .strip()
                    )

                    db_data = {
                        "🎯 项目": repo_str,
                        "🤖 软件": soft_str,
                        "👀 资料": data_str,
                        "🕸 网站": web_str,
                    }

                    for key, value in db_data.items():
                        parse_item(weekly_year, weekly_number, key, value)
                        print(f"第 {weekly_number} 期周刊，类别：{key} 持久化完毕！")


def parse_item(weekly_year: int, weekly_number: int, item_type: str, content: str):
    """处理单个项目Item

    Args:
        weekly_year (int): 周刊年份
        weekly_number (int): 周刊号
        item_type (str): Item类型
        content (str): 文本内容
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    for each in content.split("###")[1:]:
        item_content = each.strip()
        if item_content:
            cursor.execute(
                f"insert into items values (NULL,'{weekly_year}', '{weekly_number}', '{item_type}', '{item_content}')"
            )
            conn.commit()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    parse_md()
