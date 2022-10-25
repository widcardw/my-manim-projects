# widcardw 曾写过的 manim 动画源文件

## 写在前面

由于个人原因，该仓库可能会长久不更新。

我本人觉得写 manim 动画变得有些吃力不讨好，这个动画库是留给那些有耐心的人的。

我从 2019 年末开始接触 manim ，那时甚至还是个连 Python 代码都不会写的小白（虽然到现在还是没有那么熟悉 Python ），到现在已经出了不少 manim 教程，期间阅读过一些源码，提交过寥寥几个 pr ，也逐渐能够理解这背后的动画的原理。manim 所涉及的方面真的很多，尤其是自从 Grant 引入了 shader 之后，灵活程度进一步提升，同时学习成本也大幅增加。

在机缘巧合之下，我在某个学期选到了一门数据可视化的课程，刚好需要学习 OpenGL 的内容（虽然涉及到的方面还是很少），借此机会，我尝试解剖 manimgl 的上色机制，并以文档的形式发表在 manim 官方中文文档 https://docs.manim.org.cn 和我的博客 https://widcardw.github.io 上，希望能为后来者铺上一条路。

我想我应该是不会通过自媒体这条路，通过花费大量时间制作 “精美” 的 manim 视频来牟利，毕竟我所掌握的知识远不如其他 up 主，只是将希望寄托给他们，为他们打下基础罢了。

manim 将只会作为我的一个业余爱好，在闲时稍微写一写吧。至于 manim 的交互 API ，只要学过 Javascript 的同学，这些应该都不是问题吧。至于同步异步、互斥锁，这些都能够找到相关的资料，应该也不用过多赘述吧。

## 注意

本仓库中的代码可能会有不少无法成功运行，因为 manim 一直在更新，同时也会经常出现 bug ，在不影响主要功能的情况下，基本上就只是 “能用就行”，例如 2022 暑假期间， become 和 updater 组合依然是失效的，所以我们还是尽可能使用其他方法去实现想要的动画，或者是拥抱 [ManimCE](https://manim.community) 。

## 新手遇到报错后应当怎么做

Python 的报错有相当完整的 Traceback ，在熟悉 Python 语法之后，你应当首先去阅读报错信息，一层一层的追溯报错的源头，而不是遇到一个问题就去问群友。如果你有能力，最好还是去阅读一些 manim 的源码，了解其运行的基本原理，纵使你不了解 FFmpeg 视频流处理工具，或者不了解 OpenGL Shading Language 着色语言，也应当分析出错误在哪里，对症下药才能解决问题。

在此还是忍不住想挂 “红绿蓝” 这位前群友


<div class="chat-container">
    <div style="text-align: center;">
        2021-08-24
    </div>
    <div class="message" style="justify-content: end;">
        <div class="bubble">
            了解一下什么叫对象，什么叫传入方法
        </div>
        <div class="person">widcardw</div>
    </div>
    <div class="message">
        <div class="person">红绿蓝</div>
        <div class="bubble">
            我只追求最简单的设计
        </div>
    </div>
    <div class="message">
        <div class="person">红绿蓝</div>
        <div class="bubble">
            花里胡哨的交给你们了
        </div>
    </div>
    <div class="message">
        <div class="person">红绿蓝</div>
        <div class="bubble">
            我要做精品设计
        </div>
    </div>
    <div class="message">
        <div class="person">红绿蓝</div>
        <div class="bubble">
            这个为什么报错？
            <pre>np.-1/x</pre>
        </div>
    </div>
    <div class="message">
        <div class="person">群友 A</div>
        <div class="bubble">
            翔哥息怒 🧯🧯🧯
        </div>
    </div>
    <div class="message">
        <div class="person">群友 B</div>
        <div class="bubble">
            翔哥息怒 🧯🧯🧯
        </div>
    </div>
    <div class="message">
        <div class="person">群友 C</div>
        <div class="bubble">
            翔哥息怒 🧯🧯🧯
        </div>
    </div>
</div>

<br />

因此，翔哥编写了 [manim 从没入门到被劝退](https://manim.org.cn/problems/persuade2quit)。

在此之后，我几乎不再回复过于基础的问题，因为这些问题不值得我们回答。

## 综上

如果你觉得你必须使用 manim 制作视频，请首先保持清醒，有充分的思考能力，有解决问题的决心，有持久的毅力，再决定你是否要坚持做下去。

widcardw

2022-08-20


<style>
.chat-container {
    border: 1px solid #7f7f7f40;
    padding: 0.5rem;
    border-radius: 0.5rem;
}
.message {
    display: flex;
    margin: 0.5rem 0;
}
.person {
    padding: 0.5rem;
}
.bubble {
    background: #7f7f7f20;
    padding: 0.5rem;
    border-radius: 0.5rem;
}
</style>