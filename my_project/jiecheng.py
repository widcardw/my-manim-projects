from manimlib.imports import *


class scene1(Scene):
    def construct(self):
        text1 = TextMobject("“", "!", "”是什么？").scale(2)
        text1[1].set_color(RED)
        self.play(Write(text1))
        text2 = TextMobject("感叹号?", color=BLUE).next_to(
            text1, DOWN, buff=0).align_to(text1, LEFT)
        mob1 = Text("√", font="思源宋体 SemiBold", color=RED_A).next_to(
            text2, RIGHT, buff=2).scale(0.6)
        self.play(ApplyMethod(text1.shift, UP*0.8), FadeInFromDown(text2))
        self.wait(0.8)
        self.play(Write(mob1))
        self.wait(1)
        vg = VGroup(text1, text2, mob1)
        text3 = TextMobject("阶乘?", color=BLUE).next_to(
            text2, DOWN, buff=0.4).align_to(text2, LEFT)
        self.play(FadeInFromDown(text3), ApplyMethod(vg.shift, UP*0.8))
        self.wait(0.8)
        text4 = TextMobject("没错，这就是我今天要讲的！", color=RED).next_to(
            text3, RIGHT, buff=1)
        self.play(Write(text4))
        self.wait(2)
        sq = Square(side_length=20, fill_color=BLACK, fill_opacity=1)
        self.play(FadeIn(sq))


class scene2(Scene):
    def construct(self):
        text1 = TextMobject("符号史", color=YELLOW).to_edge(UP)
        self.play(Write(text1))
        self.wait(0.8)
        text2 = TextMobject(
            "$\\bullet$瑞士数学家欧拉(Euler,L.)于1751年用大写字母$M$表示$m$阶乘$M=1\\cdot 2\\cdot 3\\cdot \\cdots \\cdot m$").next_to(text1, DOWN).scale(0.6)
        self.play(Write(text2), run_time=4)
        self.wait(0.8)
        text3 = TextMobject("$\\bullet$意大利数学家鲁菲尼(Ruffini,P.)在1799年出版的方程著述中，\\newline 用小写字母$\\pi$表示$m$阶乘。").next_to(
            text2, DOWN).scale(0.6)
        self.play(Write(text3), run_time=4.4)
        self.wait(0.8)
        text4 = TextMobject(
            "$\\bullet$德国数学家高斯(Gauss,C.F)于1818年则用$\\displaystyle\\prod(n)$表示$n$阶乘。").next_to(text3, DOWN).scale(0.6)
        self.play(Write(text4), run_time=3.5)
        self.wait(0.8)
        text5 = TextMobject("$\\bullet$用符号$\\underline{|n}$表示$n$阶乘的方法起源于英国，尚不能确定其创始人，\\newline 1827年，由雅来特(Jarrett)的建议得以流行，现代有时亦用此阶乘符号。").next_to(
            text4, DOWN).scale(0.6)
        self.play(Write(text5), run_time=7)
        self.wait(1)
        text6 = TextMobject("$\\bullet$现在通用的阶乘符号$n!$是法国数学家克拉姆(Kramp,C.)于1808年\\newline 最先提出来的，后经德国数学家、物理学家格奥尔格$\\cdot$欧姆(Ohm,M.)\\newline 等人的倡议而流行起来，直用到现在。").next_to(
            text5, DOWN).scale(0.6)
        self.play(Write(text6), run_time=9)
        self.wait(4)
        sq = Square(side_length=20, fill_color=BLACK, fill_opacity=1)
        self.play(FadeIn(sq))


class scene3(Scene):
    def construct(self):
        text1 = TextMobject(
            "阶乘的递推公式：$n!=n\\cdot (n-1)!=\\displaystyle\\prod_{k=1}^{n}k\\ (\\forall n\\geqslant 1)$").to_edge(UP).scale(0.8)
        self.play(Write(text1), run_time=2.8)
        self.wait(0.8)
        text2 = TextMobject("定义：", "0!=1!=1").next_to(
            text1, DOWN, buff=0).align_to(text1, LEFT).scale(0.8)
        text2[0].set_color(RED)
        self.play(Write(text2))
        self.wait(0.8)
        text3 = TextMobject("$n!=n\\cdot (n-1)!$", "$\\Rightarrow$", "$\\displaystyle\\frac{1}{n}n!=(n-1)!$", "$\\Rightarrow$", "$n!=\\displaystyle\\frac{1}{n+1}(n+1)!$").scale(
            0.8).move_to(UP*1)
        text3[0].set_color(YELLOW)
        text3[2].set_color(YELLOW)
        text3[4].set_color(YELLOW)
        for i in range(5):
            self.play(Write(text3[i]))
            self.wait(0.1)
        self.wait(0.7)
        text4 = TextMobject(
            "当$n$为负整数时:$n!=\\displaystyle\\frac{1}{n+1}(n+1)!=\\displaystyle\\frac{1}{n+1}\\cdot \\displaystyle\\frac{1}{n+2}\\cdot \\cdots \\cdot \\displaystyle\\frac{1}{-1}\\cdot $", "$\\displaystyle\\frac{1}{0}$", "$\\cdot 0!$").scale(0.8)
        self.play(Write(text4), run_time=6)
        rect = Rectangle(height=1.2, width=0.4, color=BLUE).move_to(
            text4[1].get_center())
        self.play(ShowCreationThenDestruction(rect), run_time=2)
        text5 = TextMobject("可以发现，", "负整数的阶乘无意义。").scale(0.8).move_to(DOWN*1)
        text5[1].set_color(YELLOW)
        self.play(Write(text5))
        self.wait(1)
        text6 = TextMobject("阶乘的运用非常广泛，例如：", color=BLUE_A).scale(
            0.6).move_to(DOWN*1.6)
        text7 = TextMobject(
            "泰勒公式：$e^x=1+x+\\displaystyle\\frac{x^2}{2!}+\\displaystyle\\frac{x^3}{3!}+\\cdots +\\displaystyle\\frac{x^n}{n!}+\\displaystyle\\frac{e^{\\theta x}}{(n+1)!}{x^{n+1}} \\ (0< \\theta <1)$").scale(0.5).move_to(DOWN*2.2)
        self.play(Write(text6))
        self.wait(0.4)
        self.play(Write(text7))
        self.wait(0.8)
        text8 = TextMobject(
            "组合数：$A_n^m=\\displaystyle\\frac{n!}{(n-m)!}$\\qquad $C_n^m=\\displaystyle\\frac{n!}{m!(n-m)!}$").scale(0.5).move_to(DOWN*2.9)
        self.play(Write(text8))
        self.wait(1.5)
        sq = Square(side_length=20, fill_color=BLACK, fill_opacity=1)
        self.play(FadeIn(sq))


class scene4(Scene):
    def construct(self):
        text1 = TextMobject("阶乘的解析拓展", color=YELLOW)
        self.play(Write(text1))
        self.wait(0.5)
        self.play(text1.scale, 0.7, text1.to_edge, UP)
        text2 = TextMobject("首先，我们引入Gamma函数的定义：").scale(
            0.6).move_to(UP*2.7+LEFT*4)
        self.play(Write(text2))
        text3 = TextMobject(
            "$\\Gamma (x)=\\displaystyle\\int_{0}^{\\infty}t^{x-1}e^{-t}\\rm{d}\\it{t}$", color=BLUE_A).scale(0.6).next_to(text2, RIGHT)
        self.play(Write(text3))
        self.wait(0.6)
        text4 = TextMobject("$\\Gamma (n+1)=\\displaystyle\\int_{0}^{\\infty}t^{n}e^{-t}\\rm{d}\\it{t}$", color=BLUE_A).scale(
            0.6).next_to(text2, DOWN).align_to(text2, LEFT)
        self.play(Write(text4))
        self.wait(0.5)
        text5 = TextMobject(
            "$=-\\displaystyle\\int_{0}^{\\infty}t^{n}\\rm{d}\\it{e^{-t}}$", color=BLUE_A).scale(0.6).next_to(text4, RIGHT, buff=SMALL_BUFF)
        self.play(Write(text5))
        self.wait(0.5)
        text6 = TextMobject("$=-\\displaystyle[t^{n}e^{-t}]_{0}^{\\infty}+$", "$\\displaystyle\\int_{0}^{\\infty}e^{-t}\\rm{d}\\it{t^n}$",
                            color=BLUE_A).scale(0.6).next_to(text5, RIGHT, buff=SMALL_BUFF)
        text6[1].set_color(RED_A)
        self.play(Write(text6))
        self.wait(0.5)
        text6_1 = TextMobject("$n$", "$\\displaystyle\\int_{0}^{\\infty}t^{n-1}e^{-t}\\rm{d}\\it{t}$", color=RED_A).scale(
            0.6).move_to(text6[1].get_center()+RIGHT*0.4)
        self.play(ReplacementTransform(text6[1], text6_1))
        self.wait(0.8)
        rect1 = Rectangle(height=0.6, width=1.4, color=YELLOW).move_to(
            text6[0].get_center())
        self.play(ShowCreation(rect1))
        text6_2 = TextMobject(
            "$-\\displaystyle[t^{n}e^{-t}]_{0}^{\\infty}$", color=BLUE_A).scale(0.6).move_to(LEFT*6+UP*1)
        self.play(ReplacementTransform(text6[0].copy(), text6_2))
        text7 = TextMobject("$=-\\displaystyle\\lim_{t\\to \\infty}\\displaystyle\\frac{t^n}{e^t}+0^{n}\\cdot e^{0}$",
                            "$=-\\displaystyle\\lim_{t\\to \\infty}\\displaystyle\\frac{n!}{e^t}$", "$=0$").scale(0.6).next_to(text6_2, RIGHT, buff=SMALL_BUFF)
        text8 = TextMobject("洛必达$n$次可得").scale(
            0.6).next_to(text7, RIGHT, buff=1)
        for i in range(3):
            self.play(Write(text7[i]))
            if i == 1:
                self.play(Write(text8))
                self.wait(0.4)
                self.play(FadeOut(text8))
            self.wait(0.3)
        self.wait(0.7)
        rect2 = Rectangle(height=1, width=2, color=YELLOW).move_to(
            text6_1[1].get_center())
        self.play(ShowCreation(rect2))
        self.wait(0.2)
        arr = TexMobject("\\Downarrow", color=RED).scale(
            0.6).next_to(rect2, DOWN, buff=0.05)
        self.play(Write(arr))
        self.wait(0.2)
        text9 = TextMobject("$\\Gamma (n)$", color=RED).scale(
            0.6).next_to(arr, DOWN, buff=0.05)
        self.play(Write(text9))
        self.wait(1)
        self.play(*[FadeOut(obj)
                    for obj in [rect1, rect2, arr, text9, text6_2, text7]])
        text10 = TexMobject("=n\\Gamma (n)", color=YELLOW_A).scale(
            0.6).next_to(text6_1, RIGHT, buff=0.1)
        self.play(Write(text10))
        self.wait(1)
        text11 = TextMobject("嗯哼？这与阶乘的递推似乎非常相似呢。",
                             color=BLUE).scale(0.7).move_to(UP*1.1)
        self.play(Write(text11))
        self.wait(0.8)
        self.play(FadeOut(text11))
        text12 = TextMobject(
            "$\\Gamma (1)=\\displaystyle\\int_{0}^{\\infty}e^{-t}\\rm{d}\\it{t}$", "$=[-e^{-t}]_0^{+\\infty}$", "=$\\displaystyle\\lim_{t\\to +\\infty}(-e^{-t})-(-e^0)$", "$=-\\displaystyle\\lim_{t\\to +\\infty}(\\displaystyle\\frac{1}{e^t})+1$", "=1").scale(0.6).next_to(text4, DOWN).align_to(text2, LEFT)
        for i in range(5):
            self.play(Write(text12[i]))
            self.wait(0.3)
        self.wait(0.5)
        text13 = TextMobject("因此，$\\Gamma (n)=(n-1)\\Gamma(n-1)=(n-1)(n-2)\\Gamma(n-2)=\\cdots=(n-1)!$",
                             color=YELLOW_A).scale(0.6).next_to(text12, DOWN).align_to(text2, LEFT)
        self.play(Write(text13))
        text13_1 = TexMobject("(n\\in N^*)", color=YELLOW_A).scale(
            0.6).next_to(text13, RIGHT, buff=0.6)
        self.play(Write(text13_1))
        self.wait(1.5)
        text14 = TextMobject("但是，伽马函数与阶乘还是有一些差别的。", color=RED_A).scale(
            0.6).next_to(text13, DOWN).align_to(text2, LEFT)
        self.play(Write(text14))
        self.wait(0.7)
        text15 = TextMobject("在阶乘中，是不允许有小数的。例如2.33!，0.5!就是错误的。", color=BLUE_A).scale(
            0.6).next_to(text14, DOWN).align_to(text2, LEFT)
        self.play(Write(text15))
        self.wait(0.8)
        text16 = TextMobject("但是在伽马函数中是允许小数计算的。", color=RED_A).scale(
            0.6).next_to(text15, DOWN).align_to(text2, LEFT)
        self.play(Write(text16))
        self.wait(0.8)
        text17 = TextMobject("接下来我将会呈现Gamma函数在平面直角坐标系中的图像。", color=YELLOW_A).scale(
            0.6).next_to(text16, DOWN).align_to(text2, LEFT)
        self.play(Write(text17))
        self.wait(1.4)
        sq = Square(side_length=20, fill_color=BLACK, fill_opacity=1)
        self.play(FadeIn(sq))


class test11(Scene):

    def construct(self):
        text1 = TexMobject("\\text{湿法冶金：}Al+Cu \\xlongequal{} Au+Cl",
                           background_stroke_width=0).to_edge(UP)
        self.play(Write(text1))
        text2 = TexMobject("\\text{自制咖啡：}CO+2Fe \\xlongequal{\\text{加热}} coffee",
                           background_stroke_width=0).next_to(text1, DOWN)
        self.play(Write(text2))
        text3 = TexMobject("\\text{工业制香蕉：}Ba+2Na \\xlongequal{} Banana",
                           background_stroke_width=0).next_to(text2, DOWN)
        self.play(Write(text3))
        text4 = TexMobject("2CO+3Ni\\xlongequal{} niconiconi",
                           background_stroke_width=0).next_to(text3, DOWN)
        self.play(Write(text4))
        text5 = TexMobject("4W+2In+D_2+O_2+2S\\xlongequal{} 2Windows",
                           background_stroke_width=0).next_to(text4, DOWN)
        self.play(Write(text5))

        text6 = MyText("Na", "+", "O", "+", "KI", "=", "Nokia",
                       default_font="ShadowedGermanica").next_to(text5, DOWN)
        replace_dict = {"Na": "Na", "O": "O", "KI": "KI",
                        "Nokia": "Nokia", "+": "+", "=": "="}
        new_text6 = text6.get_new_font_texs(replace_dict)
        self.play(Write(new_text6))
        self.wait()
