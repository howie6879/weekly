# 今日推荐(自动生成)

> 老胡的信息周刊**历史信息回顾**，主要针对计算机领域，内容主题极大程度被我个人喜好主导。这个项目核心目的在于记录让自己有印象的信息做一个**留存**以及**共享**。


## 🎯 项目 

### [wg-easy](https://github.com/wg-easy/wg-easy)

 `wg-easy` 提供一种简单的方式来运行 WireGuard VPN，并配备了 Web 管理界面。

![wg-easy](https://images-1252557999.file.myqcloud.com/uPic/sXhRQS.png) 

### [poster-design](https://github.com/palxiao/poster-design)

一款漂亮且功能强大的在线海报图片设计器，仿稿定设计。适用于海报图片生成、电商分享图、文章长图、视频/公众号封面等多种场景，不过需要注意的是项目后端服务没有开源，特性如下：

- 导入 PSD 文件解析成模板、在线导出图片下载
- 元素拖拽、组合、缩放、层级调整、对齐等操作。
- 图片素材插入、替换、裁剪，图片容器等功能。
- SVG 素材颜色、透明度编辑，文字花字组合。
- 画布自定义尺寸、滚轮缩放、自适应画布
- 吸附对齐、辅助引导线、标尺功能。
- 键盘快捷键、右键菜单快捷操作，复制删除等常用操作。
- 风格二维码编辑，支持单色、渐变、自定义 logo 等。
- 图层操作，支持拖拽变更层级。
- 颜色调色板，原生级取色器颜色吸管（Chrome）

![poster-design](https://images-1252557999.file.myqcloud.com/uPic/poster-design.jpg) 

### [PicImpact](https://github.com/besscroft/PicImpact)

一个摄影师专用的摄影作品展示网站，基于 `Next.js + Hono.js` 开发：

- 瀑布流相册展示图片，支持实况照片(Live Photos)，基于 LivePhotosKit JS 开发。
- 点击图片查看原图，浏览图片信息和 EXIF 信息，支持直链访问。
- 响应式设计，在 PC 和移动端都有不错的体验，支持暗黑模式。
- 图片存储兼容 S3 API、Cloudflare R2、AList API。
- 图片支持绑定标签，并且可通过标签进行交互，筛选标签下所有图片。
- 支持输出 RSS，可以使用 Follow 订阅，并支持订阅源所有权验证。
- 支持批量自动化上传，上传图片时会生成 0.3 倍率的压缩图片，以提供加载优化。
- ...

![PicImpact](https://images-1252557999.file.myqcloud.com/uPic/NFu7vG.png) 

## 🤖 软件 

### [immersive-translate](https://github.com/immersive-translate/immersive-translate)

沉浸式双语网页翻译扩展：

- 智能识别网页主内容区进行翻译，区别于同类插件翻译网页所有区域的行为，降低对原网页的“侵入性”，增强译文的阅读体验，所以该扩展被命名为“沉浸式翻译”。
- 双语显示，中文/英文对照（按照段落自然分割，或可设置为“将段落以句子分割”，实现每句话对照翻译）
- 定制优化了常见的主流网站，比如 Twitter，Reddit，Discord, Gmail, Telegram, Youtube, Hacker News 等。
- 支持 10 余种常见的翻译服务，包括 Deepl，谷歌，彩云小译，腾讯翻译君，百度翻译，火山翻译等。
- 支持 PDF 文件双语翻译。
- 支持 EPUB 电子书双语阅读，需配合 epub 在线阅读网站使用：https://epub-reader.online/  或  https://readwise.io/read
- 提供多种译文样式选择，包括弱化、模糊、下划线、分隔线等样式，随心所欲的个性化你的翻译体验。

![immersive-translate](https://images-1252557999.file.myqcloud.com/uPic/immersive-translate.jpg) 

### [全是漫画](https://github.com/hongchacha/cartoon)

全是漫画App，是替代网页浏览器，专门阅读漫画的工具，无需注册完全免费，基本上覆盖了所有的漫画网站。

![comic](https://images-1252557999.file.myqcloud.com/uPic/FXXmY5.jpg) 

### [AppManager](https://github.com/MuntashirAkon/AppManager)

一个功能全面的 `Android` 包管理器和应用查看器，支持复制自由软件的功能，提供了丰富的应用管理和操作功能，如列出应用信息、安装 / 卸载 `APK`、备份 / 恢复应用、查看日志等，同时支持根权限和 `ADB` 命令，以实现更高级的操作，如撤销权限、修改 `APP` 操作模式等：

![AppManager](https://images-1252557999.file.myqcloud.com/uPic/zIgjSp.png) 

## 👀 资料 

### [llm-universe](https://github.com/datawhalechina/llm-universe)

本项目是一个面向小白开发者的大模型应用开发教程，旨在结合个人知识库助手项目，通过一个课程完成大模型开发的重点入门，主要内容包括：

- 大模型简介，何为大模型、大模型特点是什么、LangChain 是什么，针对小白开发者的简单介绍；
- 如何调用大模型 API，本节介绍了国内外知名大模型产品 API 的多种调用方式，包括调用原生 API、封装为 LangChain LLM、封装为 Fastapi 等调用方式，同时将包括百度文心、讯飞星火、智谱AI等多种大模型 API 进行了统一形式封装；
- 大模型开发流程及架构，大模型应用开发的基本流程、一般思想和本项目的架构分析；
- 数据库搭建，不同类型知识库文档的加载、处理，向量数据库的搭建；
- Prompt 设计，如何设计 Prompt 来让大模型完成特定任务，Prompt Engineering 的原则和技巧有哪些；
- 验证迭代，大模型开发如何实现验证迭代，一般的评估方法有什么；
- 前后端开发，如何使用 Gradio、FastAPI 等框架快速开发大模型 Demo，展示应用能力。

![llm-universe](https://images-1252557999.file.myqcloud.com/uPic/llm-universe.png) 

### [hacker-laws-zh](https://github.com/nusr/hacker-laws-zh)

对开发人员有用的定律、理论、原则和模式，这是项目[hacker-laws](https://github.com/dwmkerr/hacker-laws) 的的中文翻译。 

### [qianguyihao/Web](https://github.com/qianguyihao/Web)

千古前端图文教程，超详细的前端入门到进阶知识库。从零开始学前端，做一名精致优雅的前端工程师:

- 网上的大部分入门教程，都不太适合初学者，本项目争取照顾到每一位前端入门者的同理心。即使你完全不懂前端，甚至不懂编程，通过这个教程，也能让小白入门。
- 帮助前端同学提供一个精品学习资源和路线，提高学习效率，少走很多弯路。

![qianguyihao](https://images-1252557999.file.myqcloud.com/uPic/qianguyihao.jpg)

可以当做前端字典，随时翻阅，查漏补缺，在线观看地址：[web.qianguyihao.com](https://web.qianguyihao.com/)。 

## 🕸 网站 

### [drawl.ink](https://drawl.ink/)

将链接转化成好看的图片：

![drawl](https://images-1252557999.file.myqcloud.com/uPic/eltzuF.png) 

### [jsonvisio](https://jsonvisio.com/editor)

将你的Json数据进行可视化，该项目也开源在[github-jsonvisio](https://github.com/AykutSarac/jsonvisio.com)：

![](https://images-1252557999.file.myqcloud.com/uPic/jsonvisio.jpg) 

### [coze](https://www.coze.cn/)

扣子为你提供了一站式 AI 开发平台，无需编程，你的创新理念都能迅速化身为下一代的 AI 应用，字节跳动此前是在海外推出 [Coze](https://www.coze.com/)，国内扣子与其分开运营：

![coze](https://images-1252557999.file.myqcloud.com/uPic/coze.jpg) 

## ✍️ 说明

周刊相关信息：

- 公众号：[老胡的储物柜](https://images-1252557999.file.myqcloud.com/uPic/ETIbMe.jpg)，欢迎加我微信进**周刊群聊**
- [TG 频道订阅](https://t.me/howie_weekly)：老胡周刊 TG 信息频道，对周刊的信息补充，会分享更多的资源，欢迎关注👏
- [聚合周刊](https://www.fre321.com/weekly)：老胡收集了国内外60+优质技术周刊进行信息聚合🔥
- Github 地址：[howie6879/weekly/](https://github.com/howie6879/weekly/)，觉得不错麻烦给我一个**Star**，谢谢 ❤️
- 浏览地址：[老胡的信息周刊](https://weekly.howie6879.com) | [今日推荐](https://weekly.howie6879.com/recommend/index.html) | [MacOS 软件推荐](https://weekly.howie6879.com/soft/mac.html)

🙌如果你阅读到这里，说明我们对信息的认可区域是有一定交集的，可以说我们是**同道中人**，所以如果你有自认为不错的信息获取渠道，欢迎**留言**或者**私聊**我，谢谢。