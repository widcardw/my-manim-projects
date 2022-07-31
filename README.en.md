# This is a repository forked from 3b1b.  
I would like to have uploaded onto [github](https://github.com), but it takes less time to clone the repo at gitee in China.    

This repo includes code of manim_sandbox, since I am a member of [manim-kindergarten](https://github.com/manim-kindergarten).   

Here are some tutorials of manim. 

>[updater tutorial#00](https://b23.tv/BV1yi4y1g7e6)  The discription of target  
>[updater tutorial#01](https://b23.tv/BV1S64y1c7ik)  The usage of updater and ValueTracker  
>[updater tutorial#02](https://b23.tv/BV1D64y1c7pq)  The usage of dt  
>[updater tutorial#03](https://b23.tv/BV1ZT4y157kP)  UpdateFromFunc UpdateFromAlphaFunc    
>[updater tutorial#04](https://b23.tv/BV1ev41117dU)  The summary of tutorial series *Updater*  
  
github: [widcardw](https://github.com/widcardw)  

bilibili: [widcardw](https://space.bilibili.com/31976300) 

To import these libs, you should insert these lines at the beginning of your `py` files

```python
from manimlib.imports import *
from manim_sandbox.utils.imports import *
```

If you find that the `tex` raises errors, please change these lines in `manimlib/constants`, if you only need to write English words in your videos. 

```python
TEX_USE_CTEX = True  =>  TEX_USE_CTEX = False
```

~~英语好差~~