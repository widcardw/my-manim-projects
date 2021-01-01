# 这是一个菜鸡从3b1b那里fork过来的库    

[Here is the way to ReadMe in English](https://github.com/widcardw/my-manim-projects/blob/master/README.en.md)

本来想放到 github 上面的，但是还是先放到 gitee 这边来吧，因为克隆/上传可以快一点   

这个仓库包含了 manim_sandbox 的代码，毕竟是 MK 的成员，大家可以去 MK 看看：[Manim-Kindergarten](https://github.com/manim-kindergarten)

下面是我制作的一些教程

>[updater教程#00](https://b23.tv/BV1yi4y1g7e6)  target 的描述   
>[updater教程#01](https://b23.tv/BV1S64y1c7ik)  updater 常用方法&nbsp;ValueTracker 用法   
>[updater教程#02](https://b23.tv/BV1D64y1c7pq)  dt 的用法   
>[updater教程#03](https://b23.tv/BV1ZT4y157kP)  UpdateFromFunc&nbsp;UpdateFromAlphaFunc 用法  
>[updater教程#04](https://b23.tv/BV1ev41117dU)  Updater 总集篇  

欢迎大佬批评指正    
github: [widcardw](https://github.com/widcardw)   
bilibili: [31976300_bili](https://space.bilibili.com/31976300)  

使用说明：  
在调用库的过程中，请在文件的头部插入以下代码

```python
from manimlib.imports import *
from manim_sandbox.utils.imports import *
```

这里与直接克隆的 manim_sandbox 有所区别，因为 manim_sandbox 中将 imports 放在了另外的地方。    
如果要参考代码的话，就进到 my_projects 文件夹，这里面有我写过的几乎所有工程，大家可以稍微参考参考。    

另外，有时候我可能会在我的博客更新教程：[https://widcardw.github.io](https://widcardw.github.io)

对了，我已经将 ctex_template.tex 文件中的中文字体使用改成了思源宋体，所以如果你想要使用的话，那就必须先安装这个系列的字体，或者将这一行注释（前面插入一个百分号）。

```tex
\setCJKmainfont{SourceHanSerifSC-Medium.otf}
↓
%\setCJKmainfont{SourceHanSerifSC-Medium.otf}
```

