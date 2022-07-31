from manimlib.imports import *
from manim_sandbox.utils.imports import *


class Scene01(DarkScene):
    def construct(self):
        title1 = TextMobject("updater教程").scale(2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("重制版").scale(1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title3 = TextMobject("Episode 1").scale(2).shift(UP * 0.5).to_edge(LEFT)
        title4 = TextMobject("从矢量到updater").scale(1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title4[0][1:3].set_color(YELLOW)
        title4[0][4:].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        title1.add_updater(anim)
        title2.add_updater(anim)
        anim1 = Write(title1)
        anim2 = Write(title2)
        anim3 = Write(title3)
        anim4 = Write(title4)
        self.wait()
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait(0.4)
        self.wait(2)
        title1.clear_updaters()
        title2.clear_updaters()
        title3.add_updater(anim)
        title4.add_updater(anim)
        self.add(title3, title4)
        turn_animation_into_updater(anim3)
        turn_animation_into_updater(anim4)
        self.play(title1.shift, UP * 5,
                  title1.scale, 0.5,
                  title2.shift, DOWN * 5,
                  title2.scale, 0.5)
        self.wait(3)


class Scene02(DarkScene):
    def construct(self):
        t1 = TextMobject("前置知识").scale(2).set_fill(opacity=0).set_stroke(opacity=1, width=1.5)
        t0 = t1.copy().set_fill(opacity=0)
        for j in range(len(t0[0])):
            for i in range(len(t0[0][j].points)):
                t0[0][j].points[i] = np.array([
                    2.5 * np.random.randn(),
                    1.3 * np.random.randn(), 0
                ])
        self.play(ShowCreation(t0), lag_ratio=0.1, rate_func=linear)
        self.play(ReplacementTransform(t0, t1), lag_ratio=0.1, run_time=2)
        self.wait()
        t2 = TextMobject("1. 矢量图").scale(2).shift(UP * 0.5).to_edge(LEFT)
        t3 = TextMobject("Vector").scale(1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        anim2 = Write(t2)
        anim3 = Write(t3)

        def anim_to_center(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        t2.add_updater(anim_to_center)
        t3.add_updater(anim_to_center)
        self.add(t2, t3)
        turn_animation_into_updater(anim2)
        turn_animation_into_updater(anim3)
        self.play(FadeOut(t1))
        self.wait(2)


class Scene03(DarkScene):
    def construct(self):
        o1 = Line(np.array([-3, -2, 0]), np.array([3, 2, 0]), color=ORANGE)
        o2 = ParametricFunction(lambda t: np.array([t, 2 * np.sin(t), 0]), t_min=-PI, t_max=PI, stroke_color=YELLOW)
        o3 = Circle().scale(2)
        o4 = Polygon(
            np.array([-2, -2, 0]),
            np.array([2, -2, 0]),
            np.array([1, 2, 0])
        )
        t0 = Triangle(color=WHITE, fill_opacity=1)
        t0.set_height(0.4, stretch=True).shift(DOWN * 3)
        t0.set_width(0.5)
        group = VGroup(o1, o2, o3, o4)
        group[1:].set_stroke(opacity=0.2)
        group.arrange(RIGHT, buff=1)
        group.to_edge(LEFT, buff=4.1)
        self.play(FadeInFrom(group, DOWN * 0.5), lag_ratio=0.9)
        self.play(Write(t0))
        self.wait()
        self.play(group.shift, LEFT * (4 + PI),
                  group.set_stroke, {"opacity": 0.2},
                  group[1].set_stroke, {"opacity": 1},
                  group[1].shift, LEFT * (4 + PI),
                  )
        self.wait()
        self.play(group.shift, LEFT * 6,
                  group.set_stroke, {"opacity": 0.2},
                  group[2].set_stroke, {"opacity": 1},
                  group[2].shift, LEFT * 6,
                  )
        self.wait()
        self.play(group.shift, LEFT * 5,
                  group.set_stroke, {"opacity": 0.2},
                  group[3].set_stroke, {"opacity": 1},
                  group[3].shift, LEFT * 5,
                  )
        self.wait()
        t1 = Text("矢量图形", font="庞门正道标题体").scale(5).move_to(DOWN * 0.5)
        t2 = Text("VMobject", font="庞门正道标题体").scale(4).next_to(t1, DOWN)
        self.play(FadeOut(t0),
                  group.scale, 0.55,
                  group.move_to, UP * 2.1,
                  group.set_stroke, {"opacity": 1},
                  FadeInFrom(t1, DOWN),
                  FadeInFrom(t2, DOWN),
                  lag_ratio=0.2,
                  rate_func=sine,
                  run_time=2
                  )
        self.wait()
        groupall = VGroup(o1, o2, o3, o4, t1, t2)
        # groupall.save_state()
        tracker = ValueTracker(1.0)
        dec = DecimalNumber(1.0)
        dec.move_to(UP * 3.2 + RIGHT * 5).add_updater(lambda a: a.set_value(tracker.get_value()))
        t3 = TextMobject("Scale").next_to(dec, LEFT)
        self.play(Write(t3), Write(dec))
        self.play(groupall.shift, (DOWN + RIGHT * 1.68) * 10,
                  groupall.scale, 10,
                  tracker.set_value, 10,
                  run_time=3)
        self.wait()
        groupall.remove(o1, o3, o4, t1, t2)
        self.play(groupall.scale, {"scale_factor": 10, "about_point": ORIGIN},
                  groupall.shift, DOWN * 5.5,
                  tracker.set_value, 100,
                  run_time=3)
        self.wait()
        self.play(groupall.scale, {"scale_factor": 10, "about_point": ORIGIN},
                  groupall.shift, DOWN * 7.5,
                  tracker.set_value, 1000,
                  run_time=3)
        self.wait()
        dec.clear_updaters()
        self.play(groupall.scale, 0.1,
                  groupall.shift, UP * 10,
                  t1.scale, 0.2,
                  t1.move_to, ORIGIN,
                  FadeOut(dec), FadeOut(t3),
                  rate_func=sine,
                  run_time=3)
        self.wait()
        self.play(t1.set_stroke, {"opacity": 1, "color": WHITE, "width": 2},
                  t1.set_fill, {"opacity": 0},
                  t1.scale, 2,
                  t1.shift, RIGHT * 3,
                  rate_func=sine,
                  )
        pts = ObjPoints(t1, color=ORANGE)
        self.play(FadeIn(pts))
        self.wait()


class Scene04(DarkScene):
    def construct(self):
        cir1 = Circle(radius=2.5)
        cir1.set_stroke(BLUE)
        cir2 = Circle(radius=2.5).set_stroke(width=0)
        cir2.set_fill(PURPLE_D, opacity=1)
        cir = VGroup(cir2, cir1)
        self.play(Write(cir))
        self.wait()
        t1 = Text("线条", font="庞门正道标题体", color="#999").scale(2).shift(RIGHT * 3 + UP)
        t2 = Text("图块", font="庞门正道标题体", color="#999").scale(2).shift(RIGHT * 3 + DOWN)
        self.play(cir.shift, LEFT * 2,
                  FadeInFrom(t1, LEFT),
                  FadeInFrom(t2, LEFT),
                  )
        self.wait()
        self.play(cir1.scale, {"scale_factor": 1.1},
                  t1.set_fill, {"color": WHITE},
                  t2.set_fill, {"color": DARK_GREY},
                  rate_func=there_and_back_with_pause,
                  run_time=2
                  )
        self.wait()
        self.play(cir2.become, cir2.copy().scale(0.9).set_fill(PURPLE_A),
                  t2.set_fill, {"color": WHITE},
                  t1.set_fill, {"color": DARK_GREY},
                  rate_func=there_and_back_with_pause,
                  run_time=2
                  )
        self.wait()
        self.play(t1.shift, UP * 2, t2.shift, UP * 4 + RIGHT * 2.5)
        self.play(t1.set_fill, WHITE, t2.set_fill, WHITE)
        t2c = {
            "xml": "#D86066",
            "?": "#60B4B4",
            "svg": "#D86066",
            "<": "#60B4B4",
            ">": "#60B4B4",
            "path": "#D86066",
            "style": "#C695C6",
            " d": "#D86066",
            "use": "#D86066",
            "g": "#D86066",
            "/": "#60B4B4",
            '"': "#60B4B4",
            "...": "#99C794",
            "surface21": "#99C794",
            "=": "#A6ACB9",
            "id": "#C695C6"
        }
        t_path = Text('<path style="..." d="...">',
                      font="Fira Code Medium", t2c=t2c).scale(0.6)
        t_path.next_to(VGroup(t1, t2), DOWN, buff=1.8)
        t_graphic = VGroup(
            Text(r'<g id="surface21">', font="Fira Code Medium", t2c=t2c).scale(0.6),
            Text(r'<g style="...">', font="Fira Code Medium", t2c=t2c).scale(0.6),
            Text(r'  <use ...>', font="Fira Code Medium", t2c=t2c).scale(0.6),
            Text(r'</g>', font="Fira Code Medium", t2c=t2c).scale(0.6),
            Text(r'</g>', font="Fira Code Medium", t2c=t2c).scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT)
        t_graphic.next_to(t_path, DOWN, aligned_edge=LEFT)

        t_ign = Text("...", font="Fira Code Medium", t2c=t2c).scale(0.6) \
            .next_to(t_graphic, DOWN, aligned_edge=LEFT)
        t_ign0 = t_ign.copy().next_to(t_path, UP, aligned_edge=LEFT)
        t_svg = Text("<svg ...>", font="Fira Code Medium", t2c=t2c).scale(0.6) \
            .next_to(t_ign0, UP, aligned_edge=LEFT)
        t_svge = Text("</svg>", font="Fira Code Medium", t2c=t2c).scale(0.6) \
            .next_to(t_ign, DOWN, aligned_edge=LEFT)

        t_xml = Text("<?xml...?>", font="Fira Code Medium", t2c=t2c).scale(0.6) \
            .next_to(t_svg, UP, aligned_edge=LEFT)
        t_group = VGroup(
            t_xml, t_svg, t_svge, t_ign, t_ign0
        )
        self.play(TransformFromCopy(t1, t_path))
        self.wait()
        self.play(TransformFromCopy(t2, t_graphic))
        self.wait()
        self.play(*[FadeInFrom(obj, obj.get_center() - np.array([obj.get_center()[0], 0, 0]))
                    for obj in t_group],
                  lag_ratio=0.2)
        self.wait()


class Scene06(DarkScene):
    def construct(self):
        squ = Square(side_length=4, color=BLUE)
        ptx = ObjPoints(squ, color=WHITE)
        self.play(Write(squ), FadeIn(ptx))
        self.wait()

        def func1(obj):
            obj.points[5:7] += RIGHT * 1 / self.camera.frame_rate
            ptx[5:7].shift(RIGHT * 1 / self.camera.frame_rate)

        def func2(obj):
            obj.points[13:15] += LEFT * 1 / self.camera.frame_rate
            ptx[13:15].shift(LEFT * 1 / self.camera.frame_rate)

        self.play(UpdateFromFunc(squ, func1))
        self.wait()
        self.play(UpdateFromFunc(squ, func2))
        self.wait()


class Scene07(Scene):
    def construct(self):
        t2c = {
            ",": GREY,
            "(": GOLD_A,
            ")": GOLD_A
        }
        # img = ImageMobject("./my_projects/new/tu01-png.png")
        text = Text("rgba(197,116,255,255)", t2c=t2c, font="Consolas")
        text[0:4].set_color(YELLOW_A)
        text[5:8].set_color("#ff0000")
        text[9:12].set_color("#00ff00")
        text[13:16].set_color("#0000ff")
        text.add_background_rectangle("#222", 0.75, buff=0.3)
        # self.add(img)
        self.play(Write(text))
        self.wait()


class Scene07_1(DarkScene):
    def construct(self):
        net = VGroup()
        for i in range(10):
            for j in range(10):
                net.add(Square(side_length=0.5, stroke_width=1).move_to(np.array([i / 2, j / 2, 0])),
                        )
        net.move_to(ORIGIN)
        net.rotate(PI / 2, about_point=ORIGIN)
        net[3:7].set_fill(BLUE, opacity=0.6)
        net[93:97].set_fill(BLUE, opacity=0.6)
        net[30:70:10].set_fill(BLUE, opacity=0.6)
        net[39:79:10].set_fill(BLUE, opacity=0.6)
        for obj in [net[12], net[21], net[17], net[28],
                    net[71], net[82], net[78], net[87]]:
            obj.set_fill(BLUE, opacity=0.6)
        self.play(WriteRandom(net))
        self.play(net.shift, LEFT * 2.5)
        t0 = TextMobject("circle.png").shift(RIGHT * 3 + UP)
        self.play(Write(t0))
        self.wait()
        self.play(TransformFromCopy(net, VGroup(*[Dot(RIGHT * 3 + DOWN * 0.2) for i in range(100)])),
                  lag_ratio=0.03, run_time=5, rate_func=sine)
        self.wait()


class Scene08(DarkScene):
    def construct(self):
        t1 = TextMobject("2. 插值").scale(2).shift(UP * 0.5).to_edge(LEFT)
        t2 = TextMobject("interpolate").scale(1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        anim1 = Write(t1)
        anim2 = Write(t2)

        def anim_to_center(obj, dt):
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        t1.add_updater(anim_to_center)
        t2.add_updater(anim_to_center)
        self.add(t1, t2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait(3)
        t1.clear_updaters()
        t2.clear_updaters()
        t3 = TextMobject("图像image").scale(2).shift(UP * 0.5).to_edge(LEFT)
        t4 = TextMobject("坐标coordinate").scale(1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        t3.add_updater(anim_to_center)
        t4.add_updater(anim_to_center)
        anim3 = Write(t3)
        anim4 = Write(t4)
        self.add(t3, t4)
        turn_animation_into_updater(anim3)
        turn_animation_into_updater(anim4)
        self.play(t1.shift, UP * 5,
                  t2.shift, DOWN * 5,
                  run_time=2)
        self.wait()
        t3.clear_updaters()
        t4.clear_updaters()
        bk = Rectangle(width=FRAME_WIDTH, height=3,
                       stroke_width=0, fill_color=BLACK,
                       fill_opacity=0.75)
        t5 = Text("STATIC静态", font="庞门正道标题体", stroke_width=1, stroke_color=BLACK).scale(3)
        self.play(FadeIn(bk), Write(t5))
        self.wait()
        t6 = Text("DYNAMIC动态", font="庞门正道标题体", stroke_width=1, stroke_color=BLACK).scale(3).to_edge(DOWN, buff=1)
        self.play(FadeOut(t3), FadeOut(t4), FadeOut(bk), FadeInFrom(t6, UP), t5.to_edge, UP, 1)
        self.wait()
        self.play(TransformFromCopy(t5, t6.copy()),
                  rate_func=linear, run_time=2)
        self.wait()


class Scene10(DarkScene):
    def construct(self):
        text0 = VGroup(
            Text("补", font="庞门正道标题体").scale(2),
            Text("间", font="庞门正道标题体").scale(2),
            Text("动", font="庞门正道标题体").scale(2),
            Text("画", font="庞门正道标题体").scale(2),
        ).arrange(RIGHT).set_color(YELLOW_A)
        text0.move_to(ORIGIN)
        self.add(text0)
        self.wait()
        self.play(text0.arrange, DOWN,
                  text0.shift, LEFT)
        self.wait()
        text1 = VGroup(
            Text("足图像中", font="庞门正道标题体").scale(1.2),
            Text("过程的", font="庞门正道标题体").scale(1.2),
        )
        text1[0].next_to(text0[0], RIGHT, aligned_edge=DOWN)
        text1[1].next_to(text0[1], RIGHT, aligned_edge=DOWN)
        self.play(Write(text1), lag_ratio=0.2)
        self.wait()


class Scene11(DarkScene):
    def construct(self):
        texta = TexMobject("A").move_to(LEFT * 3 + DOWN)
        textb = TexMobject("B").move_to(RIGHT * 3 + DOWN)
        sqa = DashedVMobject(Square(side_length=1.2, color=GREY)).next_to(texta, UP).scale(1.05)
        sqb = DashedVMobject(Square(side_length=1.2, color=GREY)).next_to(textb, UP).scale(1.05)
        squ = Square(side_length=1.2, color=BLUE, fill_opacity=1).next_to(texta, UP)
        squ.set_sheen(0.5, UL)
        self.play(ShowCreation(sqa), ShowCreation(sqb))
        self.play(Write(texta), Write(textb))
        self.play(FadeIn(squ))
        self.wait()
        arr = Line(texta.get_center(), textb.get_center(), buff=0.3).add_tip(tip_look=1)
        self.play(ShowCreation(arr))
        self.wait()
        self.play(squ.shift, RIGHT * 6, rate_func=linear, run_time=2)
        group_all = VGroup(texta, textb, sqa, sqb, squ, arr)
        self.wait()
        code = VGroup(
            CodeLine("def "),
            CodeLine("interpolate"),
            CodeLine("(start, end, alpha):"),
            CodeLine("return (1 - alpha) * start + alpha * end")
        ).arrange(RIGHT, buff=0.1)
        code[3].next_to(code[0], DR, buff=0.1)
        code.move_to(ORIGIN)
        self.play(group_all.shift, UP * 2, FadeInFrom(code, DOWN))
        self.wait()
        self.play(squ.shift, LEFT * 6)
        self.wait()
        t_alpha = TexMobject("\\alpha=").move_to(DOWN * 1.15 + RIGHT * 2.2)
        dec = DecimalNumber(0.0).next_to(t_alpha, RIGHT)
        tri = Triangle(fill_opacity=1, color=YELLOW).scale(0.1).rotate(PI) \
            .add_updater(lambda a: a.next_to(squ, UP))
        squ.save_state()
        axes = Axes(
            x_min=-0.1, x_max=2.51, y_min=-0.1, y_max=2.51,
        ).shift(DOWN * 3 + LEFT * 4.2)
        alb_0 = TexMobject("O").next_to(axes, DL, buff=0).scale(0.8)
        alb_x1 = TexMobject("1").scale(0.8).next_to(alb_0, RIGHT, buff=2.2)
        alb_y1 = TexMobject("1").scale(0.8).next_to(alb_0, UP, buff=2.1)

        l_start = Line(np.array([-4.2, -1, 0]), np.array([-2.2, -3, 0]), color="#60B4B4")
        l_end = Line(np.array([-4.2, -3, 0]), np.array([-2.2, -1, 0]), color="#FAB763")
        lb_start = VGroup(Line(LEFT, ORIGIN, color="#60B4B4"),
                          TextMobject("start权重")).arrange(RIGHT).scale(0.7).next_to(l_end, buff=0.8, aligned_edge=UP)
        lb_end = VGroup(Line(LEFT, ORIGIN, color="#FAB763"),
                        TextMobject("end权重")).arrange(RIGHT).scale(0.7).next_to(lb_start, DOWN, aligned_edge=LEFT)

        l_squ = Line(sqa.get_center(), sqb.get_center(), color="#FA9044")

        def anim(obj, alpha):
            obj.restore()
            obj.shift(6 * RIGHT * alpha)
            dec.set_value(alpha)

        self.play(Write(t_alpha), Write(dec), ShowCreation(tri), ShowCreation(axes),
                  Write(alb_0), Write(alb_x1), Write(alb_y1))
        self.play(Write(lb_start), Write(lb_end))
        self.wait()
        self.play(UpdateFromAlphaFunc(squ, anim),
                  ShowCreation(l_start), ShowCreation(l_end),
                  ShowCreation(l_squ),
                  rate_func=linear, run_time=3)
        self.wait()
        title = Text("线性插值", font="庞门正道标题体").scale(3).next_to(lb_end, DOWN, aligned_edge=LEFT)
        write_t = DrawBorderThenFill(title)
        pos = title.get_center()
        title.shift(DOWN * 3)
        title.add_updater(lambda a, dt: a.shift((-title.get_center() + pos) * dt * 2))
        self.add(title)
        turn_animation_into_updater(write_t)
        self.wait(3)


class Scene13(DarkScene):
    def construct(self):
        t1 = TextMobject("3. 对象").scale(2).shift(UP / 2).to_edge(LEFT)
        t2 = TextMobject("Object").scale(1.5).shift(DOWN / 2).to_edge(RIGHT)
        anim1 = Write(t1)
        anim2 = Write(t2)

        def anim_to_center(obj, dt):
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        t1.add_updater(anim_to_center)
        t2.add_updater(anim_to_center)
        self.add(t1, t2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait(3)


class Scene14(DarkScene):
    def construct(self):
        t_c = TextMobject("C").scale(6)
        b_c = BackgroundRectangle(t_c, fill_color="#1f252A", fill_opacity=1) \
            .set_width(8, stretch=True, about_edge=RIGHT)

        t_1 = TextMobject("面向过程").scale(1.2).align_to(b_c, LEFT)
        t_2 = TextMobject("Procedure Oriented").next_to(t_1, DOWN, aligned_edge=LEFT)
        self.add(t_1, t_2, b_c)
        self.play(Write(t_c))
        self.wait()
        self.play(t_c.shift, LEFT * 2.4, b_c.shift, LEFT * 2.4,
                  t_1.shift, RIGHT * 6, t_2.shift, RIGHT * 6)
        self.wait()
        self.remove(b_c)
        t_p = TextMobject("Python").scale(3).shift(DOWN * 8)
        b_c2 = BackgroundRectangle(t_p, fill_color="#1f252A", fill_opacity=1)
        t_3 = TextMobject("面向对象").scale(1.2).align_to(b_c2, UL)
        t_4 = TextMobject("Object Oriented").next_to(t_3, DOWN, aligned_edge=LEFT)

        self.add(t_3, t_4, b_c2, t_p)
        self.play(t_c.shift, UP * 8, t_1.shift, UP * 8, t_2.shift, UP * 8,
                  t_p.shift, UP * 8)
        self.wait()
        for obj in [t_3, t_4, b_c2]:
            obj.shift(UP * 8)
        self.play(t_p.shift, UP * 0.8, b_c2.shift, UP * 0.8,
                  t_3.shift, DOWN * 0.8, t_4.shift, DOWN * 0.8)
        self.wait()


class Scene15(DarkScene):
    def construct(self):
        t_i = VGroup(CodeLine("digit x"),
                     CodeLine("String ss"),
                     CodeLine("class MyBox ... box"),
                     CodeLine("function gcd(...)")
                     ).arrange(DOWN, aligned_edge=LEFT).scale(1.5)
        t_i.move_to(ORIGIN)
        t_t = VGroup(
            Text("皆", font="庞门正道标题体"),
            Text("为", font="庞门正道标题体"),
            Text("对", font="庞门正道标题体"),
            Text("象", font="庞门正道标题体")) \
            .arrange(DOWN, buff=0.19).scale(1.5).align_to(t_i, UL)
        b_c = BackgroundRectangle(t_i, fill_color="#1f252A", fill_opacity=1)
        self.add(t_t, b_c)
        self.play(Write(t_i))
        self.wait()
        self.play(b_c.shift, RIGHT * 0.4, t_i.shift, RIGHT * 0.4, t_t.shift, LEFT * 0.4)
        self.wait()
        self.remove(b_c)

        code1 = VGroup(
            CodeLine("self.play(obj.shift(UP))"),
            CodeLine("self.play(obj.shift, UP)"),
        ).scale(1.5).arrange(DOWN, aligned_edge=LEFT).move_to(UP * 1.3)
        code1[0][14:19].set_color("#569CD6")
        code2 = VGroup(
            CodeLine("mob.add_updater(anim(mob))"),
            CodeLine("mob.add_updater(anim)")
        ).scale(1.5).arrange(DOWN, aligned_edge=LEFT) \
            .next_to(code1, DOWN, buff=1, aligned_edge=LEFT)
        code2[0][16:20].set_color("#569CD6")
        cross1 = Cross(code1[0]).set_stroke(opacity=0.5)
        cross2 = Cross(code2[0]).set_stroke(opacity=0.5)
        t_d1 = Text("传入函数对象", font="庞门正道标题体", color=GREEN).next_to(code1[1], RIGHT, buff=-1)
        t_d2 = t_d1.copy().next_to(code2[1], RIGHT, buff=-1)
        tx1 = Text("传入实例", font="庞门正道标题体", color=RED).next_to(code1[0], RIGHT, buff=-1)
        tx2 = Text("传入实例", font="庞门正道标题体", color=RED).next_to(code2[0], RIGHT, buff=-1)
        self.play(FadeInFrom(code1, UP), FadeInFrom(code2, DOWN),
                  *[FadeOutAndShift(t_i[i], np.array([0, -t_i[i].get_center()[1], 0])) for i in range(len(t_i))],
                  *[FadeOutAndShift(t_t[i], np.array([0, -t_t[i].get_center()[1], 0])) for i in range(len(t_t))])
        self.wait()
        self.play(ShowCreation(cross1), ShowCreation(cross2),
                  lag_ratio=0.1)
        self.wait()
        self.play(code1.shift, LEFT * 1.5, code2.shift, LEFT * 1.5,
                  cross1.shift, LEFT * 1.5, cross2.shift, LEFT * 1.5,
                  FadeInFrom(t_d1, LEFT), FadeInFrom(t_d2, LEFT),
                  FadeInFrom(tx1, LEFT), FadeInFrom(tx2, LEFT),
                  )
        self.wait()


class Scene16(DarkScene):
    def construct(self):
        t1 = TextMobject("*. 引入概念").scale(2).shift(UP / 2).to_edge(LEFT)
        t2 = TextMobject("target").scale(1.7).shift(DOWN * 0.5).to_edge(RIGHT)
        anim1, anim2 = Write(t1), Write(t2)

        def anim_to_center(obj, dt):
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        t1.add_updater(anim_to_center)
        t2.add_updater(anim_to_center)
        self.add(t1, t2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait(3)


class Scene17(DarkScene):
    def construct(self):
        t1 = CodeLine("math_object")
        t2 = CodeLine("mobject")
        t3 = CodeLine(".generate_target()").next_to(t2, buff=0.1)
        self.play(Write(t1))
        self.wait()
        self.play(ReplacementTransform(t1, t2))
        self.play(FadeInFrom(t3, LEFT))
        self.wait()


class SceneFinal(DarkScene):
    def construct(self):
        t0 = Text("动画：", font="庞门正道标题体")
        t1 = Text("manim-cairo-backend", font="Fira Code Medium")
        t2 = Text("manim-shaders", font="Fira Code Medium")
        t3 = Text("movy.js", font="Fira Code Medium")
        t_n = VGroup(t0, t1, t2, t3).arrange(DOWN,aligned_edge=LEFT)\
            .set_color_by_gradient(RED_B,ORANGE, GOLD, YELLOW).move_to(ORIGIN)
        self.play(Write(t_n))
        self.wait(3)

        
