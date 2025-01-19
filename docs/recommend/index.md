# 今日推荐(自动生成)

> 老胡的信息周刊**历史信息回顾**，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个**留存**以及**共享**。


## 🎯 项目 

### [PanIndex](https://github.com/libsgh/PanIndex)

网盘目录列表，目前支持天翼云、teambition盘、阿里云盘、OneDrive等：

- 跨平台、易部署
- 多模式、多网盘
- 多主题
- 下载直链
- 防盗链
- 短链、分享
- 访问控制
- 分流
- WebDav

![PanIndex](https://images-1252557999.file.myqcloud.com/uPic/PanIndex.jpg) 

### [sql-studio](https://github.com/frectonz/sql-studio)

SQL 数据库浏览器，支持 `SQLite、libSQL、PostgreSQL、MySQL&DuckDB`，可以理解成一个简洁轻量的数据库客户端，安装使用也很简单：

```shell
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/frectonz/sql-studio/releases/download/0.1.23/sql-studio-installer.sh | sh
# 以周刊数据库为例
sql-studio --address=0.0.0.0:3030 sqlite /Users/howie/Documents/workspace/weekly/weekly.db
```

这样通过 Web 即可查看数据库信息：

- 数据库整体元数据信息概览
- 表格数据浏览
- 自定义查询（提示不全面，如果能接入 AI 感觉会更好）

![sql-studio](https://images-1252557999.file.myqcloud.com/uPic/sql-studio.jpg) 

### [talebook](https://github.com/talebook/talebook)

这是一个基于Calibre的简单的个人图书管理系统，支持在线阅读。主要特点是：

- 美观的界面：由于Calibre自带的网页太丑太难用，于是基于Vue，独立编写了新的界面，支持PC访问和手机浏览；
- 支持多用户：为了网友们更方便使用，开发了多用户功能，支持豆瓣（已废弃）、QQ、微博、Github等社交网站的登录；
- 支持在线阅读：借助Readium.js 库，支持了网页在线阅读电子书；
- 支持批量扫描导入书籍；
- 支持邮件推送：可方便推送到Kindle；
- 支持OPDS：可使用KyBooks等APP方便地读书；
- 支持一键安装，网页版初始化配置，轻松启动网站；
- 优化大书库时文件存放路径，可以按字母分类、或者文件名保持中文；
- 支持快捷更新书籍信息：支持从百度百科、豆瓣搜索并导入书籍基础信息；
- 支持私人模式：需要输入访问码，才能进入网站，便于小圈子分享网站；

![talebook](https://images-1252557999.file.myqcloud.com/uPic/VmLmag.png) 

## 🤖 软件 

### [mytv-android](https://github.com/yaoxieyoulei/mytv-android)

使用 Android 原生开发的电视直播软件：

![mytv-android](https://cdn.jsdelivr.net/gh/howie6879/oss/uPic/mytv-android.jpg)

老胡试了不是很稳定，大家可根据地域使用测试。 

### [Free-NTFS-for-Mac](https://github.com/hoochanlon/Free-NTFS-for-Mac)

这是一款支持苹果芯片的 `Free NTFS for Mac` 小工具软件，主要是为了方便想要免费使用 `NTFS` 格式移动存储的文件拷贝与共享的苹果电脑用户：

![Free-NTFS-for-Mac](https://images-1252557999.file.myqcloud.com/uPic/Free-NTFS-for-Mac.png) 

### [oneAnime](https://github.com/Predidit/oneAnime)

一款简洁清爽无广告的看番软件。 一款带弹幕的 anime1 第三方客户端，界面符合 Material You 规范：

![oneAnime](https://images-1252557999.file.myqcloud.com/uPic/oneAnime.jpg) 

## 👀 资料 

### [rCore-Tutorial-Book 第三版](https://rcore-os.github.io/rCore-Tutorial-Book-v3/index.html)

清华大学的开源教程，这本教程旨在一步一步展示如何从零开始用 Rust 语言写一个基于 RISC-V 架构的 类 Unix 内核，值得注意的是，本项目不仅支持模拟器环境（如 Qemu/terminus 等），还支持在真实硬件平台 Kendryte K210 上运行。

更新记录如下：

- 2020-11-03：环境搭建完成，开始着手编写文档。
- 2020-11-13：第一章完成。
- 2020-11-27：第二章完成。
- 2020-12-20：前七章代码完成。
- 2021-01-10：第三章完成。
- 2021-01-18：加入第零章。
- 2021-01-30：第四章完成。
- 2021-02-16：第五章完成。
- 2021-02-20：第六章完成。
- 2021-03-06：第七章完成。到这里为止第一版初稿就已经完成了。
- 2021-10-20：第八章代码于前段时间完成。开始更新前面章节文档及完成第八章文档。

热乎着，有兴趣可以试试。热乎着，有兴趣可以试试，这里一份[读书笔记](https://github.com/hemashushu/practice-toy-os-riscv-rust)可以参考。 

### [just-react](https://github.com/BetaSu/just-react)

「React技术揭秘」 一本自顶向下的React源码分析书 

### [craftinginterpreters_zh](https://github.com/GuoYaxiang/craftinginterpreters_zh)

这是一个还在进行中的翻译项目，原项目是[craftinginterpreters](https://github.com/munificent/craftinginterpreters)，同时还有配套的英文书，可免费[在线阅读](http://www.craftinginterpreters.com/)。

该书由一门小型的自创语言Lox开始，分别使用Java和C实现了两种类型的解释器，jlox和clox，其中前者是将语法解析成Java中的表示代码，主要依赖Java本身的语法能力实现代码的真正运行；后者则采用了类似编译和虚拟机的机制，实现了一个看上去“更高效”的解释器：

![craftinginterpreters](https://images-1252557999.file.myqcloud.com/uPic/craftinginterpreters.jpg) 

## 🕸 网站 

### [iconfont](https://www.iconfont.cn/)

阿里巴巴矢量图标库：

![iconfont](https://images-1252557999.file.myqcloud.com/uPic/iconfont.jpg) 

### [emojiall](https://www.emojiall.com/)

网站提供了最新、完整的 `Emoji` 搜索和相关信息， 包括表情符号含义、使用示例、`Unicode` 代码点、高分辨率图片、复制和粘贴， 以及 `Emoji` 大数据排名等：

![emojiall](https://images-1252557999.file.myqcloud.com/uPic/emojiall.jpg) 

### [uxdatabase](https://www.uxdatabase.io/)

国外一个免费开放的产品设计教程，包含了设计基础、产品规划与探索、交互设计、产品原型设计、开发与测试、技能训练等六大模块的相关知识：

![uxdatabase](https://images-1252557999.file.myqcloud.com/uPic/uxdatabase.jpg) 

## ✍️ 说明

周刊相关信息：

- 公众号：[老胡的储物柜](https://images-1252557999.file.myqcloud.com/uPic/ETIbMe.jpg)，欢迎加我微信进**周刊群聊**
- [TG 频道订阅](https://t.me/howie_weekly)：老胡周刊 TG 信息频道，对周刊的信息补充，会分享更多的资源，欢迎关注👏
- [聚合周刊](https://www.fre321.com/weekly)：老胡收集了国内外60+优质技术周刊进行信息聚合🔥
- Github 地址：[howie6879/weekly/](https://github.com/howie6879/weekly/)，觉得不错麻烦给我一个**Star**，谢谢 ❤️
- 浏览地址：[老胡的信息周刊](https://weekly.howie6879.com) | [今日推荐](https://weekly.howie6879.com/recommend/index.html) | [MacOS 软件推荐](https://weekly.howie6879.com/soft/mac.html)

🙌如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是**同道中人**，所以如果你有自认为不错的信息获取渠道，欢迎**留言**或者**私聊**我，谢谢。