# 今日推荐(自动生成)

> 老胡的信息周刊**历史信息回顾**，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个**留存**以及**共享**。


## 🎯 项目 

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

### [outline](https://github.com/outline/outline)

使用 `React &Node.js` 构建的协作知识库，支持团队协作，样式美观，可自建：

![outline](https://images-1252557999.file.myqcloud.com/uPic/outline.jpg) 

### [neko](https://github.com/m1k1o/neko)

可在服务器上运行的浏览器，核心功能如下：

- 娱乐层面可以在你的服务器上面部署这个虚拟浏览器，你会很**自由**
- 公司层面，有一些服务和限制你搭建 VPN 的话，你可以开放虚拟浏览器来进行内部服务访问，保证安全性
- 还有权限管理，也很方便远程演示，操作也还是很流畅的

![neko](https://images-1252557999.file.myqcloud.com/uPic/neko.jpg) 

## 🤖 软件 

### [EyesGuard](https://github.com/avestura/EyesGuard)

`Eyes Guard` 在你使用电脑时，根据设置的时间提醒你休息、保护眼睛（Windows）：

![EyesGuard](https://images-1252557999.file.myqcloud.com/uPic/EyesGuard.jpeg) 

### [TinyPNG4Mac](https://github.com/kyleduo/TinyPNG4Mac)

`TinyPNG`的`Mac`客户端：

![TinyPNG4Mac](https://images-1252557999.file.myqcloud.com/uPic/TinyPNG4Mac.png) 

### [yarr](https://github.com/nkanaev/yarr)

基于 `Web` 的 `RSS` 阅读器，可使用 `Docker` 快速体验：

```shell
mkdir -p ./yarr/data
docker run -it -p 7070:7070 -v $(pwd)/yarr/data:/data wbsu2003/yarr
```

总体来说还是挺简洁轻量的：

![yarr](https://images-1252557999.file.myqcloud.com/uPic/yarr.jpg) 

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

### [openmlsys-zh](https://github.com/openmlsys/openmlsys-zh)

机器学习系统：设计和实现，本开源项目试图给读者讲解现代机器学习系统的设计原理和实现经验。

![openmlsys](https://images-1252557999.file.myqcloud.com/uPic/openmlsys.jpg) 

### [python-guide-for-javascript-engineers](https://github.com/luckrnx09/python-guide-for-javascript-engineers)

《JavaScript 工程师的 Python 指南》是一本AI为主编写的开源电子书，涵盖了从 `Python` 环境安装到项目开发的方方面面。本书通过大量案例对比 `JavaScript` 和 `Python` 语言的异同，帮助 `JavaScript` 工程师快速掌握 `Python` 语言：

![python-guide-for-javascript-engineers](https://images-1252557999.file.myqcloud.com/uPic/python-guide-for-javascript-engineers.jpg) 

## 🕸 网站 

### [picdiet.eula.club](https://picdiet.eula.club/)

`Picdiet` 是一款在线批量压缩图片神器，它不需要后端服务器或者API的支持，仅通过你的浏览器来压缩图片大小，这意味着它压缩图片极快并且不会导致隐私或敏感图片泄漏：

![picdiet](https://images-1252557999.file.myqcloud.com/uPic/picdiet.jpg) 

### [send.internxt.com](https://send.internxt.com/)

文件上传分享网站，如果有临时文件传输的场景，可以使用：

![internxt](https://images-1252557999.file.myqcloud.com/uPic/internxt.jpg) 

### [caesium-image-compressor](https://caesium.app/)

免费开源的图片压缩工具：

![caesium](https://images-1252557999.file.myqcloud.com/uPic/caesium.png)

还支持[桌面端](https://github.com/Lymphatus/caesium-image-compressor)：

![caesium-image-compressor](https://images-1252557999.file.myqcloud.com/uPic/caesium-image-compressor.png) 

## ✍️ 说明

周刊相关信息：

- 公众号：[老胡的储物柜](https://images-1252557999.file.myqcloud.com/uPic/ETIbMe.jpg)，欢迎加我微信进**周刊群聊**
- [TG 频道订阅](https://t.me/howie_weekly)：老胡周刊 TG 信息频道，对周刊的信息补充，会分享更多的资源，欢迎关注👏
- [聚合周刊](https://www.fre321.com/weekly)：老胡收集了国内外60+优质技术周刊进行信息聚合🔥
- Github 地址：[howie6879/weekly/](https://github.com/howie6879/weekly/)，觉得不错麻烦给我一个**Star**，谢谢 ❤️
- 浏览地址：[老胡的信息周刊](https://weekly.howie6879.com) | [今日推荐](https://weekly.howie6879.com/recommend/index.html) | [MacOS 软件推荐](https://weekly.howie6879.com/soft/mac.html)

🙌如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是**同道中人**，所以如果你有自认为不错的信息获取渠道，欢迎**留言**或者**私聊**我，谢谢。