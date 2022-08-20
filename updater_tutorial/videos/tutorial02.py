from manimlib import *


# from manim_sandbox.utils.imports import *


class TexIndex(VGroup):
    CONFIG = {
        "scale_factor": 0.5,
        "color": PURPLE,
    }

    def __init__(self, obj, **kwargs):
        VGroup.__init__(self, **kwargs)
        for index, single_tex in enumerate(obj):
            tex_index = Integer(index, background_stroke_width=2) \
                .scale(self.scale_factor).set_color(self.color)
            tex_index.move_to(single_tex.get_center())
            self.add(tex_index)


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
            'lambda': "#C594C5",
            "int": "#569CD6",
            'interpolate': "#60B4B4",
            'smooth': "#60B4B4",
            'smooth_interpolate': "#60B4B4",
            'start': "#FAB763",
            'end': "#FAB763",
            'alpha': "#FAB763",
            ":": "#FA9044",
            "+": "#FA9044",
            "*": "#FA9044",
            "-": "#FA9044",
            ",": GREY,
            # "digit": "#569CD6",
            # "x": "#9CDCFE",
            # "ss": "#9CDCFE",
            # "String": "#4EC9B0",
            "class": "#C594C5",
            # "MyBox": "#4EC9B0",
            # "function": "#569CD6",
            # "gcd": "#DCDCAA",
            ".": GREY,
            "box": "#9CDCFE",
            "self": "#D86066",
            "play": "#569CD6",
            "next_to": "#569CD6",
            "add_updater": "#569CD6",
            "remove_updater": "#569CD6",
            "clear_updaters": "#569CD6",
            "shift": "#569CD6",
            "animate": "#569CD6",
            "UP": "#FAB763",
            "LEFT": "#FAB763",
            "RIGHT": "#FAB763",
            "DOWN": "#FAB763",
            "DR": "#FAB763",
            "PI": "#FAB763",
            "(": GREY_B,
            ")": GREY_B,
            "generate_target": "#569CD6",
            "__init__": "#569CD6",
            "super": "#569CD6",
            "save_state": "#569CD6",
            "restore": "#569CD6",
            "rotate": "#569CD6",
            "interpolate_mobject": "#60B4B4",
            "move_to": "#569CD6",
            "set_value": "#569CD6",
            "point_from_proportion": "#569CD6",
        },
        "t2s": {
            "lambda": OBLIQUE,
            "self": OBLIQUE,
            "def": OBLIQUE,
            "class": OBLIQUE,
        },
        'font': 'Monaco_fix',
        'size': 0.64,
        'color': "#e0e0e0",
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class UpdateFromAlphaFuncExample(Scene):
    def construct(self):
        cir = Circle()
        squ = Square()

        def anim(obj, alpha):
            obj.set_points(
                interpolate(cir.get_all_points(),
                            squ.copy().align_points(cir).get_all_points(),
                            alpha)
            )
            obj.set_color(interpolate_color(cir.get_color(), squ.get_color(), alpha))

        self.add(cir)
        self.play(UpdateFromAlphaFunc(cir, anim))


class Dash(VMobject):
    CONFIG = {
        "positive_space_ratio": 0.5,
        "dash_length": 0.2,
        "color": WHITE,
    }

    def __init__(self, vmobject, **kwargs):
        super().__init__(**kwargs)
        digest_config(self, kwargs)
        psr = self.positive_space_ratio
        dash_len = self.dash_length
        arc_len = vmobject.get_arc_length()
        # print(arc_len)
        num_dashes = int(arc_len / dash_len)
        pnts = []
        # print(pnts)
        for i in range(num_dashes):
            for j in range(3):
                # pnts = np.concatenate((pnts, vmobject.point_from_proportion((i+j/6)/num_dashes)), axis=0)
                pnts.append(vmobject.point_from_proportion((i + j / 6) / num_dashes))
        # print(len(pnts))
        self.set_points(pnts)


class Scene01(Scene):
    def construct(self):
        t1 = TexText("Updater教程").scale(2).shift(UP / 2).to_edge(LEFT)
        t2 = TexText("重制版").scale(1.3).shift(DOWN / 2).to_edge(RIGHT)
        t3 = TexText("Episode 2").scale(2).shift(UP / 2).shift(LEFT * 5)
        t4 = TexText("再话alpha与updater").scale(1.3).shift(DOWN / 2).shift(7 * RIGHT)
        t4[0][2:7].set_color(ORANGE)
        t4[0][8:].set_color(YELLOW)

        def anim_to_center(obj, dt):
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        t1.add_updater(anim_to_center)
        t2.add_updater(anim_to_center)
        anim1 = Write(t1)
        anim2 = Write(t2)
        self.add(t1, t2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait(3)
        t1.clear_updaters()
        t2.clear_updaters()
        t3.add_updater(anim_to_center)
        t4.add_updater(anim_to_center)
        anim3 = Write(t3)
        anim4 = Write(t4)
        self.add(t3, t4)
        turn_animation_into_updater(anim3)
        turn_animation_into_updater(anim4)
        self.play(t1.shift, UP * 6, t1.scale, 0.5,
                  t2.shift, DOWN * 6, t2.scale, 0.5)
        self.wait(2)


# class Scene02(Scene):
#     def construct(self):
#         space1 = Dash(Square(side_length=1.5), color=GREY).shift(LEFT*3).scale(1.05).rotate(PI/4)
#         space2 = Dash(Square(side_length=1.5), color=GREY).shift(RIGHT*3).scale(1.05).rotate(PI/4)
#         squ1 = Square(side_length=1.5, fill_opacity=1, stroke_width=0).shift(LEFT*3).rotate(PI/4)
#         squ1.set_color(BLUE)
#         self.play(ShowCreation(space1), ShowCreation(space2))
#         self.play(FadeInFromPoint(squ1, squ1.get_center()))
#         self.wait()
#         self.play(squ1.shift, RIGHT*6, run_time=3, rate_func=linear)
#         self.wait()
#         cir = Circle(radius=1, fill_opacity=1, stroke_width=0).shift(RIGHT*3).scale(2)
#         cir.set_color(RED)
#         pol = RegularPolygon(8, color=ORANGE).shift(LEFT*3).scale(2)
#         self.play(
#             ReplacementTransform(squ1, cir),
#             Transform(space2, Dash(Circle(radius=1).shift(RIGHT*3).scale(2.05), color=GREY)),
#             Transform(space1, Dash(RegularPolygon(8).shift(LEFT*3).scale(2.05), color=GREY)),
#         )


class Scene03(Scene):
    CONFIG = {
        "camera_config": {"background_color": "#1f252a"}
    }

    def construct(self):
        axes = VGroup(
            Axes(x_range=[0, 11, 1], y_range=[0, 6, 1], width=11, height=6, color=GREY),
            Tex("\\alpha").scale(0.6),
            TexText("start").scale(0.6), TexText("end").scale(0.6)
        )
        axes[1].next_to(axes[0].c2p(11, 0))
        axes[2].move_to(axes[0].c2p(-0.5, 0))
        axes[3].move_to(axes[0].c2p(-0.5, 5))
        self.add(axes)
        dot0 = Dot(axes[0].c2p(0, 0), color=BLUE)
        dot = Dot(axes[0].c2p(0, 0), color=GOLD)
        tri = Triangle(fill_opacity=1, color=YELLOW).scale(0.1).move_to(axes[0].c2p(0, -0.3))
        self.play(Write(dot0), Write(tri), Write(dot))
        self.wait()
        # 原正比例函数
        line_func = VGroup(
            *[Line(axes[0].c2p(i / 5, i / 10), axes[0].c2p((i + 1) / 5, (i + 1) / 10), color=ORANGE) for i in
              range(50)])
        line_x = DashedLine().add_updater(
            lambda a: a.put_start_and_end_on([dot.get_center()[0], -3, 0], dot.get_center()))
        line_y = DashedLine().add_updater(
            lambda a: a.put_start_and_end_on([-5.5, dot.get_center()[1], 0], dot.get_center()))
        self.add(line_x, line_y)
        # 原点的运动轨迹
        line_w = VGroup(
            *[Line(axes[0].c2p(0, i / 10), axes[0].c2p(0, (i + 1) / 10), color=BLUE, stroke_width=20) for i in
              range(50)])
        self.play(
            ShowCreation(line_func),
            ShowCreation(line_w),
            dot0.shift, UP * 5,
            dot.shift, [10, 5, 0],
            tri.shift, RIGHT * 10,
            run_time=3, rate_func=linear
        )
        line_x.clear_updaters()
        line_y.clear_updaters()
        self.wait()
        text1 = Text("连续", font="庞门正道标题体").scale(2).next_to(line_w, RIGHT)
        text2 = Text("离散", font="庞门正道标题体").scale(2).next_to(line_w, RIGHT)
        self.play(Write(text1))
        self.wait()
        # 离散运动轨迹
        dot_group = VGroup(*[Dot(axes[0].c2p(0, i / 10), color=YELLOW).scale(0.2) for i in range(50)])
        # 离散函数
        line_group = VGroup(*[
            Line(axes[0].c2p(i / 5, i / 10), axes[0].c2p((i + 1) / 5, i / 10), color=ORANGE)
            for i in range(50)
        ])
        self.play(
            ReplacementTransform(line_w, dot_group),
            ReplacementTransform(line_func, line_group),
            ReplacementTransform(text1, text2)
        )
        self.wait()
        self.play(
            line_group.set_stroke, {"opacity": 0.3},
            line_x.set_stroke, {"opacity": 0.3},
            line_y.set_stroke, {"opacity": 0.3},
        )

        data_right = Dot(LEFT * 2).scale(0.3)
        data_fix = Dot(LEFT * 2).scale(0.3)

        lable_opengl = VGroup(
            TexText("OpenGL")
        )
        lable_opengl.add(SurroundingRectangle(lable_opengl[0]))

        label_pyglet = VGroup(
            TexText("Pyglet")
        )
        label_pyglet.add(SurroundingRectangle(label_pyglet[0]))
        label_ffmpeg = VGroup(
            TexText("FFmpeg")
        )
        label_ffmpeg.add(SurroundingRectangle(label_ffmpeg[0]))

        lable_opengl.next_to(data_fix, buff=1)
        label_pyglet.next_to(lable_opengl, UR)
        label_ffmpeg.next_to(lable_opengl, DR)

        line_1 = Line(data_fix.get_center(), lable_opengl.get_left(), color=GREY)
        line_show_1 = line_1.copy().set_stroke(YELLOW, width=10)

        line_2 = Line(lable_opengl.get_right(), label_pyglet.get_left(), color=GREY)
        line_show_2 = line_2.copy().set_stroke(YELLOW, width=10)
        line_3 = Line(lable_opengl.get_right(), label_ffmpeg.get_left(), color=GREY)
        line_show_3 = line_3.copy().set_stroke(YELLOW, width=10)

        label_window = VGroup(TexText("Window"))
        label_window.add(SurroundingRectangle(label_window[0]))
        label_window.next_to(label_pyglet)
        label_video = VGroup(TexText("video file"))
        label_video.add(SurroundingRectangle(label_video[0]))
        label_video.next_to(label_ffmpeg)

        line_4 = Line(label_pyglet.get_right(), label_window.get_left(), color=GREY)
        line_5 = Line(label_ffmpeg.get_right(), label_video.get_left(), color=GREY)
        line_show_4 = line_4.copy().set_stroke(YELLOW, width=10)
        line_show_5 = line_5.copy().set_stroke(YELLOW, width=10)
        label_preview = TexText("预览").scale(0.8).next_to(label_pyglet, UP)
        label_write = TexText("写入").scale(0.8).next_to(label_ffmpeg, DOWN)

        self.play(
            Write(lable_opengl), Write(line_1),
            Write(label_pyglet), Write(label_ffmpeg),
            Write(label_video), Write(label_window),
            Write(line_2), Write(line_3),
            Write(line_4), Write(line_5),
            Write(label_preview), Write(label_write),
        )
        # self.add(line_show)
        # turn_animation_into_updater(anim_flash, cycle=True)
        for i in range(50):
            self.play(dot_group[i].scale, 10,
                      dot_group[i].set_color, BLUE,
                      run_time=0.3)
            self.play(
                TransformFromCopy(dot_group[i], data_right),
                ShowPassingFlash(line_show_1),
                ShowPassingFlash(line_show_2),
                ShowPassingFlash(line_show_3),
                ShowPassingFlash(line_show_4),
                ShowPassingFlash(line_show_5),
                dot_group[i].scale, 0.1,
                dot_group[i].set_color, YELLOW,
                run_time=0.3)
            if i == 0:
                self.add(data_fix)
        self.wait()


class Scene04(Scene):
    def construct(self):
        code = VGroup(
            CodeLine("def interpolate(start, end, alpha):"),
            CodeLine("return (1 - alpha) * start + alpha * end"),
        )
        code[1].next_to(code[0][4], DOWN, aligned_edge=LEFT, buff=0.5)
        code.move_to(ORIGIN)
        self.play(Write(code))
        self.wait()
        # label_yici = TexText("一次函数").shift(RIGHT*4)
        fomula = CodeLine("s = interpolate(0, 1, t)")
        fomula2 = CodeLine("s = vt, v = 1")
        fomula[-2].set_color("#FAB763")
        fomula2[4].set_color("#60B4B4")
        fomula2[5].set_color("#FAB763")
        fomula2[8].set_color("#60B4B4")
        self.play(
            FadeIn(fomula, UP),
            code.to_edge, UP
        )
        self.play(ReplacementTransform(fomula, fomula2))
        self.wait()
        axes = Axes(
            x_range=[0, 1.25, 0.25], y_range=[0, 1.25, 0.25],
            width=5, height=5).shift(LEFT * 3.3 + DOWN / 2)
        axes.add_coordinate_labels(num_decimal_places=2)
        label_s = Tex("s").scale(0.8).move_to(axes.c2p(0.1, 1.25))
        label_t = Tex("t").scale(0.8).move_to(axes.c2p(1.25, 0.1))
        self.play(Write(axes), Write(label_s), Write(label_t))
        self.wait()
        self.play(fomula2.shift, RIGHT * 1.5)
        line_func = Line(axes.c2p(0, 0), axes.c2p(1, 1), color="#FAB763")
        line_x = DashedLine()
        line_y = DashedLine()
        self.wait()
        self.add(line_x, line_y)
        line_x.add_updater(lambda a: a.put_start_and_end_on(
            line_func.get_end(), np.array([line_func.get_end()[0], axes.c2p(0, 0)[1] - 0.05, 0]),
        ))
        line_y.add_updater(lambda a: a.put_start_and_end_on(
            line_func.get_end(), np.array([axes.c2p(0, 0)[0] - 0.05, line_func.get_end()[1], 0]),
        ))
        self.play(ShowCreation(line_func), rate_func=linear, run_time=2)
        line_x.clear_updaters()
        line_y.clear_updaters()
        self.wait()
        code2 = VGroup(
            CodeLine("def smooth_interpolate(start, end, alpha):"),
            CodeLine("def smooth(t):"),
            CodeLine("return"),
            Tex(r"{t^3}{(10(1-t)^2+5(1-t)t+t^2)}").scale(0.7),
            CodeLine("return (1-smooth(alpha))*start+smooth(alpha)*end"),
        )
        code2[1].next_to(code2[0][4], DOWN, buff=0.5, aligned_edge=LEFT)
        code2[2].next_to(code2[1][4], DOWN, buff=0.5, aligned_edge=LEFT)
        code2[3].next_to(code2[2], RIGHT)
        code2[4].next_to(code2[1], DOWN, buff=0.8, aligned_edge=LEFT)
        code2[1][-3].set_color("#FAB763")
        # ind = TexIndex(code2[3][0])
        # self.add(ind)
        for i in [0, 8, 16, 18, 20]:
            code2[3][0][i].set_color("#FAB763")
        code2.move_to(ORIGIN)
        code2.to_edge(UP)
        sm_func = FunctionGraph(smooth, [0, 1, 0.05], stroke_width=6, color="#FAB763")
        sm_func.move_to(line_func.get_center()).set_width(line_func.get_width())
        self.play(FadeOut(fomula2), TransformMatchingShapes(code, code2), ReplacementTransform(line_func, sm_func))
        self.wait()
        funcs = VGroup(
            CodeLine("rush_into(start, end, alpha)"),
            CodeLine("rush_from(start, end, alpha)"),
            CodeLine("slow_into(start, end, alpha)"),
            CodeLine("running_start(start, end, alpha)"),
            CodeLine("wiggle(start, end, alpha)"),
            CodeLine("...")
        ).arrange(DOWN, aligned_edge=LEFT).move_to(RIGHT * 2.8 + DOWN)
        for i in range(4):
            funcs[i][:9].set_color("#60B4B4")
        funcs[3][:13].set_color("#60B4B4")
        funcs[4][:6].set_color("#60B4B4")
        self.play(FadeIn(funcs, DOWN), lag_ratio=0.02, run_time=3)
        self.wait()


class Scene05(Scene):
    def construct(self):
        l_s2e = Line(LEFT * 3, RIGHT * 3)
        t_start = CodeLine("start").scale(1.3).move_to(l_s2e.get_start() + DOWN * 0.5)
        t_end = CodeLine("end").scale(1.3).move_to(l_s2e.get_end() + DOWN * 0.5)
        p_tri = Triangle(fill_opacity=1, color=YELLOW).scale(0.15).move_to(l_s2e.get_start() + UP * 0.3).rotate(PI)
        t_alpha = VGroup(
            Tex("\\alpha ="),
            DecimalNumber()
        )
        t_alpha[1].next_to(t_alpha[0])
        t_alpha.next_to(p_tri, UP)
        t_lim = Tex("\\alpha\\in [0,1]").next_to(l_s2e, DOWN)
        self.play(Write(t_start), Write(t_end), ShowCreation(l_s2e))
        self.wait()
        self.play(ShowCreation(p_tri), Write(t_alpha))
        self.wait()
        self.play(Write(t_lim))
        # self.wait()
        self.play(
            UpdateFromAlphaFunc(t_alpha[1], lambda a, alpha: a.set_value(alpha)),
            UpdateFromFunc(t_alpha, lambda a: a.next_to(p_tri, UP)),
            p_tri.shift, RIGHT * 6,
            run_time=3, rate_func=linear,
        )
        self.wait()
        t_func_a = VGroup(
            Tex("f(\\alpha)="),
            DecimalNumber(),
        ).arrange(RIGHT).move_to(l_s2e.get_start() + UP * 0.9)
        t_fun_lim = Tex("f(\\alpha)\\in [0,1]").next_to(t_lim, DOWN)
        self.play(
            ReplacementTransform(t_alpha, t_func_a),
            Write(t_fun_lim),
            p_tri.shift, LEFT * 6
        )
        self.wait()
        self.play(
            UpdateFromAlphaFunc(t_func_a[1], lambda a, alpha: a.set_value(alpha)),
            UpdateFromFunc(t_func_a, lambda a: a.next_to(p_tri, UP)),
            p_tri.shift, RIGHT * 6,
            run_time=3
        )
        self.wait()


class Scene05_1(Scene):
    def construct(self):
        l_s2e = Line(LEFT * 2, RIGHT * 2)
        t_start = CodeLine("start").scale(1.3).move_to(l_s2e.get_start() + DOWN * 0.5)
        t_end = CodeLine("end").scale(1.3).move_to(l_s2e.get_end() + DOWN * 0.5)
        p_tri = Triangle(fill_opacity=1, color=YELLOW).scale(0.15).move_to(l_s2e.get_start() + UP * 0.3).rotate(PI)
        t_alpha = VGroup(
            Tex("\\alpha ="),
            DecimalNumber()
        )
        t_alpha[1].next_to(t_alpha[0])
        t_alpha.next_to(p_tri, UP)
        t_lim = Tex("\\alpha\\in [0,1]").next_to(l_s2e, DOWN)

        l_s2e2 = Line(LEFT * 2, RIGHT * 2).move_to(UP * 3 + RIGHT * 3.2)
        p_tri_l2 = Triangle(fill_opacity=1, color=YELLOW).scale(0.15).move_to(l_s2e2.get_start() + UP / 6).rotate(PI)
        t_func_a = t_func_a = VGroup(
            Tex("f(\\alpha)="),
            DecimalNumber(),
        ).arrange(RIGHT).next_to(p_tri_l2, UP, buff=0.1)
        t_func_lim = Tex("f(\\alpha)\\in [0,1]").set_width(1).next_to(l_s2e2, DOWN)
        numline2 = VGroup(
            l_s2e2, p_tri_l2, t_func_a, t_func_lim
        )
        self.play(Write(t_start), Write(t_end), ShowCreation(l_s2e))
        self.wait()
        self.play(ShowCreation(p_tri), Write(t_alpha))
        self.wait()
        self.play(Write(t_lim))
        self.play(
            UpdateFromAlphaFunc(t_alpha[1], lambda a, alpha: a.set_value(alpha)),
            UpdateFromFunc(t_alpha, lambda a: a.next_to(p_tri, UP)),
            p_tri.shift, RIGHT * 4,
            run_time=2, rate_func=linear,
        )
        self.wait()
        self.play(
            l_s2e.animate.move_to(UP * 3 + LEFT * 4),
            t_start.animate.scale(0.6),
            t_end.animate.scale(0.6),
            UpdateFromFunc(t_start, lambda a: a.move_to(l_s2e.get_start() + DOWN / 3)),
            UpdateFromFunc(t_end, lambda a: a.move_to(l_s2e.get_end() + DOWN / 3)),
            UpdateFromAlphaFunc(p_tri, lambda a, alpha: a.move_to(l_s2e.point_from_proportion(1 - alpha) + UP / 6)),
            UpdateFromFunc(t_lim, lambda a: a.next_to(l_s2e, DOWN)),
            UpdateFromAlphaFunc(t_lim, lambda a, alpha: a.set_width(
                np.clip(t_lim.get_width() * (1 - alpha), 1, t_lim.get_width()))),
            UpdateFromFunc(t_alpha, lambda a: a.next_to(p_tri, UP, buff=0.1)),
            UpdateFromAlphaFunc(t_alpha[1], lambda a, alpha: a.set_value(1 - alpha)),
            Write(numline2),
        )
        self.wait()

        axes1 = Axes(
            x_range=[0, 1.25, 0.25], y_range=[0, 1.25, 0.25],
            width=5, height=5
        ).shift(LEFT * 3.5 + DOWN / 3)
        axes1.add_coordinate_labels(num_decimal_places=2)
        axes1.add(
            Tex("\\alpha").scale(0.5).move_to(axes1.c2p(1.25, 0.1)),
            Tex("\\text{linear}(\\alpha)").scale(0.5).move_to(axes1.c2p(0.18, 1.25)),
        )
        axes2 = Axes(
            x_range=[0, 1.25, 0.25], y_range=[0, 1.25, 0.25],
            width=5, height=5
        ).shift(RIGHT * 3.5 + DOWN / 3)
        axes2.add_coordinate_labels(num_decimal_places=2)
        axes2.add(
            Tex("\\alpha").scale(0.5).move_to(axes2.c2p(1.25, 0.1)),
            Tex("\\text{smooth}(\\alpha)").scale(0.5).move_to(axes2.c2p(0.2, 1.25)),
        )
        self.play(DrawBorderThenFill(axes1), DrawBorderThenFill(axes2))
        self.wait()
        l_func1 = Line(axes1.c2p(0, 0), axes1.c2p(1, 1), color="#FAB763")
        l_func2 = FunctionGraph(smooth, x_range=[0, 1, 0.05], color="#FAB763")
        l_func2.set_width(l_func1.get_width()).move_to(axes2.c2p(0.5, 0.5))
        self.play(ShowCreation(l_func1), ShowCreation(l_func2))
        self.wait()
        dot_linear_g = VGroup(*[
            Dot(axes1.c2p(i / 20, 0), color=YELLOW).scale(0.5)
            for i in range(1, 21)
        ])
        dot_smooth_g = VGroup(*[
            Dot(axes2.c2p(i / 20, 0), color=YELLOW).scale(0.5)
            for i in range(1, 21)
        ])
        self.play(
            Write(dot_linear_g), Write(dot_smooth_g),
            UpdateFromAlphaFunc(p_tri, lambda a, alpha: a.move_to(l_s2e.point_from_proportion(alpha) + UP / 5)),
            UpdateFromAlphaFunc(p_tri_l2,
                                lambda a, alpha: a.move_to(l_s2e2.point_from_proportion(smooth(alpha)) + UP / 5)),
            UpdateFromAlphaFunc(t_alpha[1], lambda a, alpha: a.set_value(alpha)),
            UpdateFromAlphaFunc(t_func_a[1], lambda a, alpha: a.set_value(alpha)),
            UpdateFromFunc(t_alpha, lambda a: a.next_to(p_tri, UP, buff=0.1)),
            UpdateFromFunc(t_func_a, lambda a: a.next_to(p_tri_l2, UP, buff=0.1)),
            run_time=2, rate_func=linear
        )
        self.wait()
        dot_li_g_func = dot_linear_g.copy().set_color(GREEN)
        dot_sm_g_func = dot_smooth_g.copy().set_color(GREEN)
        self.play(
            *[
                dot_li_g_func[i].animate.shift(UP * (i + 1) / 5)
                for i in range(20)
            ],
            *[
                dot_sm_g_func[i].animate.shift(UP * smooth((i + 1) / 20) * 4)
                for i in range(20)
            ]
        )
        self.wait()
        dot_li_g_y = dot_li_g_func.copy().set_color(BLUE)
        dot_sm_g_y = dot_sm_g_func.copy().set_color(BLUE)
        self.play(
            *[
                dot_li_g_y[i].animate.shift(LEFT * (i + 1) / 5)
                for i in range(20)
            ],
            *[
                dot_sm_g_y[i].animate.shift(LEFT * (i + 1) / 5)
                for i in range(20)
            ]
        )
        self.wait()
        g_axes1 = VGroup(axes1, l_func1, dot_linear_g, dot_li_g_func, dot_li_g_y)
        g_axes2 = VGroup(axes2, l_func2, dot_smooth_g, dot_sm_g_func, dot_sm_g_y)

        axes3 = Axes(
            x_range=[0, 1.25, 0.25], y_range=[0, 1.25, 0.25],
            width=5, height=5
        ).shift(LEFT * 3.5 + DOWN / 3)
        # axes3.add_coordinate_labels(num_decimal_places=2)
        axes3.add(
            Tex("\\text{linear}(\\alpha)").scale(0.5).move_to(axes3.c2p(1.25, 0.1)),
            Tex("\\text{interpolate}(\\text{linear}(\\alpha))").scale(0.5).move_to(axes3.c2p(0.36, 1.25)),
        )
        axes4 = Axes(
            x_range=[0, 1.25, 0.25], y_range=[0, 1.25, 0.25],
            width=5, height=5
        ).shift(RIGHT * 3.5 + DOWN / 3)
        # axes4.add_coordinate_labels(num_decimal_places=2)
        axes4.add(
            Tex("\\text{smooth}(\\alpha)").scale(0.5).move_to(axes4.c2p(1.25, 0.1)),
            Tex("\\text{interpolate}(\\text{smooth}(\\alpha))").scale(0.5).move_to(axes4.c2p(0.36, 1.25)),
        )
        g_axes1.save_state()
        g_axes2.save_state()

        def rotate_axes1(obj, alpha):
            obj.restore()
            obj.rotate(-PI / 2 * alpha, about_point=obj[0].c2p(0, 0))
            obj[:-1].set_opacity(np.clip(1 - alpha, 0.2, 1))

        self.play(
            UpdateFromAlphaFunc(g_axes1, rotate_axes1),
            UpdateFromAlphaFunc(g_axes2, rotate_axes1),
            FadeIn(axes3), FadeIn(axes4),
            UpdateFromAlphaFunc(p_tri, lambda a, alpha: a.move_to(l_s2e.point_from_proportion(1 - alpha) + UP / 5)),
            UpdateFromAlphaFunc(p_tri_l2,
                                lambda a, alpha: a.move_to(l_s2e2.point_from_proportion(smooth(1 - alpha)) + UP / 5)),
            UpdateFromAlphaFunc(t_alpha[1], lambda a, alpha: a.set_value(1 - alpha)),
            UpdateFromAlphaFunc(t_func_a[1], lambda a, alpha: a.set_value(1 - alpha)),
            UpdateFromFunc(t_alpha, lambda a: a.next_to(p_tri, UP, buff=0.1)),
            UpdateFromFunc(t_func_a, lambda a: a.next_to(p_tri_l2, UP, buff=0.1)),
            run_time=2,
        )
        self.wait()
        dot_li_g_in_func = dot_li_g_y.copy().set_color(GREEN)
        dot_sm_g_in_func = dot_sm_g_y.copy().set_color(GREEN)
        self.play(
            *[
                dot_li_g_in_func[i].animate.shift(UP * (i + 1) / 5)
                for i in range(20)
            ],
            *[
                dot_sm_g_in_func[i].animate.shift(UP * (dot_sm_g_in_func[i].get_center() - axes4.c2p(0, 0))[0])
                for i in range(20)
            ]
        )
        self.wait()
        dot_li_in_y = dot_li_g_in_func.copy().set_color(YELLOW)
        dot_sm_in_y = dot_sm_g_in_func.copy().set_color(YELLOW)
        self.play(
            *[
                dot_li_in_y[i].animate.shift(LEFT * (i + 1) / 5)
                for i in range(20)
            ],
            *[
                dot_sm_in_y[i].animate.shift(LEFT * (dot_sm_in_y[i].get_center() - axes4.c2p(0, 0))[0])
                for i in range(20)
            ]
        )
        self.wait()
        p_tri1 = Triangle(fill_opacity=1, color=RED).scale(0.15).rotate(-PI / 2)
        p_tri2 = Triangle(fill_opacity=1, color=RED).scale(0.15).rotate(-PI / 2)
        p_tri1.move_to(axes3.c2p(0, 0) + LEFT * 0.3)
        p_tri2.move_to(axes4.c2p(0, 0) + LEFT * 0.3)
        self.play(ShowCreation(p_tri1), ShowCreation(p_tri2))
        self.play(
            UpdateFromAlphaFunc(p_tri1, lambda a, alpha: a.move_to(axes3.c2p(0, alpha) + LEFT * 0.3)),
            UpdateFromAlphaFunc(p_tri2, lambda a, alpha: a.move_to(axes4.c2p(0, smooth(alpha)) + LEFT * 0.3)),
            UpdateFromAlphaFunc(p_tri, lambda a, alpha: a.move_to(l_s2e.point_from_proportion(alpha) + UP / 5)),
            UpdateFromAlphaFunc(p_tri_l2,
                                lambda a, alpha: a.move_to(l_s2e2.point_from_proportion(smooth(alpha)) + UP / 5)),
            UpdateFromAlphaFunc(t_alpha[1], lambda a, alpha: a.set_value(alpha)),
            UpdateFromAlphaFunc(t_func_a[1], lambda a, alpha: a.set_value(alpha)),
            UpdateFromFunc(t_alpha, lambda a: a.next_to(p_tri, UP, buff=0.1)),
            UpdateFromFunc(t_func_a, lambda a: a.next_to(p_tri_l2, UP, buff=0.1)),
            run_time=2.5, rate_func=linear
        )
        self.wait()
        v_func1 = Line(axes3.c2p(0, 1), axes3.c2p(1, 1), color=TEAL)

        def smooth_pie(t):
            return 30 * np.power(t, 4) - 60 * np.power(t, 3) + 30 * np.power(t, 2)

        v_func2 = FunctionGraph(smooth_pie, x_range=[0, 1, 0.02], stroke_color=TEAL)
        v_func2.set_width(v_func1.get_width())
        v_func2.align_to(axes4.c2p(0, 0), DL)
        self.play(ShowCreation(v_func1), ShowCreation(v_func2))
        self.wait()
        self.play(
            v_func1.animate.shift(DOWN * 4 * (2 / 3)),
            v_func2.animate.set_height(v_func2.get_height() / 3, stretch=True, about_edge=DOWN)
        )
        label = Text("在这里将速度曲线进行了一定比例的压缩", font="SourceHanSerifSC-Medium").scale(0.6)
        label.move_to(axes4.c2p(0.7, 1.1))
        self.play(Write(label))
        self.wait()


class Scene06(Scene):
    def construct(self):
        axes = VGroup(
            VGroup(*[NumberPlane(
                x_range=[0, 1, 0.5], y_range=[0, 1, 0.5],
                width=2, height=2,
            ) for i in range(5)
            ]).arrange(RIGHT),
            VGroup(
                *[NumberPlane(
                    x_range=[0, 1, 0.5], y_range=[0, 1, 0.5],
                    width=2, height=2,
                ) for i in range(3)
                ]).arrange(RIGHT),
            VGroup(
                *[NumberPlane(
                    x_range=[0, 1, 0.5], y_range=[0, 1, 0.5],
                    width=2, height=2,
                ) for i in range(3)
                ]).arrange(RIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).shift(UP / 6)
        axes[1].add(
            NumberPlane(
                x_range=[0, 1, 0.5], y_range=[-1, 1.5, 0.5],
                width=2, height=4.5,
            ).next_to(axes[1][2], RIGHT, aligned_edge=UP),
            NumberPlane(
                x_range=[0, 1, 0.5], y_range=[-1, 1.5, 0.5],
                width=2, height=4.5,
            ).next_to(axes[1][2], RIGHT, aligned_edge=UP, buff=2.5),
        )
        self.play(ShowCreation(axes), run_time=2, lag_ratio=0.001)
        graphs = VGroup(
            FunctionGraph(linear, x_range=[0, 1, 0.01], stroke_color="#FAB763").set_width(2).align_to(
                axes[0][0].c2p(0, 0), DL),
            FunctionGraph(smooth, x_range=[0, 1, 0.01], stroke_color="#FAB763").set_width(2).align_to(
                axes[0][1].c2p(0, 0), DL),
            FunctionGraph(rush_into, x_range=[0, 1, 0.01], stroke_color="#FAB763").set_width(2).align_to(
                axes[0][2].c2p(0, 0), DL),
            FunctionGraph(rush_from, x_range=[0, 1, 0.01], stroke_color="#FAB763").set_width(2).align_to(
                axes[0][3].c2p(0, 0), DL),
            Arc(start_angle=PI / 2, angle=PI / 2, stroke_color="#FAB763").set_width(2).align_to(axes[0][4].c2p(0, 0),
                                                                                                DL),
            FunctionGraph(double_smooth, x_range=[0, 1, 0.01], stroke_color="#FAB763").set_width(2).align_to(
                axes[1][0].c2p(0, 0), DL),
            FunctionGraph(there_and_back, x_range=[0, 1, 0.01], stroke_color="#FAB763").set_width(2).align_to(
                axes[1][1].c2p(0, 0), DL),
            FunctionGraph(there_and_back_with_pause, x_range=[0, 1, 0.01], stroke_color="#FAB763").set_width(2).move_to(
                axes[1][2].c2p(0.5, 0.5)),
            FunctionGraph(running_start, x_range=[0, 1, 0.01], stroke_color="#FAB763").set_width(2).align_to(
                axes[1][3].c2p(1, 1), UR),
            FunctionGraph(wiggle, x_range=[0, 1, 0.01], stroke_color="#FAB763").set_width(2).move_to(
                axes[1][4].c2p(0.5, 0)),
            FunctionGraph(lingering, x_range=[0, 1, 0.01], stroke_color="#FAB763").set_width(2).align_to(
                axes[2][0].c2p(0, 0), DL),
            FunctionGraph(exponential_decay, x_range=[0, 1, 0.01], stroke_color="#FAB763").set_width(2).align_to(
                axes[2][1].c2p(0, 0), DL),
            ParametricCurve(lambda t: np.array([(1 + t) * np.cos(t), (1 + t) * np.sin(t), 0]),
                            t_range=[0, 10 * PI, PI / 20], stroke_color="#FAB763").set_width(2).move_to(axes[2][2])
        )
        self.play(ShowCreation(graphs), run_time=2, lag_ratio=0.01)
        self.wait()
        text = VGroup(
            Text("linear").scale(0.7).move_to(axes[0][0].get_bottom() + DOWN / 5),
            Text("smooth").scale(0.7).move_to(axes[0][1].get_bottom() + DOWN / 5),
            Text("rush_into").scale(0.7).move_to(axes[0][2].get_bottom() + DOWN / 5),
            Text("rush_from").scale(0.7).move_to(axes[0][3].get_bottom() + DOWN / 5),
            Text("slow_into").scale(0.7).move_to(axes[0][4].get_bottom() + DOWN / 5),
            Text("double_smooth").scale(0.5).move_to(axes[1][0].get_bottom() + DOWN / 5),
            Text("there_and_back").scale(0.5).move_to(axes[1][1].get_bottom() + DOWN / 5),
            Text("there_and_back_with_pause").scale(0.45).move_to(axes[1][2].get_bottom() + DOWN / 5),
            Text("running_start").scale(0.6).move_to(axes[1][3].get_bottom() + DOWN / 5),
            Text("wiggle").scale(0.7).move_to(axes[1][4].get_bottom() + DOWN / 5),
            Text("lingering").scale(0.7).move_to(axes[2][0].get_bottom() + DOWN / 5),
            Text("exponential_decay").scale(0.6).move_to(axes[2][1].get_bottom() + DOWN / 5),
            Text("蚊香", font="Source Han Serif SC", weight="MEDIUM").scale(0.5).move_to(
                axes[2][2].get_bottom() + DOWN / 5),
        )
        self.play(Write(text))
        self.wait()
        ttl = Text("请选出所有平滑结束的曲线", font="Source Han Serif SC",
                   t2c={"平滑结束": "#FAB763"}, weight=BOLD
                   ).arrange(DOWN, buff=1).to_edge(LEFT)
        btn = VGroup(
            Text("确认", font="Source Han Serif SC", weight=BOLD).add_background_rectangle(color=RED, buff=0.1),
            Text("取消", font="Source Han Serif SC", weight=BOLD).add_background_rectangle(color=GREY, buff=0.1)
        ).arrange(DOWN).to_edge(RIGHT, buff=0.25)
        self.play(Write(ttl), Write(btn))
        self.wait()


class Scene07(Scene):
    def construct(self):
        code = VGroup(
            CodeLine("text.add_updater(lambda m: m.next_to(dot))"),
            CodeLine("self.play(dot.animate.shift(DR*2))"),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)
        code[0][24].set_color("#FAB763")
        m_dot = Dot(color="#FAB763").shift(UL)
        m_obj = Text("This is a dot").next_to(m_dot)
        self.play(Write(m_dot), Write(m_obj))
        self.wait()
        self.play(Write(code[0]))
        self.play(Indicate(m_obj, rate_tunc=there_and_back_with_pause))
        self.wait()
        self.play(Write(code[1]))
        m_ori = VGroup(m_dot.copy(), m_obj.copy()).set_opacity(0.1)
        m_target = VGroup(m_dot.copy(), m_obj.copy()).set_opacity(0.3).shift(DR * 2)
        self.play(FadeIn(m_target), run_time=0.7)
        self.wait()
        m_path = VGroup()
        self.play(
            m_ori.animate.shift(DR * 2),
            UpdateFromFunc(m_path, lambda a: a.add(m_ori.copy())),
            Indicate(code[0][-13:-6], rate_tunc=there_and_back_with_pause),
            ShowPassingFlash(Line(m_dot.get_center(), m_target[0].get_center(), color=RED)),
            run_time=2
        )
        self.wait()
        self.play(
            m_dot.animate.shift(DR * 2),
            UpdateFromFunc(m_obj, lambda a: a.next_to(m_dot)),
            UpdateFromFunc(m_path, lambda a: a.remove(m_path[0])),
            run_time=2
        )
        self.wait()


class Scene08(Scene):
    def construct(self):
        code = VGroup(
            CodeLine("text.add_updater(lambda m: m.next_to(dot))"),
            CodeLine("self.play(dot.animate.shift(DR*2))"),
            CodeLine("text.clear_updaters()"),
            CodeLine("self.play(...)"),
            CodeLine("text.add_updater(anim)"),
            CodeLine("self.play(...)"),
            CodeLine("text.remove_updater(anim)"),
            CodeLine("..."),
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP / 2)
        self.add(code)
        comment = Text("# 太繁琐了吧...", font="Sans", weight="MEDIUM", color=GREY).scale(0.6).next_to(code, DOWN,
                                                                                                  aligned_edge=LEFT)
        self.wait()
        self.play(Write(comment))
        self.wait()


class Scene09(Scene):
    def construct(self):
        code_func = CodeLine(
            """class UpdateFromFunc(Animation):\n
            
                CONFIG = {...}\n
            
                def __init__(self, mobject, update_function, **kwargs):\n
                    self.update_function = update_function\n
                    super().__init__(mobject, **kwargs)\n
            
                def interpolate_mobject(self, alpha):\n
                    self.update_function(self.mobject)
            """,
            t2c={"Animation": "#60B4B4", "UpdateFromFunc": "#fab763"})
        code_func[79:86].set_color("#fab763")
        code_func[88:103].set_color("#fab763")
        code_func[107:113].set_color("#fab763")
        code_func[267:282].set_color("#569CD6")
        code_alp = CodeLine(
            """class UpdateFromAlphaFunc(UpdateFromFunc):\n
            
                def interpolate_mobject(self, alpha):\n
                    self.update_function(self.mobject, alpha)
            """,
            t2c={"UpdateFromFunc": "#60B4B4", "UpdateFromAlphaFunc": "#fab763",
                 "update_function": "#569CD6"})
        code_alp.next_to(code_func, DOWN, aligned_edge=LEFT, buff=0.4)
        code = VGroup(code_func, code_alp).to_corner(UL)
        self.play(FadeIn(code, UP))
        # self.add(code)
        self.wait()
        sur = VGroup(
            SurroundingRectangle(code_func[215:]),
            SurroundingRectangle(code_alp[49:]),
        )
        self.play(
            ShowCreation(sur), lag_ratio=0.1
        )
        text_exp = Text("重写插值函数", font="Sans", color=YELLOW).next_to(sur[1])
        self.play(Write(text_exp))
        self.wait()
        self.play(FadeOut(sur), FadeOut(text_exp))
        self.wait()
        self.play(code.animate.scale(0.7, about_point=[-6.8, 3.5, 0]))
        self.wait()

        s_code0 = CodeLine(
            """def anim(obj):\n
                obj.next_to(dot, RIGHT)""", t2c={"anim": "#60b4b4"}).scale(0.7).to_edge(UP).shift(RIGHT * 3.5)
        s_code1 = CodeLine(
            """self.play(UpdateFromFunc(text, anim))""", t2c={"UpdateFromFunc": "#569CD6"}
        ).scale(0.7).next_to(s_code0, DOWN, aligned_edge=LEFT)
        self.play(
            Write(s_code0),
            Write(s_code1[:25]),
            Write(s_code1[-2:]),
        )
        self.wait()
        self.play(FadeTransform(code_func[79:102].copy(), s_code1[25:-2], path_arc=PI / 2))
        self.play(ShowCreationThenFadeAround(SurroundingRectangle(s_code1[-6:-1])))
        self.wait()
        s_code2 = CodeLine(
            """self.play(\n
                UpdateFromFunc(\n
                    text,\n
                    lambda a: a.next_to(dot)\n
                )\n
            )""", t2c={"UpdateFromFunc": "#569CD6"}
        ).scale(0.7).to_edge(UP).shift(RIGHT * 3.5)
        s_code2[-27].set_color("#FAB763")
        self.play(FadeTransform(VGroup(s_code0, s_code1), s_code2))
        self.play(ShowCreationThenFadeAround(SurroundingRectangle(s_code2[-33:-8])))
        self.wait()
        dot = Dot().to_corner(DL).shift(UP)
        text = Text("This is a dot").scale(0.7).next_to(dot, buff=5)
        self.play(FadeIn(dot), FadeIn(text))
        self.play(text.animate.next_to(dot))
        self.wait()

        self.play(ShowCreationThenFadeAround(SurroundingRectangle(code_alp[-6:-1])))
        self.wait()
        code_itp = CodeLine(
            """def interpolate(start, end, alpha):\n
                return (1 - alpha) * start + alpha * end"""
        ).scale(0.7).next_to(code_alp, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(code_itp, UP))
        self.wait()
        s_code3 = CodeLine(
            """text.save_state()\n
            
            def my_rotate(obj, alpha):\n
                obj.restore()\n
                obj.shift(RIGHT*10*alpha)\n
                obj.rotate(alpha*TAU)\n
            
            self.play(\n
                UpdateFromAlphaFunc(text, my_rotate)\n
            )""",
            t2c={"my_rotate": "#60B4B4", "UpdateFromAlphaFunc": "#569CD6"}
        ).scale(0.7).next_to(s_code2, DOWN, aligned_edge=LEFT, buff=0.4)
        s_code3[34:37].set_color("#FAB763")
        s_code3[-13:-4].set_color(WHITE)
        self.play(FadeIn(s_code3, UP))
        self.wait()
        # ind = TexIndex(s_code3, scale_factor=0.2)
        # self.add(ind)
        group_path = VGroup()
        numline = NumberLine(
            x_range=[0, 1, 1 / 10], width=8,
            include_numbers=True, decimal_number_config={"num_decimal_places": 1, "font_size": 24}
        ).shift(DOWN * 2.5)
        tip_tri = Triangle(fill_opacity=1, color=YELLOW).scale(0.1).rotate(PI).move_to(numline.n2p(0) + UP / 8)
        pnt_tri = Triangle(fill_opacity=1, color=YELLOW).scale(0.1).rotate(-PI / 2).next_to(s_code3[0], LEFT)
        self.play(ShowCreation(numline), ShowCreation(tip_tri), ShowCreation(pnt_tri), FadeOut(dot))
        self.play(text.animate.move_to(numline.n2p(0)))
        text.save_state()
        self.add(group_path)
        group_path.add(text.copy().set_opacity(0.3))

        for i in range(10):
            self.play(Restore(text), pnt_tri.animate.next_to(s_code3[52], LEFT), run_time=0.6)
            self.wait(0.2)
            self.play(tip_tri.animate.shift(RIGHT * 0.8), run_time=0.6)
            self.play(
                text.animate.shift(RIGHT * 0.8 * (i + 1)),
                pnt_tri.animate.next_to(s_code3[71], LEFT),
                run_time=0.6)
            self.wait(0.2)
            self.play(
                text.animate.rotate((i + 1) * TAU / 10),
                pnt_tri.animate.next_to(s_code3[102], LEFT),
                run_time=0.6)
            group_path.add(text.copy().set_opacity(0.15))
            self.wait(0.2)

        self.wait()
        self.play(
            Restore(text),
            FadeOut(tip_tri),
            pnt_tri.animate.next_to(s_code3[142], LEFT),
        )

        def myrotate(obj, alpha):
            obj.restore()
            obj.shift(8 * RIGHT * alpha)
            obj.rotate(alpha * TAU)

        self.play(
            UpdateFromAlphaFunc(text, myrotate),
            run_time=3
        )
        self.wait()


class Scene10(Scene):
    def construct(self):
        code0 = VGroup(
            CodeLine("cir = Circle()", t2c={"Circle": "#569CD6"}),
            CodeLine("squ = Square()", t2c={"Square": "#569CD6"}),
            CodeLine("def anim(obj, alpha):", t2c={"anim": "#60B4B4", "obj": "#FAB763"}),
            CodeLine("obj.set_points(interpolate(", t2c={"set_points": "#569CD6"}),
            CodeLine("cir.get_all_points(),", t2c={"get_all_points": "#569CD6"}),
            CodeLine("squ.copy().align_points(cir).get_all_points(),",
                     t2c={"align_points": "#569CD6", "get_all_points": "#569CD6", "copy": "#569CD6"}),
            CodeLine("alpha)) # 对锚点插值", t2f={"对锚点插值": "Sans"}),
            # CodeLine("obj.set_color(interpolate_color(", t2c={"set_color":"#569CD6","interpolate_color":"#60B4B4"}),
            # CodeLine("cir.get_color(),", t2c={"get_color":"#569CD6"}),
            # CodeLine("squ.get_color(),", t2c={"get_color":"#569CD6"}),
            # CodeLine("alpha)) # 对颜色插值", t2f={"对颜色插值":"Sans"}),
            CodeLine("self.add(cir)", t2c={"add": "#569CD6"}),
            CodeLine("self.play(UpdateFromAlphaFunc(cir, anim))", t2c={"UpdateFromAlphaFunc": "#569CD6"})
        ).scale(0.7).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        code0[:2].shift(UP / 10)
        code0[-2:].shift(DOWN / 10)
        code0[6][7:].set_color("#555555")
        # code0[10][7:].set_color("#555555")
        for i in [3, 4]:
            code0[i].align_to(code0[2][4], LEFT)
        for i in [4, 5, 6]:
            code0[i].align_to(code0[2][8], LEFT)
        code0.to_edge(LEFT)
        self.play(DrawBorderThenFill(code0))
        self.wait()

        cir = Circle(radius=2).shift(RIGHT * 4)
        squ = Square(side_length=4).shift(RIGHT * 4)

        def my_transform(obj, alpha):
            obj.set_points(
                interpolate(cir.get_all_points(),
                            squ.copy().align_points(cir).get_all_points(),
                            alpha)
            )
            # obj.set_color(interpolate_color(cir.get_color(), squ.get_color(), alpha))

        self.play(ShowCreation(cir))
        self.wait()
        self.play(UpdateFromAlphaFunc(cir, my_transform), rate_func=linear, run_time=2)
        self.wait()
        # comment = Text("更新之后颜色补间似乎出了点问题", font="Sans").set_width(3.5).move_to(squ.get_center())
        # self.play(Write(comment))
        # self.wait()


class Scene11(Scene):
    def construct(self):
        t1 = CodeLine("turn updater", t2c={"updater": "#FAB763"}).scale(2).shift(LEFT * 2.8)
        t2 = CodeLine("into animation", t2c={"into": "#ffffff", "animation": "#D86066"}).scale(2)
        t2.next_to(t1[-1], RIGHT, buff=0.5).shift(UP * (t1[-1].get_center()[1] - t2[-1].get_center()[1]))
        pos1 = np.array(t1.get_center())
        pos2 = np.array(t2.get_center())

        anim1 = Write(t1)
        anim2 = Write(t2)
        t1.shift(LEFT * 10)
        t2.shift(RIGHT * 10)

        def anim_to_tg(pos):
            def update(obj, dt):
                obj.shift(2 * dt * (pos - obj.get_center()))

            return update

        t1.add_updater(anim_to_tg(pos1))
        t2.add_updater(anim_to_tg(pos2))
        self.add(t1, t2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        # print(pos1, pos2)
        self.wait(4)
        t1.clear_updaters()
        t2.clear_updaters()
        t3 = CodeLine(
            "turn animation into updater",
            t2c={"updater": "#FAB763", "into": "#ffffff", "animation": "#D86066"}
        ).scale(2)
        self.play(TransformMatchingShapes(VGroup(t1, t2), t3, path_arc=PI / 2))
        self.wait()


# class Scene11(Scene):
#     def construct(self):
#         t1 = TexText("turn ","animation ","into ","updater").scale(2)
#         t1[1].set_color("#D86066")
#         t1[3].set_color("#FAB763")
#         pos1 = np.array(t1[:2].get_center())
#         pos2 = np.array(t1[2:].get_center())
#         anim1 = Write(t1[:2])
#         anim2 = Write(t1[2:])
#         t1[:2].shift(LEFT)
#         t1[2:].shift(LEFT)
#         def anim_to_tg(pos):
#             def update(obj, dt):
#                 obj.shift(2*dt*(pos-obj.get_center()))
#             return update
#         t1[:2].add_updater(anim_to_tg(pos1))
#         t1[2:].add_updater(anim_to_tg(pos2))
#         self.add(t1)
#         turn_animation_into_updater(anim1)
#         turn_animation_into_updater(anim2)
#         self.wait(3)


class Scene12(Scene):
    def construct(self):
        code = VGroup(
            CodeLine("def anim(obj, alpha):", t2c={"anim": "#60B4B4", "obj": "#FAB763"}),
            CodeLine("obj.move_to(line.point_from_proportion(alpha))"),
            CodeLine("num.set_value(alpha)"),
            CodeLine("self.play(UpdateFromAlphaFunc(dot, anim))", t2c={"UpdateFromAlphaFunc": "#569CD6"})
        ).arrange(DOWN, aligned_edge=LEFT)
        code[1:3].align_to(code[0][4], LEFT)
        self.play(Write(code))
        line = Line([-3, -1, 0], [3, -1, 0], color=GREY)
        dot = Dot([-3, -1, 0], color="#fab763")
        tex = VGroup(Tex("\\alpha="), DecimalNumber(0.0)).arrange(RIGHT)
        self.play(
            code.animate.to_edge(UP, buff=1),
            ShowCreation(line),
            ShowCreation(dot),
            Write(tex)
        )
        self.wait()

        def anim(obj, alpha):
            obj.move_to(line.point_from_proportion(alpha))
            tex[1].set_value(alpha)

        self.play(
            UpdateFromAlphaFunc(dot, anim),
            run_time=2
            # UpdateFromAlphaFunc(tex[1], lambda a, alpha:a.set_value(alpha))
        )
        self.wait()
        self.play(dot.animate.shift(LEFT * 6), tex[1].animate.set_value(0))
        self.wait()
        self.play(
            UpdateFromAlphaFunc(dot, anim),
            UpdateFromAlphaFunc(tex[1], lambda a, alpha: a.set_value(alpha)),
            run_time=2
        )
        self.wait()


class SceneAdd1(Scene):
    def construct(self):
        t1 = Text("复合函数", font="Source Han Serif SC", weight="SEMIBOLD").scale(2.5)
        self.play(Write(t1))
        self.wait()
        tex1 = Tex(r"\alpha\rightarrow f(\alpha)").shift(DOWN / 2)
        tex2 = Tex(
            r"\left\{ \alpha | \alpha \in [0,1] \right\} \rightarrow \left\{ f(\alpha)|f(\alpha)\in[0,1] \right\} ").shift(
            DOWN * 1.7)
        self.play(
            t1.animate.shift(UP),
            FadeIn(tex1, UP)
        )
        self.wait()
        self.play(FadeIn(tex2, UP))
        self.wait()
        self.play(FadeOut(t1, DOWN), FadeOut(tex1, DOWN), FadeOut(tex2, DOWN))


class SceneAdd2(Scene):
    def construct(self):
        methods = VGroup(
            Text("ShowCreation"),
            Text("DrawBorderThenFill"),
            Text("Write"),
            Text("Rotate"),
            Text("FadeIn")
        ).scale(1.6).arrange(DOWN, aligned_edge=RIGHT, buff=0.5)
        methods[3].rotate(PI)
        methods[3].save_state()

        def anim(obj, alpha):
            obj.restore()
            obj.set_opacity(alpha)
            obj.rotate(-PI * alpha)

        self.play(
            LaggedStart(ShowCreation(methods[0]),
                        DrawBorderThenFill(methods[1]),
                        Write(methods[2]),
                        UpdateFromAlphaFunc(methods[3], anim),
                        FadeIn(methods[4]), lag_ratio=0.4)
        )
        self.wait()
        squ = Square(side_length=methods[0].get_height(), color=BLUE, fill_opacity=0.5).next_to(methods[0], buff=6)
        cir = Circle(fill_opacity=0.5, radius=methods[1].get_height() / 2, color=RED).next_to(methods[1], buff=6)
        code = CodeLine("code", color=YELLOW).set_height(methods[2].get_height()).next_to(methods[2], buff=6)
        tri = Triangle(fill_opacity=0.5, color=TEAL).set_height(methods[3].get_height()).next_to(methods[3], buff=6)
        dec = DecimalNumber(color=PURPLE).next_to(methods[4], buff=6)

        def anim_shift(obj, dt):
            obj.shift(LEFT * (obj.get_left()[0] - 1.5) * dt * 2)

        squ.add_updater(anim_shift)
        cir.add_updater(anim_shift)
        code.add_updater(anim_shift)
        tri.add_updater(anim_shift)
        dec.add_updater(anim_shift)
        dec.add_updater(lambda a, dt: a.increment_value(dt))
        dec.add_updater(lambda a: a.set_opacity(abs(np.sin(PI * self.time))))
        self.add(squ, cir, code, tri, dec)
        turn_animation_into_updater(ShowCreation(squ, run_time=2))
        turn_animation_into_updater(DrawBorderThenFill(cir, run_time=2))
        turn_animation_into_updater(Write(code, run_time=2))
        turn_animation_into_updater(Rotate(tri, 2 * TAU, run_time=2))
        self.play(methods.animate.shift(LEFT * 2.5))
        self.wait(5)
