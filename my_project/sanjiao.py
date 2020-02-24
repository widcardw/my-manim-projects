from manimlib.imports import *


class scene1(Scene):
    def construct(self):
        text1 = Text("上过排列组合的同学大概都知道下面这个题目怎么解决吧",
                     font="思源宋体 Heavy").move_to(UP*0.4).scale(0.4)
        tex1 = TextMobject(
            "C$_{2n}^{0}$+C$_{2n}^{2}$+C$_{2n}^{4}$+ $\\cdots$ +C$_{2n}^{2n-2}$+C$_{2n}^{2n}$=?").move_to(DOWN*0.4)
        self.play(Write(text1), Write(tex1), run_time=2.5, lag_ratio=0.2)
        self.wait(1.4)
        self.play(FadeOut(text1), ApplyMethod(tex1.scale, 0.7))
        self.play(ApplyMethod(tex1.to_edge, UL))
        self.wait(1)
        tex2 = TextMobject(
            "$(1+x)^{2n}$=C$_{2n}^{0}$+C$_{2n}^{1}x$+C$_{2n}^{2}x^2$+C$_{2n}^{3}x^3$+C$_{2n}^{4}x^4$+$\cdots$+C$_{2n}^{2n-1}x^{2n-1}$+C$_{2n}^{2n}x^{2n}$",).move_to(UP*2.6).scale(0.7)
        # texgroup1=VGroup(tex2[1],tex2[5],tex2[9])
        # texgroup2=VGroup(tex2[3],tex2[7],tex2[11])
        self.play(Write(tex2))
        self.wait(0.7)
        text2 = Text("我们令x=1,可以得到", font="思源宋体 Heavy").scale(
            0.3).move_to(UP*2+LEFT*4.7)
        self.play(Write(text2))
        self.wait(0.3)
        tex3 = TextMobject(
            "$(1+1)^{2n}$=C$_{2n}^{0}$+C$_{2n}^{1}$+C$_{2n}^{2}$+C$_{2n}^{3}$+C$_{2n}^{4}$+$\\cdots$+C$_{2n}^{2n-1}$+$C_{2n}^{2n}$").move_to(UP*1.4+LEFT*0.6).scale(0.7)
        reminder1 = Text("①", font="思源宋体 Heavy").scale(
            0.3).next_to(tex3, RIGHT)
        self.play(Write(tex3))
        self.play(Write(reminder1))
        self.wait(0.8)
        text3 = Text("而令x=-1,我们会得到下面一个式子",
                     font="思源宋体 Heavy").scale(0.3).move_to(UP*2+RIGHT*4)
        self.play(Write(text3))
        self.wait(0.3)
        tex4 = TextMobject(
            "$(1-1)^{2n}$=C$_{2n}^{0}-$C$_{2n}^{1}$+C$_{2n}^{2}-$C$_{2n}^{3}$+C$_{2n}^{4}$+$\\cdots -$C$_{2n}^{2n-1}$+C$_{2n}^{2n}$").move_to(UP*0.8+LEFT*0.6).scale(0.7)
        reminder2 = Text("②", font="思源宋体 Heavy").scale(
            0.3).next_to(tex4, RIGHT)
        self.play(Write(tex4))
        self.play(Write(reminder2))
        self.wait(0.8)
        text4 = Text("我们将①、②两式相加,可得", font="思源宋体 Heavy").scale(
            0.3).move_to(UP*0.2)
        rect1 = Rectangle(height=1.2, width=0.9,
                          color=ORANGE).move_to(UP*1.1+LEFT*2.2)
        rect2 = Rectangle(height=1.2, width=0.9,
                          color=ORANGE).move_to(UP*1.1+LEFT*0.45)
        rect3 = Rectangle(height=1.2, width=1.25,
                          color=ORANGE).move_to(UP*1.1+RIGHT*2.25)
        self.play(Write(text4), ShowCreation(rect1),
                  ShowCreation(rect2), ShowCreation(rect3))
        self.wait(0.3)
        tex5 = TextMobject(
            "$2^{2n}$=2(C$_{2n}^{0}$+C$_{2n}^{2}$+C$_{2n}^{4}$+ $\\cdots$ +C$_{2n}^{2n}$)").scale(0.7).move_to(DOWN*0.4)
        self.play(Write(tex5))
        self.wait(0.6)
        text5 = Text("所以,我们的答案是：", font="思源宋体 Heavy").scale(
            0.3).move_to(DOWN*1)
        self.play(Write(text5))
        tex6 = TextMobject("C$_{2n}^{0}$+C$_{2n}^2$+C$_{2n}^4$+ $\\cdots$ +C$_{2n}^{2n-2}$+C$_{2n}^{2n}$=$2^{2n-1}$",
                           color=YELLOW).scale(0.7).move_to(DOWN*1.6)
        self.play(Write(tex6))
        self.wait(1.5)
        square = Square(side_length=30, color=BLACK,
                        fill_color=BLACK, fill_opacity=1)
        self.play(FadeIn(square))
        self.wait(0.5)


class scene2(Scene):
    def construct(self):
        text1 = Text("那么，如果是下面这个该怎么做？", font="思源宋体 Heavy").scale(
            0.4).move_to(UP*0.8)
        tex1 = TexMobject(
            "\\rm C_{3n}^0+C_{3n}^3+C_{3n}^{6}+ \\cdots +C_{3n}^{3n-3}+C_{3n}^{3n}=?", color=YELLOW)
        text2 = Text("能否用类似的方法来做呢?", font="思源宋体 Heavy").scale(
            0.4).move_to(DOWN*0.8)
        self.play(Write(text1), Write(tex1))
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(tex1), FadeOut(text2))
        self.wait(0.3)


class scene3(Scene):
    def construct(self):
        text1_1 = Text("大家应该也都听说过", font="思源宋体 Heavy").scale(
            0.4).move_to(UP*0.4+LEFT*1)
        text1_2 = Text("复数", font="思源宋体 Heavy", color=YELLOW).scale(
            0.4).next_to(text1_1, RIGHT)
        text1_3 = Text("吧", font="思源宋体 Heavy").scale(
            0.4).next_to(text1_2, RIGHT)
        text1_4 = Text("定义", font="思源宋体 Heavy").scale(
            0.4).move_to(DOWN*0.4+LEFT*1)
        text1 = VGroup(text1_1, text1_2, text1_3)
        tex1 = TexMobject(
            "i= \\sqrt{-1}", color=YELLOW).move_to(DOWN*0.4+RIGHT*0.6)
        self.play(Write(text1), Write(text1_4), Write(tex1))
        group1 = VGroup(text1_1, text1_2, text1_3, text1_4, tex1)
        self.wait(1)
        self.play(group1.to_edge, UP)
        # self.wait(0.8)
        text2_1 = Text("而且也都大概了解过复数的", font="思源宋体 Heavy").scale(
            0.4).move_to(UP*1.6+LEFT*1.5)
        text2_2 = Text("三角形式", font="思源宋体 Heavy", color=RED).scale(
            0.4).next_to(text2_1, RIGHT)
        text2_3 = Text("吧", font="思源宋体 Heavy").scale(
            0.4).next_to(text2_2, RIGHT)
        tex2 = TexMobject("z=r(\\cos\\theta+i\\sin\\theta)",
                          color=RED).move_to(UP*0.8)
        group2 = VGroup(text2_1, text2_2, text2_3, tex2)
        self.play(Write(group2))
        line_x = Arrow(np.array([-5, -4, 0]),
                       np.array([-5, 1, 0]), color=WHITE, stroke_width=1.5)
        line_y = Arrow(np.array([-6, -3, 0]),
                       np.array([-1, -3, 0]), color=WHITE, stroke_width=1.5)
        xx = TexMobject("Re").scale(0.8).next_to(line_y, RIGHT)
        yy = TexMobject("Im").scale(0.8).next_to(line_x, UP)
        group_zbx = VGroup(line_x, line_y, xx, yy)
        self.play(ShowCreation(group_zbx))
        arrow1 = Arrow(np.array([-5.17, -3.17, 0]),
                       np.array([-2.5, -0.5, 0]), color=RED, stroke_width=1.5)
        zz = TexMobject("z", color=RED).scale(
            0.8).next_to(arrow1, RIGHT+UP, buff=0.1)
        self.play(ShowCreation(arrow1), Write(zz))
        arc1 = Arc(start_angle=line_x.get_angle(),
                   angle=arrow1.get_angle(), radius=0.4, color=BLUE).move_to(DOWN*2.85+LEFT*4.65).rotate(PI*3/2)
        xita = TexMobject("\\theta", color=BLUE).next_to(
            arc1, RIGHT, buff=0.1).scale(0.8)
        self.play(ShowCreation(arc1), Write(xita))
        self.wait(0.4)
        bracez = Brace(arrow1, LEFT+UP, buff=0.1, color=YELLOW)
        rr = TexMobject("r", color=YELLOW).next_to(
            bracez, LEFT+UP, buff=-1).rotate(PI/4)
        self.play(ShowCreation(bracez), Write(rr))
        self.wait(0.8)
        text3 = Text("r表示模长", font="思源宋体 Heavy").scale(
            0.4).move_to(DOWN*0.3+RIGHT*2)
        text4 = Text("θ表示在复平面内从实轴开始逆时针旋转的角度", font="思源宋体 Heavy").scale(
            0.4).move_to(DOWN*1+RIGHT*2.5)
        self.play(Write(text3), WiggleOutThenIn(rr))
        self.play(Write(text4), WiggleOutThenIn(xita))
        self.wait(2)
        square = Square(side_length=20, fill_color=BLACK, fill_opacity=1)
        self.play(FadeIn(square))


class scene4(Scene):
    def construct(self):
        text1 = Text("但这与我们今天解决开头的问题有什么关系吗？", font="思源宋体 Heavy").scale(
            0.4).move_to(UP*0.4)
        self.play(Write(text1))
        self.wait(1)
        text2 = Text("似乎有什么猫腻？", font="思源宋体 Heavy").scale(
            0.4).next_to(text1, DOWN)
        self.play(Write(text2))
        self.wait(1)
        self.play(FadeOut(text1), FadeOut(text2))


class scene5(Scene):
    def construct(self):
        text1 = Text("我们看一看这个方程", font="思源宋体 Heavy").scale(0.4).to_corner(UL)
        self.play(Write(text1))
        formula1 = TexMobject("x^3=1").next_to(text1, DOWN)
        self.play(Write(formula1))
        self.wait(0.6)
        text2 = Text("它在实数范围内只有一个根", font="思源宋体 Heavy").scale(
            0.4).move_to(UP*2+LEFT*4.4)
        self.play(Write(text2))
        self.wait(0.8)
        text3_1 = Text("但是在", font="思源宋体 Heavy").scale(
            0.4).move_to(UP*1.4+LEFT*6)
        text3_2 = Text("复数范围内", font="思源宋体 Heavy", color=YELLOW).scale(
            0.4).next_to(text3_1, RIGHT, buff=SMALL_BUFF)
        text3_3 = Text("呢？", font="思源宋体 Heavy").scale(
            0.4).next_to(text3_2, RIGHT, buff=SMALL_BUFF)
        text3 = VGroup(text3_1, text3_2, text3_3)
        self.play(Write(text3))
        self.wait(1)
        formula2 = TexMobject("x^3-1=0").next_to(text3_3, DOWN+LEFT)
        self.play(Write(formula2))
        self.wait(0.6)
        formula3 = TexMobject("(x-1)(x^2+x+1)=0").move_to(LEFT*4.2)
        self.play(Write(formula3))
        self.wait(0.8)
        formula4 = TexMobject(
            "(x-1)[(x^2+x+\\frac{1}{4})+\\frac{3}{4}]=0").move_to(LEFT*3.6+DOWN*0.2)
        self.play(ReplacementTransform(formula3, formula4))
        self.wait(0.8)
        formula5 = TexMobject(
            "(x-1)[(x+\\frac{1}{2})^2+\\frac{3}{4}]=0").move_to(LEFT*4+DOWN*0.2)
        self.play(ReplacementTransform(formula4, formula5))
        self.wait(1)
        text4 = Text("不难得到，在复数范围内，它有三个解：", font="思源宋体 Heavy").scale(
            0.4).move_to(DOWN*1.1+LEFT*3.6)
        self.play(Write(text4))
        self.wait(0.8)
        tex1 = TexMobject("x_1=1", color=YELLOW).move_to(
            DOWN*1.7+LEFT*5).scale(0.7)
        tex2 = TexMobject(
            "x_2=-\\frac{1}{2}+\\frac{\\sqrt{3}}{2}i", color=YELLOW).next_to(tex1, DOWN, buff=0).scale(0.7)
        tex3 = TexMobject(
            "x_3=-\\frac{1}{2}-\\frac{\\sqrt{3}}{2}i", color=YELLOW).next_to(tex2, DOWN, buff=0).scale(0.7)
        answer = VGroup(tex1, tex2, tex3)
        self.play(Write(answer))
        self.wait(1)
        text5 = Text("我们发现，x2与x3不仅共轭",
                     font="思源宋体 Heavy").scale(0.4).to_corner(UR)
        self.play(Write(text5))
        self.wait(0.3)
        text6 = Text("还满足：", font="思源宋体 Heavy").scale(
            0.4).move_to(UP*2.5+RIGHT*2.6)
        text7 = TextMobject("$x_2^2=x_3,x_3^2=x_2$").next_to(
            text6, RIGHT, buff=0)
        self.play(Write(text6))
        self.play(Write(text7))
        self.wait(0.6)
        tex4 = TexMobject("x_1,x_2,x_3").move_to(UP*1.8+RIGHT*3.2)
        text8 = Text("均满足:", font="思源宋体 Heavy").scale(
            0.4).next_to(tex4, RIGHT, buff=SMALL_BUFF)
        self.play(Write(tex4), Write(text8))
        text9 = TextMobject("$x^3=1$", "(废话)").move_to(UP*1.1+RIGHT*3.8)
        text9[1].set_color(GREY)
        self.play(Write(text9))
        self.wait(0.6)
        tex5 = TexMobject("x_2,x_3").move_to(UP*0.4+RIGHT*3)
        text10 = Text("满足:", font="思源宋体 Heavy").scale(
            0.4).next_to(tex5, RIGHT, buff=0.1)
        self.play(Write(tex5), Write(text10))
        tex6 = TexMobject("x_2+x_3+1=0").move_to(DOWN*0.3+RIGHT*3.7)
        self.play(Write(tex6))
        text10 = Text("因为x1=1", font="思源宋体 Heavy", color=ORANGE).scale(
            0.4).next_to(tex6, DOWN)
        self.play(Write(text10))
        self.wait(0.3)
        self.play(FadeOut(text10))
        tex7 = TexMobject(
            "x_1+x_2+x_3=0", color=ORANGE).move_to(DOWN*0.3+RIGHT*3.7)
        self.play(ReplacementTransform(tex6, tex7))
        self.wait(1.3)
        text11 = Text("观众：这跟我们的题目", font="思源宋体 Heavy", color=RED).scale(
            0.6).move_to(DOWN*1.4+RIGHT*3)
        text12 = Text("还是没有什么关系吧…", font="思源宋体 Heavy", color=RED).scale(
            0.6).next_to(text11, DOWN, buff=0.1)
        texx = VGroup(text11, text12)
        self.play(Write(texx))
        self.wait(1.3)
        text13 = Text("先别急，到后面大家就知道了", font="思源宋体 Heavy", color=BLUE).scale(
            0.8).move_to(DOWN*3.2+RIGHT*1.9)
        self.play(Write(text13))
        self.wait(0.8)
        square = Square(side_length=20, fill_color=BLACK, fill_opacity=1)
        self.play(FadeIn(square))


class scene6(Scene):
    def construct(self):
        tex1 = TextMobject(
            "$(1+x)^{3n}=$C$_{3n}^0$+C$_{3n}^{1}x$+C$_{3n}^{2}x^2$+$\\cdots$+C$_{3n}^{3n-2}x^{3n-2}$+C$_{3n}^{3n-1}x^{3n-1}$+C$_{3n}^{3n}x^{3n}$").to_edge(UP).scale(0.7)
        self.play(Write(tex1))
        self.wait(1)
        text1 = Text("令x等于1，可得", font="思源宋体 Heavy").scale(
            0.3).move_to(UP*2.5+LEFT*4.5)
        self.play(Write(text1))
        tex2 = TextMobject(
            "$2^{3n}$=C$_{3n}^0$+C$_{3n}^{1}$+C$_{3n}^{2}$+$\\cdots$+C$_{3n}^{3n-2}$+C$_{3n}^{3n-1}$+C$_{3n}^{3n}$").scale(0.7).next_to(text1, RIGHT)
        self.play(Write(tex2))
        self.wait(1)
        text2 = Text("令x等于刚刚的x2，可得", font="思源宋体 Heavy").scale(
            0.3).move_to(UP*1.8+LEFT*5.05)
        self.play(Write(text2))
        tex3 = TextMobject(
            "$(\\frac{1}{2}+\\frac{\\sqrt{3}}{2}i)^{3n}$=C$_{3n}^0$+C$_{3n}^{1}x_2$+C$_{3n}^{2}x_2^2$+$\\cdots$+C$_{3n}^{3n-2}x_2^{3n-2}$+C$_{3n}^{3n-1}x_2^{3n-1}$+C$_{3n}^{3n}x_2^{3n}$").scale(0.7).move_to(UP*1.2)
        self.play(Write(tex3))
        self.wait(1)
        tex3_1 = TextMobject(
            "而$(\\frac{1}{2}+\\frac{\\sqrt{3}}{2}i)^{3n}=(-x_3)^{3n}=(-1)^{3n}$", "$[(x_3)^3]^n$", "$=(-1)^n$").scale(0.7).next_to(tex3, DOWN)
        tex3_1[1].set_color(ORANGE)
        self.play(Write(tex3_1))
        self.wait(0.6)
        text3 = Text("根据上一段视频的“废话”，橘红色部分为1", font="思源宋体 Heavy").scale(
            0.3).next_to(text2, RIGHT, buff=3)
        self.play(Write(text3))
        self.wait(0.3)
        self.play(FadeOut(text3))
        self.wait(1)
        self.play(FadeOut(tex3_1[0]), FadeOut(tex3_1[1]), ApplyMethod(
            tex3.shift, LEFT*0.6), ApplyMethod(tex3_1[2].move_to, UP*1.2+RIGHT*6))
        self.wait(1.3)
        text4 = Text("令x等于刚刚的x3，可得", font="思源宋体 Heavy").scale(
            0.3).move_to(UP*0.6+LEFT*5.05)
        self.play(Write(text4))
        tex4 = TextMobject(
            "$(\\frac{1}{2}-\\frac{\\sqrt{3}}{2}i)^{3n}$=C$_{3n}^0$+C$_{3n}^{1}x_3$+C$_{3n}^{2}x_3^2$+$\\cdots$+C$_{3n}^{3n-2}x_3^{3n-2}$+C$_{3n}^{3n-1}x_3^{3n-1}$+C$_{3n}^{3n}x_3^{3n}$").scale(0.7)
        self.play(Write(tex4))
        self.wait(1)
        tex4_1 = TextMobject("而$(\\frac{1}{2}-\\frac{\\sqrt{3}}{2}i)^{3n}=(-x_2)^{3n}=(-1)^{3n}$",
                             "$[(x_2)^3]^n$", "$=(-1)^n$").scale(0.7).next_to(tex4, DOWN)
        tex4_1[1].set_color(ORANGE)
        self.play(Write(tex4_1))
        self.wait(0.6)
        self.play(FadeOut(tex4_1[0]), FadeOut(tex4_1[1]), ApplyMethod(
            tex4.shift, LEFT*0.6), ApplyMethod(tex4_1[2].move_to, RIGHT*6))
        self.wait(1.3)
        text5 = Text("等等，有点乱，我们稍微整理一下", font="思源宋体 Heavy",
                     color=ORANGE).scale(0.5).move_to(DOWN*1)
        self.play(Write(text5))
        self.wait(0.6)
        self.play(FadeOut(text5))
        tex2_1 = TextMobject(
            "C$_{3n}^0$+C$_{3n}^{1}x_1$+C$_{3n}^{2}x_1^2$+$\\cdots$+C$_{3n}^{3n-2}x_1^{3n-2}$+C$_{3n}^{3n-1}x_1^{3n-1}$+C$_{3n}^{3n}x_1^{3n}$=$2^{3n}$").scale(0.7).move_to(UP*2.4+RIGHT*0.9)
        self.play(ReplacementTransform(tex2, tex2_1), FadeOut(
            text2), FadeOut(text4), FadeOut(tex1), FadeOut(text1))
        self.wait(1)
        text6 = TextMobject("还记得刚刚的$x_2^2=x_3,x_3^2=x_2$吗?",
                            color=YELLOW).move_to(DOWN*1)
        self.play(Write(text6))
        self.wait(0.8)
        tex5 = TexMobject("x_2^{3k}=x_3^{3k}=1,x_2^{3k+1}=x_2,x_3^{3k+1}=x_3,x_2^{3k+2}=x_3,x_3^{3k+2}=x_2",
                          color=ORANGE).next_to(text6, DOWN).scale(0.8)
        self.play(Write(tex5))
        self.wait(1)
        tex2_2 = TextMobject(
            "C$_{3n}^{0}$+C$_{3n}^{1}x_1$+C$_{3n}^{2}x_1$+$\\cdots$+C$_{3n}^{3n-2}x_1$+C$_{3n}^{3n-1}x_1$+C$_{3n}^{3n}$=$2^{3n}$").scale(0.7).move_to(UP*2.4+RIGHT*0.6)
        tex3_2 = TextMobject(
            "$(\\frac{1}{2}+\\frac{\\sqrt{3}}{2}i)^{3n}$=C$_{3n}^{0}$+C$_{3n}^{1}x_2$+C$_{3n}^{2}x_3$+$\\cdots$+C$_{3n}^{3n-2}x_2$+C$_{3n}^{3n-1}x_3$+C$_{3n}^{3n}$").scale(0.7).move_to(UP*1.2+LEFT*0.9)
        tex4_2 = TextMobject(
            "$(\\frac{1}{2}-\\frac{\\sqrt{3}}{2}i)^{3n}$=C$_{3n}^{0}$+C$_{3n}^{1}x_3$+C$_{3n}^{2}x_2$+$\\cdots$+C$_{3n}^{3n-2}x_3$+C$_{3n}^{3n-1}x_2$+C$_{3n}^{3n}$").scale(0.7).move_to(LEFT*0.9)
        self.play(ReplacementTransform(tex2_1, tex2_2), ReplacementTransform(
            tex3, tex3_2), ReplacementTransform(tex4, tex4_2), ApplyMethod(tex3_1[2].next_to, tex3_2, RIGHT), ApplyMethod(tex4_1[2].next_to, tex4_2, RIGHT))
        self.wait(1)
        text7 = Text("仔细思考一下，也可以在草稿纸上计算一下", font="思源宋体 Heavy",
                     color=ORANGE).scale(0.5).move_to(DOWN*2.8)
        self.play(Write(text7))
        self.wait(1)
        self.play(FadeOut(text7), FadeOut(text6), FadeOut(tex5))
        self.wait(0.6)
        text8 = Text("将这三个式子相加", font="思源宋体 Heavy",
                     color=YELLOW).scale(0.4).to_edge(UP)
        self.play(Write(text8))
        rect1 = Rectangle(height=3.2, width=1,
                          color=BLUE).move_to(LEFT*2.45+UP*1.2)
        rect2 = Rectangle(height=3.2, width=1,
                          color=BLUE).move_to(LEFT*1.2+UP*1.2)
        rect3 = Rectangle(height=3.2, width=1.35,
                          color=BLUE).move_to(RIGHT*1+UP*1.2)
        rect4 = Rectangle(height=3.2, width=1.35,
                          color=BLUE).move_to(RIGHT*2.6+UP*1.2)
        zero1 = Text("蓝色矩形框起来的部分都是0", font="思源宋体 Heavy",
                     color=BLUE).move_to(DOWN*1+LEFT*2.5).scale(0.4)
        zero2 = TexMobject("x_1+x_2+x_3=0", color=BLUE_A).next_to(zero1, RIGHT)
        zeroo = VGroup(zero1, zero2)
        rectangle = VGroup(rect1, rect2, rect3, rect4)
        self.play(ShowCreation(rectangle),  lag_ratio=0.1)
        self.play(Write(zeroo))
        self.wait(1)
        self.play(FadeOut(rectangle), FadeOut(zeroo))
        rectr1 = Rectangle(height=3.2, width=0.7,
                           color=RED).move_to(UP*1.2+LEFT*3.44)
        rectr2 = Rectangle(height=3.2, width=0.7,
                           color=RED).move_to(UP*1.2+RIGHT*3.9)
        rectr = VGroup(rectr1, rectr2)
        self.play(ShowCreation(rectr), lag_ratio=0.1)
        text9 = Text("而上标为3的整数倍的部分保留下来了", font="思源宋体 Heavy",
                     color=RED).scale(0.4).move_to(DOWN*1)
        self.play(Write(text9))
        formula6 = TextMobject(
            "3(", "C$_{3n}^0$+C$_{3n}^3$+C$_{3n}^6$+C$_{3n}^9+\\cdots+$C$_{3n}^{3n-3}$+C$_{3n}^{3n}$", ")=$2^{3n}+2(-1)^n$").move_to(DOWN*1.8)
        formula6[1].set_color(RED)
        self.play(Write(formula6))
        self.wait(0.6)
        text10 = Text("稍微化一下", font="思源宋体 Heavy",
                      color=ORANGE).move_to(DOWN*2.6).scale(0.5)
        self.play(Write(text10))
        self.play(FadeOut(text10))
        formula7 = TextMobject("C$_{3n}^0$+C$_{3n}^3$+C$_{3n}^6$+C$_{3n}^9+\\cdots+$C$_{3n}^{3n-3}$+C$_{3n}^{3n}$",
                               "$=\\frac{1}{3}$", "$[2^{3n}+2(-1)^n]$").move_to(DOWN*2.6)
        formula7[1].set_color(YELLOW)
        formula7[2].set_color(ORANGE)
        self.play(ReplacementTransform(formula6[1].copy(), formula7[0]))
        self.play(ReplacementTransform(formula6[0].copy(), formula7[1]))
        self.play(ReplacementTransform(formula6[2].copy(), formula7[2]))
        self.wait(1)
        square1 = Square(side_length=20, fill_color=BLACK, fill_opacity=1)
        # formula7.plot_depth(2)
        formula8 = TextMobject(
            "$\\displaystyle\\sum_{i=0}^{n}$C$_{3n}^{3i}=\\displaystyle\\frac{1}{3}[2^{3n}+2(-1)^n]$")
        self.play(FadeIn(square1), ReplacementTransform(formula7, formula8))
        self.wait(2)
        text11 = Text("这就是我们的最终结果", font="思源宋体 Heavy").scale(
            0.4).next_to(formula8, DOWN)
        self.play(Write(text11))
        self.wait(2.6)
        self.play(FadeOut(formula8), FadeOut(text11))

class scene7(Scene):
    def construct(self):
        text1=Text("嗯？用这一方法似乎可以求出通解？",font="思源宋体 Heavy").move_to(UP*2).scale(0.5)
        text2=Text("等一下，刚刚好像还有什么没有用到？",font="思源宋体 Heavy",color=YELLOW).scale(0.5).move_to(UP*1)
        text3=Text("复数的三角形式在这个视频里有用到吗？",font="思源宋体 Heavy",color=RED).scale(0.5)
        text4=Text("通解怎么得到呢？",font="思源宋体 Heavy").scale(0.5).move_to(DOWN*1)
        tex=TextMobject("$\\displaystyle\\sum_{i=0}^{n}$C$_{kn}^{ki}=?$",color=BLUE_A).move_to(DOWN*2)
        text5=Text("请大家自行思考",font="思源宋体 Heavy",color=BLUE).move_to(DOWN*3).scale(0.3)
        line=Line(np.array([-1,-3,0]),np.array([1,-3,0]),color=RED)
        text6=Text("敬请期待",font="思源宋体 Heavy",color=BLUE).move_to(DOWN*3.4)
        self.play(Write(text1))
        self.wait(0.8)
        self.play(Write(text2))
        self.wait(0.8)
        self.play(Write(text3))
        self.wait(0.8)
        self.play(Write(text4))
        self.play(Write(tex))
        self.wait(0.8)
        self.play(Write(text5),ShowCreation(line),run_time=0.5)
        self.play(FadeOut(text5),FadeOut(line),run_time=0.5)
        self.play(Write(text6))
        self.wait(1.5)

