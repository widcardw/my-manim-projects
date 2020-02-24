from manimlib.imports import *


class test1(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65*DEGREES, theta=PI/3)
        s = Sphere(radius=2)
        self.play(ShowPassingFlashWithThinningStrokeWidth(s))
        self.wait()


class test2(Scene):
    def construct(self):
        graph = ParametricFunction(
            lambda t: np.sin(t)*UP+RIGHT*t, t_min=-10, t_max=10)
        self.play(ShowCreation(graph))


class test3(Scene):
    def construct(self):
        nump = NumberPlane(y_line_frequency=PI/2)
        self.play(ShowCreation(nump))
        self.wait()


class test4(Scene):

    def construct(self):
        color_map = {
            "x": RED,
            "y": YELLOW,
            "z": BLUE,
        }
        tex = TexMobject("\\frac{a}{b}=c")
        tex.set_color_by_tex_to_color_map(color_map)
        self.play(Write(tex))


class test5(Scene):
    def construct(self):
        numpl = NumberPlane(y_line_frequency=PI/2)
        graph = ParametricFunction(lambda t: np.sin(
            t)*UP+t*RIGHT, t_min=-10, t_max=10).set_color("#FF2222")
        self.play(ShowCreation(numpl), run_time=3, lag_ratio=0.1)
        self.play(ShowCreation(graph))
        self.wait()


class test6(Scene):
    def construct(self):
        color_dict = {
            "\\overrightarrow{AB}": YELLOW,
            "\\overrightarrow{AC}": YELLOW,
            "\\overrightarrow{AD}": PURPLE,
            "\\overrightarrow{DB}": BLUE,
            "\\overrightarrow{DC}": RED,
            "AD": PURPLE,
            "\\frac{1}{2}\\overrightarrow{CB}": BLUE,
            "\\frac{1}{2}\\overrightarrow{BC}": RED,
            "\\frac{1}{4}BC^2": PINK
        }
        DC = np.array([2, -1, 0])
        DB = np.array([-2, -1, 0])
        DA = np.array([1, 2, 0])
        DD = np.array([0, -1, 0])
        texa = TexMobject("A").move_to(DA+UP*0.5)
        texb = TexMobject("B").move_to(DB+LEFT*0.5)
        texc = TexMobject("C").move_to(DC+RIGHT*0.5)
        texd = TexMobject("D").move_to(DD+DOWN*0.5)
        dot_d = Dot(DD)
        triangle1 = Polygon(DC, DA, DB).set_color(WHITE)
        self.play(ShowCreation(triangle1))
        self.play(*[Write(tex) for tex in [texa, texb, texc, texd, dot_d]])
        self.wait(0.5)
        vec_ab = Arrow(DA, DB, buff=0).set_color(YELLOW)
        vec_ac = Arrow(DA, DC, buff=0).set_color(YELLOW)
        vec_ad = Arrow(DA, DD, buff=0).set_color(PURPLE)
        vec_db = Arrow(DD, DB, buff=0).set_color(BLUE)
        vg_ab = VGroup(vec_ad, vec_db)
        vec_dc = Arrow(DD, DC, buff=0).set_color(RED)
        vg_ac = VGroup(vec_ad, vec_dc)
        text00 = TexMobject("\\overrightarrow{AB}", "=", "\\overrightarrow{AD}",
                            "+", "\\overrightarrow{DB}").set_color_by_tex_to_color_map(color_dict).move_to(DOWN*2.1)
        text01 = TexMobject("\\overrightarrow{AC}", "=", "\\overrightarrow{AD}",
                            "+", "\\overrightarrow{DC}").set_color_by_tex_to_color_map(color_dict).move_to(DOWN*3.1)
        self.play(ShowCreation(vec_ab))
        self.play(ReplacementTransform(vec_ab.copy(), text00[0:2]))
        self.wait(0.5)
        self.play(ReplacementTransform(vec_ab.copy(), vg_ab))
        self.play(ReplacementTransform(vg_ab.copy(), text00[2:]))
        self.wait(0.5)
        self.play(ShowCreation(vec_ac))
        self.play(ReplacementTransform(vec_ac.copy(), text01[0:2]))
        self.wait(0.5)
        self.play(ReplacementTransform(vec_ac.copy(), vg_ac))
        self.play(ReplacementTransform(vg_ac.copy(), text01[2:]))
        self.wait()
        vg_all = VGroup(texa, texb, texc, texd, dot_d,
                        triangle1, vec_ad, vec_db, vec_dc, vec_ab, vec_ac, text00, text01)
        self.play(vg_all.shift, LEFT*3.8)
        text1 = TexMobject(
            "\\overrightarrow{AB} \\cdot \\overrightarrow{AC}", " = (", "\\overrightarrow{AD}", "+", "\\overrightarrow{DB}", ") \\cdot (", "\\overrightarrow{AD}", "+", "\\overrightarrow{DC}", ")").move_to(RIGHT*2+UP*3)
        text1[0].set_color(YELLOW)
        text1[2].set_color(PURPLE)
        text1[4].set_color(BLUE)
        text1[6].set_color(PURPLE)
        text1[8].set_color(RED)
        self.play(Write(text1))
        self.wait(0.5)

        text2 = TexMobject("=", "\\overrightarrow{AD}", "^2", "+",
                           "\\overrightarrow{AD}", "\\cdot", "(", "\\overrightarrow{DB}", "+",
                           "\\overrightarrow{DC}", ")", "+", "\\overrightarrow{DB}", "\\cdot", "\\overrightarrow{DC}").set_color_by_tex_to_color_map(color_dict)
        text2.move_to(UP*2+RIGHT*2.3)
        self.play(Write(text2))
        self.wait(0.8)
        text3 = TexMobject(
            "\\overrightarrow{DB}", "+", "\\overrightarrow{DC}", "=", "\\vec{0}").set_color_by_tex_to_color_map(color_dict)
        text3.move_to(UP*1+RIGHT*2.5)
        self.play(Write(text3[0]), WiggleOutThenIn(vec_db))
        self.play(Write(text3[1]))
        self.play(Write(text3[2]), WiggleOutThenIn(vec_dc))
        self.play(Write(text3[3:]))
        self.wait(0.3)
        self.play(FadeOut(text3))
        self.play(FadeOut(text2[4:12]))
        self.play(text2[0:4].shift, RIGHT*2.05,
                  text2[12:].shift, LEFT*2.4)
        rect = Rectangle(height=0.9, width=2.2, color=YELLOW).move_to(
            text2[-2].get_center()+UP*0.1)
        self.play(ShowCreation(rect))
        text4 = TexMobject("\\overrightarrow{DB}", "\\cdot", "\\overrightarrow{DC}",  "=", "\\frac{1}{2}\\overrightarrow{CB}", "\\cdot", "\\frac{1}{2}\\overrightarrow{BC}",
                           "=", "-\\frac{1}{4}BC^2").set_color_by_tex_to_color_map(color_dict).move_to(rect.get_center()+DOWN*1+LEFT*1)
        self.play(Write(text4))
        self.wait(1.5)
        self.play(FadeOut(text4), FadeOut(rect))
        text5 = TexMobject(
            "=", "AD^2", "-\\frac{1}{4}BC^2").move_to(UP*1+RIGHT*1.7).set_color_by_tex_to_color_map(color_dict)
        self.play(Write(text5))
        self.wait(1.5)
        self.play(*[FadeOut(obj)
                    for obj in [text1[1:], text2[:4], text2[-3:], text00, text01]])
        self.play(text5.move_to, text1[0].get_center()+RIGHT*3+DOWN*0.1)
        vg_jl = VGroup(text1[0], text5)
        self.play(vg_jl.move_to, RIGHT*1.8+UP*1)
        text6 = TextMobject("极化恒等式", color="#FFFF00").next_to(vg_jl, DOWN)
        self.play(Write(text6))
        self.wait(2)


class test7(Scene):
    def construct(self):
        text1 = TextMobject("这是某个组合恒等式：", color="#FFFF00")
        self.play(Write(text1))
        text2 = TexMobject(
            "\\sum_{k=1}^{n}kC_n^k=n2^{n-1},\\ n\\in N_{+}")
        self.play(text1.shift, UP, FadeInFrom(text2, DOWN))
        text3 = TextMobject("(这里为了照顾中学生，没有写成$\\displaystyle\\binom{n}{k}$的形式)", color="#777777").scale(0.5).next_to(
            text2, DOWN)
        self.play(Write(text3))
        self.wait(0.3)
        self.play(FadeOut(text3))
        text4 = TextMobject("那么，如何证明呢？", color="#99AAFF").next_to(
            text2, DOWN)
        self.play(Write(text4))
        self.wait(2)
        self.play(*[FadeOut(obj) for obj in [text1, text2, text4]])


class test8(Scene):
    def construct(self):
        color_dict = {
            "n": "#88ddff",
            "k": "#FF7777",
            "班委": "#FF7777",
            "班长": "#9966FF"
        }
        text1 = TextMobject("首先，我们做这样一个假设", color="#FFFF00")
        self.play(Write(text1))
        self.play(text1.scale, 0.7,
                  text1.to_edge, UP)
        text2 = TextMobject("你的班级里有", "$n$", "个学生，你们打算选举班委").scale(
            0.7).move_to(UP*2.7+LEFT*3.2).set_color_by_tex_to_color_map(color_dict)
        text2[-1].set_color("#FFFFFF")
        self.play(Write(text2))
        rect0 = Rectangle(height=4, width=3, color="#aaffff").to_edge(RIGHT)
        dots = VGroup()
        for i in range(7):
            for j in range(5):
                dot_i_j = Dot(np.array([4.1+0.5*j, 1.5-0.5*i, 0]))
                dots.add(dot_i_j)
        self.play(FadeIn(rect0), FadeIn(dots))
        self.wait(0.8)
        text3 = TextMobject("你们打算从", "$n$", "名同学中选出", "$k$", "名作为班委,", "方法数为", "$C_n^k$").scale(
            0.7).set_color_by_tex_to_color_map(color_dict).next_to(text2, DOWN, aligned_edge=LEFT)
        text3[-3].set_color("#FF7777")
        text3[-1].set_color("#FFFFFF")
        self.play(Write(text3[:-2]))
        rect1 = Rectangle(height=1.1, width=2.6,
                          color="#FF7777").move_to(RIGHT*5.1+UP*1.3)
        self.play(FadeIn(rect1))
        self.play(Write(text3[-2:]))
        self.wait(0.8)
        text4 = TextMobject("接着，你们打算从这", "$k$", "名班委", "中选出", "一名班长,", "方法数为", "$C_k^1$").scale(
            0.7).set_color_by_tex_to_color_map(color_dict).next_to(text3, DOWN, aligned_edge=LEFT)
        text4[-3].set_color("#9966FF")
        text4[-1].set_color("#FFFFFF")
        text4[2].set_color("#FF7777")
        self.play(Write(text4[:-2]))
        rect2 = Rectangle(height=0.4, width=0.4,
                          color="#9966FF").move_to(RIGHT*4.1+UP*1.45)
        self.play(FadeIn(rect2))
        self.play(Write(text4[-2:]))
        self.wait(0.8)
        text5 = TextMobject("因此，总方法数为：", "$C_{k}^{1}C_{n}^{k}$", "即等于", "$kC_n^k$").scale(
            0.7).next_to(text4, DOWN, aligned_edge=LEFT)
        text5[-1].set_color("#FFFF33")
        self.play(Write(text5))
        self.wait(1)
        self.play(*[FadeOut(obj) for obj in [rect1, rect2]])
        text6 = TextMobject("我们还有另一种办法来选举", "班委", "和", "班长").scale(0.7).next_to(text5, DOWN, buff=0.5, aligned_edge=LEFT)\
            .set_color_by_tex_to_color_map(color_dict)
        self.play(Write(text6))
        self.wait(0.5)
        text7 = TextMobject("我们先在", "$n$", "名学生中选出", "一个班长,", "方法数为", "$C_n^1$").scale(
            0.7).next_to(text6, DOWN, aligned_edge=LEFT).set_color_by_tex_to_color_map(color_dict)
        text7[-1].set_color("#FFFFFF")
        self.play(Write(text7[:-2]))
        self.play(FadeIn(rect2))
        self.play(Write(text7[-2:]))
        self.wait(0.5)
        text8 = TextMobject("接着，我们从其余", "$n-1$", "个学生中选出", "$k-1$", "个", "不是班长",
                            "的", "班委").scale(0.7).next_to(text7, DOWN, aligned_edge=LEFT).set_color_by_tex_to_color_map(color_dict)
        self.play(Write(text8))
        rect3 = Polygon(np.array([4.4, 1.7, 0]), np.array(
            [6.3, 1.7, 0]), np.array([6.3, 0.7, 0]), np.array([3.9, 0.7, 0]),
            np.array([3.9, 1.2, 0]), np.array([4.4, 1.2, 0])).set_color("#FF7777")
        self.play(ShowCreation(rect3))
        text8_1 = TextMobject("方法数为", "$C_{n-1}^{k-1}$").scale(
            0.7).next_to(text8, DOWN, buff=SMALL_BUFF, aligned_edge=LEFT)
        self.play(Write(text8_1))
        self.wait(0.8)
        text9 = TextMobject(
            "因此，总方法数为：", "$C_{n}^{1}C_{n-1}^{k-1}$", "即等于", "$nC_{n-1}^{k-1}$").scale(
                0.7).next_to(text8_1, DOWN, aligned_edge=LEFT)
        text9[-1].set_color("#FFFF00")
        self.play(Write(text9))
        self.wait(1)
        text10 = TextMobject("我们发现，以上两种选举方式可以达到相同的结果，", "即$kC_n^k=nC_{n-1}^{k-1}$").scale(
            0.7).next_to(text9, DOWN, buff=0.5, aligned_edge=LEFT)
        text10[-1].set_color("#FFFF00")
        self.play(Write(text10))
        self.wait(3)
        sq = Square(fill_color="#000000", fill_opacity=1, side_length=20)
        self.play(FadeIn(sq))


class test9(Scene):
    def construct(self):
        text1 = TextMobject("有了刚才的结论", "$kC_n^k$", "$=$", "$nC_{n-1}^{k-1}$")
        text1[-3:].set_color("#FF7777")
        self.play(Write(text1))
        text2 = TextMobject("$\\displaystyle\\sum_{k=1}^{n}$", "$kC_n^k$",
                            "这个式子似乎就能比较轻松地化简了").move_to(DOWN*0.5)
        text2[1].set_color("#33FFBB")
        self.play(text1.shift, UP*0.5,
                  FadeInFrom(text2, DOWN))
        self.wait(1)
        self.play(FadeOut(text1[0]), FadeOut(text2[2]),
                  text2[0:2].move_to, UP*2+LEFT*2,
                  text1[1:].to_corner, UR)
        self.play(ShowCreationThenDestructionAround(SurroundingRectangle(text1[1])),
                  ShowCreationThenDestructionAround(SurroundingRectangle(text2[1])))
        self.wait(0.5)
        text2_1 = TextMobject("$\\displaystyle\\sum_{k=1}^{n}$", "$n$",
                              "$C_{n-1}^{k-1}$").move_to(text2[0:2].get_center())
        text2_1[1].set_color("#33AAFF")
        self.play(ReplacementTransform(text2[0:2], text2_1))
        self.wait(0.8)
        text3 = TextMobject("我们可以将这个$n$提到求和符外面来").scale(
            0.7).next_to(text2_1, DOWN).set_color("#AAAAAA")
        self.play(Write(text3))
        self.wait(0.5)
        self.play(FadeOut(text3))
        self.play(Swap(text2_1[0], text2_1[1]), text2_1[2].shift, RIGHT*0.2)
        self.wait(0.8)
        rect0 = Rectangle(height=1.5, width=2, color="#FFFF00").move_to(
            text2_1.get_center()+RIGHT*0.2)
        self.play(ShowCreationThenDestructionAround(rect0))
        self.play(text2_1.shift, LEFT*3)
        text4 = TexMobject(
            "=n", "(C_{n-1}^{1}+C_{n-1}^{2}+C_{n-1}^{3}+\\cdots +C_{n-1}^{n-1})").next_to(text2_1, RIGHT)
        self.play(Write(text4))
        self.wait(0.8)
        self.play(ShowCreationThenDestructionAround(
            SurroundingRectangle(text4[1])))
        text4_1 = TexMobject("2^{n-1}", color="#FFFF99").move_to(RIGHT*3+UP*1)
        self.play(ReplacementTransform(text4[1].copy(), text4_1))
        self.wait(0.3)
        text5 = TexMobject("=n2^{n-1}").next_to(text4, DOWN, aligned_edge=LEFT)
        self.play(Write(text5), FadeOut(text4_1))
        self.wait(0.8)
        text6 = TexMobject(
            "\\text{即}", "\\sum_{k=1}^{n}kC_n^k=n2^{n-1}", color="#FFFF99")
        self.play(Write(text6))
        self.wait(2.5)
        self.play(
            FadeIn(Square(side_length=20, fill_color="#000000", fill_opacity=1)))


class lic(Scene):

    def construct(self):
        text1 = Text("创作环境：Manim", font="思源黑体 CN Bold").scale(
            0.7).set_color_by_gradient("#AADDFF", "#AA7F66")
        self.play(Write(text1))
        self.wait(1)


class TestArrow(Scene):
    def construct(self):
        arr = MyArrow(np.array([-2, -1, 0]),
                      np.array([3, 2, 0]), color="#FFFF00")
        self.play(ShowCreation(arr))


class TestPolygon(Scene):
    CONFIG = {
        'camera_config': {'background_color': BLUE_A}
    }

    def construct(self):
        cell = 0.8
        dot_gp = VGroup()
        x = math.ceil(18/cell)
        y = math.ceil(10/cell)
        ra_n = 4
        for j in range(y):
            for i in range(x):
                dot_i_j = Dot(
                    np.array([i*cell-8+np.random.random()/ra_n, j*cell-5+np.random.random()/ra_n, 0]))\
                    .scale(0.5).set_opacity(0.)
                dot_gp.add(dot_i_j)
                self.add(dot_i_j)
        vg_pg = VGroup()
        for j in range(y-1):
            for i in range(x-1):
                pg_i_j = Polygon(dot_gp[i+j*x].get_center(),
                                 dot_gp[i+1+j*x].get_center(),
                                 dot_gp[i+1+(j+1)*x].get_center(),
                                 dot_gp[i+(j+1)*x].get_center())\
                    .set_color(["#88bbff", "#0077ff"]).set_stroke(width=0).set_opacity(np.random.random())
                vg_pg.add(pg_i_j)
        # vg_pg.set_color_by_gradient(["#88bbff", "#0077ff"])
        self.add(vg_pg)


class ellipse(Scene):
    def get_ellipse(self, a, b, **kwargs):
        return ParametricFunction(lambda t: a*np.cos(t)*RIGHT+b*np.sin(t)*UP, t_min=-PI, t_max=PI)

    def get_ellipse_tg_line(self, a, b, x0, y0, **kwargs):
        return ParametricFunction(lambda t: (y0+b**2*x0*t)*UP+(x0-a**2*y0*t)*RIGHT, t_min=-10, t_max=10)

    CONFIG = {"const_a": 3.0, "const_b": 2.0, "theta": PI/6}

    def construct(self):
        var = ValueTracker(self.theta)
        graph = self.get_ellipse(self.const_a, self.const_b)\
            .set_color("#0077FF")
        dot_ = Dot().add_updater(lambda a: a.move_to(
            self.const_a*np.cos(var.get_value())*RIGHT+self.const_b*np.sin(var.get_value())*UP))
        tg = self.get_ellipse_tg_line(self.const_a, self.const_b,
                                      self.const_a*np.cos(var.get_value()),
                                      self.const_b*np.sin(var.get_value())).set_color("#FFFF00")
        tg.add_updater(lambda m: m.become(
            self.get_ellipse_tg_line(self.const_a, self.const_b,
                                     self.const_a * np.cos(var.get_value()),
                                     self.const_b*np.sin(var.get_value())).set_color("#FFFF00")))
        self.add(graph)
        self.add(tg)
        self.add(dot_)
        self.play(var.increment_value, 2*PI/3)
        self.play(var.increment_value, -PI/2)
        self.wait(0.8)


class testarc(Scene):
    def construct(self):
        arc = TextMobject("F", color="#FFFF00").scale(2.5)
        self.add(arc)
        self.play(arc.flip, UP)
        self.wait()


class rtl(Scene):

    def construct(self):
        text1 = TextMobject("This is some text").scale(2.5)
        text2 = TextMobject("This is some text").scale(2.5)
        self.play(Write(text1))
        self.wait(0.5)
        self.play(Erase(text1))
        self.wait(0.5)
        self.play(ReversedWrite(text2[0]))
        self.wait(0.5)
        self.play(EraseFromLeft(text2[0]))
        self.wait(0.5)
