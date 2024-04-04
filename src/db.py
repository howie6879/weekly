"""
    Created by howie.hu at 2022-05-10.
    Description: 持久化周刊数据到数据库
    Changelog: all notable changes to this file will be documented
"""
import os
import re
import sqlite3

DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "weekly.db")


def load_db():
    """
    加载数据
    """
    conn = sqlite3.connect(DB_FILE)
    # 获取游标
    cursor = conn.cursor()

    # 执行查询语句，获取结果
    cursor.execute("SELECT * FROM items ORDER BY weekly_number ASC")
    results = cursor.fetchall()

    # 关闭游标和数据库连接
    cursor.close()
    conn.close()

    # 将结果转换为列表，每个元素为一个字典
    items = {}
    for row in results:
        weekly_year = row[1]
        weekly_date = row[2]
        weekly_number = row[3]
        item_type = row[4]
        item_content = row[5]
        if items.get(weekly_number):
            # 存在，说明已经初始化
            items[weekly_number]["data"].append(
                {"item_type": item_type, "item_content": item_content}
            )
        else:
            items[weekly_number] = {
                "weekly_number": weekly_number,
                "weekly_year": weekly_year,
                "weekly_date": weekly_date,
                "data": [{"item_type": item_type, "item_content": item_content}],
            }
    return items


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
            weekly_date   varchar(10) NOT NULL,
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
                if "老胡的周刊" in file and "md" in file:
                    full_file_path = year_path + "/" + file
                    # 基础数据
                    weekly_number: int = 0
                    md_str = ""
                    with open(full_file_path, "r", encoding="utf-8") as fp:
                        md_str = fp.read()
                    weekly_date = file.split(".")[0]
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
                        parse_item(weekly_year, weekly_date, weekly_number, key, value)
                        print(f"第 {weekly_number} 期周刊，类别：{key} 持久化完毕！")


def parse_item(
    weekly_year: int, weekly_date: str, weekly_number: int, item_type: str, content: str
):
    """处理单个项目Item

    Args:
        weekly_year (int): 周刊年份
        weekly_date (int): 周刊日期
        weekly_number (int): 周刊号
        item_type (str): Item类型
        content (str): 文本内容
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    for each in content.split("###")[1:]:
        item_content = each.strip()
        if item_content:
            sql = f"insert into items values (NULL,'{weekly_year}', '{weekly_date}', '{weekly_number}', '{item_type}', '{item_content}')"
            cursor.execute(sql)
            conn.commit()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    parse_md()
