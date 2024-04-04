"""
    Created by howie.hu at 2023-03-14.
    Description: 文件重命名
    Changelog: all notable changes to this file will be documented
"""


import os

DOCS_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")
print(DOCS_PATH)
for each in os.listdir(DOCS_PATH):
    if each.startswith("20"):
        # 年份
        weekly_year = each
        # 周刊文件在对应年份下面
        year_path = DOCS_PATH + "/" + weekly_year

        for file in os.listdir(year_path):
            if "我的周刊" in file:
                file_path = f"{year_path}/{file}"
                t_file_path = file_path.replace("我的", "老胡的")
                os.system(f"mv {file_path} {t_file_path}")
