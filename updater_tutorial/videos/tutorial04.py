from manim_sandbox.utils.imports import *
from manim_sandbox.utils.mobjects.Gear import Gear_outline
from my_videos.tutorial.DouPandulum import DouPandulumLine, DouPandulumSim
from my_videos.tutorial.path_dir_vector import PathVector
from my_videos.tutorial.rolling_list import RollingList2, RollVerticallyTo2

# 注意，这里引入了 manimlib 以外的模块，需要用另外的命令来进行渲染，即
# $ python manimlib ${FileName} ${SceneName}
# 而不是 $ manimgl ${FileName} ${SceneName}
SOURCE = "Source Han Serif SC"


class TestBezier1(Scene):
    def construct(self):
        b1 = BezierGenerator(np.array([
            [-6, -3, 0],
            [-2, 3, 0],
            [0, 0, 0],
            [2, 3, 0],
            [6, -2, 0]
        ]))
        self.play(MakeBezier2(b1))
        self.wait()


# 注意：这个类用到了窗口交互，即调用了 Pyglet Window 的一些属性
# 用旧版 manim-cairo 是无法运行的
# 同时要注意，窗口映射模式有些问题，所以鼠标点击的位置会有亿点点偏差
# 在点击窗口之前先将窗口大小缩放为 1280x720

# 2021/6/19 更新 不需要缩放窗口了, 或者加入 -f 参数全屏预览
class InteractiveBezier(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dot_list = []  # 存储所有的锚点
        self.pre_dot_group = VGroup()  # 已经点击过的地方显示这是第几个锚点
        self.count = 0
        self.bezier = None  # 贝塞尔曲线生成物件

    def init_draw_area(self):
        rect = Rectangle(11, 7, fill_opacity=0, color=BLACK).shift(LEFT + DOWN * 0.3)
        notice = Text("Click to add points.").scale(0.7).next_to(rect, UP)
        self.add(notice)

        def area_on_click(mobject):
            print(self.mouse_point.get_location())
            self.dot_list.append(self.mouse_point.get_location())
            d = Integer(self.count, color=PURPLE_A).scale(0.4).move_to(self.mouse_point.get_location())
            self.add(d)
            self.pre_dot_group.add(d)
            self.count += 1

        self.draw_area = Button(rect, area_on_click)
        self.add(self.draw_area)
        self.add(self.pre_dot_group)

    def init_play_button(self):
        play_rect = Text("Play").add_background_rectangle(color=BLACK, opacity=1, buff=0.25).to_corner(UR)

        def play_clicked(mobject):
            try:
                if self.bezier != None:
                    self.remove(self.bezier.curve_path)
                    self.remove(self.bezier)
                    self.bezier = None
                self.remove(*[d for d in self.pre_dot_group])
                self.bezier = BezierGenerator(self.dot_list)
                print("Start to play")
                self.play(MakeBezier2(self.bezier))
            except:
                print('Failed to play, previous points would be cleared. ')
                self.clear_btn.on_click(self.clear_btn)

        self.play_btn = Button(play_rect, play_clicked)
        self.add(self.play_btn)

    def init_clear_button(self):
        clear_rect = Text("Clear") \
            .add_background_rectangle(color=BLACK, opacity=1, buff=0.25)
        clear_rect.set_width(self.play_btn.get_width()).next_to(self.play_btn, DOWN)

        def clear_clicked(mobject):
            self.count = 0
            self.dot_list = []
            self.remove(*[d for d in self.pre_dot_group])
            self.pre_dot_group.remove(*self.pre_dot_group.submobjects)
            if self.bezier != None:
                self.remove(self.bezier.curve_path)
                self.remove(self.bezier)
                self.bezier = None
            print("Cleared")

        self.clear_btn = Button(clear_rect, clear_clicked)
        self.add(self.clear_btn)

    def init_pop_button(self):
        pop_rect = Text("Pop").add_background_rectangle(BLACK, 1, buff=0.25)
        pop_rect.background_rectangle.set_width(self.play_btn.get_width(), True)
        pop_rect.background_rectangle.set_height(self.clear_btn.get_height(), True)
        pop_rect.next_to(self.clear_btn, DOWN)

        def pop_clicked(mobject):
            assert (len(self.dot_list) >= 1)
            self.count -= 1
            self.dot_list.pop()
            self.remove(self.pre_dot_group[-1])
            self.pre_dot_group.remove(self.pre_dot_group[-1])
            print('Popped')

        self.pop_btn = Button(pop_rect, pop_clicked)
        self.add(self.pop_btn)

    def setup(self):
        self.init_draw_area()
        self.init_play_button()
        self.init_clear_button()
        self.init_pop_button()


class ShowBezier(Scene):
    def construct(self):
        l = Line()
        p = AllPointsIndex(l, color=ORANGE_M)
        self.add(l, p)


class TestReverse(Scene):
    def construct(self):
        v = VMobject()
        v.set_points(np.array([[-1, 0, 0], [3, 0, 0], [1, 0, 0]]))
        p = AllPointsIndex(v, color=ORANGE_M)
        self.add(v, p)


def anim_to_target(target: np.ndarray):
    def update(obj, dt):
        obj.shift((target - obj.get_center()) * 2 * dt)

    return update


class Scene01(Scene):
    def construct(self):
        t1 = TexText("manim教程").scale(2).shift(UP / 2).to_edge(LEFT)
        t2 = Text("自定义物件"[::-1],
                  font="Source Han Serif SC", weight="MEDIUM"
                  ).arrange(LEFT, buff=0.04).scale(1.2).shift(DOWN / 2).to_edge(RIGHT)
        t1.add_updater(anim_to_target(UP / 2))
        t2.add_updater(anim_to_target(DOWN / 2))
        self.add(t1, t2)
        turn_animation_into_updater(Write(t1))
        turn_animation_into_updater(Write(t2))
        # self.play(Write(t1), Write(t2))
        self.wait(3)


class Scene02(Scene):
    def construct(self):
        t1 = CodeLine('object', color=PURPLE_M).scale(1.55)
        self.play(Write(t1))
        self.wait()
        t2 = SurroundingRectangle(t1, color=WHITE_M)
        self.play(ShowCreation(t2))
        self.play(VGroup(t1, t2).animate.shift(UP + RIGHT * 0.8))
        self.wait()
        t3 = CodeLine(
            '''self.data = {\n
  "points": np.zeros((0, 3)),\n
  "bounding_box": np.zeros((3, 3)),\n
  "rgbas": np.zeros((1, 4)),\n
}\n
self.uniforms = {...}\n
functions...\n''',
            t2c={'points': GREEN_M, 'bounding_box': GREEN_M, 'rgbas': GREEN_M, 'zeros': BLUE_M}
        ).scale(0.5).next_to(t2, DOWN, aligned_edge=RIGHT)
        self.play(Write(t3))
        self.play(VGroup(t1, t2, t3).animate.center())
        self.wait()
        t4 = CodeLine('Math', color=TEAL_M).scale(1.55).next_to(t2, LEFT)
        t5 = SurroundingRectangle(VGroup(t2, t3), color=WHITE_M)
        self.play(Write(t4), ShowCreation(t5))
        self.wait()
        t8 = CodeLine(
            'stroke,fill,color,functions...',
            t2c={'stroke': YELLOW_M, 'fill': GREEN_M}
        ).scale(0.6).next_to(t5, DOWN)
        self.play(Write(t8))
        t6 = CodeLine('Vectorized', color=ORANGE_M).scale(1.5).next_to(t5, UP)
        t7 = SurroundingRectangle(VGroup(t5, t6, t8), color=YELLOW_M)
        self.play(Write(t6), ShowCreation(t7))
        self.wait()
        self.play(VGroup(*self.mobjects).animate.shift(LEFT * 2))
        self.wait()
        com1 = CodeLine(
            '''data: {\n
  "points": ...\n
  "bounding_box": ...,\n
  "rgbas": ...,\n
}\n
uniform: {...}\n''',
            t2c={'points': GREEN_M, 'bounding_box': GREEN_M, 'rgbas': GREEN_M, 'array': BLUE_M}
        ).scale(0.7).next_to(t7, RIGHT, aligned_edge=UP)
        com2 = CodeLine(
            '''stroke\n
fill\n
color\n
functions\n
...\n''',
            t2c={'stroke': YELLOW_M, 'fill': GREEN_M}
        ).scale(0.7).next_to(com1, DOWN, aligned_edge=LEFT)
        self.play(TransformMatchingShapes(t3.copy(), com1))
        self.wait()
        self.play(TransformMatchingShapes(t8.copy(), com2))
        self.wait()
        cir = Circle(radius=1.5).shift(RIGHT * 6)
        cir.add_updater(anim_to_target(RIGHT * 4))
        self.play(
            VGroup(*self.mobjects).animate.shift(LEFT * 2),
            ShowCreation(cir)
        )
        cir.clear_updaters()
        self.wait()
        self.play(FocusOn(com2[0:6].get_center()))
        cir_points = np.array(cir.get_points())

        def focus_bezier_curves(obj: VMobject, alpha):
            for i in range(obj.get_num_curves()):
                obj.data['points'][3 * i:3 * (i + 1)] = \
                    cir_points[3 * i:3 * (i + 1)] + (cir_points[3 * i + 1] - RIGHT * 4) * alpha * 0.3

        self.play(UpdateFromAlphaFunc(cir, focus_bezier_curves), rate_func=there_and_back_with_pause, run_time=1.6)
        self.wait()
        self.play(FocusOn(com2[8:12].get_center()))
        self.play(cir.animate.set_fill(opacity=0.5), rate_func=there_and_back_with_pause)
        self.wait()
        self.play(
            VGroup(t1, t2, t3, t4, t5, t6, t7, t8, com1, com2).animate.shift(LEFT * 14),
            cir.center, cir.scale, 2,
            run_time=2
        )
        self.remove(t1, t2, t3, t4, t5, t6, t7, t8, com1, com2)
        self.wait()
        dot_anchors = ObjPoints(cir, color=WHITE)
        self.play(Write(dot_anchors))
        self.wait()
        dot_handle_anchors = ObjAnchorHandle(cir, line_color=YELLOW_M)
        com3 = Text("manimgl").scale(0.7).next_to(cir, DOWN)
        self.play(
            FadeTransform(dot_anchors, dot_handle_anchors),
            Write(com3)
        )
        self.wait()


class Scene03(Scene):
    def construct(self):
        bg_squ1 = Square(9, fill_color="#1f252a", fill_opacity=1, stroke_width=10).shift(LEFT * 4.545)
        bg_squ2 = Square(9, fill_color="#1f252a", fill_opacity=1, stroke_width=10).shift(RIGHT * 4.545).rotate(PI)
        self.play(ShowCreation(bg_squ1), ShowCreation(bg_squ2), run_time=3, rate_func=slow_into)
        fomula = Tex("B(t)=\\sum_{i=0}^{n}\\binom{n}{i}P_{i}(1-t)^{i}t^{n-i},t\\in[0,1]")
        bez = Text("Bézier Curve").next_to(fomula, UP)
        self.add(fomula, bez)
        self.add(bg_squ2, bg_squ1)
        self.wait()
        self.play(
            bg_squ2.animate.shift(RIGHT * 10),
            bg_squ1.animate.shift(LEFT * 10),
        )
        self.remove(bg_squ2, bg_squ1)
        self.wait()
        dots = np.array([
            [-6, 1, 0], [-4, -3, 0], [1, 1.5, 0],
            [6, -3, 0], [4, 1, 0], [-2, -3, 0]
        ])
        bezier_generator = BezierGenerator(dots)
        self.play(
            bez.animate.to_edge(UP),
            UpdateFromFunc(fomula, lambda a: a.next_to(bez, DOWN)),
            FadeIn(bezier_generator, UP)
        )
        self.play(MakeBezier2(bezier_generator))
        self.wait()
        t1 = Text("Complex!").scale(2.5).move_to(bezier_generator.get_center()) \
            .add_background_rectangle(buff=0.5, color=BLACK, opacity=0.5)
        t1.background_rectangle.set_width(2 * FRAME_WIDTH, True)
        self.play(Write(t1))
        self.wait()
        self.play(*[
            FadeOut(obj, DOWN) for obj in [bezier_generator.curve_path, bezier_generator, t1]
        ])
        self.wait()
        curves = VGroup(*[
            BezierGenerator(np.array([
                [i - 1, -1, 0],
                [i, -1 + 2 * np.sin(PI / 2 * i), 0],
                [i + 1, -1, 0]
            ]))
            for i in range(-5, 6, 2)
        ])
        self.play(FadeIn(curves))
        self.play(LaggedStart(*[
            MakeBezier2(obj, run_time=0.7, rate_func=linear) for obj in curves
        ], lag_ratio=1))
        self.play(FadeOut(curves))
        self.wait()
        t2 = Text("Concatenate!").scale(2.5).move_to(curves.get_center()) \
            .add_background_rectangle(buff=0.8, color=BLACK, opacity=0.5)
        t2.background_rectangle.set_width(2 * FRAME_WIDTH, True)
        self.play(Write(t2))
        self.wait()


class Scene04(Scene):
    def construct(self):
        r = 2
        axes = Axes(x_range=[-3, 3, 1], width=6, y_range=[-3, 3, 1], height=6)
        self.add(axes)
        cir = Circle(radius=r, color=GREY_B)
        self.play(ShowCreation(cir))
        self.wait()
        theta = ValueTracker(0.01)
        h = ValueTracker(0).add_updater(
            lambda a: a.set_value(r * 4 / 3 * (1 - np.cos(theta.get_value() / 2)) / np.sin(theta.get_value() / 2))
        )
        self.add(h)
        dot_a = Dot().move_to(axes.c2p(r, 0))
        dot_b = Dot().add_updater(
            lambda a: a.move_to(axes.c2p(r, h.get_value()))
        )
        dot_c = Dot().add_updater(
            lambda a: a.move_to(axes.c2p(
                r * math.cos(theta.get_value()) + h.get_value() * math.sin(theta.get_value()),
                r * math.sin(theta.get_value()) - h.get_value() * math.cos(theta.get_value()),
            ))
        )
        dot_d = Dot().add_updater(
            lambda a: a.move_to(axes.c2p(r * math.cos(theta.get_value()), r * math.sin(theta.get_value()))))
        self.play(*[Write(obj) for obj in [dot_a, dot_b, dot_c, dot_d]])
        self.wait()
        curve = VMobject().add_updater(
            lambda a: a.become(
                BezierFunc([dot_a.get_center(), dot_b.get_center(), dot_c.get_center(), dot_d.get_center()],
                           color=ORANGE_M))
        )
        l_ab = Line().add_updater(lambda a: a.become(Line(dot_a.get_center(), dot_b.get_center(), color=YELLOW_M)))
        l_cd = Line().add_updater(lambda a: a.become(Line(dot_c.get_center(), dot_d.get_center(), color=YELLOW_M)))
        self.add(curve, l_ab, l_cd)
        self.play(theta.animate.set_value(PI * 3 / 2), run_time=8, rate_func=there_and_back)
        self.wait()


class Scene05(Scene):
    def construct(self):
        t1 = Text("Custom Object").scale(2).shift(UP * 0.7).to_edge(LEFT)
        t2 = Text("自定义物件", font="Source Han Serif SC", weight="MEDIUM").scale(1.5).shift(DOWN * 0.7).to_edge(RIGHT)
        t1.add_updater(anim_to_target(UP * 0.7))
        t2.add_updater(anim_to_target(DOWN * 0.7))
        self.add(t1, t2)
        self.play(Write(t1), Write(t2))
        self.wait(3)


class Scene06(Scene):
    def construct(self):
        t1 = CodeLine('''self.data = {\n
    "points": np.zeros((0, 3))\n
    ...\n
}\n''', t2c={"points": GREEN_M, "zeros": BLUE_M})
        self.play(Write(t1))
        rect = Rectangle(width=7, height=0.8, color=YELLOW_M).shift(UP * 0.28 + RIGHT * 0.5)
        self.play(ShowCreationThenFadeOut(rect))
        self.wait()
        t2 = CodeLine('points', color=YELLOW_M).to_corner(UL, buff=1)
        self.play(TransformMatchingShapes(t1, t2))
        self.wait()
        t3 = CodeLine('''=[[x1, y1, z1],\n
  [x2, y2, z2],\n
  ...\n
  [xn, yn, zn]]\n''', t2c={'x': ORANGE_M, 'y': ORANGE_M, 'z': ORANGE_M, 'n': ORANGE_M})
        t3.next_to(t2, RIGHT, aligned_edge=UP)
        self.play(Write(t3))
        t4 = CodeLine('len(points) % 3 == 0 in manimgl', t2c={'len': PURPLE_M, 'in': '#C594C5', 'points': YELLOW_M})
        t4.next_to(t2, DOWN, buff=2.5, aligned_edge=LEFT)
        self.play(Write(t4))
        t5 = CodeLine('len(points) % 4 == 0 in manim-cairo',
                      t2c={'len': PURPLE_M, 'in': '#C594C5', 'points': YELLOW_M, '-': "#e0e0e0"})
        t5.next_to(t4, DOWN, aligned_edge=LEFT)
        self.play(Write(t5))
        self.wait()
        bez1 = BezierGenerator(np.array([
            [1, 1, 0], [3, 3, 0], [5, 1, 0]
        ]))
        bez2 = BezierGenerator(np.array([
            [-4, -3, 0], [-1, -1.5, 0], [1, -3, 0], [4, -1.5, 0]
        ]))
        self.play(Write(bez1), Write(bez2))
        self.play(MakeBezier2(bez1), MakeBezier2(bez2), run_time=4)
        self.wait()


class Scene07(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.douPandulumSimulator = DouPandulumSim(120., -10.)

    def refresh_lines_from_ticks(self, ts):
        x1 = self.douPandulumSimulator.x1[ts]
        x2 = self.douPandulumSimulator.x2[ts]
        y1 = self.douPandulumSimulator.y1[ts]
        y2 = self.douPandulumSimulator.y2[ts]
        line1 = Line(np.array((0., 0., 0.)), np.array((x1, y1, 0.)), color=RED_M)
        line2 = Line(np.array((x1, y1, 0.)), np.array((x2, y2, 0.)), color=ORANGE_M)
        return line1, line2

    def construct(self):
        line1, line2 = self.refresh_lines_from_ticks(0)
        doupandulumline = DouPandulumLine(line1, line2)

        def update_doupandulum(obj, dt):
            ts = int(np.floor((1.0 + self.time / 5) / 0.002))
            line_1, line_2 = self.refresh_lines_from_ticks(ts)
            obj.resetLines(line_1, line_2)

        doupandulumline.add_updater(update_doupandulum)
        path = TrajectoryOnTime(
            doupandulumline.get_end, scene=self, life_time=2, stroke_color=YELLOW_M, fade_ratio=3)
        self.add(doupandulumline, path)
        self.wait(20)


class Scene08(Scene):
    def construct(self):
        codes = CodeLines(
            'class ObjectPoints(VGroup):',
            '~~~~CONFIG = {',
            '~~~~~~~~"scale_factor": 0.5,',
            '~~~~~~~~"color": WHITE,',
            '~~~~}',
            '~~~~def __init__(self, obj: VMobject, **kwargs):',
            '~~~~~~~~VGroup.__init__(self, **kwargs)',
            '~~~~~~~~for point in obj.get_all_points():',
            '~~~~~~~~~~~~dot_i = Dot(point, color=self.color).scale(self.scale_factor)',
            '~~~~~~~~~~~~self.add(dot_i)',
            t2c={'ObjectPoints': YELLOW_M, 'for': PINK_M, 'add': BLUE_M, '__init__': BLUE_M,
                 'set_color': BLUE_M, 'scale': BLUE_M, 'get_all_points': BLUE_M, 'kwargs': YELLOW_M,
                 'Dot': BLUE_M, 'scale_factor': WHITE_M}
        )
        codes[2][9:21].set_color(GREEN_M)
        codes[3][9:14].set_color(GREEN_M)
        codes[5][23:26].set_color(YELLOW_M)
        codes[7][18:20].set_color(PINK_M)
        codes[-2][31:36].set_color(YELLOW_M)
        self.play(FadeIn(codes))
        self.wait()
        self.play(codes.animate.to_edge(LEFT))
        self.wait()
        pentago = RegularPolygon(5, color=ORANGE_M).scale(1.5).shift(RIGHT * 3 + UP)
        self.play(ShowCreation(pentago))
        self.wait()
        pnts = ObjPoints(pentago, color=WHITE)
        self.play(Write(pnts))
        self.wait()
        codes2 = CodeLines(
            'class PointIndex(VGroup):',
            '~~~~CONFIG = {',
            '~~~~~~~~"scale_factor": 0.5,',
            '~~~~~~~~"color": WHITE,',
            '~~~~}',
            '~~~~def __init__(self, obj: VMobject, **kwargs):',
            '~~~~~~~~VGroup.__init__(self, **kwargs)',
            '~~~~~~~~for i, point in enumerate(obj.get_all_points()):',
            '~~~~~~~~~~~~index = Integer(i).move_to(point.get_center())',
            '~~~~~~~~~~~~index.scale(self.scale_factor).set_color(self.color)',
            '~~~~~~~~~~~~self.add(index)',
            t2c={'PointIndex': YELLOW_M, 'for': PINK_M, 'add': BLUE_M, '__init__': BLUE_M,
                 'set_color': BLUE_M, 'scale': BLUE_M, 'get_all_points': BLUE_M, 'kwargs': YELLOW_M,
                 'Dot': BLUE_M, 'scale_factor': WHITE_M, 'enumerate': PURPLE_M, 'move_to': BLUE_M,
                 'get_center': BLUE_M, 'Integer': BLUE_M}
        ).to_edge(LEFT)
        codes2[2][9:21].set_color(GREEN_M)
        codes2[3][9:14].set_color(GREEN_M)
        codes2[5][23:26].set_color(YELLOW_M)
        codes2[7][21:23].set_color(PINK_M)
        self.play(FadeOut(codes), FadeIn(codes2))
        self.wait()
        ind = AllPointsIndex(pentago, color=WHITE)
        self.play(ReplacementTransform(pnts, ind))
        self.play(
            pentago.animate.shift(UP * 0.5),
            UpdateFromFunc(ind, lambda a: a.become(AllPointsIndex(pentago, color=WHITE)))
        )
        center = np.array(pentago.get_center())
        all_points = np.array(pentago.get_all_points())
        pentago.save_state()

        def apply_points_shift(i, op):
            def update(obj: Mobject, alpha):
                assert (0 <= i < obj.get_num_points() // 3)
                obj.data['points'][3 * i: 3 * (i + 1)] = \
                    all_points[3 * i:3 * (i + 1)] + (all_points[3 * i + 1] - center) * 0.4 * alpha * op

            return update

        ind.add_updater(lambda a: a.become(AllPointsIndex(pentago, color=WHITE)))
        self.add(ind)
        self.play(
            LaggedStart(*[
                UpdateFromAlphaFunc(pentago, apply_points_shift(i, 1), run_time=0.4)
                for i in range(5)
            ], lag_ratio=0.4),
        )
        self.wait()
        self.play(
            Restore(pentago),
        )
        self.play(
            FadeOut(codes2, LEFT),
            pentago.animate.center()
        )
        self.wait()
        code_anim = CodeLine(
            'self.play(ApplyPointwiseFunction(np.exp, pentago))',
            t2c={'ApplyPointwiseFunction': BLUE_M, 'play': BLUE_M}
        ).next_to(pentago, DOWN).scale(0.8)
        self.play(FadeIn(code_anim, UP))
        self.play(
            ApplyPointwiseFunction(np.exp, pentago),
        )
        self.wait()


class Scene09(Scene):
    def construct(self):
        t1 = Text("操控锚点？", font=SOURCE, weight="MEDIUM")
        self.play(FadeIn(t1, DOWN))
        self.wait()
        t2 = CodeLine(
            'mob.',
            t2c={'points': GREEN_M, 'array': BLUE_M, 'mob': YELLOW_M}
        ).shift(LEFT * 5)
        t3 = RollingList2(
            CodeLine('data["points"]=np.array([...])', t2c={'points': GREEN_M, 'array': BLUE_M}),
            CodeLine('set_points(point_list)', t2c={'set_points': BLUE_M}),
            CodeLine('apply_points_function(func)', t2c={'apply_points_function': BLUE_M}),
            CodeLine('apply_complex_function(func)', t2c={'apply_complex_function': BLUE_M}),
            CodeLine('add_line_to(point)', t2c={'add_line_to': BLUE_M}),
            CodeLine('add_quadratic_bezier_curve_to(handle, anchor)', t2c={'add_quadratic_bezier_curve_to': BLUE_M}),
            CodeLine('set_points_as_corners(points)', t2c={'set_points_as_corners': BLUE_M}),
            CodeLine('reverse_points()', t2c={'reverse_points': BLUE_M}),
            transparent_ratio=0.05
        ).next_to(t2, RIGHT, aligned_edge=UP, buff=0.15)
        t3.refresh_color()
        self.play(FadeOut(t1, UP), FadeIn(t2, UP), FadeIn(t3, UP))
        self.wait()
        self.play(RollVerticallyTo2(t3, 1))
        self.wait()
        self.play(RollVerticallyTo2(t3, 2))
        self.wait()
        self.play(RollVerticallyTo2(t3, 4))
        self.wait()
        self.play(RollVerticallyTo2(t3, 6))
        self.wait()
        self.play(RollVerticallyTo2(t3, 7))
        self.wait()
        self.play(RollVerticallyTo2(t3, 0))
        self.wait()
        self.play(RollVerticallyTo2(t3, 7))
        self.wait()
        t2.save_state()
        t3.save_state()
        self.play(
            t2.animate.scale(10, about_point=LEFT * 5.6),
            t3.animate.scale(10, about_point=LEFT * 5.6),
        )
        self.wait()
        self.play(
            t2.set_stroke, {'width': 2},
            t2.set_fill, {'opacity': 0}
        )
        self.wait()
        ind = ObjPoints(t2)
        self.play(Write(ind), lag_ratio=0.7, run_time=4)
        self.wait()
        tips = VGroup(*[PathVector(obj, offset=0) for obj in t2])
        self.play(FadeOut(ind), FadeIn(tips))
        self.wait()

        # updater 会报 assertion error, 找不到原因, 就只能逐帧了
        # def update_tips(vmobject: VMobject):
        #     def update(obj, alpha):
        #         obj.become(
        #             PathVector(vmobject, offset=alpha / 8)
        #         )
        #
        #     return update

        for i in range(180):
            self.remove(tips)
            tips.become(
                VGroup(*[PathVector(obj, offset=i / 60 / 16) for obj in t2])
            )
            self.add(tips)
            self.wait(1 / 60)
        self.wait()
        self.play(
            tips.animate.become(
                VGroup(*[PathVector(obj, offset=1 / 8, reversed=-1) for obj in t2])
            )
        )
        for i in range(300):
            self.remove(tips)
            tips.become(
                VGroup(*[PathVector(obj, offset=i / 60 / 16, reversed=-1) for obj in t2])
            )
            self.add(tips)
            self.wait(1 / 60)
        self.wait()


class Scene10(Scene):
    def construct(self):
        rect = Rectangle(width=4, height=4, color=BLUE_M)
        hexagon = RegularPolygon(6, color=PURPLE_M).reverse_points()
        self.play(ShowCreation(rect))
        tips1 = PathVector(rect, 1 / 16)
        self.play(Write(tips1, lag_ratio=0.5))
        self.wait()
        self.play(ShowCreation(hexagon))
        tips2 = PathVector(hexagon, offset=1 / 16, vector_num=6)
        self.play(Write(tips2, lag_ratio=0.5))
        self.wait()
        self.remove(rect, hexagon)
        rect.append_points(hexagon.get_points())
        # rect.set_color_by_gradient(BLUE_M, PURPLE_M)
        self.add(rect)
        self.add(tips1, tips2)
        self.play(rect.set_fill, {'opacity': 1}, rect.set_stroke, {'width': 0})
        self.wait()
        t1 = Text('+凸包+布尔运算', font=SOURCE, weight="MEDIUM").scale(1.5).shift(RIGHT * 2.3)
        self.play(
            rect.animate.shift(LEFT * 3.6),
            tips1.animate.shift(LEFT * 3.6),
            tips2.animate.shift(LEFT * 3.6),
            FadeIn(t1, LEFT)
        )
        self.wait()


class Scene10_0(Scene):
    def construct(self):
        squ = Square(side_length=4, color=BLUE_M)
        heg = RegularPolygon(6, color=PURPLE_M).reverse_points()
        self.add(squ, heg)
        tips1 = PathVector(squ, offset=1 / 16, vector_num=8)
        tips2 = PathVector(heg, offset=1 / 16, vector_num=6)
        poly = Square(side_length=4, color=BLUE_M, stroke_width=1,
                      fill_opacity=1).append_points(heg.get_all_points())
        huge = Rectangle(color=PURPLE_M).scale(40).append_points(heg.get_all_points())
        self.add(huge, poly, tips1, tips2)
        self.play(FadeOut(poly))
        self.wait()
        self.play(squ.animate.set_fill(opacity=0.5), run_time=2, rate_func=there_and_back_with_pause)
        self.wait()
        self.play(huge.animate.set_fill(opacity=0.5), run_time=2, rate_func=there_and_back_with_pause)
        self.wait()
        self.add(poly, tips1, tips2)
        self.play(FadeIn(poly))
        self.wait()


class Scene11(Scene):
    def construct(self):
        t1 = VGroup(Text('The World!').scale(2).shift(UP * 0.8),
                    Text('時よ止まれ！', font=SOURCE, weight="BOLD").scale(1.5).shift(DOWN * 0.8))
        self.play(Write(t1))
        self.wait()

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

        def the_world(begin_points, end_points):
            def update_color(obj: VMobject, alpha):
                obj.set_points(
                    interpolate(
                        begin_points,
                        end_points,
                        alpha
                    )
                )
                # obj.apply_function(shrink_func)
                obj.set_color(Color(hsl=(alpha, 2 * alpha * (1 - alpha), 0.4)))
                obj.set_fill(opacity=1)

            return update_color

        begin_points = np.array(t1.get_all_points())
        end_points = np.array(fuhe_mul(begin_points))

        bg_rect = Rectangle(15, 9, fill_opacity=1, fill_color="#252525", stroke_width=1)
        cir1 = Annulus(inner_radius=1e-2, outer_radius=2e-2, stroke_width=0, fill_opacity=0.4, color=WHITE)
        cir2 = Annulus(inner_radius=3e-2, outer_radius=4e-2, stroke_width=0, fill_opacity=0.4, color=WHITE)
        cir0 = Circle(radius=5e-3, fill_opacity=1, color=WHITE, stroke_width=0)

        self.add(cir1, cir2, cir0, t1)
        self.play(
            ApplyMethod(cir0.scale, 5000),
            UpdateFromAlphaFunc(t1, the_world(begin_points, end_points)),
            AnimationGroup(
                ApplyMethod(cir1.scale, 5000),
                ApplyMethod(cir2.scale, 5000),
                lag_ratio=0.1
            ),
            run_time=1
        )
        self.add(bg_rect)
        self.add(cir1, cir2, cir0, t1)
        self.play(
            ApplyMethod(cir0.scale, 1 / 5000),
            UpdateFromAlphaFunc(t1, the_world(begin_points, end_points), rate_func=lambda t: smooth(1 - t)),
            AnimationGroup(
                ApplyMethod(cir1.scale, 1 / 5000),
                ApplyMethod(cir2.scale, 1 / 5000),
                lag_ratio=0.1
            ),
            run_time=1,
        )
        self.remove(cir1, cir2, cir0)
        self.wait()


class Scene12(Scene):
    def construct(self):
        numplane = NumberPlane()
        self.play(ShowCreation(numplane), lag_ratio=0.1, run_time=3)
        self.wait()

        def func(p):
            return p + np.array([np.sin(p[1]), np.sin(p[0]), 0])

        numplane.prepare_for_nonlinear_transform()
        t1 = Text('Function from Opening Manim Example').add_background_rectangle(BLACK, buff=0.2).to_edge(UP)
        self.play(Write(t1))
        self.play(ApplyPointwiseFunction(func, numplane), run_time=4, rate_func=there_and_back_with_pause)
        self.wait()
        self.play(
            t1.animate.become(
                Tex('z\\rightarrow \exp(z)').add_background_rectangle(BLACK, buff=0.2).to_edge(UP)
            )
        )
        self.play(numplane.apply_complex_function, np.exp, run_time=5, rate_func=there_and_back_with_pause)
        self.wait()
        self.play(
            t1.animate.become(
                Tex('z\\rightarrow z^{2}').add_background_rectangle(BLACK, buff=0.2).to_edge(UP)
            )
        )
        self.play(numplane.apply_complex_function, lambda z: z ** 2, run_time=5, rate_func=there_and_back_with_pause)
        self.wait()


class Scene10_1(Scene):
    def construct(self):
        gear = Gear_outline(tooth_hight=0.3, color=YELLOW_M)
        self.play(ShowCreation(gear))
        self.wait()
        self.play(gear.animate.scale(8, about_edge=UP))
        pnts = ObjPoints(gear)
        self.play(Write(pnts), lag_ratio=1, run_time=8)
        self.wait()


class Scene10_2(Scene):
    def construct(self):
        def cycloid(t):
            return np.array([t - np.sin(t), 1 - np.cos(t), 0])

        axes = Axes(x_range=[-1, 2 * PI + 1, 1], y_range=[-1, 3, 1], width=2 * PI + 2, height=4)
        labels = axes.get_axis_labels()
        axes.add(labels)
        self.play(Write(axes))
        self.wait()
        path = axes.get_parametric_curve(
            cycloid, t_range=[0, 2 * PI, 0.1],
            stroke_color=ORANGE_M
        )
        self.play(ShowCreation(path))
        self.wait()
        self.play(
            axes.animate.shift(LEFT * 3),
            path.animate.shift(LEFT * 3),
        )
        self.play(FadeOut(path))
        self.wait()
        t1 = CodeLines(
            'def cycloid(t):',
            '~~~~return np.array([',
            '~~~~~~~~t - np.sin(t),',
            '~~~~~~~~1 - np.cos(t), 0])',
            'v = VMobject().start_new_path(ORIGIN)',
            'n = 120',
            'for i in range(n):',
            '~~~~v.add_line_to(cycloid(i / n * TAU))',
            'v.close_path()',
            t2c={'in': PINK_M, 'close_path': BLUE_M, 'sin': BLUE_M, 'cos': BLUE_M, 'VMobject': BLUE_M, 'TAU': YELLOW_M,
                 'array': BLUE_M, 'add_line_to': BLUE_M, 'cycloid': BLUE_M, 'for': PINK_M, 'range': PURPLE_M,
                 'start_new_path': BLUE_M, 'ORIGIN': YELLOW_M}
        ).to_corner(UR)
        t1[0][4:11].set_color(TEAL_M)
        t1[0][-3].set_color(YELLOW_M)
        self.play(FadeIn(t1))
        v = VMobject(color=ORANGE_M).start_new_path(axes.c2p(0, 0))
        n = 120
        for i in range(n):
            pos = cycloid(i / n * TAU)
            self.play(v.animate.add_line_to(axes.c2p(pos[0], pos[1])), run_time=0.03, rate_func=linear)
        self.play(v.animate.close_path())
        self.wait()
        t2 = CodeLines(
            'def cycloid(t):',
            '~~~~return np.array([',
            '~~~~~~~~t - np.sin(t),',
            '~~~~~~~~1 - np.cos(t), 0])',
            'v = ParametricCurve(',
            '~~~~cycloid, ',
            '~~~~t_range=[0, TAU, 0.1]',
            ')',
            'v.close_path()',
            t2c={'in': PINK_M, 'close_path': BLUE_M, 'sin': BLUE_M, 'cos': BLUE_M, 'TAU': YELLOW_M,
                 'array': BLUE_M, 'add_line_to': BLUE_M,
                 'ParametricCurve': BLUE_M, 't_range': YELLOW_M}
        ).to_corner(UR).shift(LEFT * 1.5)
        t2[0][4:11].set_color(TEAL_M)
        t2[0][-3].set_color(YELLOW_M)
        self.play(FadeTransformPieces(t1, t2), FadeOut(v))
        self.wait()
        path.close_path()
        self.play(ShowCreation(path))
        self.wait()


class Scene10_3(Scene):
    def construct(self):
        star = RegularPolygon(4, color=BLUE_M).scale(2)
        self.play(ShowCreation(star))
        self.play(star.animate.shift(LEFT * 3))
        pnts = ObjPoints(star)
        self.play(Write(pnts))
        pnts.add_updater(
            lambda a: a.become(ObjPoints(star))
        )
        self.add(pnts)
        codes = CodeLines(
            'star = RegularPolygon(4)',
            'ratio = 0.9',
            'star.data["points"][1::3] -= \\',
            '~~~~star.data["points"][1::3] * ratio',
            t2c={'RegularPolygon': BLUE_M, 'points': GREEN_M}
        ).to_edge(RIGHT, buff=1.5)
        self.play(FadeIn(codes, LEFT))
        self.wait()

        def move_points(obj, alpha):
            for i in range(obj.get_num_curves()):
                obj.data['points'][1 + 3 * i] -= (obj.data['points'][1 + 3 * i] - LEFT * 3) * alpha * 0.08

        self.play(UpdateFromAlphaFunc(star, move_points))
        self.wait()


class Blog01(Scene):
    def construct(self):
        arc0 = Arc(0, TAU * 3 / 4, radius=3, stroke_width=1)
        t = TAU * 3 / 4 / 8 / 2
        self.add(arc0)
        dots = VGroup(
            *[Dot(arc0.pfp(i / 16), color=YELLOW).scale(0.5) for i in range(17)]
        )
        sample = Text("Samples", size=48).to_corner(DR)
        sample1 = Tex(r"\theta=\frac{\mathrm{angle}}{\mathrm{n\_components}}").to_corner(DR)
        sample2 = CodeLine("samples[1::2] /= np.cos(theta / 2)", size=30,
                           t2c={"cos": BLUE_M}
                           ).to_corner(DR)
        self.play(Write(dots), Write(sample))
        lines = VGroup(
            *[Line(ORIGIN, dots[2 * i], color=YELLOW_M, stroke_width=2) for i in range(9)]
        )
        self.wait()
        self.play(ShowCreation(lines))
        theta = VGroup(
            Angle(dots[0], Dot(ORIGIN), dots[2]),
            Tex("\\theta")
        )
        theta[1].next_to(theta[0], RIGHT)
        self.play(Write(theta), FadeTransform(sample, sample1))
        self.wait()
        dots.generate_target()
        for i in range(8):
            dots.target[2 * i + 1].move_to(dots[2 * i + 1].get_center() / np.cos(t))
        self.play(*[
            WiggleOutThenIn(dots[i], scale_value=6)
            for i in range(1, 17, 2)
        ])
        self.play(
            MoveToTarget(dots),
            FadeTransform(sample1, sample2)
        )
        self.wait()
        points1 = VGroup(dots[0:-1:2].copy())
        points2 = VGroup(dots[1::2].copy().set_color(ORANGE_M))
        points3 = VGroup(dots[2::2].copy().set_color(RED_M))

        roll = RollingList2(
            CodeLine("points[0::3] = samples[0:-1:2]", size=30),
            CodeLine("points[1::3] = samples[1::2]", size=30),
            CodeLine("points[2::3] = samples[2::2]", size=30),
            transparent_ratio=0.2
        ).to_corner(DR)
        roll.refresh_color()

        self.play(dots.animate.set_opacity(0.1), FadeOut(lines), FadeOut(theta), FadeOut(sample2))
        self.play(FadeIn(points1, scale=0.8), FadeIn(roll, UP))
        self.wait()
        self.play(FadeIn(points2, scale=0.8), RollVerticallyTo2(roll, 1))
        self.wait()
        self.play(FadeIn(points3, scale=0.8), RollVerticallyTo2(roll, 2))
        self.wait()

        arc1 = Arc(0, TAU * 3 / 4, radius=3, color=YELLOW)
        self.play(ShowCreation(arc1))
        self.wait()


class Blog02(Scene):
    def construct(self):
        a = Circle(radius=3, color=BLUE_M)
        a.append_points(Circle(radius=1.5, color=BLUE_M).reverse_points().get_all_points())
        a.set_fill(opacity=0.5)
        p = AllPointsIndex(a, color=WHITE)
        self.add(a, p)


class BlogZH(Scene):
    def construct(self):
        t = Text("""Vectorized Math Object
          in Manim""").set_width(14)
        self.add(t)
