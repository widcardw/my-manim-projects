from manimlib import *


class Logo(VGroup):
    CONFIG = {
        'color_1': [WHITE, BLUE_B, BLUE_D],
        'color_2': [WHITE, '#C59978', '#8D5630'],

        # 'color_3': [average_color("#CCCCCC", BLUE_C), BLUE_C, BLUE_D],
        # 'color_4': [average_color("#CCCCCC", "#C59978"), '#C59978', '#8D5630'],

        'color_3': [average_color(WHITE, BLUE_C), BLUE_C, BLUE_D],
        'color_4': [average_color(WHITE, "#C59978"), '#C59978', '#8D5630'],

        'center': ORIGIN,
        'size': 2,
        'shift_out': ORIGIN,
        'black_bg': True,
        'add_bg_square': False,
    }

    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.create_logo()

    def create_logo(self):

        p1 = Polygon(ORIGIN, RIGHT, 2 * UP, stroke_width=0).set_fill(self.color_1[0], 1)
        p2 = Polygon(1.5 * RIGHT, 3 * UR, 3 * UP, stroke_width=0).set_fill(self.color_1[1], 1)
        p3 = Polygon(2 * RIGHT, 3 * RIGHT, 3 * RIGHT + 2 * UP, stroke_width=0).set_fill(self.color_1[2], 1)
        if not self.black_bg:
            p1.set_fill(self.color_3[0], 1), p2.set_fill(self.color_3[1], 1), p3.set_fill(self.color_3[2], 1)

        self.bg = Square(stroke_width=0, fill_color=BLACK if self.black_bg else WHITE, fill_opacity=1).set_height(
            self.size * 2.5)
        if self.add_bg_square:
            self.add(self.bg)

        self.part_ur = VGroup(p1, p2, p3).move_to([2.5, 1., 0] + self.shift_out)
        self.part_ul = self.part_ur.copy().rotate(PI / 2, about_point=ORIGIN)
        self.part_dl = self.part_ur.copy().rotate(PI, about_point=ORIGIN)
        self.part_dr = self.part_ur.copy().rotate(3 * PI / 2, about_point=ORIGIN)

        self.add(self.part_ur, self.part_ul, self.part_dl, self.part_dr)
        self.set_height(self.size).move_to(self.center)
        if self.black_bg:
            self.part_ur[0].set_fill(self.color_2[0], 1), self.part_ur[1].set_fill(self.color_2[1], 1), self.part_ur[
                2].set_fill(self.color_2[2], 1)
        else:
            self.part_ur[0].set_fill(self.color_4[0], 1), self.part_ur[1].set_fill(self.color_4[1], 1), self.part_ur[
                2].set_fill(self.color_4[2], 1)

        self.inner_triangles = VGroup(self.part_ur[0], self.part_ul[0], self.part_dl[0], self.part_dr[0])
        self.mid_triangles = VGroup(self.part_ur[1], self.part_ul[1], self.part_dl[1], self.part_dr[1])
        self.outer_triangles = VGroup(self.part_ur[2], self.part_ul[2], self.part_dl[2], self.part_dr[2])


class EndScene(Scene):
    def construct(self):
        # self.add(NumberPlane())
        mk_logo = ImageMobject("mk.png")
        text_mk = VGroup(
            VGroup(
                Text("A", font="Novecento wide Light Regular", font_size=54),
                Text("Manim-Kindergarten", font="Orbitron", font_size=48),
            ).arrange(RIGHT, aligned_edge=ORIGIN),
            Text("PRODUCTION", font="Novecento wide Light Regular", font_size=54),
        ).arrange(DOWN, aligned_edge=LEFT).set_width(9).set_color(BLACK)
        text_mk.move_to(LEFT * 2.5, aligned_edge=UL)
        text_mk[0][1].shift(0.08 * DOWN)
        mk_logo.move_to([-4.25, 1.25, 0]).scale(1.3).shift(RIGHT * 0.1)

        self.add(mk_logo, text_mk)
        mk_logo.save_state()
        text_mk.save_state()

        mk_logo.shift(LEFT * 5)
        text_mk.shift(RIGHT * 10)

        self.play(Restore(mk_logo), Restore(text_mk), rate_func=slow_into, run_time=3)

        gs_logo = ImageMobject("3b1b.png")
        text_gs = VGroup(
            VGroup(
                Text("WITH", font="Novecento wide Light Regular", font_size=54),
                Text("Grant Sanderson", font="Orbitron", font_size=48),
            ).arrange(RIGHT, aligned_edge=ORIGIN),
            VGroup(
                Text("AS", font="Novecento wide Light Regular", font_size=54),
                Text("3Blue1Brown", font="Orbitron", font_size=48),
            ).arrange(RIGHT, aligned_edge=ORIGIN),
        ).arrange(DOWN, aligned_edge=LEFT).set_width(9).set_color(BLACK)
        text_gs.move_to(LEFT * 6.5, aligned_edge=UL).shift(DOWN * 0.05)
        gs_logo.move_to([-4.25, 1.25, 0]).scale(1.3).shift(RIGHT * 8)

        # self.add(gs_logo, text_gs)
        self.play(
            FadeTransform(mk_logo, gs_logo),
            FadeTransform(text_mk, text_gs),
            rate_func=slow_into, run_time=3
        )
        self.play(
            text_gs.animate.shift(LEFT * 10),
            gs_logo.animate.shift(RIGHT * 6),
            rate_func=rush_from, run_time=2
        )


class EndScene2(Scene):
    CONFIG = {"camera_config": {"background_color": WHITE}}

    def construct(self):
        logo = Logo(black_bg=False).shift([-9, 1, 0]).scale(2)
        logo_text = VGroup(
            VGroup(
                Text("A", font="Novecento wide Light Regular", font_size=54, color=BLACK),
                Text("Manim-Kindergarten", color=BLACK, t2c={"M": "#8D5630", "K": BLUE_D}, font="Orbitron",
                     font_size=48),
            ).arrange(RIGHT, aligned_edge=ORIGIN),
            Text("PRODUCTION", color=BLACK, font="Novecento wide Light Regular", font_size=54),
        ).arrange(DOWN, aligned_edge=LEFT).set_width(9)
        logo.set_stroke(BLACK)
        logo_text.move_to([14, -1, 0]).set_stroke(BLACK)

        def anim_to_tg(arr):
            def update(obj, dt):
                obj.shift(2 * dt * np.array([
                    arr[0] - obj.get_center()[0],
                    arr[1] - obj.get_center()[1], 0
                ]))

            return update

        logo.add_updater(anim_to_tg([-4.3, 1]))
        logo_text.add_updater(anim_to_tg([1.8, -1, 0]))
        anim1 = DrawBorderThenFill(logo)
        anim2 = Write(logo_text)
        self.add(logo, logo_text)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait(5)
        logo.clear_updaters()
        logo_text.clear_updaters()

        # _3b1b = ImageMobject("3b1b.png")
        # text_gs = VGroup(
        #     VGroup(
        #         Text("WITH", font="Novecento wide Light Regular", font_size=54),
        #         Text("Grant Sanderson", font="Orbitron", font_size=48),
        #     ).arrange(RIGHT, aligned_edge=ORIGIN),
        #     VGroup(
        #         Text("AS", font="Novecento wide Light Regular", font_size=54),
        #         Text("3Blue1Brown", font="Orbitron", font_size=48),
        #     ).arrange(RIGHT, aligned_edge=ORIGIN),
        # ).arrange(DOWN, aligned_edge=LEFT).set_width(9).set_color(BLACK)


class AllPointsIndex(VGroup):
    CONFIG = {
        "scale_factor": 0.5,
        "color": PURPLE,
    }

    def __init__(self, obj, **kwargs):
        # digest_config(self, kwargs)
        VGroup.__init__(self, **kwargs)
        for index, points in enumerate(obj.get_all_points()):
            point_id = Integer(index, background_stroke_width=2) \
                .scale(self.scale_factor).set_color(self.color)
            point_id.move_to(points)
            self.add(point_id)


class TestShaders(Scene):
    def construct(self):
        bloom = Circle(fill_opacity=1, stroke_width=0).scale(4).set_gloss(0.1)
        # glsl_code = ''''''
        # bloom.set_color_by_xyz_func("x * 2 + y * 2")
        bloom.set_color_by_code("""color.a=1-pow((point.x)/3,2);""")
        self.add(bloom)
        # point.x / 3
        # pow(point.x/3, 2)
        # (exp(point.x)+exp(-point.x))/16.0
        # 1-pow((point.x)/3,2)
        # 45/(exp(abs(point.x)+abs(point.y)))
        # exp(abs(point.x)+1/exp(abs(point.y)))/50


class TestCubicBezier(Scene):
    def construct(self):
        cir = ParametricCurve(
            lambda t: np.array([
                2 * np.cos(5 * PI * t),
                2 * np.sin(5 * PI * t),
                t
            ]), t_range=[-5, 5, 0.01]
        )
        self.add(cir)


class MIcicle(Scene):
    def construct(self):
        a = 1
        b = 1
        m = 3
        n = 3
        t = ValueTracker(0)
        dot = Dot(color=YELLOW, background_stroke_color=WHITE, background_stroke_width=2, radius=0.05)
        dot.add_updater(lambda d: d.move_to(
            2 * np.array([
                pow(abs(np.cos(t.get_value())), 2 / m) * a * np.sign(np.cos(t.get_value())),
                pow(abs(np.sin(t.get_value())), 2 / n) * b * np.sign(np.sin(t.get_value())),
                0])))
        path = TracedPath(dot.get_center, stroke_color=RED, stroke_width=4)
        trace = ParametricCurve(
            lambda k: np.array([
                pow(abs(np.cos(k)), 2 / m) * a * np.sign(np.cos(k)),
                pow(abs(np.sin(k)), 2 / n) * b * np.sign(np.sin(k)),
                0
            ]),
            t_min=0, t_max=TAU
        ).scale(3)
        self.play(ShowCreation(trace), rate_func=linear, run_time=2)
        self.wait()


class TestMatrix(Scene):
    def construct(self):
        m = [[2, 3], [4, 5]]
        matrix = IntegerMatrix(m)
        self.add(matrix)


class TestWriteFromRight(Scene):
    def construct(self):
        v = VMobject(fill_opacity=1)
        text = Text("Hello World").scale(3)
        v.set_points(text.get_all_points()[::-1])
        self.play(Write(v))
        self.wait()


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


class MultilineText(Scene):
    def construct(self):
        text = Text('''
        Hello World\n
            widcardw
        ''')
        ind = TexIndex(text, scale_factor=0.3)
        self.add(text, ind)