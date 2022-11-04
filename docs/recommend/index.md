# 今日推荐(自动生成)

> 我的信息周刊**历史信息回顾**，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个**留存**以及**共享**。


## 🎯 项目 

### [BGmi](https://github.com/BGmi/BGmi)

`BGmi` 用于订阅 `bangumi` 漫画更新的项目，支持 `Web UI` 和终端：

![BGmi](https://images-1252557999.file.myqcloud.com/uPic/BGmi.png) 

### [markdown-nice](https://github.com/mdnice/markdown-nice)

有很多朋友问我的公众号排版是怎么做的，答案就是`markdown-nice`开源项目：

> 支持主题设计的 Markdown 编辑器，让排版变 Nice

你可以选择直接访问[官方](https://editor.mdnice.com/)，也可以自建，自建的好处是不需要登录，下面截图就是我自建的：

![](https://img.turingark.com/uPic/oGeICY.png)

官方并不支持`Docker`部署，为了方便大家使用，直接用我打包上传的镜像，一行命令即可体验`mdnice`:

```shell
docker run --name mdnice -p 8080:80 -d howie6879/mdnice:22.02.11
``` 

### [kanboard](https://kanboard.org/)

`Kanboard`是一个免费开源的看板项目管理软件，为什么要引入看板：

- 可视化：映射团队现有的工作成卡片工作流，让团队更加聚焦且**资源分配最大化，减少浪费**
- 灵活且持续：没有规定阶段的持续时间且分阶段持续交付以逐步建立信任关系，核心在于`Pull System & WIP`
- 可评估：方便收集如任务完成数量、质量、时间等性能指标

![Kanboard](https://img.turingark.com/uPic/76TTj6.png) 

## 🤖 软件 

### [CopyTranslator](https://github.com/CopyTranslator/CopyTranslator)

科研人员总少不了阅读大量文献，理解文献内容就成了科研生活常态，而我们平时复制PDF内容黏贴到网页翻译的时候可能会出现多余换行而导致翻译乱码，译文与中文阅读习惯不符的情况，翻译结果很差，需要手动删除换行，而CopyTranslator可以帮我们快速且完美地解决这个问题。

![CopyTranslator](https://img.turingark.com/uPic/CopyTranslator.gif)

还有一款基于`DeepL`的同类型翻译软件可以参考使用，也叫一样的名字：[copy-translator](https://github.com/zu1k/copy-translator)，不过是用`Rust`写的，速度和体积有很大优势。 

### [AnotherRedisDesktopManager](https://github.com/qishibo/AnotherRedisDesktopManager)

快速稳定好用的Redis跨平台桌面管理软件：

![AnotherRedisDesktopManager](https://img.turingark.com/uPic/AnotherRedisDesktopManager.png) 

### [lemon-cleaner](https://github.com/Tencent/lemon-cleaner)

腾讯柠檬清理是针对 `macOS` 系统专属制定的清理工具。主要功能包括重复文件和相似照片的识别、软件的定制化垃圾扫描、可视化的全盘空间分析、内存释放、浏览器隐私清理以及设备实时状态的监控等。重点聚焦清理功能，对上百款软件提供定制化的清理方案，提供专业的清理建议，帮助用户轻松完成一键式清理。

![lemon_app](https://images-1252557999.file.myqcloud.com/uPic/lemon_app.png) 

## 👀 资料 

### [Rust嵌入式开发入门](https://space.bilibili.com/500416539/channel/collectiondetail?sid=177577)

 Rust嵌入式开发入门视频教程系列，由 Rust 中文社区 myrfy 来制作，其中也包含了一些非嵌入式领域需要懂的基础知识，比如链接脚本工作机制，视频教程持续更新中：

 ![rust_embedded_dev](https://img.turingark.com/uPic/rust_embedded_dev.jpg) 

### [产品经理的无限游戏](https://jiewang.gitbook.io/chan-pin-jing-li-de-wu-xian-you-xi/)

《结网》作者王坚的开源新书：

![产品经理的无线游戏](https://images-1252557999.file.myqcloud.com/uPic/产品经理的无线游戏.jpg) 

### [cs-video-courses](https://github.com/Developer-Y/cs-video-courses)

计算机科学课程和视频讲座列表：

![cs-video-courses](https://img.turingark.com/uPic/cs-video-courses.jpg) 

## 🕸 网站 

### [pika](https://pika.style/)

[pika](https://github.com/rishimohan/pika)是一个开源项目，可以快速将你的截图变得漂亮：

![pika](https://img.turingark.com/uPic/pika.jpg) 

### [websequencediagrams](https://www.websequencediagrams.com/)

提供在线绘制时序图的网站：

![websequencediagrams](https://images-1252557999.file.myqcloud.com/uPic/websequencediagrams.jpg) 

### [privacytools.io](https://www.privacytools.io/)

大部分软件都在监控你的一些隐私数据，这个网站基于数据安全的前提罗列了一些软件的替代品：

![privacytools](https://images-1252557999.file.myqcloud.com/uPic/privacytools.jpg) 

## ✍️ 说明

周刊相关信息：

- Github 地址：[howie6879/weekly/](https://github.com/howie6879/weekly/)，觉得不错麻烦给我一个**Star**，谢谢 ❤️
- 官网：[weekly.howie6879.cn](https://weekly.howie6879.cn/)

🙌如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是**同道中人**，所以如果你有自认为不错的信息获取渠道，欢迎**留言**或者**私聊**我，谢谢。
