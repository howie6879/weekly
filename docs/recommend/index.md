# 今日推荐(自动生成)

> 老胡的信息周刊**历史信息回顾**，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个**留存**以及**共享**。


## 🎯 项目 

### [llama3](https://github.com/meta-llama/llama3)

Meta 正式发布开源大模型 `Llama 3` ，其提供两个版本：`8B` 版本适合在消费级 `GPU` 上高效部署和开发；`70B` 版本则专为大规模 `AI` 应用设计。每个版本都包括基础和指令调优两种形式。此外，基于 `Llama 3 8B` 微调后的 `Llama Guard` 新版本也已作为 `Llama Guard 2`（安全微调版本）发布：

![hc_llama3](https://images-1252557999.file.myqcloud.com/uPic/hc_llama3.jpg)

你可以在 [Hugging Chat](https://huggingface.co/chat) 上面体验，其他相关优秀的衍生开源项目老胡顺便做了个整理：

- [llama](https://github.com/meta-llama/llama)|[llama.cpp](https://github.com/ggerganov/llama.cpp)|[llamafile](https://github.com/Mozilla-Ocho/llamafile)|[codellama](https://github.com/meta-llama/codellama)|[llm-course](https://github.com/mlabonne/llm-course)
- 问答系统：
	- [FastGPT](https://github.com/labring/FastGPT)
	- [anything-llm](https://github.com/Mintplex-Labs/anything-llm)
	- [MaxKB](https://github.com/1Panel-dev/MaxKB)
	- [quivr](https://github.com/QuivrHQ/quivr)
	- [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)
	- [QAnything](https://github.com/netease-youdao/QAnything)
	- [private-gpt](https://github.com/zylon-ai/private-gpt)
	- [llm-answer-engine](https://github.com/developersdigest/llm-answer-engine)
- WebUI：
	- [ChatGPT-Next-Web](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web)
	- [lobe-chat](https://github.com/lobehub/lobe-chat)
	- [ChuanhuChatGPT](https://github.com/GaiZhenbiao/ChuanhuChatGPT)
	- [open-webui](https://github.com/open-webui/open-webui)
	- [chat-ollama](https://github.com/sugarforever/chat-ollama)
	- [chat-ui](https://github.com/huggingface/chat-ui)
	- [aichat](https://github.com/sigoden/aichat)
	- [open-webui2](https://github.com/open-webui/open-webui)
	- [LocalAI](https://github.com/mudler/LocalAI)
- APP：[LM Studio](https://lmstudio.ai/)|[jan](https://github.com/janhq/jan)||[ollama](https://github.com/ollama/ollama)|[chatbox](https://github.com/Bin-Huang/chatbox)
- 应用开发：
	- [langchain](https://github.com/langchain-ai/langchain)：为AI开发者提供工具，将语言模型与外部数据源连接起来，辅助构建 AI 应用程序
	- [MetaGPT](https://github.com/geekan/MetaGPT)：Multi-Agent 框架
	- [Dify](https://docs.dify.ai/)：开源的大语言模型(LLM) 应用开发平台
	- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)：让大模型微调更简单
	- [Flowise](https://github.com/FlowiseAI/Flowise)：轻松构建 LLM 应用程序
	- [llm-app](https://github.com/pathwaycom/llm-app)：30 行代码构建你的 LLM 应用程序
- [LLM Leaderboard](https://www.vellum.ai/llm-leaderboard)：各大主流 LLMs 评比 

### [eagleuse](https://github.com/meetqy/eagleuse)

**@meetqy** 自荐项目，把  `Eagle App` 打造成本地后台管理系统，快速构建 `WEB` 图片站：

![eagleuse](https://images-1252557999.file.myqcloud.com/uPic/eagleuse.jpg) 

### [Stirling-PDF](https://github.com/Frooodle/Stirling-PDF)

基于 `Docker` 的 `Web PDF` 操作工具，允许您对 `PDF` 文件执行各种操作，如拆分、合并、转换、重新组织、添加图像、旋转、压缩等：

![Stirling-PDF](https://images-1252557999.file.myqcloud.com/uPic/Stirling-PDF.png) 

## 🤖 软件 

### [hetty](https://github.com/dstotijn/hetty)

`Hetty` 是用于安全性研究的 `HTTP` 工具包。它的目标是成为 `Burp Suite Pro` 这样的商业软件的开源替代品，其强大的功能是根据信息安全和漏洞奖励社区的需要量身定制的：

![hetty](https://images-1252557999.file.myqcloud.com/uPic/hetty.png) 

### [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR)

适用于 Win10 x64 平台的离线OCR软件。批量导入本地图片 / 读取剪贴板，识别图片中的文本，输出到软件面板或本地 .txt / .md 文件。

- **免费**：本项目所有代码开源，完全免费。
- **方便**：解压即用，无需安装。不需要网络。
- **高效**：OCR识别引擎是C++编译的  [PaddleOCR-json](https://github.com/hiroi-sora/PaddleOCR-json)  （PP-OCRv2.6 cpu\_avx\_mkl），比前代提速20%。只要电脑性能足够且支持mkldnn，通常能比在线OCR服务更快。
- **精准**：默认使用PPOCR-v3模型库。除了能准确辨认常规文字，对非常规字形（手写、艺术字、小字、方向不正、杂乱背景等）也有不错的识别率。可设置**忽略区域**排除水印，进一步提高精准性。

![Umi-OCR](https://images-1252557999.file.myqcloud.com/uPic/R4LmuM.jpg) 

### [macGPT](https://github.com/hellokuls/macGPT)

一款 `ChatGPT for Mac` 原生客户端：

![macGPT](https://images-1252557999.file.myqcloud.com/uPic/macGPT.png) 

## 👀 资料 

### [凤凰架构](https://github.com/fenixsoft/awesome-fenix)

这是一部以“**如何构建一套可靠的分布式大型软件系统**”为叙事主线的开源文档，是一幅帮助开发人员整理现代软件架构各条分支中繁多知识点的技能地图。文章《[什么是凤凰架构](https://icyfenix.cn/introduction/about-the-fenix-project.html)》详细阐述了这部文档的主旨、目标与名字的来由，文章《[如何开始](https://icyfenix.cn/exploration/guide/quick-start.html)》简述了文档每章讨论的主要话题与内容详略分布，供阅前参考。

![icyfenix](https://images-1252557999.file.myqcloud.com/uPic/icyfenix.jpg) 

### [深入分析LINUX内核源码](http://www.kerneltravel.net/book/)

陈莉君老师二十多年来专注Linux内核研究，业余时间主办的Linux内核之旅网站，为Linux爱好者默默提供着无私的帮助，值得一提的是，把自己2002年撰写的《深入分析Linux内核源代码》一书，因为绝版而全文公布于网络，这为嵌入式开发者和Linux内核爱好者提供了触手可得的资料。

![kerneltravel](https://images-1252557999.file.myqcloud.com/uPic/kerneltravel.jpg) 

### [Leetcode-retag](https://github.com/resumejob/Leetcode-retag)

重新分类 Leetcode 高频题 2021 版

- 题目按照面试频率降序排列
- 增加难度分类，适合从简单开始学习
- 增加细分类别，例如单调栈，前缀树等，一道题目可能会有多个类别 

## 🕸 网站 

### [chuhai.tools](https://chuhai.tools/)

独立开发者出海技术栈和工具集合:

![chuhai](https://images-1252557999.file.myqcloud.com/uPic/chuhai.jpg) 

### [pixian.ai](https://pixian.ai/)

免登录图片背景消除网页，2023-07-21 当前属于测试期间，是免费的：

![pixian](https://images-1252557999.file.myqcloud.com/uPic/pixian.jpg) 

### [web-check](https://web-check.xyz/)

输入目标网址，分析该网站各项 `web` 检查信息，非常详细：

![web-check](https://images-1252557999.file.myqcloud.com/uPic/web-check.jpg) 

## ✍️ 说明

周刊相关信息：

- 公众号：[老胡的储物柜](https://images-1252557999.file.myqcloud.com/uPic/ETIbMe.jpg)，欢迎加我微信进**周刊群聊**
- [TG 频道订阅](https://t.me/howie_weekly)：老胡周刊 TG 信息频道，对周刊的信息补充，会分享更多的资源，欢迎关注👏
- [聚合周刊](https://www.fre321.com/weekly)：老胡收集了国内外60+优质技术周刊进行信息聚合🔥
- Github 地址：[howie6879/weekly/](https://github.com/howie6879/weekly/)，觉得不错麻烦给我一个**Star**，谢谢 ❤️
- 浏览地址：[老胡的信息周刊](https://weekly.howie6879.com) | [今日推荐](https://weekly.howie6879.com/recommend/index.html) | [MacOS 软件推荐](https://weekly.howie6879.com/soft/mac.html)

🙌如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是**同道中人**，所以如果你有自认为不错的信息获取渠道，欢迎**留言**或者**私聊**我，谢谢。