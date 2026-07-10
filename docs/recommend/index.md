# 今日推荐(自动生成)

> 老胡的信息周刊**历史信息回顾**，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个**留存**以及**共享**。


## 🎯 项目 

### [public-image-mirror](https://github.com/DaoCloud/public-image-mirror)

有一些 `Docker` 镜像托管在 `gcr.io`，这样国内下载就会很不方便，使用这个项目就可以快速下载，简单加个前缀就行：

```shell
k8s.gcr.io/coredns/coredns => m.daocloud.io/k8s.gcr.io/coredns/coredns
```

其他资源：

- 常用镜像仓库：[一些国内镜像源](https://gist.github.com/qwfys/aec4d2ab79281aeafebdb40b22d0b748)
- [x-mirrors/gcr.io](https://github.com/x-mirrors/gcr.io) 

### [Textual](https://github.com/Textualize/textual)

`Textual` 是一个 TUI (文本用户界面)的 Python 框架，灵感来自于现代 web 开发。

![Textual](https://images-1252557999.file.myqcloud.com/uPic/Textual.png) 

### [lobe-chat](https://github.com/lobehub/lobe-chat)

`LobeChat` 是一个开源的、可扩展的（Function Calling）高性能聊天机器人框架，它支持一键免费部署私人 `ChatGPT/LLM` 网页应用程序：

- 💨 快速部署：支持 Vercel 平台
-  💎 精致 UI 设计
-  🗣️ 流畅的对话体验
-  🧩 支持插件与自定义插件开发
-  🔒 隐私安全
-  🤖 自定义助手角色
-  🌐 自定义域名
-  🏬 角色市场

![lobe-chat](https://images-1252557999.file.myqcloud.com/uPic/lobe-chat.webp) 

## 🤖 软件 

### [lossless-cut](https://github.com/mifi/lossless-cut)

`LosslessCut` 是一个强大的跨平台视频/音频编辑工具，旨在通过快速且无损的操作，提供对视频、音频、字幕等媒体文件的剪辑和处理。它支持几乎所有主流视频和音频格式的无损剪切，能够快速提取视频中的精彩片段，而无需重新编码，从而保证画质不降低。此外，它还支持合并、重新排列、添加音轨或字幕、批量处理等功能，非常适合从相机、`GoPro`、无人机等设备中处理大文件。

特点包括：
- 支持大多数视频和音频格式的无损剪切
- 快速多文件工作流程和键盘快捷键操作
- 支持自定义时间段导出和编辑文件元数据
- 提供黑场检测、静音检测、场景变化检测等实用工具

`LosslessCut` 可以在不同操作系统上运行，并提供各种可执行文件下载选择，是处理和编辑媒体文件的理想选择。

![lossless-cut](https://images-1252557999.file.myqcloud.com/uPic/lossless-cut.jpg) 

### [social-media-copilot](https://github.com/iszhouhua/social-media-copilot)

社媒助手 - 小红书、抖音等平台数据采集的浏览器插件。支持一键导出无水印图片/视频、评论采集、作品数据采集、达人数据采集等功能：

![social-media-copilot](https://images-1252557999.file.myqcloud.com/uPic/HvvXRg.png) 

### [SwiftBar](https://github.com/swiftbar/SwiftBar)

一个开源工具，可以定制 Mac 电脑的菜单栏，通过简单的步骤在 `macOS` 上添加自定义菜单栏程序，提供大量小组件：

![SwiftBar](https://images-1252557999.file.myqcloud.com/uPic/SwiftBar.jpg) 

## 👀 资料 

### [分布式系统模式](https://github.com/dreamhead/patterns-of-distributed-systems)

[《分布式系统模式》（Patterns of Distributed Systems）](https://martinfowler.com/articles/patterns-of-distributed-systems/)是 `Unmesh Joshi` 编写的一系列关于分布式系统实现的文章。这个系列的文章采用模式的格式，介绍了像 Kafka、Zookeeper 这种分布式系统在实现过程采用的通用模式，是学习分布式系统实现的基础。

目前也提供了中文版：

![patterns-of-distributed-systems](https://images-1252557999.file.myqcloud.com/uPic/ZlA2Zu.png) 

### [note-hack](https://github.com/xdite/note-hack)

《打造超人笔记》是一本关于如何有效记录和整理笔记的书籍。

作者认为，笔记是一个看起来复杂但实际上比学习和阅读更简单的问题。通过拆解笔记的流程，作者发现主要问题的结构变得非常简单。此外，随着科技的发展，许多快速记录工具和笔记整理软件已经被发明出来，使笔记搜寻变得更加容易。

在本书中，作者探讨了如何通过做笔记和整理笔记来挖掘和整理自己对一个领域的各种答案。通过阅读本书，读者可以学习到如何使用各种工具和方法来提高自己的笔记能力，成为一个笔记超人。 

### [craftinginterpreters_zh](https://github.com/GuoYaxiang/craftinginterpreters_zh)

这是一个还在进行中的翻译项目，原项目是[craftinginterpreters](https://github.com/munificent/craftinginterpreters)，同时还有配套的英文书，可免费[在线阅读](http://www.craftinginterpreters.com/)。

该书由一门小型的自创语言Lox开始，分别使用Java和C实现了两种类型的解释器，jlox和clox，其中前者是将语法解析成Java中的表示代码，主要依赖Java本身的语法能力实现代码的真正运行；后者则采用了类似编译和虚拟机的机制，实现了一个看上去“更高效”的解释器：

![craftinginterpreters](https://images-1252557999.file.myqcloud.com/uPic/craftinginterpreters.jpg) 

## 🕸 网站 

### [zzollo](https://github.com/Sanix-Darker/zzollo)

开源项目搜索引擎，支持`Github, GitLab, Bitbucket `，在网地址访问地址为[zzollo.co](https://zzollo.co/)：

![zzollo](https://images-1252557999.file.myqcloud.com/uPic/NJXulr.png) 

### [myfirstnft](https://myfirstnft.info/)

我的第一个NFT，在这个网站，你可以：

- 理解NFT的价值
- 铸造一个免费的NFT
- 了解Web3.0

![myfirstnft](https://images-1252557999.file.myqcloud.com/uPic/myfirstnft.jpg) 

### [eja.tv](https://eja.tv/?)

提供3808个在线电视频道，包含143个国家以及82种不同语言。

![eja_tv](https://images-1252557999.file.myqcloud.com/uPic/eja_tv-min.png) 

## ✍️ 说明

周刊相关信息：

- 公众号：[老胡的储物柜](https://images-1252557999.file.myqcloud.com/uPic/ETIbMe.jpg)，欢迎加我微信进**周刊群聊**
- [TG 频道订阅](https://t.me/howie_weekly)：老胡周刊 TG 信息频道，对周刊的信息补充，会分享更多的资源，欢迎关注👏
- [聚合周刊](https://www.fre321.com/weekly)：老胡收集了国内外60+优质技术周刊进行信息聚合🔥
- Github 地址：[howie6879/weekly/](https://github.com/howie6879/weekly/)，觉得不错麻烦给我一个**Star**，谢谢 ❤️
- 浏览地址：[老胡的信息周刊](https://weekly.howie6879.com) | [今日推荐](https://weekly.howie6879.com/recommend/index.html) | [MacOS 软件推荐](https://weekly.howie6879.com/soft/mac.html)

🙌如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是**同道中人**，所以如果你有自认为不错的信息获取渠道，欢迎**留言**或者**私聊**我，谢谢。