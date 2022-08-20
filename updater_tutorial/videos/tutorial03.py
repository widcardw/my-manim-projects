from manimlib import *
from manim_sandbox.utils.scenes.mariana_color import *


class AllPointsIndex(VGroup):
    CONFIG = {
        "scale_factor": 0.5,
        "color": PURPLE,
    }

    def __init__(self, obj, **kwargs):
        VGroup.__init__(self, **kwargs)
        for index, single_tex in enumerate(obj.get_all_points()):
            tex_index = Integer(index, background_stroke_width=2) \
                .scale(self.scale_factor).set_color(self.color)
            tex_index.move_to(single_tex)
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
            'dt': "#FAB763",
            ":": "#FA9044",
            "+": "#FA9044",
            "*": "#FA9044",
            "-": "#FA9044",
            ">": "#FA9044",
            "<": "#FA9044",
            "/": "#FA9044",
            "%": "#FA9044",
            "=": "#FA9044",
            ",": GREY,
            # "digit": "#569CD6",
            # "x": "#9CDCFE",
            # "ss": "#9CDCFE",
            # "String": "#4EC9B0",
            "class": "#C594C5",
            "if": "#C594C5",
            "else": "#C594C5",
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
            "deg": "#FAB763",
            "ORIGIN": "#FAB763",
            "True": "#FAB763",
            "False": "#FAB763",
            "kwargs": "#FAB763",
            "(": GREY_B,
            ")": GREY_B,
            "generate_target": "#569CD6",
            "__init__": "#569CD6",
            "super": "#569CD6",
            "save_state": "#569CD6",
            "restore": "#569CD6",
            "rotate": "#569CD6",
            "Scene": "#60B4B4",
            "wait": "#569CD6",
            "interpolate_mobject": "#60B4B4",
            "move_to": "#569CD6",
            "set_value": "#569CD6",
            "set_stroke": "#569CD6",
            "get_center": "#569CD6",
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


class TestColor(Scene):
    def construct(self):
        cir = Square(fill_opacity=1, stroke_width=0).scale(4)

        def color_func(point: np.ndarray):
            return [
                np.clip(abs(point[0] - point[1]), 0, 1),
                np.clip(abs(point[0] + point[1]), 0, 1),
                np.clip(abs(point[0] + point[1]), 0, 1), 1]

        cir.set_color_by_rgba_func(color_func)
        self.add(cir)


class TestDash(Scene):
    def construct(self):
        squ1 = DashedVMobject(Square(3, color=GREY)).shift(LEFT * 3).shift(UP * 2)
        squ2 = squ1.copy().shift(RIGHT * 6)
        pnt = AllPointsIndex(squ1, scale_factor=0.3)
        cir1 = DashedVMobject(Circle(radius=1.5)).shift(LEFT * 3 + DOWN * 2)
        cir2 = cir1.copy().shift(RIGHT * 6)
        pnt2 = AllPointsIndex(cir2, scale_factor=0.3)
        self.add(squ1, pnt, squ2)
        self.add(cir1, pnt2, cir2)


class ChasingCurve(Scene):
    def construct(self):
        dot_a = Dot([3.5, 3.5, 0]).scale(0.3)
        dot_b = Dot([-3.5, 3.5, 0]).scale(0.3)
        dot_c = Dot([-3.5, -3.5, 0]).scale(0.3)
        dot_d = Dot([3.5, -3.5, 0]).scale(0.3)
        l_ab = Line([3.5, 3.5, 0], [-3.5, 3.5, 0], color=BLUE)
        l_bc = Line([-3.5, 3.5, 0], [-3.5, -3.5, 0], color=BLUE)
        l_cd = Line([-3.5, -3.5, 0], [3.5, -3.5, 0], color=BLUE)
        l_da = Line([3.5, -3.5, 0], [3.5, 3.5, 0], color=BLUE)
        trace = VGroup()

        def dot_anim(target: Dot):
            def update(obj: Dot, dt):
                obj.shift((target.get_center() - obj.get_center()) * dt * self.time)

            return update

        def line_anim(p1: Dot, p2: Dot):
            def update(obj: Line):
                obj.put_start_and_end_on(p1.get_center(), p2.get_center())

            return update

        dot_a.add_updater(dot_anim(dot_b))
        dot_b.add_updater(dot_anim(dot_c))
        dot_c.add_updater(dot_anim(dot_d))
        dot_d.add_updater(dot_anim(dot_a))
        l_ab.add_updater(line_anim(dot_a, dot_b))
        l_bc.add_updater(line_anim(dot_b, dot_c))
        l_cd.add_updater(line_anim(dot_c, dot_d))
        l_da.add_updater(line_anim(dot_d, dot_a))

        trace.add_updater(lambda a, dt: a.add(
            l_ab.copy().clear_updaters().set_stroke(width=0.6),
            l_bc.copy().clear_updaters().set_stroke(width=0.6),
            l_cd.copy().clear_updaters().set_stroke(width=0.6),
            l_da.copy().clear_updaters().set_stroke(width=0.6),
        ))

        self.add(dot_a, dot_b, dot_c, dot_d, l_ab, l_bc, l_cd, l_da, trace)
        self.wait(5)


class Scene01(Scene):
    def construct(self):
        t1 = TexText("Updater教程").scale(2).shift(UP / 2).to_edge(LEFT)
        t2 = TexText("重制版").scale(1.3).shift(DOWN / 2).to_edge(RIGHT)
        t3 = TexText("Episode 3").scale(2).shift(UP / 2).shift(LEFT * 5)
        t4 = TexText("Time based updater").scale(1.3).shift(DOWN / 2).shift(7 * RIGHT)
        t4[0][0:4].set_color(ORANGE)
        t4[0][-7:].set_color(YELLOW)

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
        t3.clear_updaters()
        t4.clear_updaters()

        def shifting_to_pos(pos: np.ndarray):
            def update(obj, dt):
                obj.shift(dt * 2 * (pos - obj.get_center()))

            return update

        t5 = TexText(r"d$t$").to_edge(LEFT).scale(2.5)
        t6 = TexText("微分").to_edge(RIGHT).scale(2)
        t5.add_updater(shifting_to_pos(LEFT))
        t6.add_updater(shifting_to_pos(RIGHT))
        self.add(t5, t6)
        turn_animation_into_updater(Write(t5))
        turn_animation_into_updater(Write(t6))
        self.play(
            t3.shift, UP * 6, t3.scale, 0.5,
            t4.shift, DOWN * 6, t4.scale, 0.5,
        )
        self.wait(2)
        t5.clear_updaters()
        t6.clear_updaters()
        path = ParametricCurve(
            lambda t: np.array([t, np.sin(PI * t) / 2 - 1.5, 0]),
            t_range=[-8, 8, 0.1],
            stroke_color=YELLOW_A
        )
        self.play(
            t5.animate.shift(UP * 1.5),
            t6.animate.shift(UP * 1.5),
            ShowCreation(path)
        )
        self.wait()


class Scene02(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 11, 1],
            y_range=[-6, 6, 1],
            width=11, height=12
        ).shift(DOWN * 3)
        graph_description = VGroup(
            Line(color="#FAB763").scale(0.5), Tex("s"),
            Line(color="#60b4b4").scale(0.5), Tex("v"),
            Line(color="#569CD6").scale(0.5), Tex("a"),
        ).arrange_in_grid(3, 2, h_buff=0.2, v_buff=0.1).to_corner(UR)
        self.play(Write(axes), lag_ratio=0, run_time=1)
        self.wait()
        wheel = VGroup(
            Circle(radius=1),
            Line(LEFT, RIGHT, color=RED_B),
            Line(LEFT, RIGHT, color=RED_B).rotate(TAU / 3),
            Line(LEFT, RIGHT, color=RED_B).rotate(PI / 3),
        ).scale(0.8).move_to(axes.c2p(0, 0.8))
        self.play(ShowCreation(wheel))
        self.wait()
        wheel.save_state()

        def wheel_rolling(obj, alpha):
            obj.restore()
            obj.shift(RIGHT * 10 * alpha)
            obj.rotate(-10 / 0.8 * alpha)

        self.play(Write(graph_description))
        func_smooth = FunctionGraph(
            smooth,
            x_range=[0, 1, 0.01],
            stroke_color="#FAB763"
        ).set_width(10, stretch=True).set_height(5, stretch=True) \
            .move_to(axes.c2p(5, 2.5))
        l = Line()
        self.play(
            ShowCreation(func_smooth),
            UpdateFromAlphaFunc(wheel, wheel_rolling),
            UpdateFromAlphaFunc(l, lambda a, alpha: a.become(axes.get_v_line(func_smooth.get_end()))),
            run_time=4
        )
        self.play(FadeOut(wheel), FadeOut(l))

        def smooth_pie(t):
            return 30 * np.power(t, 4) - 60 * np.power(t, 3) + 30 * np.power(t, 2)

        def smooth_liangpie(t):
            return 120 * np.power(t, 3) - 180 * np.power(t, 2) + 60 * t

        func_dao = FunctionGraph(
            smooth_pie,
            x_range=[0, 1, 0.01],
            stroke_color="#60B4B4"
        ).set_width(10, stretch=True).set_height(5, stretch=True) \
            .align_to(axes.c2p(0, 0), DL)
        self.play(ShowCreation(func_dao))
        self.wait()
        func_dao2 = FunctionGraph(
            smooth_liangpie,
            x_range=[0, 1, 0.01],
            stroke_color="#569CD6"
        ).set_width(10, stretch=True).set_height(5, stretch=True) \
            .move_to(axes.c2p(5, 2.5))
        self.play(
            axes.animate.set_height(6, True, about_point=axes.c2p(0, 5)),
            func_smooth.animate.set_height(2.5, stretch=True, about_edge=UP),
            func_dao.animate.set_height(2.5, stretch=True, about_edge=UP),
            ShowCreation(func_dao2),
        )
        axes.become(Axes(
            x_range=[0, 11, 1],
            y_range=[-6, 6, 1],
            width=11, height=6
        )).shift(DOWN / 2)
        self.wait()


class Scene03(Scene):
    def construct(self):
        axes = Axes(
            [-1, 9, 1], [-2, 4, 1], height=7
        )
        self.add(axes)
        graph = axes.get_graph(lambda x: x + 1 / x - 3, x_range=[0.15, 7, 0.01], stroke_color="#fab764")
        self.play(ShowCreation(graph))
        lin_dian = VGroup(
            Dot(axes.c2p((3 + 5 ** 0.5) / 2, 0), color="#D86066"),
            Dot(axes.c2p((3 - 5 ** 0.5) / 2, 0), color="#D86066")
        )
        self.play(Write(lin_dian))
        jizhidian = Dot(axes.c2p(1, -1), color="#569CD6")
        self.play(Write(jizhidian))
        arrow1 = TipableVMobject()
        arrow1.set_points([
            axes.c2p(0.3, 2.5), axes.c2p(0.3, 1.5), axes.c2p(0.6, 0.5)
        ])
        arrow1.add_tip()
        arrow2 = TipableVMobject()
        arrow2.set_points([
            axes.c2p(2, 0.3), axes.c2p(3, 1), axes.c2p(4, 2.2)
        ])
        arrow2.shift(RIGHT * 0.5).add_tip()
        self.play(Write(arrow1), Write(arrow2))
        func_linear = axes.get_graph(lambda x: x, x_range=[-0.5, 6, 1], stroke_color="#4EC9B0")
        self.play(ShowCreation(func_linear))
        self.wait()
        emoji = Text("(╯‵□′)╯︵┻━┻", font="Source Han Serif SC").shift([3, -2, 0])
        emoji.flip()
        self.play(Write(emoji))
        self.wait(2)
        self.play(*[
            FadeOut(obj) for obj in [arrow1, arrow2, lin_dian, jizhidian, func_linear, emoji]
        ])
        line_v1 = axes.get_v_line(graph.point_from_proportion(0.5))
        line_v2 = axes.get_v_line(graph.point_from_proportion(0.55))
        line_h1 = axes.get_h_line(graph.point_from_proportion(0.5) + RIGHT * 0.4)
        tex_delta_t = Tex(r"\Delta t").move_to(axes.c2p(3.75, -0.3))
        self.play(ShowCreation(line_v1), ShowCreation(line_v2), ShowCreation(line_h1), Write(tex_delta_t))
        self.wait()
        self.play(*[
            obj.animate.scale(10, about_point=graph.point_from_proportion(0.5))
            for obj in [axes, graph, line_v1, line_v2, line_h1]
        ],
                  tex_delta_t.animate.move_to(graph.point_from_proportion(0.5) + DR / 2),
                  run_time=2)
        self.wait()
        self.play(
            line_v2.animate.become(axes.get_v_line(graph.point_from_proportion(0.504))),
            line_v1.animate.become(axes.get_v_line(graph.point_from_proportion(0.5))),
            line_h1.animate.become(axes.get_h_line(graph.point_from_proportion(0.5) + RIGHT / 4)),
            tex_delta_t.animate.shift(LEFT / 3)
        )


class Scene04(Scene):
    def construct(self):
        numline = NumberLine(
            [0, 1, 1 / 60],
            width=10,
            numbers_with_elongated_ticks=[i / 10 for i in range(0, 11)]
        )
        tex_1s = Tex("1s").move_to(numline.n2p(1) + DOWN / 2)
        self.play(Write(tex_1s), Write(numline))
        tip = ArrowTip().move_to(numline.n2p(0) + UP / 3).scale(0.5).rotate(-PI / 2)
        # tick = Line(UP/10, DOWN/10, color=YELLOW).move_to(numline.n2p(0))
        ticks = numline.copy()
        self.play(Write(tip))
        self.wait()
        tip.move_to(numline.n2p(1 / 60) + UP / 3)
        self.play(
            ApplyMethod(tip.shift, RIGHT * (10 - 1 / 6), rate_func=linear),
            Succession(*[
                Indicate(ticks.ticks[i], scale_factor=2, rate_func=there_and_back)
                for i in range(1, len(ticks.get_tick_marks()))
            ]),
            rate_func=linear, run_time=5
        )


class Scene05(Scene):
    def construct(self):
        tex_dt = TexText("d$t$", color=YELLOW_M)
        tex_equ = TexText("=").shift(LEFT)
        tex_dis = Tex(r"\frac{1}{\text{Frames per second}}").next_to(tex_equ)
        tex_value = VGroup(
            Tex(r"\frac{1}{\qquad\qquad\qquad\qquad\quad}"),
            CodeLine("self.camera.frame_rate").scale(1.1)
        ).arrange(DOWN).next_to(tex_equ)
        self.play(Write(tex_dt))
        self.play(
            tex_dt.animate.shift(LEFT * 1.6),
            FadeIn(tex_equ, LEFT * 3.5),
            FadeIn(tex_dis, LEFT * 6.5)
        )
        self.wait()
        self.play(
            FadeOut(tex_dis, DOWN),
            FadeIn(tex_value, DOWN)
        )
        self.wait()


class Scene06(Scene):
    def construct(self):
        fps_s = VGroup(
            CodeLine("15fps"),
            CodeLine("30fps"),
            CodeLine("60fps"),
        ).scale(2.5).arrange(DOWN, buff=1).to_edge(LEFT)
        self.add(fps_s)
        self.t = 0

        def target_fps(fps: int):
            real_dt = 60 // fps

            def update(obj, dt):
                if self.t % real_dt == 0:
                    obj.shift(RIGHT * 2 / fps)
                self.t += 1

            return update

        squ_s1 = Square(side_length=1.5, fill_opacity=1)
        squ_s2 = Square(side_length=1.5, fill_opacity=1)
        squ_s3 = Square(side_length=1.5, fill_opacity=1)

        squ_s1.set_color_by_xyz_func("x/y")
        squ_s1.next_to(fps_s[0], RIGHT)
        squ_s2.set_color_by_xyz_func("x/y")
        squ_s2.next_to(fps_s[1], RIGHT)
        squ_s3.set_color_by_xyz_func("x/y")
        squ_s3.next_to(fps_s[2], RIGHT)
        self.play(
            ShowCreation(squ_s1),
            ShowCreation(squ_s2),
            ShowCreation(squ_s3),
        )
        squ_s1.add_updater(target_fps(15))
        squ_s2.add_updater(target_fps(30))
        squ_s3.add_updater(target_fps(60))
        self.wait(4)
        squ_s1.clear_updaters()
        squ_s2.clear_updaters()
        squ_s3.clear_updaters()


class Scene07(Scene):
    def construct(self):
        def shrink_func(x: np.ndarray):
            return np.array([
                x[0] + (np.exp(x[0] / 2 + np.sin(x[0] + np.exp(x[0])) / 3) / 2 - np.exp(
                    -x[0] / 2 + np.cos(x[0] + np.exp(-x[0] / 3)) / 3) / 2 + np.sin(x[1]) / 3),
                x[1] + (np.sin(np.exp(x[1] + np.sin(x[0] + np.exp(x[0])))) - np.cos(
                    x[0] * np.exp(-x[1] + (np.cos(-x[1]))))) / 5,
                0
            ])

        def center_expand(x: np.ndarray):
            return np.array([
                (np.exp(x[0]) - np.exp(-x[0])) / 6,
                np.exp(x[1]) - np.exp(-x[1]) / 1.5,
                0
            ])

        def fuhe(x: np.ndarray):
            return shrink_func(center_expand(x))

        def fuhe_mul(x: np.ndarray):
            y = np.array([[0, 0, 0]])
            for i in range(len(x)):
                y = np.concatenate((y, np.array([fuhe(x[i])])))
            return y[1:]

        code1 = CodeLine("Scene.play(...)").scale(2).shift(UP / 2)
        code2 = CodeLine("Scene.    (...)").scale(2).shift(DOWN / 2)
        code3 = CodeLine("wait").scale(2).shift(DOWN / 2 + RIGHT / 5)
        cir1 = Circle(stroke_color=WHITE, stroke_width=0, stroke_opacity=0.15, radius=0.1).move_to(code3.get_center())
        cir2 = Circle(stroke_color=WHITE, stroke_width=0, stroke_opacity=0.15, radius=0.1).move_to(
            code3.get_center()).scale(0.1)

        begin_points1 = np.array(code1.get_all_points())
        end_points1 = np.array(fuhe_mul(begin_points1))
        begin_points2 = np.array(code2.get_all_points())
        end_points2 = np.array(fuhe_mul(begin_points2))

        def the_world(begin_points, end_points):
            def update_color(obj: Mobject, alpha):
                obj.set_points(
                    interpolate(
                        begin_points,
                        end_points,
                        alpha
                    )
                )
                # obj.apply_function(shrink_func)
                obj.set_color(Color(hsl=(alpha, 2 * alpha * (1 - alpha), 0.4)))

            return update_color

        bg_rect = Rectangle(15, 9, fill_opacity=0, fill_color="#252525", stroke_width=1)
        cir0 = Circle(fill_opacity=0, fill_color="#fff", stroke_width=0).scale(0.01).move_to(code3.get_center())
        self.add(bg_rect, cir0)
        self.play(Write(code1))
        self.wait()
        self.play(Write(code2), Write(code3))
        self.add(cir1, cir2)
        cir1.set_stroke(width=20)
        cir2.set_stroke(width=40)
        cir0.set_fill(opacity=0.8)
        self.play(
            ApplyMethod(cir0.scale, 1500),
            UpdateFromAlphaFunc(code1, the_world(begin_points1, end_points1)),
            UpdateFromAlphaFunc(code2, the_world(begin_points2, end_points2)),
            AnimationGroup(
                ApplyMethod(cir1.scale, 300),
                ApplyMethod(cir2.scale, 5000),
                lag_ratio=0.1
            ),
            run_time=1
        )
        bg_rect.set_opacity(1)
        self.play(
            ApplyMethod(cir0.scale, 1 / 1500),
            UpdateFromAlphaFunc(code1, the_world(begin_points1, end_points1), rate_func=lambda t: smooth(1 - t)),
            UpdateFromAlphaFunc(code2, the_world(begin_points2, end_points2), rate_func=lambda t: smooth(1 - t)),
            AnimationGroup(
                ApplyMethod(cir1.scale, 1 / 300),
                ApplyMethod(cir2.scale, 1 / 5000),
                lag_ratio=0.1
            ),
            run_time=1,
        )
        self.remove(cir1, cir2, cir0)
        self.wait()
        text = Text(
            "反正这个ザ・ワールド就做的非常拉",
            font="Source Han Serif SC", weight="MEDIUM"
        ).scale(0.6).to_edge(DOWN).set_color("#555")
        self.play(Write(text))
        self.wait()


class Scene08(Scene):
    def construct(self):
        t1 = Text("Time based updater").scale(2).shift(UP / 2).to_edge(LEFT)
        t2 = Text("基于时间的更新"[::-1], font="Source Han Serif SC").arrange(LEFT, buff=0.05).scale(2).shift(
            DOWN / 2).to_edge(RIGHT)

        def anim_to_center(obj, dt):
            obj.shift(-2 * dt * obj.get_center()[0] * RIGHT)

        def shifting_out(obj, dt):
            obj.set_opacity(np.clip(3 - self.time / 2, 0, 1))
            obj.shift(dt * obj.get_center()[0] * RIGHT * 3)

        t1.add_updater(anim_to_center)
        t2.add_updater(anim_to_center)
        self.add(t1, t2)
        self.play(Write(t1), Write(t2), run_time=1)
        self.wait(3)
        t1.clear_updaters()
        t2.clear_updaters()
        t1.shift(RIGHT / 100)
        t2.shift(LEFT / 100)
        clock = Clock().scale(3)
        t1.add_updater(shifting_out)
        t2.add_updater(shifting_out)
        self.play(
            FadeIn(clock)
        )
        clock.add_updater(lambda a, dt: a.set_stroke(opacity=np.clip(3.5 - self.time / 2, 0.1, 1)))
        anim = ClockPassesTime(clock, run_time=10)
        turn_animation_into_updater(anim, True)
        code1 = CodeLine("""def anim(obj, dt):\n
    obj.rotate(dt, about_point=ORIGIN)\n
square.add_updater(anim)""", t2c={"about_point": RED_M}).to_corner(UL)
        code1[4:8].set_color(GREEN_M)
        code1[9:12].set_color(YELLOW_M)
        code2 = CodeLine(
            """square.add_updater(lambda a, dt: a.rotate(-3 * dt))"""
        ).next_to(code1, DOWN, aligned_edge=LEFT)
        code2[26].set_color(YELLOW_M)
        code2[29:31].set_color(YELLOW_M)
        code3 = CodeLine("self.play(...)").next_to(code2, DOWN, aligned_edge=LEFT)
        code4 = CodeLine("self.wait(...)").next_to(code3, DOWN, aligned_edge=LEFT)
        squ = Square(side_length=1, color=RED_M).shift(RIGHT * 3)
        self.play(ShowCreation(squ))
        squ.add_updater(lambda a, dt: a.rotate(dt, about_point=ORIGIN))
        self.play(Write(code1))
        squ.add_updater(lambda a, dt: a.rotate(-3 * dt))
        self.play(Write(code2))
        self.wait()
        self.play(Write(code3))
        self.wait()
        self.play(Write(code4))
        self.wait(5)


class Scene09(Scene):
    def construct(self):
        code1 = CodeLine("""def interpolate(start, end, alpha):\n
    return (1 - alpha) * start + alpha * end""")
        self.play(FadeIn(code1, UP))
        self.wait()
        code2 = CodeLine("""obj.add_updater(lambda m, dt: ...)\n
self.add(obj)\n
self.wait(...)\n""", t2c={"add": BLUE_M})
        code2[23].set_color(YELLOW_M)
        self.play(FadeOut(code1, DOWN), FadeIn(code2, DOWN))
        self.wait()


class Scene10(Scene):
    def construct(self):
        dot_group = VGroup(
            *[Dot(4 * np.array([np.cos(PI / 4 + PI / 2 * i), np.sin(PI / 4 + PI / 2 * i), 0]))
              for i in range(4)]
        )
        label_group = VGroup(
            Tex("A").next_to(dot_group[0], UR),
            Tex("B").next_to(dot_group[1], UL),
            Tex("C").next_to(dot_group[2], DL),
            Tex("D").next_to(dot_group[3], DR),
        ).set_color(YELLOW_M)
        self.play(Write(dot_group), Write(label_group), lag_ratio=0)
        arrow_group = VGroup(
            *[Line(
                4 * np.array([np.cos(PI / 4 + PI / 2 * i), np.sin(PI / 4 + PI / 2 * i), 0]),
                4 * np.array([np.cos(PI / 4 + PI / 2 * (i + 1)), np.sin(PI / 4 + PI / 2 * (i + 1)), 0]),
                buff=0.8
            ).add_tip(width=0.25, length=0.25).set_color(GREY_B)
              for i in range(4)]
        )
        self.play(ShowCreation(arrow_group), lag_ratio=0)
        self.wait()
        line_group = VGroup(
            *[Line(
                4 * np.array([np.cos(PI / 4 + PI / 2 * i), np.sin(PI / 4 + PI / 2 * i), 0]),
                4 * np.array([np.cos(PI / 4 + PI / 2 * (i + 1)), np.sin(PI / 4 + PI / 2 * (i + 1)), 0]),
                color=BLUE
            ) for i in range(4)]
        )
        self.play(ShowCreation(line_group, lag_ratio=0), FadeOut(arrow_group))
        self.wait()
        code1 = CodeLine("""def update_a(obj, dt):\n
    obj.shift((dot_b.get_center() - obj.get_center()) * dt)\n""",
                         t2c={"update_a": GREEN_M, "get_center": BLUE_M}
                         ).to_corner(UL)
        code1[13:16].set_color(YELLOW_M)
        code2 = CodeLine("""def update_b(obj, dt):\n
    obj.shift((dot_c.get_center() - obj.get_center()) * dt)\n""",
                         t2c={"update_b": GREEN_M, "get_center": BLUE_M}
                         ).next_to(code1, DOWN)
        code2[13:16].set_color(YELLOW_M)
        code3 = CodeLine("""def update_c(obj, dt):\n
    obj.shift((dot_d.get_center() - obj.get_center()) * dt)\n""",
                         t2c={"update_c": GREEN_M, "get_center": BLUE_M}
                         ).next_to(code2, DOWN)
        code3[13:16].set_color(YELLOW_M)
        code4 = CodeLine("""def update_d(obj, dt):\n
    obj.shift((dot_a.get_center() - obj.get_center()) * dt)\n""",
                         t2c={"update_d": GREEN_M, "get_center": BLUE_M}
                         ).next_to(code3, DOWN)
        code4[13:16].set_color(YELLOW_M)
        self.play(
            line_group.animate.scale(0.45, about_point=[9, -4, 0]),
            dot_group.animate.scale(0.45, about_point=[9, -4, 0]),
            label_group.animate.scale(0.45, about_point=[9, -4, 0]),
            FadeIn(code1, RIGHT),
            FadeIn(code2, RIGHT),
            FadeIn(code3, RIGHT),
            FadeIn(code4, RIGHT),
        )
        code5 = CodeLine("""dot_a.add_updater(update_a)\n
dot_b.add_updater(update_a)\n
dot_c.add_updater(update_c)\n
dot_d.add_updater(update_d)\n
self.add(dot_a, dot_b, dot_c, dot_d)\n
self.wait(5)\n""", t2c={"add": BLUE_M}
                         ).next_to(code4, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(code5))
        self.wait()
        code6 = CodeLine("""def update_dot(target):\n
    def anim(obj, dt):\n
        obj.shift(\n
            (target.get_center() - obj.get_center()) * dt\n
        )\n
    return anim\n""",
                         t2c={"update_dot": GREEN_M, "get_center": BLUE_M}
                         ).next_to(code1, DOWN, aligned_edge=LEFT)
        code6[15:21].set_color(YELLOW_M)
        code6[38:41].set_color(YELLOW_M)
        code6[33:37].set_color(GREEN_M)
        self.play(
            FadeOut(code2),
            FadeOut(code3),
            FadeOut(code4),
        )
        self.play(FadeIn(code6))
        self.wait(2)
        self.play(FadeOut(code1), code6.animate.to_corner(UL))
        code7 = CodeLine("""dot_a.add_updater(update_dot(dot_b))\n
dot_b.add_updater(update_dot(dot_c))\n
dot_c.add_updater(update_dot(dot_d))\n
dot_d.add_updater(update_dot(dot_a))\n
self.add(dot_a, dot_b, dot_c, dot_d)\n
self.wait(5)\n""", t2c={"add": BLUE_M, "update_dot": BLUE_M}
                         ).next_to(code6, DOWN, aligned_edge=LEFT)
        self.play(
            TransformMatchingShapes(code5, code7),
            line_group.animate.scale(1.5, about_point=[7, -4, 0]),
            dot_group.animate.scale(1.5, about_point=[7, -4, 0]),
            FadeOut(label_group),
        )
        self.wait()
        dot_group.save_state()

        def update_dot(target):
            def anim(obj, dt):
                obj.shift(
                    (target.get_center() - obj.get_center()) * dt
                )

            return anim

        dot_group[0].add_updater(update_dot(dot_group[1]))
        dot_group[1].add_updater(update_dot(dot_group[2]))
        dot_group[2].add_updater(update_dot(dot_group[3]))
        dot_group[3].add_updater(update_dot(dot_group[0]))
        self.add(dot_group[0], dot_group[1], dot_group[2], dot_group[3])
        self.wait(4)
        dot_group.clear_updaters()
        self.play(Restore(dot_group))
        self.wait()
        code8 = CodeLine("""def put_line_on(a, b):\n
    def update(line):\n
        line.put_start_and_end_on(a.get_center(), b.get_center())\n
    return update\n""",
                         t2c={"put_line_on": BLUE_M, "put_start_and_end_on": BLUE_M}
                         ).scale(0.75).to_corner(UL)
        code8[16].set_color(YELLOW_M)
        code8[19].set_color(YELLOW_M)
        code8[39:43].set_color(YELLOW_M)
        code8[32:38].set_color(GREEN_M)
        self.play(
            FadeOut(code7, UP),
            FadeOut(code6, UP),
        )
        self.play(
            FadeIn(code8, UP)
        )
        self.wait()
        code9 = CodeLine("""l_ab.add_updater(put_line_on(dot_a, dot_b))\n
l_bc.add_updater(put_line_on(dot_b, dot_c))\n
l_cd.add_updater(put_line_on(dot_c, dot_d))\n
l_da.add_updater(put_line_on(dot_d, dot_a))\n""",
                         t2c={"put_line_on": BLUE_M}
                         ).scale(0.8).next_to(code8, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(code9, UP))
        self.wait()
        code10 = CodeLine("""trace = VGroup()\n
trace.add_updater(lambda a, dt: a.add(\n
    l_ab.copy().clear_updaters().set_stroke(width=0.6),\n
    l_bc.copy().clear_updaters().set_stroke(width=0.6),\n
    l_cd.copy().clear_updaters().set_stroke(width=0.6),\n
    l_da.copy().clear_updaters().set_stroke(width=0.6),\n
))\n""", t2c={"copy": BLUE_M, "width": RED_M, "add": BLUE_M, "VGroup": BLUE_M}
                          ).scale(0.8).next_to(code9, DOWN, aligned_edge=LEFT)
        code10[43].set_color(YELLOW_M)
        self.play(FadeIn(code10, UP))
        self.wait()
        code11 = CodeLine("""self.add(dots, lines, trace...)\n
self.wait(...)\n""", t2c={"add": BLUE_M, "wait": BLUE_M}
                          ).scale(0.8).next_to(code10, DOWN, aligned_edge=LEFT)
        self.play(FadeIn(code11, UP))
        self.wait()

        dot_group[0].add_updater(update_dot(dot_group[1]))
        dot_group[1].add_updater(update_dot(dot_group[2]))
        dot_group[2].add_updater(update_dot(dot_group[3]))
        dot_group[3].add_updater(update_dot(dot_group[0]))
        self.add(dot_group[0], dot_group[1], dot_group[2], dot_group[3])

        def line_anim(p1: Dot, p2: Dot):
            def update(obj: Line):
                obj.put_start_and_end_on(p1.get_center(), p2.get_center())

            return update

        line_group[0].add_updater(line_anim(dot_group[0], dot_group[1]))
        line_group[1].add_updater(line_anim(dot_group[1], dot_group[2]))
        line_group[2].add_updater(line_anim(dot_group[2], dot_group[3]))
        line_group[3].add_updater(line_anim(dot_group[3], dot_group[0]))
        self.add(line_group[0], line_group[1], line_group[2], line_group[3])

        trace = VGroup()
        trace.add_updater(lambda a, dt: a.add(
            line_group.copy().clear_updaters().set_stroke(width=0.6)
        ))
        self.add(trace)
        self.wait(5)
        dot_group.clear_updaters()
        line_group.clear_updaters()
        trace.clear_updaters()
        self.wait()


class Bullet(Triangle):
    CONFIG = {
        "fill_opacity": 1,
        "stroke_width": 0,
        "length": DEFAULT_ARROW_TIP_LENGTH,
        "start_angle": PI,
        "aspect": 1.5,
        "angle": 0,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        digest_config(self, kwargs)
        self.set_height(self.length, stretch=True)
        self.set_width(self.length * self.aspect, stretch=True)
        self.data["points"][4] += np.array([self.length, 0, 0])
        self.scale(0.35)

    def get_angle(self):
        return self.angle
        # return angle_of_vector(self.get_vector())

    def get_vector(self):
        return self.point_from_proportion(0.5) - self.get_start()

    def rotate(self, angle, axis=OUT, **kwargs):
        super().rotate(angle, axis, **kwargs)
        self.angle = angle
        return self


class Scene11(Scene):
    def construct(self):
        code1 = CodeLine("angle = 0").to_edge(UP).add_background_rectangle(buff=0.25)
        code2 = CodeLine("angle = PI").to_edge(UP).add_background_rectangle(buff=0.25)
        code3 = CodeLine("angle = 120 deg").to_edge(UP).add_background_rectangle(buff=0.25)
        code4 = CodeLine("angle = angle + 1 deg").to_edge(UP).add_background_rectangle(buff=0.25)
        code5 = CodeLine("angle = angle + 45 deg").to_edge(UP).add_background_rectangle(buff=0.25)
        code6 = CodeLine("angle = angle + 120 deg").to_edge(UP).add_background_rectangle(buff=0.25)
        code7 = CodeLine("angle = angle + time deg", t2c={"time": YELLOW_A}).to_edge(UP).add_background_rectangle(
            buff=0.25)
        text1 = Text("发射角", font="Source Han Serif SC").to_corner(DR).add_background_rectangle(buff=0.25)
        text2 = Text("伪线", font="Source Han Serif SC").to_corner(DR).add_background_rectangle(buff=0.25)
        text3 = Text("变量", font="Source Han Serif SC").to_corner(DR).add_background_rectangle(buff=0.25)

        def anim1(obj, dt):
            obj.add(Bullet())
            obj.set_color_by_gradient(PURPLE, BLUE, TEAL, GREEN, YELLOW, GOLD, ORANGE, RED)
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(get_norm(k.get_center() - ORIGIN)) > 7.5:
                    obj.remove(k)

        def anim2(obj, dt):
            obj.add(Bullet().rotate(PI))
            obj.set_color_by_gradient(PURPLE, BLUE, TEAL, GREEN, YELLOW, GOLD, ORANGE, RED)
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(get_norm(k.get_center() - ORIGIN)) > 7.5:
                    obj.remove(k)

        def anim3(obj, dt):
            obj.add(Bullet().rotate(TAU / 3))
            obj.set_color_by_gradient(PURPLE, BLUE, TEAL, GREEN, YELLOW, GOLD, ORANGE, RED)
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(get_norm(k.get_center() - ORIGIN)) > 7.5:
                    obj.remove(k)

        def anim4(obj, dt):
            obj.add(Bullet().rotate(self.time * PI))
            obj.set_color_by_gradient(PURPLE, BLUE, TEAL, GREEN, YELLOW, GOLD, ORANGE, RED)
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(get_norm(k.get_center() - ORIGIN)) > 7.5:
                    obj.remove(k)

        def anim5(obj, dt):
            obj.add(Bullet().rotate(self.time * 15 * PI))
            obj.set_color_by_gradient(PURPLE, BLUE, TEAL, GREEN, YELLOW, GOLD, ORANGE, RED)
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(get_norm(k.get_center() - ORIGIN)) > 7.5:
                    obj.remove(k)

        def anim6(obj, dt):
            obj.add(Bullet().rotate(self.time * PI * 40))
            obj.set_color_by_gradient(PURPLE, BLUE, TEAL, GREEN, YELLOW, GOLD, ORANGE, RED)
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(get_norm(k.get_center() - ORIGIN)) > 7.5:
                    obj.remove(k)

        def anim7(obj, dt):
            obj.add(Bullet().rotate(self.time ** 2))
            obj.set_color_by_gradient(PURPLE, BLUE, TEAL, GREEN, YELLOW, GOLD, ORANGE, RED)
            for k in obj:
                k.shift(dt * 2 * np.array([
                    np.cos(k.get_angle()),
                    np.sin(k.get_angle()),
                    0
                ]))
                if abs(get_norm(k.get_center() - ORIGIN)) > 7.5:
                    obj.remove(k)

        trail = VGroup()
        trail.add_updater(anim1)
        self.add(trail)
        self.play(FadeIn(code1, DOWN), FadeIn(text1, DOWN))
        self.wait()
        trail.clear_updaters()
        trail.add_updater(anim2)
        self.play(
            FadeOut(code1, DOWN),
            FadeIn(code2, DOWN),
        )
        self.wait()
        trail.clear_updaters()
        trail.add_updater(anim3)
        self.play(
            FadeOut(code2, DOWN),
            FadeIn(code3, DOWN),
        )
        self.wait()
        trail.clear_updaters()
        self.ka = 0
        trail.add_updater(anim4)
        self.play(
            FadeOut(code3, DOWN),
            FadeIn(code4, DOWN),
        )
        self.wait()
        trail.clear_updaters()
        trail.add_updater(anim5)
        self.play(
            FadeOut(text1, DOWN),
            FadeIn(text2, DOWN),
            FadeOut(code4, DOWN),
            FadeIn(code5, DOWN),
        )
        self.wait(2)
        trail.clear_updaters()
        trail.add_updater(anim6)
        self.play(
            FadeOut(code5, DOWN),
            FadeIn(code6, DOWN),
        )
        self.wait(3)
        trail.clear_updaters()
        trail.add_updater(anim7)
        self.play(
            FadeOut(code6, DOWN),
            FadeOut(text2, DOWN),
            FadeIn(code7, DOWN),
            FadeIn(text3, DOWN),
        )
        self.wait(6)


# Scene12 for recording


class Scene13(Scene):
    def construct(self):
        text = Tex(r"\text{d}t=\frac{1}{\text{self.camera.frame\_rate}}")
        text[0][0:2].set_color(YELLOW_M)
        text[0][5:9].set_color(RED_M)
        self.play(FadeIn(text, UP))
        self.wait()
        code1 = CodeLine("""obj_a.add_updater(lambda x, dt: ...)\n
self.wait(1.5)\n
obj_b.add_updater(lambda x, dt: ...)\n
self.wait(2)\n
obj_a.clear_updaters()\n
self.wait(...)\n""",
                         t2c={"x": YELLOW_M, "wait": BLUE_M}
                         )
        self.play(
            AnimationGroup(
                FadeOut(text, UP), FadeIn(code1, UP),
                lag_ratio=0.6
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                FadeOut(code1, DOWN), FadeIn(text, DOWN),
                lag_ratio=0.6
            )
        )
        self.wait()
        code2 = CodeLine('''
obj.add_updater(lambda a, dt: a.rotate(\n
    -np.exp(a.get_angle()) * dt\n
))\n
'''.strip(),
                         t2c={"get_angle": BLUE_M, "exp": BLUE_M, "rotate": BLUE_M}
                         ).to_edge(LEFT)
        code2[23].set_color(YELLOW_M)
        self.play(
            text.animate.shift(LEFT * 3.5 + UP * 1.5),
            FadeIn(code2, UL),
        )
        self.wait()
        rect = SurroundingRectangle(code2[45:67])
        # self.add(rect)
        self.play(ShowCreation(rect))
        explanation1 = Text("# 非线性",
                            font="Source Han Sans CN", color=GREY
                            ).next_to(code2[72]).scale(0.8)
        self.play(Write(explanation1))
        self.play(FadeOut(rect))
        squ = Square(color=GREEN_M).shift([3, 0, 0])
        self.play(ShowCreation(squ))
        squ.add_updater(lambda a, dt: a.rotate(
            -angle_of_vector(a.get_vertices()[2] - a.get_vertices()[1]) * dt
        ))
        self.wait(4)


class Scene14(Scene):
    def construct(self):
        t1 = TexText("Updater教程 \#03").scale(1.8).shift(UP * 0.7 + LEFT * 6)
        t2 = Text(
            "Time*based*updater"[::-1], t2c={"*": "#1f251a"}
        ).arrange(LEFT, aligned_edge=UP, buff=0.04).scale(1.5).shift(DOWN / 2 + RIGHT * 6)
        t2[5].shift(DOWN / 7)

        def shifting_to_center(obj, dt):
            obj.shift(
                2 * dt * obj.get_center()[0] * LEFT
            )

        t1.add_updater(shifting_to_center)
        t2.add_updater(shifting_to_center)
        self.add(t1, t2)
        self.play(Write(t1), Write(t2))
        self.wait()
        t1.clear_updaters()
        t2.clear_updaters()
        back_rect = Rectangle(15, 4, fill_opacity=0.85, stroke_width=0, fill_color=BLACK)
        t3 = Text("turn animation into updater",
                  t2c={"animation": RED_M, "updater": YELLOW_M}).scale(2)
        self.play(
            FadeIn(back_rect), Write(t3)
        )
        self.wait()


class Scene15(Scene):
    def construct(self):
        code = CodeLine("""def turn_animation_into_updater(animation, cycle=False, **kwargs):\n
    ...\n
    animation.begin()\n
    animation.total_time = 0\n
    ...\n
    def update(m, dt):\n
        run_time = animation.get_run_time()\n
        time_ratio = animation.total_time / run_time\n
        if cycle:\n
            alpha = time_ratio % 1\n
        else:\n
            alpha = clip(time_ratio, 0, 1)\n
            if alpha >= 1:\n
                animation.finish()\n
                m.remove_updater(update)\n
                return\n
        animation.interpolate(alpha)\n
        animation.update_mobjects(dt)\n
        animation.total_time += dt\n
\n
    mobject.add_updater(update)\n
    return mobject\n""",
                        t2c={"begin": BLUE_M, "update_mobjects": BLUE_M, "clip": BLUE_M, "finish": BLUE_M,
                             "turn_animation_into_updater": GREEN_M, "get_run_time": BLUE_M,
                             "interpolate": BLUE_M}
                        ).scale(0.7)
        code[32:41].set_color(YELLOW_M)
        code[43:48].set_color(YELLOW_M)
        code[154].set_color(YELLOW_M)
        code[147:153].set_color(GREEN_M)
        self.play(FadeIn(code))
        self.play(code.animate.to_edge(LEFT))
        tips = VGroup(
            ArrowTip(fill_color=YELLOW).scale(0.7).rotate(PI).next_to(code[259]),
            ArrowTip(fill_color=YELLOW).scale(0.7).rotate(PI).next_to(code[373]),
            ArrowTip(fill_color=YELLOW).scale(0.7).rotate(PI).next_to(code[541]),
            ArrowTip(fill_color=YELLOW).scale(0.7).rotate(PI).next_to(code[580]),
            ArrowTip(fill_color=YELLOW).scale(0.7).rotate(PI).next_to(code[616])
        )
        self.play(*[FadeIn(tip) for tip in tips])
        self.wait()
        progress_bar = Rectangle(
            0.001, 0.25, fill_opacity=1, stroke_width=0, fill_color=BLUE_M
        )
        progress_bar.shift([0, -2.5, -0.1])
        bar_border = Rectangle(6.2, 0.4).shift([3, -2.48, 0])
        self.play(ShowCreation(bar_border))
        self.add(progress_bar)

        tip_total_time = ArrowTip(fill_color=YELLOW).rotate(PI / 2).scale(0.5)
        tip_total_time.add_updater(lambda a: a.move_to(progress_bar.get_vertices()[3] + DOWN / 3))

        total_time = ValueTracker(0)
        text_total_time = VGroup(
            CodeLine(
                "total_time=", t2c={"total_time": YELLOW_M}
            ).scale(0.7),
            DecimalNumber(0).scale(0.4),
        ).arrange(RIGHT, buff=0.02)
        text_total_time.add_updater(lambda a: a.next_to(tip_total_time, DOWN, buff=0.1))
        text_total_time[1].add_updater(lambda a: a.set_value(total_time.get_value() * 3))

        text_run_time = VGroup(
            CodeLine(
                "run_time=", t2c={"run_time": YELLOW_M}
            ).scale(0.7),
            Integer(3).scale(0.4)
        ).arrange(RIGHT, buff=0.02).next_to(bar_border, UP, aligned_edge=RIGHT)
        text_alpha_value = VGroup(
            CodeLine("alpha=").scale(0.7),
            DecimalNumber(0).scale(0.4),
        ).arrange(RIGHT, buff=0.02).next_to(bar_border, UP)
        text_alpha_value[1].add_updater(lambda a: a.set_value(total_time.get_value() % 1))

        cir = Circle(stroke_color=WHITE).shift([3.5, 0, 0]).scale(0.5)
        cir2 = Circle(stroke_color=WHITE).shift([3.5, 0, 0]).scale(0.5)
        cir3 = Circle(stroke_color=WHITE).shift([3.5, 0, 0]).scale(0.5)
        cir4 = Circle(stroke_color=WHITE).shift([3.5, 0, 0]).scale(0.5)
        example_code1 = CodeLine("""
anim = FadeIn(circle, rate_func=there_and_back)\n
turn_animation_into_updater(anim)\n
""",
                                 t2c={"FadeIn": BLUE_M, "rate_func": RED_M,
                                      "turn_animation_into_updater": BLUE_M}
                                 ).scale(0.7).shift([3.5, 2.5, 0])

        example_code2 = CodeLine("""
anim = FadeIn(circle, rate_func=there_and_back)\n
turn_animation_into_updater(anim, True)\n
self.add(circle)\n
self.wait()\n
""",
                                 t2c={"FadeIn": BLUE_M, "rate_func": RED_M, "add": BLUE_M, "wait": BLUE_M,
                                      "turn_animation_into_updater": BLUE_M}
                                 ).scale(0.7).shift([3.5, 2.2, 0])

        example_code3 = CodeLine("""
anim = FadeIn(circle, rate_func=there_and_back)\n
turn_animation_into_updater(anim, True)\n
circle.add_updater(lambda x, dt: ...)\n
self.add(circle)\n
self.wait()\n
""",
                                 t2c={"FadeIn": BLUE_M, "rate_func": RED_M, "add": BLUE_M, "wait": BLUE_M,
                                      "turn_animation_into_updater": BLUE_M, "x": YELLOW_M}
                                 ).scale(0.7).shift([3.5, 2.25, 0])

        self.play(
            Write(text_alpha_value),
            Write(text_run_time),
            Write(text_total_time),
            Write(example_code1),
            ShowCreation(tip_total_time),
        )
        anim = FadeIn(cir, rate_func=there_and_back)
        self.play(
            anim,
            ApplyMethod(total_time.set_value,
                        1, rate_func=linear,
                        ),
            ApplyMethod(progress_bar.set_width,
                        {"width": 6, "stretch": True, "about_edge": LEFT, },
                        rate_func=linear,
                        ),
            run_time=3,
        )
        self.play(tips[1].animate.next_to(code[479]))
        text_cycle_true = CodeLine(
            "cycle=True", t2c={"cycle": YELLOW_M}
        ).scale(0.7).next_to(code[48], DOWN)
        self.play(FocusOn(code[43:54]))
        self.play(
            Write(text_cycle_true),
            code[43:54].animate.set_opacity(0.1),
            tips[1].animate.next_to(code[314]),
            FadeIn(example_code2, DOWN),
            FadeOut(example_code1, DOWN),
        )
        total_time.add_updater(lambda a, dt: a.increment_value(dt / 3))
        progress_bar.add_updater(lambda a: a.set_width(
            np.clip((total_time.get_value() % 1) * 6, 0.001, 6),
            True, about_edge=LEFT
        )
                                 )
        # cir.clear_updaters()
        cycle_animation(FadeIn(cir2, rate_func=there_and_back, run_time=3))
        self.add(cir2)
        self.wait(9)
        total_time.clear_updaters()
        cir2.clear_updaters()
        self.wait()
        self.play(FadeOut(example_code2, DOWN), FadeIn(example_code3, DOWN))
        cir3.add_updater(lambda a, dt: a.move_to([3.5 + np.cos(3 * self.time), np.sin(self.time), 0]))
        cycle_animation(FadeIn(cir3, rate_func=there_and_back, run_time=3))
        self.add(cir3)
        total_time.add_updater(lambda a, dt: a.increment_value(dt / 3))
        self.wait(9)
        cir3.clear_updaters()
        text_alpha_value[1].clear_updaters()
        self.wait()
        text_clear = CodeLine("circle.clear_updaters()", t2c={"clear_updaters": BLUE_M}).scale(0.7).next_to(
            example_code3, DOWN, aligned_edge=LEFT, buff=2.5)
        self.play(Write(text_clear), FadeIn(cir4))
        self.wait(3)


class Scene16(Scene):
    def construct(self):
        code1 = CodeLine("Animation(object)", t2c={"Animation": BLUE_M, "object": GREEN_M}).shift([-3, 0, 0])
        code2 = CodeLine("""def interpolate(start, end, alpha):\n
    return (1 - alpha) * start + alpha * end\n""").next_to(code1, DOWN, aligned_edge=LEFT).shift(UP)
        self.play(FadeIn(code1, UP))
        self.play(
            FadeIn(code2, UP),
            code1.shift, UP,
        )
        self.wait()
        code3 = CodeLine("obj.add_updater(update)").next_to(code2, DOWN, aligned_edge=LEFT).shift(UP)
        self.play(
            FadeIn(code3, UP),
            code1.shift, UP,
            code2.shift, UP,
        )
        numline = NumberLine([0, 1, 0.1], width=5).next_to(code3, DOWN, aligned_edge=LEFT, buff=1)
        self.play(FadeIn(numline, UP))
        tip = ArrowTip(fill_color=YELLOW).scale(0.6).rotate(-PI / 2).move_to(numline.n2p(0) + UP / 3)
        text_alpha = CodeLine("alpha").scale(0.8).next_to(tip, UP, buff=0.15)
        self.play(Write(tip), Write(text_alpha))
        self.wait()
        for i in range(10):
            self.play(AnimationGroup(
                tip.animate.shift(RIGHT / 2),
                text_alpha.animate.shift(RIGHT / 2),
                lag_ratio=0.5, run_time=0.3
            ))
        self.wait()
        code4 = CodeLine("obj.add_updater(lambda x, dt: ...)", t2c={"x": YELLOW_M}).next_to(numline, DOWN,
                                                                                            aligned_edge=LEFT).shift(UP)
        self.play(*[
            obj.animate.shift(UP) for obj in [code1, code2, code3, tip, numline, text_alpha]
        ], FadeIn(code4, UP)
                  )
        numline2 = NumberLine([0, 14, 0.5], width=14).shift(DOWN * 2)
        self.play(FadeIn(numline2, UP))
        tip2 = ArrowTip(fill_color=YELLOW).scale(0.6).rotate(-PI / 2).move_to(numline2.n2p(1) + UP / 3)
        text_time = CodeLine("self.time").scale(0.8).add_updater(lambda a: a.next_to(tip2, UP, buff=0.15))
        tip2.add_updater(lambda a, dt: a.shift(RIGHT * dt))
        self.add(tip2, text_time)
        self.play(FadeIn(tip2, UP), FadeIn(text_time, UP))
        self.wait(10)
