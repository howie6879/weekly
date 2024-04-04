"""
    Created by howie.hu at 2021-10-30.
    Description: 周刊初始化脚本
    Changelog: all notable changes to this file will be documented
"""
import os
import re

import yaml

from src.db import parse_md
from src.gen_sitemap import gen_sitemap
from src.rss import gen_rss


def read_mkdocs_config(path=""):
    """读取mkdocs配置

    Args:
        path (str): 可选，mkdocs配置路径
    """
    config_path = path or os.path.join(os.path.dirname(__file__), "mkdocs.yml")
    with open(config_path, "r", encoding="utf-8") as f:
        result = f.read()
        return yaml.load(result, Loader=yaml.FullLoader)


def write_mkdocs_config(data: dict, path=""):
    """写入mkdocs配置

    Args:
        data (dict): 配置数据
        path (str): 可选，mkdocs配置路径
    """
    config_path = path or os.path.join(os.path.dirname(__file__), "mkdocs.yml")
    with open(config_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True)


def gen_weekly_content(years: int):
    """年度周刊汇总

    Args:
        years (int): 年份
    """
    root_path = os.path.dirname(__file__)
    target_path = os.path.join(root_path, f"docs/{years}")

    with open(f"./{years}_weekly_all.md", "w", encoding="utf-8") as pf:
        file_list = []
        for file in os.listdir(target_path):
            if str(file).endswith(".md"):
                # 目标文件
                file_path = os.path.join(target_path, file)
                file_list.append(file_path)

        for each in sorted(file_list):
            with open(each, "r", encoding="utf-8") as f:
                # pf.write(f'<div class="page-break"></div>\n\n' + f.read() + "\n\n")
                pf.write(f"以下是{years}年周刊\n\n" + f.read() + "\n\n")


def gen_weekly_title(years: int):
    """生成周刊标题

    Args:
        years (int): 年份
    """
    root_path = os.path.dirname(__file__)
    target_path = os.path.join(root_path, f"docs/{years}")
    res_dict = {}
    for file in os.listdir(target_path):
        if str(file).endswith(".md") and "老胡的周刊" in file:
            # 目标文件
            match_obj = re.compile(r"第(.*?)期").search(file)[1]
            res_dict[match_obj] = f"{file}"
    res_list = []
    for i in sorted(res_dict):
        file_name = res_dict[i]
        date_cycle = file_name.split(".")[0]
        # print(file_name)
        print(f"- 第{i}期 ({date_cycle}): ./{years}/{file_name}")
        res_list.append({f"第{i}期 ({date_cycle})": f"./{years}/{file_name}"})

    # 获取yaml配置
    mkdocs_config = read_mkdocs_config()
    # 赋值
    for each in mkdocs_config["nav"]:
        for key, _ in each.items():
            if str(years) in key:
                # 倒序
                each[key] = res_list[::-1]
    # 写入新配置
    write_mkdocs_config(mkdocs_config)


if __name__ == "__main__":
    # 生成年度周刊内容合集
    # gen_weekly_content(2023)
    # exit()
    # 生成 sitemap
    # 使用 https://www.xml-sitemaps.com/ 生成 sitemap
    # gen_sitemap()
    # 持久化周刊到 DB
    parse_md()
    # 生成 RSS
    gen_rss()
    # 生成最新周刊
    gen_weekly_title(2024)
