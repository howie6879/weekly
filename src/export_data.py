"""
    Created by howie.hu at 2023-04-10.
    Description: 对数据库的数据进行导出操作
    Changelog: all notable changes to this file will be documented
"""
import datetime
import json
import os

from src.db import load_db

today = str(datetime.datetime.now().strftime("%Y-%m-%d"))


weekley_items = load_db()

intro = f"""
奇文共欣赏，疑义相与析。加油 🎉 大家好，我是老胡，一名热爱编程，分享经验思考的程序员。

我为什么要办老胡的信息周刊？核心目的是：每周记录我看到的有价值的信息，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个**留存**以及**共享**。当前阅读渠道如下：

- [网站](https://weekly.howie6879.com)
- [公众号](https://images-1252557999.file.myqcloud.com/uPic/ETIbMe.jpg)
- [周刊RSS](https://weekly.howie6879.com/rss/rss.xml)
- [今日推荐](https://weekly.howie6879.com/recommend)

在互联网时代，信息的**过滤**与**聚合**是非常重要的，作为一名程序员，我经常会浏览过程中看到各种有意思的项目、资源、软件以及一些网站，如果浏览目标让人眼前一亮，那就说明我**过滤**到了有意思的东西，一般我会选择相应的软件进行记录然后聚合起来慢慢看。

但随着时间流逝，一些好的资源总是错过了，或者某个瞬间想起来这东西但是不知道在哪查找。

看过即忘的感觉很不好，为什么不做一个自己的资源聚合呢？于是**老胡的周刊**项目诞生了，但不要以为这就结束了，周刊在我看来不过是一种分享的形式，算是我做的一次实验：

- 第一步我想构建一个以周刊为载体的资源分享形式，实践下若将资源聚合来持续地分享会产生怎样的效果，毕竟资源除了持续积累，还需要搭配有效的分享才会产生价值；
- 第二步是构建一套资源聚合分享流程，产生更多可玩的分享方式，让资源流动起来，让互联网上相关需求方的资源检索时间缩短；
- 最终可能会产出一个脚本或者一个产品，让子弹飞一段时间吧，我满含期待。

如果大家感兴趣，请持续关注老胡的周刊网站 [https://weekly.howie6879.com](https://weekly.howie6879.com)，也请移步[howie6879/weekly](https://github.com/howie6879/weekly/)给我一个`Star`支持下吧：

老胡的周刊开始于 2021-08-16，现在日期是 {today}，老胡的信息周刊一共发表了 {len(weekley_items)} 期，如果你在看到这篇文章的时候，我依旧在更新，那么这就是最好的消息，🙌如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是**同道中人**，所以如果你有自认为不错的信息获取渠道，欢迎**留言**或者**私聊**我，谢谢。
"""

t_data = [
    {
        "item_content": intro,
        "weekly_number": "",
        "weekly_date": "",
        "weekly_year": "",
        "item_type": "",
    }
]

for index, item in weekley_items.items():
    weekly_number = item["weekly_number"]
    weekly_year = item["weekly_year"]
    weekly_date = item["weekly_date"]
    for each_data in item["data"]:
        t_data.append(
            {
                "item_content": each_data["item_content"],
                "weekly_number": weekly_number,
                "weekly_date": weekly_date,
                "weekly_year": weekly_year,
                "item_type": each_data["item_type"],
            }
        )


# print(t_data)
WEEKLY_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "weekly.json")
with open(WEEKLY_FILE, "w", encoding="utf-8") as fp:
    json.dump(t_data, fp, ensure_ascii=False)
    # fp.write(json.dumps(t_data, ensure_ascii="utf8"))

# with open(WEEKLY_FILE, "w", encoding="utf8") as fp:
#     for index, item in weekley_items.items():
#         weekly_number = index
#         weekly_year = item["weekly_year"]
#         weekly_date = item["weekly_date"]
#         data = item["data"]

#         base_str = (
#             intro
#             + f"\n标题：老胡的信息周刊第{weekly_number}期({weekly_year}年{weekly_date})\n基本信息：\n1、周刊年份：{weekly_year}\n2、周刊时间周期：{weekly_date}\n接下来将介绍本期周刊的推荐项目信息。\n\n"
#         )
#         for p_index, each in enumerate(data):
#             item_type: str = each["item_type"]
#             item_content: str = each["item_content"]

#             project_name, project_href = item_content.split(")\n")[0].split("](")
#             project_name = project_name[1:]

#             base_str += f"第 {p_index+1} 个项目信息如下：\n\n项目类型：\n{item_type} \n\n项目名称：\n{project_name}\n\n项目链接:\n{project_href}\n\n"
#             base_str += f"项目介绍(MD语法):\n{item_content}\n\n"

#             # 解析项目名称和链接
#             # try:
#             # project_name, project_href = item_content.split(")\n")[0].split("](")
#             # print(project_name, project_href)
#             # except:
#             #     print(item_content)
#             # exit()

#         fp.write(base_str)
