from manimlib import *


class ObjPoints(VGroup):
    CONFIG = {
        "scale_factor": 0.5,
        "color": YELLOW_B,
    }

    def __init__(self, obj, **kwargs):
        VGroup.__init__(self, **kwargs)
        for point in obj.get_all_points():
            dot_i = Dot(point).scale(self.scale_factor).set_color(self.color)
            self.add(dot_i)

class AllPointsIndex(VGroup):
    CONFIG = {
        "scale_factor": 0.5,
        "color": PURPLE,
    }

    def __init__(self, obj, **kwargs):
        # digest_config(self, kwargs)
        VGroup.__init__(self, **kwargs)
        for index, points in enumerate(obj.get_all_points()):
            point_id = Text(str(index)) \
                .scale(self.scale_factor).set_color(self.color)
            point_id.move_to(points)
            self.add(point_id)


class Scene12(Scene):
    def construct(self):
        cir = Circle(radius=2).shift(LEFT*3)
        pol = RegularPolygon(8, color=BLUE_D).scale(2).shift(RIGHT*3)
        self.play(ShowCreation(cir), ShowCreation(pol))
        self.wait()
        ptc = AllPointsIndex(cir, color=YELLOW_B)
        ptp = AllPointsIndex(pol, color=PURPLE_A)
        self.play(FadeIn(ptc), FadeIn(ptp))
        self.wait()
        self.play(cir.shift, UP*1.3, ptc.shift, UP*1.3,
                  pol.shift, UP*1.3, ptp.shift, UP*1.3)
        self.wait()
        brace_group = VGroup(
            VGroup(*[Text("(    )", font="Consolas").scale(0.7)for i in range(8)]).arrange(RIGHT),
            VGroup(*[Text("(    )", font="Consolas").scale(0.7)for i in range(8)]).arrange(RIGHT),
            VGroup(*[Text("(    )", font="Consolas").scale(0.7)for i in range(8)]).arrange(RIGHT),
        ).arrange(DOWN).set_color(GOLD_D)
        brace_group.move_to(DOWN*2)
        self.play(Write(brace_group))
        self.wait()
        num_group = VGroup(
            VGroup(*[Text(f"{i}", color=YELLOW_B).scale(0.5).move_to(brace_group[i//8][i%8].get_center()+LEFT*0.2)
                     for i in range(24)]),
            VGroup(*[Text(f"{i}", color=PURPLE_A).scale(0.5).move_to(brace_group[i//8][i%8].get_center()+RIGHT*0.2)
                     for i in range(24)]),
        )
        for i in range(24):
            self.play(TransformFromCopy(ptc[i], num_group[0][i]),
                      TransformFromCopy(ptp[i], num_group[1][i]),
                      run_time=max([abs((i-12.5)/12), 0.1]))
        self.wait()
        pol_ = pol.copy()
        self.play(TransformFromCopy(cir, pol_), rate_func=linear, run_time=1.8)
        self.wait()
        self.remove(pol_)
        self.play(FadeOut(brace_group, DOWN),
                  FadeOut(num_group, DOWN),
                  cir.shift, DOWN*1.3, ptc.shift, DOWN*1.3,
                  pol.shift, DOWN*1.3, ptp.shift, DOWN*1.3)
        self.wait()
        sq = Square(side_length=4, color=BLUE_D).move_to(pol.get_center())
        pts = AllPointsIndex(sq, color=PURPLE_A)
        self.play(ReplacementTransform(pol, sq),
                  ReplacementTransform(ptp, pts))
        self.wait()
        sq2 = Polygon(*[sq.data["points"][i]for i in [0,1,3,4,6,7,9,10]],color=BLUE)
        pts2 = AllPointsIndex(sq2, color=GREEN_A)
        self.play(ReplacementTransform(sq, sq2),
                  ReplacementTransform(pts, pts2))
        self.wait()
        self.play(TransformFromCopy(cir, sq2.copy()), run_time=2, rate_func=linear)
        self.wait()

class CodeLine(Text):
    CONFIG = {
        't2c': {
            '0': average_color(BLUE, PINK),
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            'return': "#C594C5",
            'def': "#C594C5",
            "int": "#569CD6",
            'interpolate': "#60B4B4",
            'interpolate_mobject': "#60B4B4",
            '"': "#60B4B4",
            "'": "#60B4B4",
            'start': "#FAB763",
            'end': "#FAB763",
            'alpha': "#FAB763",
            ":": "#FA9044",
            "+": "#FA9044",
            "*": "#FA9044",
            "-": "#FA9044",
            "=": "#FA9044",
            ",": GREY,
            "digit": "#569CD6",
            " x": "#9CDCFE",
            "ss": "#9CDCFE",
            "String": "#4EC9B0",
            "class": "#569CD6",
            "MyBox": "#4EC9B0",
            "function": "#569CD6",
            "gcd": "#DCDCAA",
            ".": GREY,
            "box": "#9CDCFE",
            "self": "#D86066",
            "shift": "#569CD6",
            "play": "#569CD6",
            "Square": "#569CD6",
            "add_updater": "#569CD6",
            "UP": "#FAB763",
            "DOWN": "#FAB763",
            "LEFT": "#FAB763",
            "RIGHT": "#FAB763",
            "ORIGIN": "#FAB763",
            "PI": "#FAB763",
            "args":"#FAB763",
            "kwargs": "#FAB763",
            "(": GREY_B,
            ")": GREY_B,
            "generate_target": "#569CD6",
            "MoveToTarget": "#569CD6",
            "anims_from_play_args": "#569CD6",
            "Scene": "#4EC9B0",
            "Rotating": "#569CD6",
            "\{":GREY_A,
            "\}":GREY_A,
            # "become": "#569CD6"
        },
        'font': 'Fira Code Medium',
        'size': 0.64,
        'color': "#e0e0e0",
        "stroke_width": 0,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)

class Scene17(Scene):
    def construct(self):
        t1 = CodeLine("math_object").scale(1.2)
        t2 = CodeLine("mobject").scale(1.2)
        t3 = CodeLine(".generate_target()").scale(1.2).next_to(t2, buff=0.12).shift(LEFT*3)
        self.play(Write(t1))
        self.wait()
        self.play(TransformMatchingShapes(t1, t2))
        self.play(t2.shift, LEFT*3,FadeIn(t3, LEFT))
        self.wait()
        self.play(t2.to_corner, UL, 
                  UpdateFromFunc(t3, lambda a:a.next_to(t2, buff=0.12)))
        cir = Circle(radius=1.5).move_to(np.array([-3.5,-0.5,0]))
        t_cur = TexText("current").next_to(cir, DOWN)
        t_tar = TexText("target").next_to(t_cur, DOWN).set_opacity(0.7)
        self.play(ShowCreation(cir), Write(t_cur), Write(t_tar))
        code = VGroup(
            CodeLine("mobject.target = Square().shift(RIGHT*3)").scale(1.2),
            CodeLine("self.play(MoveToTarget(mobject))").scale(1.2)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(t2, DOWN, aligned_edge=LEFT)
        sq = Square(side_length=3, color=BLUE).shift(RIGHT*3.5+DOWN*0.5)
        self.wait()
        self.play(Write(code[0]))
        self.wait()
        self.play(ShowCreation(sq), 
                  t_tar.become, TexText("target").next_to(sq, DOWN))
        self.wait()
        self.play(Write(code[1]))
        self.wait()
        sqk = sq.copy()
        self.play(ReplacementTransform(cir, sqk),
                  t_cur.next_to, sq, DOWN,
                  t_tar.shift, DOWN/2, run_time=1.5)
        self.wait(2)
        code_n = CodeLine(r"self.play(mobject.become,{'mobject':Square().shift(RIGHT*3)})").scale(1.1)
        code_n.align_to(code, UL)
        code_n[27:34].set_color("#99C794")
        self.play(FadeOut(t2, DOWN), FadeOut(t3, DOWN), FadeOut(code[0]), FadeOut(code[1], UP),
                  FadeIn(code_n))
        self.wait()
        ft = "庞门正道标题体"
        code_play = VGroup(
            CodeLine("# Scene中play的定义", t2f={"中":ft, "的定义":ft}).set_color(GREY),
            CodeLine("def play(self, *args, **kwargs):"),
            CodeLine("..."),
            CodeLine("animations = self.anims_from_play_args(*args, **kwargs)"),
            CodeLine("...")).scale(1.1).arrange(DOWN, aligned_edge=LEFT).align_to(code_n, LEFT).shift(UP*2.4)
        code_play[2:].shift(RIGHT*0.95)
        self.play(Write(code_play), FadeOut(sq), FadeOut(sqk), FadeOut(t_tar), FadeOut(t_cur), code_n.shift, DOWN*2.3)
        self.wait()
        self.play(ShowCreationThenFadeAround(SurroundingRectangle(code_n[10:24])),
                  ShowCreationThenFadeAround(SurroundingRectangle(code_play[1][15:20])))
        self.wait()
        self.play(ShowCreationThenFadeAround(SurroundingRectangle(code_n[25:-1])),
                  ShowCreationThenFadeAround(code_play[1][22:30]))
        self.wait()
        code_ex = VGroup(
            CodeLine("mobject.generate_target()"),
            CodeLine("mobject.target = Square().shift(RIGHT*3)"),
            CodeLine("self.play(MoveToTarget(mobject))")
        ).scale(1.2).arrange(DOWN, aligned_edge=LEFT).next_to(code_n, DOWN, buff=0.7, aligned_edge=LEFT)
        bc = BackgroundRectangle(code_ex, buff=0.25)
        self.play(FadeIn(bc))
        self.play(TransformMatchingShapes(code_n[10:24].copy(), code_ex[0]))
        self.wait()
        self.play(TransformMatchingShapes(code_n[10:-1].copy(), code_ex[1]))
        self.wait()
        self.play(TransformMatchingShapes(code_n[0:10].copy(), code_ex[2]))
        self.wait()


class Scene18(Scene):
    def construct(self):
        sq1 = VGroup(Square(side_length=1,color=BLUE), Tex("1")).shift(LEFT*2)
        sq2 = VGroup(Square(side_length=1,color=RED), Tex("2")).shift(RIGHT*2)
        axes = Axes(axis_config={ "include_tip": False, },y_range=[-6,6,1], x_range=[-10,10,1])
        # co1 = VGroup(
        #     CodeLine(r"self.play(Rotating(sq1, PI,"),
        #     CodeLine(r"about_point=ORIGIN))")
        # )

        # co1[1].next_to(co1[0][2], DR, buff=0.4)
        # co1.to_corner(UL)
        # co1[1][0:11].set_color("#FAB763")

        # co2 = VGroup(
        #     CodeLine(r"self.play(sq2.rotate,"),
        #     CodeLine(r"{'angle':PI,"),
        #     CodeLine(r"'about_point':ORIGIN})"),
        # )
        # co2[1].next_to(co2[0][2], DR, buff=0.4)
        # co2[2].next_to(co2[1], DOWN, aligned_edge=LEFT, buff=0.1)
        # co2.to_corner(UR)
        # co2[1][2:7].set_color("#99C794")
        # co2[2][1:12].set_color("#99C794")

        co1 = CodeLine(r"self.play(Rotating(sq1, PI, about_point=ORIGIN))", t2c={"about_point":"#FAB763"}).to_corner(UL)
        co2 = CodeLine(r"self.play(sq2.rotate, {'angle':PI,'about_point':ORIGIN})", 
                        t2c={
                            "about_point": "#99C794", "angle": "#99C794"
                        }).next_to(co1, DOWN, aligned_edge=LEFT)

        self.play(ShowCreation(axes))
        self.play(Write(sq1), Write(sq2))
        self.play(Write(co1), Write(co2))
        self.wait()
        self.play(Rotating(sq1, angle=PI, about_point=ORIGIN),
                  sq2.rotate, {"angle":PI,"about_point":ORIGIN},
                  run_time=5, rate_func=linear)
        self.wait()
        code2 = VGroup(
            CodeLine("sq2.generate_target()"),
            CodeLine("sq2.target=sq2.rotate(PI,about_point=ORIGIN)",t2c={"about_point":"#FAB763"}),
            CodeLine("self.play(MoveToTarget(sq2))")
        ).arrange(DOWN, aligned_edge=LEFT).next_to(co2, DOWN, aligned_edge=LEFT, buff=0.8)
        self.play(axes.shift, DOWN*2,
                  sq2.shift, DOWN*2,
                  FadeOut(sq1, DOWN*2))
        self.play(TransformMatchingShapes(co2[10:20].copy(), code2[0]))
        sq2c = VGroup(Square(side_length=1,color=RED, stroke_opacity=0.3), Tex("2", fill_opacity=0.3)).shift(LEFT*2+DOWN*2).rotate(PI)
        self.add(sq2c)
        t_tar = TexText("target").scale(0.6).next_to(sq2c, UP)
        self.play(TransformMatchingShapes(co2[10:-1].copy(), code2[1]))
        self.play(FadeIn(t_tar))
        self.add(t_tar)
        self.play(sq2c.rotate, {"angle":PI,"about_point":DOWN*2}, t_tar.shift, RIGHT*4)
        self.play(TransformMatchingShapes(co2[0:9].copy(), code2[2]))
        self.play(sq2.rotate, {"angle":PI,"about_point":DOWN*2}, run_time=2)
        self.wait()
        sq1.shift(DOWN*2)
        self.play(FadeOut(sq2), FadeOut(sq2c), FadeIn(sq1), FadeOut(code2), FadeOut(co2), FadeOut(t_tar))
        self.play(sq1.shift, RIGHT*3, axes.shift, RIGHT*3)
        _4 = CodeLine("aaaa")
        code1 = VGroup(
            CodeLine("def interpolate_mobject(self, alpha):"),
            CodeLine("..."),
            CodeLine("self.mobject.rotate(", t2c={"rotate":"#569CD6"}),
            CodeLine("alpha * self.angle,"),
            CodeLine("axis=self.axis,"),
            CodeLine("about_point=self.about_point,"),
            CodeLine("about_edge=self.about_edge,"),
            CodeLine(")")
        ).arrange(DOWN, aligned_edge=LEFT).next_to(co1, DOWN, aligned_edge=LEFT, buff=0.8)
        code1[1:].shift(RIGHT*_4.get_width())
        code1[3:7].shift(RIGHT*_4.get_width())
        code1[4][0:4].set_color("#FAB763")
        code1[5][0:11].set_color("#FAB763")
        code1[6][0:10].set_color("#FAB763")
        code1[5][-4:-1].set_color("#e0e0e0")
        self.play(Write(code1))
        self.wait()
        enve = VGroup()
        sq1c = sq1.copy()
        sq1c[0].set_stroke(opacity=0.2)
        sq1c[1].set_fill(opacity=0.2)
        sq1c.save_state()

        def en_anim(obj, alpha):
            obj.restore()
            obj.rotate(PI*alpha, about_point=np.array([3, -2, 0]))
        
        def en_anim2(obj):
            k = sq1c.copy()
            k[0].set_stroke(width=1)
            obj.add(k.copy())
        
        self.add(sq1c, enve)
        self.play(UpdateFromAlphaFunc(sq1c, en_anim),
                  UpdateFromFunc(enve, en_anim2), run_time=3, rate_func=linear)
        self.wait()
        self.play(Rotating(sq1, PI, about_point=np.array([3,-2,0])),
                  UpdateFromFunc(enve, lambda a:a.remove(enve[0])),
                  run_time=3, rate_func=linear)
        self.remove(sq1c)
        self.wait()


class UpdaterExample(Scene):
    def construct(self):
        dot = Dot(np.array([-2,-1,0]))
        text = Text("This is a dot")
        text.next_to(dot, RIGHT)

        self.add(dot, text)
        self.play(dot.shift, UP*3, 
                  rate_func=there_and_back,
                  run_time=3)
        text.add_updater(lambda a: a.next_to(dot, RIGHT))
        self.play(dot.shift, UP*3, 
                  rate_func=there_and_back,
                  run_time=3)
        text.clear_updaters()
        self.play(dot.shift, UP*3, 
                  rate_func=there_and_back,
                  run_time=3)


class TestDt(Scene):
    def construct(self):
        obj = Circle().shift(LEFT*7)
        obj.add_updater(lambda a, dt: a.shift(RIGHT*dt))
        self.add(obj)
        self.wait(10)