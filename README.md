# 这是一个菜鸡从 3b1b 那里 fork 过来的库    

[Here is the way to ReadMe in English](https://github.com/widcardw/my-manim-projects/blob/master/README.en.md)

## 概述

本仓库包含 [github](https://github.com/widcardw/my-manim-projects) 库和 [gitee](https://gitee.com/widcardw/manim) 库，由于在大陆从 [github](https://github.com/widcardw/my-manim-projects) 上克隆很慢，所以建议大陆用户到 [gitee](https://gitee.com/widcardw/manim) 上克隆下载。

这个仓库包含了 [manim_sandbox](https://github.com/manim-kindergarten/manim_sandbox) 的代码，毕竟是 MK 的成员，大家可以去 MK 看看：[Manim-Kindergarten](https://github.com/manim-kindergarten)。

其中，[鹤翔万里](https://space.bilibili.com/171431343)、[cigar666](https://space.bilibili.com/66806831)、[pdcxs](https://space.bilibili.com/10707223) 等成员做出了相当大的贡献  ~~宝藏UP不关注一下吗？~~

附：manim 中文教程文档 [manim.wiki](https://manim.wiki)（该域名由萌萌哒吉吉申请），主要都是翔哥写的，xgnb。

~~以前的域名是 manim.ml，但目前过期了。~~

## 使用说明

在调用库的过程中，请在文件的头部插入以下代码

```python
from manimlib.imports import *
from manim_sandbox.utils.imports import *
```

如果要参考代码的话，就进到 `my_projects` 文件夹，这里面有我写过的几乎所有工程，大家可以稍微参考参考。    

另外，有时候我可能会在我的博客更新教程：[https://widcardw.github.io](https://widcardw.github.io)，今后有可能转战知乎或 CSDN，虽然不是非常愿意。

对了，我已经将 `ctex_template.tex` 文件中的中文字体使用改成了思源宋体，所以如果你想要使用的话，那就必须先安装这个系列的字体，或者将这一行注释（前面插入一个百分号）。这个操作参考了[暗星姐姐](https://space.bilibili.com/4694767)的[视频](https://www.bilibili.com/video/BV1D5411s7bR)，大家也可以去看看她的视频。

```tex
\setCJKmainfont{SourceHanSerifSC-Medium.otf}
↓
%\setCJKmainfont{SourceHanSerifSC-Medium.otf}
```

## ~~自我推销~~

下面是我制作的一些教程

>[updater 教程 #00](https://b23.tv/BV1yi4y1g7e6)  target 的描述   
>[updater 教程 #01](https://b23.tv/BV1S64y1c7ik)  updater 常用方法&nbsp;ValueTracker 用法   
>[updater 教程 #02](https://b23.tv/BV1D64y1c7pq)  dt 的用法   
>[updater 教程 #03](https://b23.tv/BV1ZT4y157kP)  UpdateFromFunc&nbsp;UpdateFromAlphaFunc 用法  
>[updater 教程 #04](https://b23.tv/BV1ev41117dU)  Updater 总集篇  

以及我制作的一些炫技视频

>[用于装 X 的特效](https://www.bilibili.com/video/BV1LK411P7R9)  
>[Bezier Curve](https://www.bilibili.com/video/BV1sU4y1476k)

还有 Updater 教程的重制版

>[Updater 教程重制版](https://www.bilibili.com/video/BV1EA411g7tz)

欢迎大佬批评指正    
最近可能会开始研究 shaders 分支，届时可能会在个人博客/知乎等平台做些许分享。  
github: [widcardw](https://github.com/widcardw)   
bilibili: [widcardw](https://space.bilibili.com/31976300)  