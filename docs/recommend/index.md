# 今日推荐(自动生成)

> 老胡的信息周刊**历史信息回顾**，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个**留存**以及**共享**。


## 🎯 项目 

### [weekly_report](https://github.com/guaguaguaxia/weekly_report)

简单描述工作内容，帮你生成完整周报：

![weekly_report](https://images-1252557999.file.myqcloud.com/uPic/weekly_report.jpeg) 

### [deepclaude](https://github.com/getasterisk/deepclaude)

`Aider` 团队最新研究通过[采用 DeepSeek R1 + Claude 3.5 Sonnet](https://aider.chat/2025/01/24/r1-sonnet.html) 可以实现最好的效果：

![deepclaude-web](https://images-1252557999.file.myqcloud.com/uPic/xFt7fe.png)

![deepclaude](https://images-1252557999.file.myqcloud.com/uPic/MNsnRO.png)

相关资料：

- [R1+Sonnet set SOTA on aider’s polyglot benchmark](https://aider.chat/2025/01/24/r1-sonnet.html)
- [第三方 Python 实现](https://github.com/ErlichLiu/DeepClaude) 

### [ChatTTS](https://github.com/2noise/ChatTTS)

`ChatTTS` 是专门为对话场景设计的文本转语音模型，例如 `LLM` 助手对话任务，它支持英文和中文两种语言，最大的模型使用了10万小时以上的中英文数据进行训练：

- 对话式 TTS: ChatTTS针对对话式任务进行了优化，实现了自然流畅的语音合成，同时支持多说话人。
- 细粒度控制: 该模型能够预测和控制细粒度的韵律特征，包括笑声、停顿和插入词等。
- 更好的韵律: ChatTTS在韵律方面超越了大部分开源TTS模型。同时提供预训练模型，支持进一步的研究。

效果挺好的，相关 `Web UI` 有 [ChatTTS-ui](https://github.com/jianchang512/ChatTTS-ui) 项目：

![ChatTTS](https://images-1252557999.file.myqcloud.com/uPic/ChatTTS.jpg) 

## 🤖 软件 

### [dockit](https://github.com/geek-fun/dockit)

一个跨平台的图形用户界面客户端，支持 `Elasticsearch` 和 `Opensearch` 数据库管理。

![dockit](https://images-1252557999.file.myqcloud.com/uPic/apAgUR.png) 

### [NotepadNext](https://github.com/dail8859/NotepadNext)

`Notepad++`的跨平台开源实现：

![NotepadNext](https://images-1252557999.file.myqcloud.com/uPic/NotepadNext.png) 

### [yarr](https://github.com/nkanaev/yarr)

基于 `Web` 的 `RSS` 阅读器，可使用 `Docker` 快速体验：

```shell
mkdir -p ./yarr/data
docker run -it -p 7070:7070 -v $(pwd)/yarr/data:/data wbsu2003/yarr
```

总体来说还是挺简洁轻量的：

![yarr](https://images-1252557999.file.myqcloud.com/uPic/yarr.jpg) 

## 👀 资料 

### [visualize-ml](https://github.com/visualize-ml)

鸢尾花书：从加减乘除到机器学习，全套7册。

![visualize-ml](https://images-1252557999.file.myqcloud.com/uPic/visualize-ml.jpg) 

### [influential-cs-books](https://github.com/cs-books/influential-cs-books)

该项目整理了计算机领域最具有影响力的编程&计算机科学书籍，书单的来源是`stackoverflow`上一个名为[What is the single most influential book every programmer should read?](https://stackoverflow.com/questions/1711/what-is-the-single-most-influential-book-every-programmer-should-read) 的回答。 

### [Flutter实战·第二版](https://book.flutterchina.club/)

本书是Flutter中国开源项目 (opens new window)发起人杜文（网名wendux） 创作的一本系统介绍Flutter技术的中文书籍，旨在帮助开发者系统地、循序渐进地了解Flutter技术：

![Flutter实战·第二版](https://images-1252557999.file.myqcloud.com/uPic/Flutter实战·第二版.jpg) 

## 🕸 网站 

### [carbon](https://carbon.now.sh/)

将你的源代码转成漂亮可分享的图片：

![carbon](https://images-1252557999.file.myqcloud.com/uPic/carbon.jpg) 

### [ideogram.ai](https://ideogram.ai/)

免费无次数限制的文字转图片网页：

![ideogram](https://images-1252557999.file.myqcloud.com/uPic/ideogram.jpg) 

### [iconfont](https://www.iconfont.cn/)

阿里巴巴矢量图标库：

![iconfont](https://images-1252557999.file.myqcloud.com/uPic/iconfont.jpg) 

## ✍️ 说明

周刊相关信息：

- 公众号：[老胡的储物柜](https://images-1252557999.file.myqcloud.com/uPic/ETIbMe.jpg)，欢迎加我微信进**周刊群聊**
- [TG 频道订阅](https://t.me/howie_weekly)：老胡周刊 TG 信息频道，对周刊的信息补充，会分享更多的资源，欢迎关注👏
- [聚合周刊](https://www.fre321.com/weekly)：老胡收集了国内外60+优质技术周刊进行信息聚合🔥
- Github 地址：[howie6879/weekly/](https://github.com/howie6879/weekly/)，觉得不错麻烦给我一个**Star**，谢谢 ❤️
- 浏览地址：[老胡的信息周刊](https://weekly.howie6879.com) | [今日推荐](https://weekly.howie6879.com/recommend/index.html) | [MacOS 软件推荐](https://weekly.howie6879.com/soft/mac.html)

🙌如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是**同道中人**，所以如果你有自认为不错的信息获取渠道，欢迎**留言**或者**私聊**我，谢谢。