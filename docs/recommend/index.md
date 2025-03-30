# 今日推荐(自动生成)

> 老胡的信息周刊**历史信息回顾**，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个**留存**以及**共享**。


## 🎯 项目 

### [onelist](https://github.com/msterzhang/onelist)

一个类似emby的专注于刮削alist聚合网盘形成影视媒体库的程序:

- alist挂载云盘后能在网页端看视频，却没有分类，没有海报墙
- 使用webdav挂载本地后，用jellyfin或者emby刮削会下载视频截取封面导致封号
- 用jellyfin或者emby之类，没有大带宽公网ip，在外难以访问

![onelist](https://images-1252557999.file.myqcloud.com/uPic/telegram-cloud-photo-size-4-5997957576333046318-y.jpg) 

### [markdown-nice](https://github.com/mdnice/markdown-nice)

有很多朋友问我的公众号排版是怎么做的，答案就是`markdown-nice`开源项目：

> 支持主题设计的 Markdown 编辑器，让排版变 Nice

你可以选择直接访问[官方](https://editor.mdnice.com/)，也可以自建，自建的好处是不需要登录，下面截图就是我自建的：

![](https://images-1252557999.file.myqcloud.com/uPic/oGeICY.png)

官方并不支持`Docker`部署，为了方便大家使用，直接用我打包上传的镜像，一行命令即可体验`mdnice`:

```shell
docker run --name mdnice -p 8080:80 -d howie6879/mdnice:22.02.11
``` 

### [cadvisor](https://github.com/google/cadvisor)

一个免费开源的容器监控工具，可以实时统计容器运行时占用的资源：

- CPU 利用率
- 内存使用量
- 网络传输等信息

同时提供了 Web 可视化页面，支持 `prometheus` 格式输出，非常优秀。

![cadvisor](https://images-1252557999.file.myqcloud.com/uPic/cadvisor.jpg)

如果使用过程有镜像代理问题，可以参考 [gcr.io_mirror](https://github.com/anjia0532/gcr.io_mirror) 项目。 

## 🤖 软件 

### [AppManager](https://github.com/MuntashirAkon/AppManager)

一个功能全面的 `Android` 包管理器和应用查看器，支持复制自由软件的功能，提供了丰富的应用管理和操作功能，如列出应用信息、安装 / 卸载 `APK`、备份 / 恢复应用、查看日志等，同时支持根权限和 `ADB` 命令，以实现更高级的操作，如撤销权限、修改 `APP` 操作模式等：

![AppManager](https://images-1252557999.file.myqcloud.com/uPic/zIgjSp.png) 

### [TinyPNG4Mac](https://github.com/kyleduo/TinyPNG4Mac)

`TinyPNG`的`Mac`客户端：

![TinyPNG4Mac](https://images-1252557999.file.myqcloud.com/uPic/TinyPNG4Mac.png) 

### [milky-warp](https://github.com/hugoattal/milky-warp)

`Milky Warp` 是一个开源工具，技术栈是 `Tauri、Vite、Vue、Typescript`，核心功能就是按下快捷键时会显示一个放大镜：

- 按下可配置的快捷键时显示放大镜
- 支持使用鼠标滚轮进行放大和缩小
- 跨平台：可在Windows、macOS和Linux上运行

![milky-warp](https://images-1252557999.file.myqcloud.com/uPic/milky-warp.gif) 

## 👀 资料 

### [Leetcode-retag](https://github.com/resumejob/Leetcode-retag)

重新分类 Leetcode 高频题 2021 版

- 题目按照面试频率降序排列
- 增加难度分类，适合从简单开始学习
- 增加细分类别，例如单调栈，前缀树等，一道题目可能会有多个类别 

### [The-Site-Reliability-Workbook-CHS](https://github.com/redbearder/The-Site-Reliability-Workbook-CHS)

站点可靠性工作手册：

![The-Site-Reliability-Workbook-CHS](https://images-1252557999.file.myqcloud.com/uPic/The-Site-Reliability-Workbook-CHS.jpg) 

### [nlp-tutorial](https://github.com/shibing624/nlp-tutorial)

自然语言处理（NLP）教程，包括：词向量，词法分析，预训练语言模型，文本分类，文本语义匹配，信息抽取，翻译，对话。

![nlp-tutorial](https://images-1252557999.file.myqcloud.com/uPic/nlp-tutorial.jpg) 

## 🕸 网站 

### [apivault.dev](https://apivault.dev/)

免费开源的公共 `API` 网站：

![apivault](https://images-1252557999.file.myqcloud.com/uPic/apivault.jpg) 

### [PDF Squeezer](https://www.witt-software.com/pdfsqueezer/)

PDF Squeezer 是一款 PDF 压缩工具：

![PDFSqueezer](https://images-1252557999.file.myqcloud.com/uPic/PDF%20Squeezer.jpg) 

### [fontawesome](https://fontawesome.com/icons/)

比较完善全面的图标网站：

![fontawesome](https://images-1252557999.file.myqcloud.com/uPic/fontawesome.jpg) 

## ✍️ 说明

周刊相关信息：

- 公众号：[老胡的储物柜](https://images-1252557999.file.myqcloud.com/uPic/ETIbMe.jpg)，欢迎加我微信进**周刊群聊**
- [TG 频道订阅](https://t.me/howie_weekly)：老胡周刊 TG 信息频道，对周刊的信息补充，会分享更多的资源，欢迎关注👏
- [聚合周刊](https://www.fre321.com/weekly)：老胡收集了国内外60+优质技术周刊进行信息聚合🔥
- Github 地址：[howie6879/weekly/](https://github.com/howie6879/weekly/)，觉得不错麻烦给我一个**Star**，谢谢 ❤️
- 浏览地址：[老胡的信息周刊](https://weekly.howie6879.com) | [今日推荐](https://weekly.howie6879.com/recommend/index.html) | [MacOS 软件推荐](https://weekly.howie6879.com/soft/mac.html)

🙌如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是**同道中人**，所以如果你有自认为不错的信息获取渠道，欢迎**留言**或者**私聊**我，谢谢。