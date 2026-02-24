# 今日推荐(自动生成)

> 老胡的信息周刊**历史信息回顾**，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个**留存**以及**共享**。


## 🎯 项目 

### [autocorrect](https://github.com/huacnlee/autocorrect)

AutoCorrect 是一个基于 Rust 编写的工具，用于「自动纠正」或「检查并建议」文案，给 CJK（中文、日语、韩语）与英文混写的场景，补充正确的空格，纠正单词，同时尝试以安全的方式自动纠正标点符号等等。

类似 ESlint、Rubocop、Gofmt 等工具，AutoCorrect 可以用于 CI 环境，它提供 Lint 功能，能便捷的检测出项目中有问题的文案，起到统一规范的作用。

支持各种类型源代码文件，能自动识别文件名，并准确找到字符串、注释做自动纠正。

![autocorrect](https://images-1252557999.file.myqcloud.com/uPic/autocorrect.png) 

### [supabase](https://github.com/supabase/supabase)

`Supabase` 是一个基于开源工具构建的 `Firebase` 替代品，旨在通过使用企业级的开源技术，提供类似 `Firebase` 的功能：

![Supabase](https://images-1252557999.file.myqcloud.com/uPic/x0eIys.png) 

### [markdown-nice](https://github.com/mdnice/markdown-nice)

有很多朋友问我的公众号排版是怎么做的，答案就是`markdown-nice`开源项目：

> 支持主题设计的 Markdown 编辑器，让排版变 Nice

你可以选择直接访问[官方](https://editor.mdnice.com/)，也可以自建，自建的好处是不需要登录，下面截图就是我自建的：

![](https://images-1252557999.file.myqcloud.com/uPic/oGeICY.png)

官方并不支持`Docker`部署，为了方便大家使用，直接用我打包上传的镜像，一行命令即可体验`mdnice`:

```shell
docker run --name mdnice -p 8080:80 -d howie6879/mdnice:22.02.11
``` 

## 🤖 软件 

### [KeepingYouAwake](https://github.com/newmarcel/KeepingYouAwake)

根据自己的需求设置 `Mac` 多少分钟/多少小时后进入睡眠：

![keepingyouawake](https://images-1252557999.file.myqcloud.com/uPic/keepingyouawake.jpeg) 

### [AltTab](https://alt-tab-macos.netlify.app/)

`AltTab`将`Windows`的`Alt-Tab`窗口切换器的电源带到`Mac OS`：

![AltTab](https://images-1252557999.file.myqcloud.com/uPic/6YohNK.jpg) 

### [Plash](https://github.com/sindresorhus/Plash)

将网站变成 Mac 桌面壁纸，支持将多种网站设置为壁纸，这些网站并不局限于图片网站，还可以是新闻、气象等站点：

![Plash](https://images-1252557999.file.myqcloud.com/uPic/Plash.jpeg) 

## 👀 资料 

### [learnprompting.org](https://learnprompting.org/zh-Hans/docs/intro)

> 如何同人工智能交流，并得到你要的结果。

随着最近人工智能的不断进步，提示工程这项技能变得越来越重要。本课程会聚焦于如何使用提示工程。你不需要很多机器学习相关的知识。

![learnprompting](https://images-1252557999.file.myqcloud.com/uPic/learnprompting.jpg) 

### [Ai迷思录](https://github.com/Acmesec/theAIMythbook)

涵盖了人工智能的基础知识、法律法规、经典人工智能模型、漏洞与攻击、防御方法、安全开发与运维、相关框架、会议讲座以及实践技能等。

![theAIMythbook](https://images-1252557999.file.myqcloud.com/uPic/lPbVPg.png) 

### [craftinginterpreters_zh](https://github.com/GuoYaxiang/craftinginterpreters_zh)

这是一个还在进行中的翻译项目，原项目是[craftinginterpreters](https://github.com/munificent/craftinginterpreters)，同时还有配套的英文书，可免费[在线阅读](http://www.craftinginterpreters.com/)。

该书由一门小型的自创语言Lox开始，分别使用Java和C实现了两种类型的解释器，jlox和clox，其中前者是将语法解析成Java中的表示代码，主要依赖Java本身的语法能力实现代码的真正运行；后者则采用了类似编译和虚拟机的机制，实现了一个看上去“更高效”的解释器：

![craftinginterpreters](https://images-1252557999.file.myqcloud.com/uPic/craftinginterpreters.jpg) 

## 🕸 网站 

### [vue-color-avatar](https://vue-color-avatar.vercel.app/)

`Vue3 + Vite` 开发的纯前端在线头像生成网站，具有如下功能：

- 可视化组件配置栏
- 随机生成头像，有一定概率触发彩蛋
- 撤销/还原*更改*
- 国际化多语言

![vue-color-avatar](https://images-1252557999.file.myqcloud.com/uPic/n3gXb6.png) 

### [apitracker](https://apitracker.io/)

发现最佳的API接口和开发人员资源，覆盖社交媒体、金融、新闻、游戏、人工智能、音视频等领域：

![apitracker](https://images-1252557999.file.myqcloud.com/uPic/apitracker.jpg) 

### [awesome-chatgpt-prompts](https://prompts.chat/)

`ChatGPT` 余热不减，一周百万用户果然不是盖的，这个项目总结了 `ChatGPT` 常用姿势：

![prompts](https://images-1252557999.file.myqcloud.com/uPic/prompts.jpg) 

## ✍️ 说明

周刊相关信息：

- 公众号：[老胡的储物柜](https://images-1252557999.file.myqcloud.com/uPic/ETIbMe.jpg)，欢迎加我微信进**周刊群聊**
- [TG 频道订阅](https://t.me/howie_weekly)：老胡周刊 TG 信息频道，对周刊的信息补充，会分享更多的资源，欢迎关注👏
- [聚合周刊](https://www.fre321.com/weekly)：老胡收集了国内外60+优质技术周刊进行信息聚合🔥
- Github 地址：[howie6879/weekly/](https://github.com/howie6879/weekly/)，觉得不错麻烦给我一个**Star**，谢谢 ❤️
- 浏览地址：[老胡的信息周刊](https://weekly.howie6879.com) | [今日推荐](https://weekly.howie6879.com/recommend/index.html) | [MacOS 软件推荐](https://weekly.howie6879.com/soft/mac.html)

🙌如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是**同道中人**，所以如果你有自认为不错的信息获取渠道，欢迎**留言**或者**私聊**我，谢谢。