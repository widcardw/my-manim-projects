from manimlib.imports import *
# 两个物件交换


class swap_test(Scene):
    def construct(self):
        text1 = Text("红", font="Microsoft YaHei", color=RED).move_to(LEFT*3)
        text2 = Text("蓝", font="Microsoft YaHei", color=BLUE).move_to(RIGHT*3)

        self.add(text1, text2)
        self.wait(1)
        self.play(Swap(text1, text2))
        self.wait(1)
# 物件旋转


class TestRotation(Scene):
    def construct(self):
        square = Square(side_length=2, color=BLUE)

        self.add(square)
        self.play(Rotate(square, 180*DEGREES,
                         about_point=np.array([1, 1, 0]), run_time=3))
        self.wait(2)
# 创建三角形&突出抖动


class TestTriangle(Scene):
    def construct(self):
        triangle1 = Polygon(np.array([-2, -1, 0]),
                            np.array([2, -1, 0]), np.array([2, 2, 0]))

        self.play(ShowCreation(triangle1))
        self.play(WiggleOutThenIn(triangle1))
        self.wait(2)
# 实线，虚线


class TypicalLines(Scene):
    def construct(self):
        line1 = Line(np.array([-2, 2, 0]), np.array([2, 2, 0])).set_color(BLUE)
        line2 = DashedLine(np.array([-2, -2, 0]),
                           np.array([2, -2, 0])).set_color(RED)

        self.play(ShowCreation(line1))
        self.play(ShowCreation(line2))
        self.wait(2)
# 圆弧，从x轴正方向开始


class TestArc(Scene):
    CONFIG = {
        "theta": PI/2,
        "line_size": 3.5,
        "increment_theta": PI/2,
        "final_theta": PI,
        "radius": 0.7
    }

    def construct(self):
        theta = ValueTracker(self.theta)
        line1 = Line(ORIGIN, RIGHT*self.line_size, color=ORANGE)
        line2 = Line(ORIGIN, RIGHT*self.line_size, color=PINK)
        line2.rotate(theta.get_value(), about_point=ORIGIN)
        line2.add_updater(
            lambda m: m.set_angle(theta.get_value())
        )
        arc1 = Arc(radius=self.radius, start_angle=line1.get_angle(),
                   angle=line2.get_angle(),
                   color=YELLOW)

        self.play(*[ShowCreation(obj)for obj in [line1, line2, arc1]])
        arc1.add_updater(
            lambda m: m.become(
                Arc(
                    radius=self.radius,
                    start_angle=line1.get_angle(),
                    angle=line2.get_angle(),
                    color=YELLOW,
                )
            )
        )
        self.add(arc1)
        self.play(theta.increment_value, self.increment_theta)
        self.wait(1)
# for循环测试


class TestForCirculation(Scene):
    def construct(self):

        for i in range(16):
            doti = Dot().to_edge(LEFT, buff=i)
            self.play(DrawBorderThenFill(doti), run_time=0.2)
# 图层


class TestLayer(Scene):

    def construct(self):
        square1 = Square(side_length=2).set_color(WHITE)
        square2 = Square(side_length=1).set_color(BLUE)
        circle1 = Circle(radius=2, stroke_width=0,
                         fill_color=RED, fill_opacity=0)

        self.play(ShowCreation(circle1), ShowCreation(
            square1), ShowCreation(square2))
        self.wait(0.5)
        self.play(ApplyMethod(circle1.set_opacity, 0.8))
        self.wait(1)
# 伴随运动


class TestUpdater(Scene):
    def construct(self):
        dot1 = Dot()
        dot2 = Dot(np.array([2, 0, 0]))
        text1 = TextMobject("dot2").set_color(
            YELLOW).next_to(dot2, RIGHT, buff=SMALL_BUFF)
        self.add(dot1, dot2, text1)

        def update_text(obj):
            obj.next_to(dot2, RIGHT, buff=SMALL_BUFF)
        text1.add_updater(update_text)
        self.add(text1)
        self.wait(0.3)
        self.play(Rotate(dot2, 90*DEGREES, about_point=ORIGIN))
        self.wait(1)
# 数字更新


class UpdateNumber(Scene):
    def construct(self):
        number_line = NumberLine(x_min=-3, x_max=3)
        triangle = RegularPolygon(3, start_angle=-PI/2).scale(0.2)\
            .next_to(number_line.get_left(), UP, buff=SMALL_BUFF)
        decimal = DecimalNumber(0, number_decimal_place=3,
                                include_sign=True, unit="\\rm cm")
        decimal.add_updater(lambda d: d.next_to(triangle, UP*0.1))
        decimal.add_updater(lambda d: d.set_value(triangle.get_center()[0]))
        self.add(number_line, triangle, decimal)
        self.play(
            triangle.shift, RIGHT*6,
            rate_func=there_and_back,
            run_time=5
        )
        self.wait(1)
# 虚线圆


class DashedCircle(Scene):
    def construct(self):
        dashed_circle = VGroup()
        for i in range(60):
            arc_i = Arc(radius=3, start_angle=6*i*DEGREES,
                        angle=3*DEGREES, color=RED)
            dashed_circle.add(arc_i)
        self.play(ShowCreation(dashed_circle), run_time=2)
        self.wait(1)
# 网格


class SquareNet(Scene):
    def construct(self):
        square_net = VGroup()
        for i in range(-3, 4):
            for j in range(-3, 4):
                square_i_j = Square(side_length=1, color=BLUE, stroke_width=1).move_to(
                    np.array([i, j, 0]))
                square_net.add(square_i_j)
        self.play(ShowCreation(square_net), run_time=3, lag_ratio=0.1)
        # self.wait(1)
# 坐标系


class NetPlate(Scene):
    def construct(self):
        net_plate = VGroup()
        for l in range(6):
            line_y_l_u = Line(np.array(
                [-10, l + 0.5, 0]), np.array([10, l + 0.5, 0]), color=BLUE, stroke_width=0.2)
            line_y_l_d = Line(np.array(
                [-10, -l-0.5, 0]), np.array([10, -l-0.5, 0]), color=BLUE, stroke_width=0.2)
            net_plate.add(line_y_l_u, line_y_l_d)
        for k in range(10):
            line_x_k_l = Line(np.array(
                [k+0.5, -8, 0]), np.array([k+0.5, 8, 0]), color=BLUE, stroke_width=0.2)
            line_x_k_r = Line(np.array(
                [-k-0.5, -8, 0]), np.array([-k-0.5, 8, 0]), color=BLUE, stroke_width=0.2)
            net_plate.add(line_x_k_l, line_x_k_r)
        for j in range(6):
            line_y_j_u = Line(
                np.array([-10, j+1, 0]), np.array([10, j+1, 0]), color=BLUE, stroke_width=0.6)
            line_y_j_d = Line(
                np.array([-10, -j, 0]), np.array([10, -j, 0]), color=BLUE, stroke_width=0.6)
            net_plate.add(line_y_j_u, line_y_j_d)
        for i in range(10):
            line_x_i_l = Line(
                np.array([i+1, -8, 0]), np.array([i+1, 8, 0]), color=BLUE, stroke_width=0.6)
            line_x_i_r = Line(
                np.array([-i, -8, 0]), np.array([-i, 8, 0]), color=BLUE, stroke_width=0.6)
            net_plate.add(line_x_i_l, line_x_i_r)
        line_xx = Line(
            np.array([-10, -3, 0]), np.array([12, -3, 0]), color=WHITE, stroke_width=1)
        line_yy = Line(
            np.array([-6, -8, 0]), np.array([-6, 9, 0]), color=WHITE, stroke_width=1)
        net_plate.add(line_xx, line_yy)
        self.play(ShowCreation(net_plate), run_time=3, lag_ratio=0.02)
        self.wait(0.5)

# 背景色


class BackGroundTest(Scene):
    CONFIG = {
        'camera_config': {'background_color': WHITE}
    }

    def construct(self):
        text1 = TextMobject("这是一个背景测试", color=RED)
        self.play(Write(text1))

# 输出mov


class TestMov(Scene):
    def construct(self):
        text1 = Text("中文测试", font="思源宋体 Heavy")
        self.play(Write(text1))
        # python manim.py notes.py TestMov --high_quality -t

# 角度变化测试


class TestAngle(Scene):
    CONFIG = {
        "theta": 60*DEGREES,
        "line_size": 3.5,
        "radius": 0.7,
        "increment_theta": 60*DEGREES
    }

    def construct(self):
        theta1 = ValueTracker(self.theta)
        line1 = Line(ORIGIN, RIGHT*self.line_size, color=YELLOW)
        line2 = Line(ORIGIN, RIGHT*self.line_size, color=YELLOW)
        line2.rotate(theta1.get_value(), about_point=ORIGIN)
        line2.add_updater(lambda m: m.set_angle(theta1.get_value()))
        arc1 = Arc(radius=self.radius, start_angle=line1.get_angle(),
                   angle=line2.get_angle(), color=RED)
        decimal1 = DecimalNumber(60, number_decimal_place=3, unit="^{\\circ}")
        decimal1.add_updater(lambda d: d.next_to(arc1, UP))
        decimal1.add_updater(lambda d: d.set_value(theta1.get_value()/PI*180))
        self.play(*[ShowCreation(obj)
                    for obj in [line1, line2, arc1, decimal1]])
        arc1.add_updater(lambda m: m.become(Arc(
            radius=self.radius, color=RED, start_angle=line1.get_angle(), angle=line2.get_angle())))
        self.add(arc1,decimal1)
        self.play(theta1.increment_value, self.increment_theta)
        self.wait(1)
        self.play(theta1.increment_value, self.increment_theta)
        self.wait(1)

class rtl(Scene):
    def construct(self):
        text1=TextMobject("right to left")
        self.play(Write(text1))

class update(Scene):
    def construct(self):
        sq = Square(side_length = 1).move_to(LEFT*5)
        path = Line(LEFT*5, RIGHT*5)
        dt = 1/15
        def anim(sq, dt):
            sq.rotate(dt*PI)
            sq.shift(2.5*RIGHT*dt)
        sq.add_updater(anim)
        self.add(sq,path)
        self.wait(5)
            
