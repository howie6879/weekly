"""
    Created by howie.hu at 2021-10-30.
    Description: 周刊初始化脚本
    Changelog: all notable changes to this file will be documented
"""
import os
import re


def gen_weekly_title(years: int):
    """生成周刊标题

    Args:
        years (int): 年份
    """
    root_path = os.path.dirname(__file__)
    target_path = os.path.join(root_path, f"docs/{years}")
    res_dict = {}
    for file in os.listdir(target_path):
        if str(file).endswith(".md"):
            # 目标文件
            match_obj = re.compile(r"第(.*?)期").search(file)[1]
            res_dict[match_obj] = f"{file}"

    for i in sorted(res_dict):
        file_name = res_dict[i]
        date_cycle = file_name.split(".")[0]
        # print(file_name)
        print(f"- 第{i}期 ({date_cycle}): ./{years}/{file_name}")


if __name__ == "__main__":
    gen_weekly_title(2021)
